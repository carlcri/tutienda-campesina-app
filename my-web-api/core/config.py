import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

class Settings:
    """
    Clase para manejar las configuraciones de la aplicación
    """
    def conection_string(self) -> str: 
        mongo_details = os.environ["MONGO_DETAILS"]
        return mongo_details
    
    app_version = os.environ["APP_VERSION"]
    app_name = os.environ["APP_NAME"]
    

# Instancia de Settings para ser importada y usada en toda la aplicación
settings = Settings()



