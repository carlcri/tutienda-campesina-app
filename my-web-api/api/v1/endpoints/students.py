from fastapi import APIRouter, HTTPException, Path
from fastapi.responses import JSONResponse
from datos import STUDENTS as students_db

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