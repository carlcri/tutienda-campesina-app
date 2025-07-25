from fastapi import APIRouter, HTTPException, Path
from fastapi.responses import JSONResponse
from core.database import db_client


router = APIRouter(tags=['clients'])


@router.get("/client/{client_id_to_find}")
async def get_client_by_id(client_id_to_find:int = Path(...,
                                                        gt=0,
                                                        description="ID del cliente a buscar")):
    """
    Busca un cliente por su ID en la base de datos MongoDB.

    Args:
        client_id_to_find (int): El ID del cliente a buscar. 

    Returns:
        JSONResponse: Un JSON con los datos del cliente si es encontrado.

    Raises:
        HTTPException:
            - 500 Internal Server Error si la conexión a la base de datos no está establecida.
            - 404 Not Found si el cliente con el ID especificado no existe.
    """
    if not db_client['client']:
        raise HTTPException(status_code=500, detail={"message": "la conexion a la BD ha fallado"})
    
    collection = db_client['client']['db-tienda'].clients 
    found_client = await collection.find_one({'id': client_id_to_find})

    if not found_client:
        message = f'cliente con id:{client_id_to_find} no encontrado'
        raise HTTPException(status_code=404, detail={"message":message})
    
    found_client['_id'] = str(found_client['_id'])
    return JSONResponse(status_code=200, content=found_client)