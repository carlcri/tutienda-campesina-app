from fastapi import APIRouter, HTTPException, Path, Body
from fastapi.responses import JSONResponse
from datos import STUDENTS as students_db

from pydantic import BaseModel, Field
from typing import Optional



class StudentCreate(BaseModel):
    id: int = Field(ge=1)
    name: str = Field(min_length=3)
    lastName: str = Field(min_length=3)
    governmentId: str = Field(min_length=1)
    typeOfDocument: str = Field("CC", max_length=3)
    DOB: Optional[str] = None 
    location: str = Field("Bogota", min_length=2)


class StudentUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3)
    lastName: Optional[str] = Field(None, min_length=3)
    governmentId: Optional[str] = Field(None, min_length=1)
    typeOfDocument: Optional[str] = Field(None, max_length=3)
    DOB: Optional[str] = None 
    location: Optional[str] = Field(None, min_length=2)


router = APIRouter(tags=['students'])


# Path Parameter para encontrar un estudiante por su id 
@router.get("/student/{client_id_to_find}", status_code=200)
async def get_student_by_id(client_id_to_find: int = Path(..., 
                                                 gt=0, 
                                                 description="ID del estudiante a buscar")):
    
    """
    Busca un estudiante en DB y devuelve todos sus datos si es encontrado.
    Si el estudiante no existe, retorna un error 404 Not Found.
    """
    found_client_list = []
    pass

    for client in students_db:
        if client['id']==client_id_to_find:   
            return JSONResponse(status_code=200, content=client)

    message = f"estudiante con id {client_id_to_find} ¡no existe!"
    raise HTTPException(status_code=404, detail={"message":message})



# Crear un estudiante
@router.post("/student", status_code=201)
async def create_student(new_student: StudentCreate):
    """
    Crea un nuevo estudiante en la BD, para verificar que no existe el nuevo estudiante,
    busca por su id, si hay un conflicto retorna 409
    """
    for student in students_db:
        if student['id'] == new_student.id:
            raise HTTPException(status_code=409, detail={"message": f"estudiante {new_student.id} ya existe"})

    # Convierte la instancia de Pydantic a un diccionario
    new_student_dict = new_student.model_dump()

    students_db.append(new_student_dict)

    return JSONResponse(status_code=201, content=new_student_dict)


# --- PATCH: Update an existing student (partial update) ---
@router.patch("/student/{student_id_to_patch}", status_code=200)
async def update_student(student_id_to_patch: int = Path(gt=0, description="ID del estudiante a actualizar"),
                        student_update: StudentUpdate = Body(description="campos a actualizar" ) ):
    
    """
    Actualiza a un estudiante de acuerdo al PATH parameter, dentro del cuerpo de la peticion se envian solo los datos
    a actualizar. Si el estudiante no existe retorna un 404 
    """
    for student in students_db:
        if student['id'] == student_id_to_patch:
            # Convierte la instancia de Pydantic a un diccionario
#            new_student_dict = student_update.model_dump()
            new_student_dict = student_update.model_dump(exclude_unset=True, mode='json')
            # print('hello: student update')
            # print(student_update)

            for key in new_student_dict:
                student[key] = new_student_dict[key]
            
            return JSONResponse(status_code=200, content={"message": "Estudiante Actualizado Exitosamente", "student": student })
    
    message = f"estudiante con id {student_id_to_patch} ¡no existe!"
    raise HTTPException(status_code=404, detail={"message":message})   



# Borrar un estudiante
@router.delete("/student/{student_id_to_delete}", status_code=200)
async def delete_student_by_id(student_id_to_delete: int=Path(ge=1,
                                                    description="ID del estudiante a borrar")):
    """
    Borra un estudiante de la BD, verifica si el estudiante existe.
    Si no existe retorna no encontrado 404
    """
    for idx, student in enumerate(students_db):
        if student['id'] == student_id_to_delete:
            students_db.pop(idx)
            return JSONResponse(status_code=200, content=f'student with id {student["id"]} eliminated')
    
    raise HTTPException(status_code=404, detail={"message": f'estudiante con id:{student_id_to_delete} no existe'})