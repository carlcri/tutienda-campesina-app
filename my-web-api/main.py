from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient

# Create a FastAPI application instance
app = FastAPI()


# --- Configuración de MongoDB ---
# IMPORTANTE: Usa el nombre del contenedor de MongoDB dentro de la red Docker.
# Docker sabe cómo encontrar 'tuTiendaDB' dentro de la red 'platzinet'.
MONGO_DETAILS = "mongodb://tuTiendaDB:27017/"



# Define your first API endpoint (route)
@app.get("/", tags=['root'])
async def read_root_endpoint():
    nombre = 'Gustavo'
    html_content = f'<h1>Hello {nombre} From API, this is ROOT</h1>'
    return HTMLResponse(html_content)


# Define your first API endpoint (route)
@app.get("/cat", tags=['cat'])
async def read_cat_endpoint():
    nombre = 'Cat'
    html_content = f'<h1>Hello {nombre} From API, this is CAT(Antonia) Endpoint</h1>'
    return HTMLResponse(html_content)



# --- Nuevo Endpoint: ¡La verificación de conexión a MongoDB! ---
@app.get("/check-db-connection", tags=['database'])
async def check_db_connection():
    """
    Endpoint para verificar si la aplicación puede conectarse a MongoDB.
    Intenta crear un cliente y realizar una operación simple.
    """
    try:
        # Crea un cliente de MongoDB.
        # Aquí es donde intentamos conectar.
        client = AsyncIOMotorClient(MONGO_DETAILS)

        # Intenta una operación muy simple para confirmar que la conexión funciona.
        # 'ping' es un comando ligero que solo verifica si el servidor está vivo.
        await client.admin.command('ping')

        # Si llegamos aquí, la conexión fue exitosa.
        client.close() # Cierra la conexión (importante en este enfoque simple)
        return JSONResponse(content={"status": "success", 
                                     "message": "¡Conexión a MongoDB exitosaa!"})

    except Exception as e:
        # Si algo falla (MongoDB no está corriendo, nombre incorrecto, etc.)
        # capturamos el error y devolvemos un mensaje de fallo.
        print(f"Error durante la verificación de conexión a MongoDB: {e}")
        raise HTTPException(status_code=500, detail=f"Fallo en la conexión a MongoDB: {e}. Asegúrate de que 'tuTiendaDB' esté corriendo y en la misma red.")

