# # --- Nuevo Manejador de Eventos de Ciclo de Vida (Lifespan) ---
# @asynccontextmanager
# async def lifespan_events(app: FastAPI):
#     """
#     Gestiona el ciclo de vida de la aplicación FastAPI.
#     Establece la conexión a MongoDB al inicio y la cierra al apagar.
#     """
#     global db_client # Importante: indica que estás modificando la variable global
#     print('--- INICIAaNDO LIFESPAN EVENTS GATOS ---') # <-- ¡Añade esto!
#     # --- Código que se ejecuta en el "startup" (antes del 'yield') ---
#     try:
#         db_client = AsyncIOMotorClient(MONGO_DETAILS)
#         await db_client.admin.command('ping')
#         print('¡Conexión a MongoDB establecida exitosamente en el inicio (lifespan)!')

#     except Exception as e: # Captura cualquier tipo de excepción
#         print(f"Error crítico: No se pudo conectar a MongoDB al inicio: {e}")
#         # Lanza una excepción para evitar que la aplicación se inicie sin DB
#         raise HTTPException(status_code=500, detail={"message": f"Error de Servidor: BD no Disponible al inicio. Detalle"})

#     yield # La aplicación comienza a procesar solicitudes aquí

#     # --- Código que se ejecuta en el "shutdown" (después del 'yield') ---
#     if db_client:
#         db_client.close()
#         print('¡Se ha cerrado la conexión a MongoDB limpiamente (lifespan) Perros!')