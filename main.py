from typing import Annotated

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import ai
from input import Filter

app = FastAPI()


# cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["get"],
    allow_headers=["application/json"],
)


@app.get("/api/v1")
def index():
    return "<html><body><h1>Cheap Property Finder API</hjson></body></html>"


@app.get("/api/v1/search")
def find_house(input: Annotated[Filter, Query()]):
    response = ai.find_house(input)
    return response


app.mount("/", StaticFiles(directory="static", html=True), name="static")
