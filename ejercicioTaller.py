from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
estudiantes = []

class ContenidoMateria(BaseModel):
    nombre: str
    descripcion: str

class Materia(BaseModel):
    nombre: str
    nivel: int
    unidades_credito: int
    precio: float
    descripcion: str
    contenidos: List[ContenidoMateria]

class RecordAcademico(BaseModel):
    materia: Materia
    nota: float
    fecha_cursado: str

class Estudiante(BaseModel):
    nombres: str
    apellidos: str
    año_nacimiento: int
    telefono: str
    direccion: str
    record_academico: List[RecordAcademico]

@app.post("/estudiantes/")
async def create_student(estudiante: Estudiante):
    return {"message": "Estudiante creado exitosamente", "data": estudiante}

@app.get("/estudiante/{estudiante_id}")
async def get_estudiante(estudiante_id: int):
    return {"mensaje": "Estudiante obtenido exitosamente", "estudiante_id": estudiante_id}

@app.put("/estudiantes/{estudiante_id}")
async def modificar_estudiante(estudiante_id: int, estudiante: Estudiante):
    estudiantes[estudiante_id] = estudiante
    return {"mensaje": "Estudiante modificado exitosamente", "estudiante_id": estudiante_id, "nuevo_estudiante": estudiante}

@app.delete("/estudiantes/{estudiante_id}")
async def eliminar_estudiante(estudiante_id: int):
    eliminado = estudiantes.pop(estudiante_id)
    return {"mensaje": "Estudiante eliminado exitosamente", "estudiante_eliminado": eliminado}