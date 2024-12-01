from pydantic import BaseModel

class DataModel(BaseModel):
    ESTRATO: int
    SEMESTRE: int
    PROMEDIOSEMESTRE: float
    EDAD2: int
    PROGRAMA: int
    GENERO: int
    CIUDADRESIDENCIA: int
    CIUDADNACIMIENTO: int