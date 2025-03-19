import pandas as pd
import datetime
from fastapi import routing


class Procedimiento():
    def __init__(self, pacienteId, fecha_inicio, fecha_fin, SNOMED,descripcion):
        self.pacienteId = int(pacienteId)
        self.fecha_inicio = datetime.datetime.fromisoformat(fecha_inicio)
        self.fecha_fin = datetime.datetime.fromisoformat(fecha_fin)
        self.SNOMED = str(SNOMED)
        self.descripcion = str(descripcion)



router = routing.APIRouter(
    prefix="/procedimientos",
    tags=["procedimientos"],
    responses={404: {"description": "Not found('/procedimientos')"}},
)

data = []


for pacienteId, fecha_inicio, fecha_fin, SNOMED,descripcion in pd.read_csv("./data/cohorte_procedimientos.csv", sep=",").itertuples(index=False):
    data.append(Procedimiento(pacienteId, fecha_inicio, fecha_fin, SNOMED,descripcion))


@router.get("/")
def getAllProcedimientos():
    return {"message":"Todas los procedimientos registrados", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": data}

@router.get("/{pacienteId}")
def getProcedimientosPaciente(pacienteId:int):
    res = [ procedimiento for procedimiento in data if procedimiento.pacienteId == pacienteId]
    
    return {"message":"Los procedimientos del paciente son:", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": res}
