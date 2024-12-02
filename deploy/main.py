from typing import List
import pandas as pd
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
import json

from datamodel import DataModel
from model import PredictionModel

app = FastAPI()

# CORS settings (if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

city_mapping = {
    "76001": "Cali",
    "5002": "Palmira",
    "76111": "Jumbo",
    "76243": "Yumbo",
    "76130": "Cartago"
}


@app.get("/")
def read_root():
    return {"message": "Hello world"}

@app.post("/predict")
def make_predictions(X: List[DataModel]):
    print(X)
    df = pd.DataFrame([x.model_dump() for x in X])
    predicion_model = PredictionModel()
    print(df)
    results = predicion_model.make_predictions(df)
    print("Tipo de resultado:", type(results))
    print(results)
    return {"prediccion": results.tolist()}

@app.get("/opciones")
def get_opciones():
    # Read the files with UTF-8 encoding
    df = pd.read_csv("../data/raw/DIVIPOLA-_C_digos_municipios_20241127.csv", encoding="utf-8", delimiter=",")
    pr_df = pd.read_csv("../data/raw/programas.csv", encoding="utf-8", delimiter=",")
    
    # Sort and deduplicate data
    df_sorted = df.sort_values(by="Nombre_Municipio")
    pr_df_sorted = pr_df.sort_values(by="PROGRAMA")

    ciudad_residencia = df_sorted[["Codigo_Municipio", "Nombre_Municipio"]].drop_duplicates().reset_index(drop=True)
    ciudad_nacimiento = df_sorted[["Codigo_Municipio", "Nombre_Municipio"]].drop_duplicates().reset_index(drop=True)
    programa = pr_df_sorted[["CODIGOPROGRAMA", "PROGRAMA"]].drop_duplicates().reset_index(drop=True)

    opciones = {
        "ciudad_residencia": ciudad_residencia.to_dict(orient="records"),
        "ciudad_nacimiento": ciudad_nacimiento.to_dict(orient="records"),
        "programa": programa.to_dict(orient="records"),
    }
    return opciones

# Serve the HTML page with UTF-8 encoding
@app.get("/inicio", response_class=HTMLResponse)
def read_root():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read(), status_code=200)


# New endpoint for group prediction
@app.post("/predict-group")
async def predict_group(data: List[dict] = Body(...)):
    try:
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(data)
        # Ensure the dataframe has the required columns
        required_columns = ["ESTRATO", "SEMESTRE", "PROMEDIOSEMESTRE", "EDAD2", "PROGRAMA", "GENERO", "CIUDADRESIDENCIA", "CIUDADNACIMIENTO"]
        if not all(column in df.columns for column in required_columns):
            raise HTTPException(status_code=400, detail="El archivo JSON no contiene las columnas requeridas.")
        # Make predictions
        predicion_model = PredictionModel()
        print(df)
        results = predicion_model.make_predictions(df)
        # Return the results
        return [{"prediccion": result} for result in results.tolist()]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/student-details", response_class=HTMLResponse)
def read_root(request: Request):
    data = request.query_params.get('data')
    if data:
        student_details = json.loads(data)
        
        # Post-process the values
        student_details["GENERO"] = "masculino" if student_details["GENERO"] == "0" else "femenino"
        student_details["CIUDADRESIDENCIA"] = city_mapping.get(student_details["CIUDADRESIDENCIA"], student_details["CIUDADRESIDENCIA"])
        student_details["CIUDADNACIMIENTO"] = city_mapping.get(student_details["CIUDADNACIMIENTO"], student_details["CIUDADNACIMIENTO"])
        
        with open("student-details.html", "r", encoding="utf-8") as f:
            content = f.read()
            # Determine status text and class based on prediction
            status_text = "En riesgo de Deserción" if student_details["prediccion"] == 0 else "No en riesgo de Deserción"
            status_class = "status-desertion" if student_details["prediccion"] == 0 else "status-no-desertion"
            # Determine classes for highlighting
            estrato_class = "highlight-red" if student_details["ESTRATO"] < 2 else ""
            promedio_class = "highlight-red" if student_details["PROMEDIOSEMESTRE"] < 3 else ""
            # Replace placeholders with actual data
            content = content.replace("{{ status_text }}", status_text)
            content = content.replace("{{ status_class }}", status_class)
            content = content.replace("{{ estrato_class }}", estrato_class)
            content = content.replace("{{ promedio_class }}", promedio_class)
            for key, value in student_details.items():
                content = content.replace(f"{{{{ {key} }}}}", str(value))
                
            # add the element prediction-text to the content, if the prediccion is 0, the text will be "En riesgo de deserción", otherwise "No está en riesgo de deserción"
            if student_details["prediccion"] == 0:
                content = content.replace("{{ prediction-text }}", "En riesgo de deserción")
            else:
                content = content.replace("{{ prediction-text }}", "No está en riesgo de deserción")
            return HTMLResponse(content=content, status_code=200)
    else:
        return HTMLResponse(content="No data provided", status_code=400)
