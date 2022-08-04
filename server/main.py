from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db_setup import Base, SessionLocal
from routers import titres,echeanciers,valorisations


from db.db_setup import engine

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app = FastAPI()

app.include_router(titres.router)
app.include_router(echeanciers.router)
app.include_router(valorisations.router)
