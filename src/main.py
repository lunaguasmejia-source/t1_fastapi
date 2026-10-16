from src.templates.controllers import create_trainee, get_all_trainees,get_trainee_by_id, update_trainee, delete_trainee

from src.models.models import TraineeModel, TraineeUpdateModel
from fastapi import FastAPI, HTTPException, status

app = FastAPI(title = "Gestion de bases de datos de los aprendices", description = "API simple con FastAPI para consumir los datos de los aprendices", version = "1.0.0",)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de aprendices"}