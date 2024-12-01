from typing import List
import pandas as pd
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

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

# New endpoint to return group data
@app.get("/datos-grupales")
def get_datos_grupales():
    datos = [
        {"year": 2020, "desertores": 50, "noDesertores": 150},
        {"year": 2021, "desertores": 40, "noDesertores": 160},
        {"year": 2022, "desertores": 30, "noDesertores": 170},
    ]
    return datos

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
# Open the student-details.html file and return it as a response
def read_root():
    with open("student-details.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read(), status_code=200)
