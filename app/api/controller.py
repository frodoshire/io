from fastapi import FastAPI
from app.resource.model.basemodel import Shortener
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="URL Shortener")
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

@app.post("/shortener")
def create_shortener(shortener: Shortener):
    return shortener
