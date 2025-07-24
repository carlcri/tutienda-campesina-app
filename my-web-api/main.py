from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import HTMLResponse, JSONResponse

from datos import STUDENTS as students

# Importar la instancia de settings desde app.core.config
from core.config import settings

# Importar las funciones de conexión/desconexión de la base de datos
# Importamos 'db' para acceder al cliente
from core.database import connect_to_mongo, close_mongo_connection, db_client

# --- Configuración de MongoDB ---
MONGO_DETAILS = settings.conection_string()


# Create a FastAPI application instance
app = FastAPI()
app.title = "API Prototipo Plataforma de Comercializacion"
app.version = "0.0.3"


@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()
    


@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()


# Define your first API endpoint
@app.get("/", tags=['root'])
async def read_root_endpoint():
    nombre = 'Gustavo Petro'
    html_content = f'<h1>Hello {nombre} From API, this is ROOTERDAM</h1>'
    print('hola')
    print(db_client)
    return HTMLResponse(html_content)


# Define your Second API endpoint
@app.get("/cat", tags=['cat'])
async def read_cat_endpoint():
    nombre = 'Cat'
    html_content = f'<h1>Hello {nombre} From API, this is CAT(ANTONIA mi gatito feliz ) Endpoint</h1>'
    return HTMLResponse(html_content)




# Path Parameter para encontrar un estudiante por su id 
@app.get("/student/{client_id_to_find}", tags=['student'], status_code=200)
async def get_student_by_id(client_id_to_find: int = Path(..., 
                                                 gt=0, 
                                                 description="ID del estudiante a buscar")):
    
    """
    Busca un estudiante en DB y devuelve todos sus datos si es encontrado.
    Si el estudiante no existe, retorna un error 404 Not Found.
    """
    found_client_list = []

    for client in students:
        if client['id']==client_id_to_find:   
            return JSONResponse(status_code=200, content=client)

    message = f"estudiante con id {client_id_to_find} no existeee"
    raise HTTPException(status_code=404, detail={"message":message})




@app.get("/client/{client_id_to_find}", tags=['clients'])
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

