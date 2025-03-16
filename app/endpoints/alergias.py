import pandas as pd
import datetime
from fastapi import routing

class Alergia():
    def __init__(self, pacienteId, fecha_diagnostico, SNOMED, descripcion):
        self.pacienteId = int(pacienteId)
        self.fecha_diagnostico = datetime.datetime.strptime(fecha_diagnostico, "%Y-%m-%d").date()
        self.SNOMED = str(SNOMED)
        self.descripcion = str(descripcion)


router = routing.APIRouter(
    prefix="/alergias",
    tags=["alergias"],
    responses={404: {"description": "Not found('/alergias')"}},
)

data = []


for pacienteId, fecha_diagnostico, SNOMED, descripcion in pd.read_csv("./data/cohorte_alegias.csv", sep=",").itertuples(index=False):
    data.append(Alergia(pacienteId, fecha_diagnostico, SNOMED, descripcion))


@router.get("/getAllAlergias")
def getAllAlergias():
    return {"message":"Todas las alergias registradas", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": data}

@router.get("/getAlergiasPaciente/{pacienteId}")
def getAlergia(pacienteId:int):
    res = [ alergia for alergia in data if alergia.pacienteId == pacienteId]
    
    return {"message":"Las alergias del paciente son:", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": res}
