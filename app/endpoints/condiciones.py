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


@router.get("/")
def getAllCondiciones(fecha_inicio:datetime.datetime = None, fecha_fin:datetime.datetime = None, snomed:str = ""):
    res = [condicion for condicion in data if (condicion.fecha_inicio == fecha_inicio or fecha_inicio == None) 
                                        and (condicion.fecha_fin == fecha_fin or fecha_fin == None) 
                                        and (condicion.SNOMED == snomed or snomed == "")]


    return {"message":"Todas las alergias registradas", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": data}

@router.get("/{pacienteId}")
def getCondicionesPaciente(pacienteId:int, fecha_inicio:datetime.datetime = None, fecha_fin:datetime.datetime = None, snomed:str = ""):
    res = [condicion for condicion in data if condicion.pacienteId == pacienteId
                                        and (condicion.fecha_inicio == fecha_inicio or fecha_inicio == None) 
                                        and (condicion.fecha_fin == fecha_fin or fecha_fin == None) 
                                        and (condicion.SNOMED == snomed or snomed == "")]
    
    return {"message":"Las condiciones del paciente son:", "return-timestamp": int(datetime.datetime.timestamp(datetime.datetime.now())), "response": res}
