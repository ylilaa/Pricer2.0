from fastapi import APIRouter, Depends, HTTPException
from ..schemas import titreSchema
from ..crud import titreCRUD
from ..db.db_setup import get_db, Session
router = APIRouter()

@router.get("/titres/", response_model=list[titreSchema.titre])
def read_titres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    titres = titreCRUD.get_titres(db, skip=skip, limit=limit)
    return titres

@router.get("/titres/{titre_code}",response_model=titreSchema.titre)
def read_titre(titre_code : str, db : Session=Depends(get_db)):
    db_titre = titreCRUD.get_titre_by_code(db,titre_code=titre_code)
    if db_titre is None:
        raise HTTPException(status_code=404, detail="Ce titre n'existe pas")
    return db_titre

@router.post("/titres/",response_model=titreSchema.titreCreate)
def create_titre(titre: titreSchema.titreCreate, db: Session = Depends(get_db)):
    db_titre = titreCRUD.get_titre_by_code(db, titre_code=titre.code)
    if db_titre:
        raise HTTPException(status_code=400, detail="Ce titre existe déjà")
    return titreCRUD.create_titre(db=db, titre=titre) 

@router.put("/titres/{code}",response_model=titreSchema.titre)
def change_titre(code : str, titre : titreSchema.titreUpdate, db : Session=Depends(get_db)):
    db_titre = titreCRUD.get_titre_by_code(db, code)
    if db_titre:
        return titreCRUD.update_titre(db, code, titre)
    else:
        raise HTTPException(status_code=404, detail="Ce titre n'existe pas")

@router.delete("/titres/{code}",response_model=titreSchema.titre)
def destroy_titre(code : str,db : Session=Depends(get_db)):
    db_titre = titreCRUD.get_titre_by_code(db, code)
    if db_titre:
        return titreCRUD.delete_titre(code, db)
    if db_titre is None:
        raise HTTPException(status_code=404, detail="Ce titre n'existe pas")
