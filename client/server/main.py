from fastapi import FastAPI
from .db.db_setup import Base, SessionLocal, engine
from .routers import titres,echeanciers,valorisations

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
