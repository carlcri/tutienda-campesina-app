from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import HTMLResponse, JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from datos import CLIENTS as clients # Asegúrate de que 'datos.py' exista y contenga CLIENTS

from typing import Optional # Importa Optional

# Create a FastAPI application instance
app = FastAPI()
app.title = "Prototipo Plataforma de Comercializacion"
app.version = "0.0.1"


# --- Configuración de MongoDB ---
# MONGO_DETAILS = "mongodb://tuTiendaDB:27017/" # Si usas un servicio de Docker, etc.
MONGO_DETAILS = "mongodb://localhost:27017/"

# --- Variable global para el cliente de MongoDB ---
# Inicializamos a None, se asignará en el evento 'startup'
db_client: Optional[AsyncIOMotorClient] = None


# --- Evento de Inicio (Startup Event) ---
@app.on_event("startup")
async def startup_db_client():
    """
    Se ejecuta cuando la aplicación FastAPI se inicia.
    Establece la conexión a MongoDB y la guarda en una variable global.
    """
    global db_client # Declara que vamos a modificar la variable global
    try:
        db_client = AsyncIOMotorClient(MONGO_DETAILS)
        # Opcional: Intenta una operación simple para verificar la conexión al inicio
        await db_client.admin.command('ping')
        print("¡Conexión a MongoDB establecida exitosamente en el inicio!")
    except Exception as e:
        print(f"ERROR: No se pudo conectar a MongoDB al inicio: {e}")
        # Considera levantar una excepción aquí para evitar que la app inicie
        # si la conexión a la DB es crítica.
        # raise Exception(f"Fallo crítico al conectar a MongoDB: {e}")

# --- Evento de Apagado (Shutdown Event) ---
@app.on_event("shutdown")
async def shutdown_db_client():
    """
    Se ejecuta cuando la aplicación FastAPI se apaga.
    Cierra la conexión a MongoDB.
    """
    if db_client: # Asegúrate de que el cliente exista antes de intentar cerrarlo
        db_client.close()
        print("Conexión a MongoDB cerrada limpiamente al apagar.")


# --- Endpoint /check-db-connection (Ahora obsoleto o modificado) ---
# Este endpoint ya no es necesario para verificar la conexión,
# ya que la conexión se establece al inicio.
# Podrías eliminarlo o modificarlo para simplemente confirmar que la app está corriendo.
@app.get("/check-db-connection", tags=['database'])
async def check_db_connection_status():
    """
    Endpoint para verificar el estado de la conexión a MongoDB.
    Ahora solo reporta si el cliente de DB está inicializado.
    """
    if db_client and db_client.delegate.is_connected: # Verifica si el cliente está inicializado y conectado
        return JSONResponse(content={"status": "success",
                                      "message": "MongoDB client está conectado y listo."})
    else:
        # Esto podría indicar un fallo en el startup o que la conexión se perdió.
        raise HTTPException(status_code=500, detail="MongoDB client no está conectado o falló al iniciar.")



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



# Define your first API endpoint (route)
@app.get("/", tags=['root'])
async def read_root_endpoint():
    nombre = 'Gustavo'
    html_content = f'<h1>Hello {nombre} From API, this is Roottt</h1>'
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
    # Usamos next() para una búsqueda más eficiente y concisa
    found_client = next(
        (client for client in clients if client['id'] == client_id_to_find), # Iterador
        None # Valor por defecto si no se encuentra
    )

    if found_client is None: # Si next() devolvió None, el cliente no fue encontrado
        # Elevar la excepción HTTP 404 es la forma correcta
        message = f"cliente con id {client_id_to_find} no existeee"
        raise HTTPException(
            status_code=404,
            detail={"message": message}
        )
    else:
        # Si se encontró el cliente, devolvemos el diccionario completo.
        # FastAPI automáticamente lo convertirá a JSON con el status_code 200.
        return JSONResponse(status_code=200, content=found_client)




