# server.py
from fastapi import FastAPI, Query, Request
from request import search_species
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/hello")
async def hello():
    return {"message": "Hello!"}

@app.get("/species")
async def species(search: str = Query(..., description="Species name to search for")):
    print("I got: " + search)
    extracted_data = search_species(search)
    return {"data": extracted_data}

@app.get("/", response_class=HTMLResponse)
async def return_site(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})