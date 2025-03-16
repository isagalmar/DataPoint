import pandas as pd
import datetime
from fastapi import routing

class Condicion():
    def __init__(self, pacienteId, fecha_inicio, fecha_fin, SNOMED, descripcion):
        self.pacienteId = int(pacienteId)
        self.fecha_inicio = datetime.datetime.fromisoformat(fecha_inicio)
        self.fecha_fin = datetime.datetime.fromisoformat(fecha_fin)
        self.SNOMED = str(SNOMED)
        self.descripcion = str(descripcion)


router = routing.APIRouter(
    prefix="/condiciones",
    tags=["condiciones"],
    responses={404: {"description": "Not found('/condiciones')"}},
)

data = []


for pacienteId, fecha_inicio, fecha_fin, SNOMED, descripcion in pd.read_csv("./data/cohorte_condiciones.csv", sep=",").itertuples(index=False):
    data.append(Condicion(pacienteId, fecha_inicio, fecha_fin, SNOMED, descripcion))


@router.get("/getAllCondiciones")
def getAllCondiciones():
    return {"message":"Todas las alergias registradas", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": data}

@router.get("/getCondicionesPaciente/{pacienteId}")
def getCondicionesPaciente(pacienteId:int):
    res = [ condiciones for condiciones in data if condiciones.pacienteId == pacienteId]
    
    return {"message":"Las condiciones del paciente son:", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": res}
