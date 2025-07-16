from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import HTMLResponse, JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from datos import CLIENTS as clients
from typing import Optional


# Create a FastAPI application instance
app = FastAPI()
app.title = "Prototipo Plataforma de Comercializacion"
app.version = "0.0.2"


# --- Configuración de MongoDB ---
# MONGO_DETAILS = "mongodb://tuTiendaDB:27017/"
MONGO_DETAILS = "mongodb://localhost:27017/"


# Guarda la conexión global a MongoDB; es None inicialmente y se establece al inicio de la app.
db_client : Optional[AsyncIOMotorClient] = None



@app.on_event("startup")
async def startup_db_client():
    try:
        db_client = AsyncIOMotorClient(MONGO_DETAILS)
        print('Conexion Exitosa establecida en startup')
    except:
        raise HTTPException(status_code=500, detail={"message":"Error de Servidor BD no Disponible"})
    

@app.on_event("shutdown")
async def shutdown_db_client():
    if db_client:
        db_client.close()
        print('Se ha cerrado la conexion')



# Define your first API endpoint (route)
@app.get("/", tags=['root'])
async def read_root_endpoint():
    nombre = 'Gustavo'
    html_content = f'<h1>Hello {nombre} From API, this is ROOTERDAM</h1>'
    return HTMLResponse(html_content)


# Define your first API endpoint (route)
@app.get("/cat", tags=['cat'])
async def read_cat_endpoint():
    nombre = 'Cat'
    html_content = f'<h1>Hello {nombre} From API, this is CAT(Antoniaa) Endpoint</h1>'
    return HTMLResponse(html_content)






# Path Parameter para encontrar un cliente por su id 
@app.get("/client/{client_id_to_find}", tags=['client'], status_code=200)
async def get_client_by_id(client_id_to_find: int = Path(..., 
                                                 gt=0, 
                                                 description="ID del cliente a buscar")):
    
    """
    Busca un cliente en DB y devuelve todos sus datos si es encontrado.
    Si el cliente no existe, retorna un error 404 Not Found.
    """
    found_client_list = []

    for client in clients:
        if client['id']==client_id_to_find:   
            return JSONResponse(status_code=200, content=client)

    message = f"cliente con id {client_id_to_find} no existeee"
    raise HTTPException(status_code=404, detail={"message":message})


