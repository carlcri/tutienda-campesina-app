from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import HTMLResponse, JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

# Importar asynccontextmanager para los eventos lifespan
from contextlib import asynccontextmanager

# --- Configuración de MongoDB ---
# MONGO_DETAILS = "mongodb://tuTiendaDB:27017/" # Ejemplo si usaras un servicio de Docker
MONGO_DETAILS = "mongodb://localhost:27017/"


# Guarda la conexión global a MongoDB; es None inicialmente y se establece al inicio de la app.
db_client : Optional[AsyncIOMotorClient] = None

# --- Nuevo Manejador de Eventos de Ciclo de Vida (Lifespan) ---
@asynccontextmanager
async def lifespan_events(app: FastAPI):
    """
    Gestiona el ciclo de vida de la aplicación FastAPI.
    Establece la conexión a MongoDB al inicio y la cierra al apagar.
    """
    global db_client # Importante: indica que estás modificando la variable global

    # --- Código que se ejecuta en el "startup" (antes del 'yield') ---
    try:
        db_client = AsyncIOMotorClient(MONGO_DETAILS)
        await db_client.admin.command('ping')
        print('¡Conexión a MongoDB establecida exitosamente en el inicio (lifespan)!')

    except Exception as e: # Captura cualquier tipo de excepción para obtener su detalle
        print(f"Error crítico: No se pudo conectar a MongoDB al inicio: {e}")
        raise RuntimeError(f"Fallo crítico: La aplicación no pudo conectar a MongoDB y no iniciará. Detalle: {e}")

    yield # Aquí la aplicación comienza a procesar solicitudes

    # --- Código que se ejecuta en el "shutdown" (después del 'yield') ---
    if db_client: # Solo intenta cerrar si la conexión se estableció
        db_client.close()
        print('¡Se ha cerrado la conexión a MongoDB limpiamente (lifespan)!')
    else:
        print('La conexión a MongoDB no se estableció, no hay nada que cerrar.')


# Create a FastAPI application instance
# ¡Importante! Pasar el context manager 'lifespan_events' a la aplicación.
app = FastAPI(title="Prototipo Plataforma de Comercializacion",
              version="0.0.2",
              lifespan=lifespan_events) # <--- ¡Aquí se asigna el manejador del ciclo de vida!
