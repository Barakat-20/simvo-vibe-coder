# server.py
from fastapi import FastAPI, Query
from request import search_species

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello!"}

@app.get("/species")
async def species(search: str = Query(..., description="Species name to search for")):
    print("I got: " + search)
    extracted_data = search_species(search)
    return {"data": extracted_data}