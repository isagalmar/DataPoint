import pandas as pd
import datetime
from fastapi import routing
from urllib.parse import unquote

class Paciente():
    def __init__(self, pacienteId, genero, edad, provincia, latitud, longitud):
        self.pacientId = int(pacienteId)
        self.genero = str(genero)
        self.edad = int(edad)
        self.provincia = str(provincia)
        self.latitud = str(latitud)
        self.longitud = str(longitud)


router = routing.APIRouter(
    prefix="/pacientes",
    tags=["pacientes"],
    responses={404: {"description": "Not found('/pacientes')"}},
)


data = []


for pacienteId, genero, edad, provincia, latitud, longitud in pd.read_csv("./data/cohorte_pacientes.csv", sep=",").itertuples(index=False):
    data.append(Paciente(pacienteId, genero, edad, provincia, latitud, longitud))




@router.get("/")
def getAllAlergias(provincia:str = "", genero:str = "", edad:int = 0):
    
    res = [paciente for paciente in data if (paciente.provincia == provincia or provincia == "") 
                                        and (paciente.genero == genero or genero == "") 
                                        and (paciente.edad == edad or edad <= 0)]

    return {"message":"Todos los pacientes registrados", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": res}


@router.get("/{pacienteId}")
def getPacientePorId(pacienteId:int, provincia:str = "", genero:str = "", edad:int = 0):
    res = [paciente for paciente in data if paciente.pacienteId == pacienteId
                                        and (paciente.provincia == provincia or provincia == "") 
                                        and (paciente.genero == genero or genero == "") 
                                        and (paciente.edad == edad or edad <= 0)]

    return {"message":f"El paciente de id {pacienteId} es:", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": res}