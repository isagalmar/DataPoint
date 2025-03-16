import pandas as pd
import datetime
from fastapi import routing

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




@router.get("/getAllPacientes")
def getAllAlergias():
    return {"message":"Todos los pacientes registrados", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": data}


@router.get("/getPacientePorProvincia/{provincia}")
def getPacientePorProvincia(provincia:str):
    res = [ paciente for paciente in data if paciente.provincia == provincia]

    return {"message":f"Los pacientes de {provincia} son:", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": res}

@router.get("/getPacientePorId/{pacienteId}")
def getPacientePorId(pacienteId:int):
    res = [ paciente for paciente in data if paciente.pacienteId == pacienteId]

    return {"message":f"El paciente de id {pacienteId} es:", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": res}