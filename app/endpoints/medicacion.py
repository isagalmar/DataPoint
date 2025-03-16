import pandas as pd
import datetime
from fastapi import routing


class Dosis():

    def __init__(self, dosis_str:str):
        cantidad,tamaño = dosis_str.split(" ")
        
        self.cantidad = float(cantidad)
        self.tamaño = str(tamaño)


class Medicacion():
    def __init__(self, pacienteId, fecha_inicio, fecha_fin, codigo, nombre, dosis, frecuencia, via):
        self.pacienteId = int(pacienteId)
        self.fecha_inicio = datetime.datetime.fromisoformat(fecha_inicio)
        self.fecha_fin = datetime.datetime.fromisoformat(fecha_fin)
        self.codigo = codigo
        self.nombre = nombre
        self.dosis = Dosis(dosis)
        self.frecuencia = str(frecuencia)
        self.via = str(via)



router = routing.APIRouter(
    prefix="/medicacion",
    tags=["medicacion"],
    responses={404: {"description": "Not found('/medicion')"}},
)

data = []


for pacienteId, fecha_inicio, fecha_fin, codigo, nombre, dosis, frecuencia, via in pd.read_csv("./data/cohorte_medicationes.csv", sep=",").itertuples(index=False):
    data.append(Medicacion(pacienteId, fecha_inicio, fecha_fin, codigo, nombre, dosis, frecuencia, via))


@router.get("/getAllMedicaciones")
def getAllMedicaciones():
    return {"message":"Todas las medicaciones registradas", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": data}

@router.get("/getMedicacionPaciente/{pacienteId}")
def getMedicacionPaciente(pacienteId:int):
    res = [ medicacion for medicacion in data if medicacion.pacienteId == pacienteId]
    
    return {"message":"Las medicaciones del paciente son:", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": res}
