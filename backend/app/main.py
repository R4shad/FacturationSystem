from fastapi import FastAPI
from .database import engine, Base
from .models import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FacturationSystem API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to FacturationSystem API"}