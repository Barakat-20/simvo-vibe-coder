from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from request import search_species
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/hello")
async def hello():
    logger.info("Hello endpoint called")
    return {"message": "Hello!"}

@app.get("/species")
async def species(search: str):
    logger.info(f"Species endpoint called with search: {search}")
    try:
        extracted_data = await search_species(search)
        logger.info(f"Successfully retrieved data for: {search}")
        return {"data": extracted_data}
    except Exception as e:
        logger.error(f"Error searching species: {str(e)}")
        raise

@app.get("/", response_class=HTMLResponse)
async def return_site(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})