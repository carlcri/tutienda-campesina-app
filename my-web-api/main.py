from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import HTMLResponse, JSONResponse
from core.config import settings


# Importar la instancia de settings desde app.core.config
from core.config import settings

# Importar las funciones de conexión/desconexión de la base de datos
# Importar 'db_client' para acceder al cliente
from core.database import connect_to_mongo, close_mongo_connection, db_client

# Importar los routers de los endpoints
from api.v1.endpoints import root, students, clients


# --- Configuración de MongoDB ---
MONGO_DETAILS = settings.conection_string()


# Create a FastAPI application instance
app = FastAPI()
app.title = settings.app_name
app.version = settings.app_version


@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()
    

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()



# Incluir los routers en la aplicación principal
app.include_router(root.router)
app.include_router(students.router)
app.include_router(clients.router)


