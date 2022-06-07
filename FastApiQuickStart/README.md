## This document is all you need to get your FastApi code working with Python ##

### Step 1: ###
Install the following packages in your Python 3.8+ environment
```
fastapi==0.78.0
uvicorn==0.17.6
httpx==0.23.0
```

### Step 2: ###

Create two folders name "static" and "templates" in the same root where your main python "app.py" will be added in Step 3.
Create a simple index.html and add it to templates folder. 

- |-static
- |-templates
  -  |-index.html   
- |-app.py

### Step 3: ###

Create a File name app.py and add the folowing code:

```
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.requests import Request
import uvicorn

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
    return 'Hello from FastApi Python Backend'


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000)
```

### Step 4: ###

You can run your code from command prompt as below:

$ uvicorn app:app --reload --port 8000
