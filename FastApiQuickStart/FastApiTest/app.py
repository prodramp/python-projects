# -----------------
# fastapi==0.78.0
# uvicorn==0.17.6
# httpx==0.23.0
# ----------------
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from fastapi.requests import Request
import uvicorn

# api handlers
from api import PostApiHandler


# ASGI Server Gateway Initialization
app = FastAPI(title="App Title", description="App Description", version="0.0.1")

# Mounted Static Folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Adding Templates
templates = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse)
def get_home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Home"})


@app.get('/hello', response_class=PlainTextResponse)
def say_hello():
    return 'Hello from FastApi Python Backend to VsCode'


@app.post("/getQueryData", tags=["Post Api Section"], response_class=JSONResponse)
async def get_query_data(query: PostApiHandler.PostApiQuery):
    return PostApiHandler.get_query_response(query)


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000)
