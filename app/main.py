from fastapi import FastAPI
import endpoints.alergias as alergias
import endpoints.pacientes as pacientes
import endpoints.condiciones as condiciones
import endpoints.encuentros as encuentros
import endpoints.medicacion as medicacion
import endpoints.procedimientos as procedimientos


app = FastAPI()

app.include_router(alergias.router)
app.include_router(pacientes.router)
app.include_router(condiciones.router)
app.include_router(encuentros.router)
app.include_router(medicacion.router)
app.include_router(procedimientos.router)


@app.get("/")
def root():
    return {"message": "Hola esto es DataPoint!"}