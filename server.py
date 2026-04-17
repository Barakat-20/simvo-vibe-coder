from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from request import search_species

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "https://simvo-vibe-coder-faidat.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/hello")
async def hello():
    return {"message": "Hello!"}

@app.get("/species")
async def species(search: str):
    extracted_data = await search_species(search)
    return {"data": extracted_data}

@app.get("/", response_class=HTMLResponse)
async def return_site(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})