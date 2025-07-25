from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from core.database import db_client
from core.config import settings

app_title = settings.app_name
app_version = settings.app_version


router = APIRouter(tags=['root'])

# root endpoint
@router.get("/")
async def read_root_endpoint():
    """
    Endpoint de la raíz de la API.
    Muestra el nombre y la versión de la aplicación.
    """
    if db_client['client'] is not None:
        html_content = f"""<h1>Bienvenido a la API: {app_title}</h1>
                    <p>Versión: {app_version} | DB: {db_client['client'].address} </p> 
                    <p>Visita <a href="/docs">/docs</a> para ver la documentación de la APIII</p>
                    <p>Visita <a href="/cat">/cat</a> para ver un endpoint de prueba</p>

        """
        return HTMLResponse(html_content)
    


# cat endpoint
@router.get("/cat", tags=['root'])
async def read_cat_endpoint():
    nombre = 'gatito'
    html_content = f'<h1>Hello {nombre} From API, this is CAT(ANTONIA mi gatito feliz ) Endpoint</h1>'
    return HTMLResponse(html_content)