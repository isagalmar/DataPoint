import pandas as pd
import datetime
from fastapi import routing

class Encuentro():
    def __init__(self, pacienteId, tipo_encuentro, fecha_inicio, fecha_fin):
        self.pacienteId = int(pacienteId)
        self.tipo_encuentro = str(tipo_encuentro)
        self.fecha_inicio = datetime.datetime.fromisoformat(fecha_inicio)
        self.fecha_fin = datetime.datetime.fromisoformat(fecha_fin)


router = routing.APIRouter(
    prefix="/encuentros",
    tags=["encuentros"],
    responses={404: {"description": "Not found('/encuentros')"}},
)

data = []


for pacienteId, tipo_encuentro, fecha_inicio, fecha_fin in pd.read_csv("./data/cohorte_encuentros.csv", sep=",").itertuples(index=False):
    data.append(Encuentro(pacienteId, tipo_encuentro, fecha_inicio, fecha_fin))


@router.get("/")
def getAllEncuentros():
    return {"message":"Todas las alergias registradas", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": data}

@router.get("/{pacienteId}")
def getEncuentrosPaciente(pacienteId:int):
    res = [ encuentro for encuentro in data if encuentro.pacienteId == pacienteId]
    
    return {"message":"Los encuentros del paciente son:", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": res}
