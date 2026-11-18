from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db

app = FastAPI(title="CampusConnect", version="0.1.0")


@app.get("/")
def root():
    return{"message":"Welcome to CampusConnect API"}

@app.get("/health")
def health_check():
    return{"status":"ok"}

@app.get("/db_check")
def db_check(db: Session = Depends(get_db)):
    return {"message": "database created successfully"}