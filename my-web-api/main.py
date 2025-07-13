from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Create a FastAPI application instance
app = FastAPI()

# Define your first API endpoint (route)
@app.get("/", tags=['root'])
async def read_root():
    nombre = 'Gustavo'
    html_content = f'<h1>Hello {nombre} From API, this is root</h1>'
    return HTMLResponse(html_content)


# Define your first API endpoint (route)
@app.get("/cat", tags=['cat'])
async def read_root():
    nombre = 'Cat'
    html_content = f'<h1>Hello {nombre} From API, this is CAT Endpoint</h1>'
    return HTMLResponse(html_content)