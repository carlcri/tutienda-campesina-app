from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import HTTPException
from typing import Optional, Dict
from core.config import settings


# Guarda la conexión global a MongoDB

db_client: Dict[str, Optional[AsyncIOMotorClient]] = {
    "client": None,
}

#db_client : Optional[AsyncIOMotorClient] = None


async def connect_to_mongo():
#    global db_client
    try:
        db_client['client'] = AsyncIOMotorClient(settings.conection_string())
        print(f'Conexion Exitosaa a la BD: {settings.conection_string()}')
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message":"Error de Servidor BD no Disponib"})



async def close_mongo_connection():
    print('hola hijuemadre')
    if db_client['client']:
        db_client['client'].close()
        print('Se ha cerrado la conexion')
    else:
        print('La conexión a MongoDB no se estableció, no hay nada que cerrar.')   



# Opcional pero recomendado
    # def get_database_client() -> AsyncIOMotorClient:
    #     """
    #     Función de ayuda para obtener el cliente de la base de datos.
    #     Útil para inyectar en dependencias de FastAPI.
    #     """
    #     if not db["client"]:
    #         raise Exception("La conexión a la base de datos no está establecida.")
    #     return db["client"]

