from fastapi import APIRouter, Depends, HTTPException
from schemas import echeancierSchema, titreSchema
from crud import echeancierCRUD
from db.db_setup import get_db, Session
router = APIRouter()



@router.post("/titres/{titre_code}/echeancier",response_model=echeancierSchema.echeancierCreate)
def create_titre_echeancier(titre_code:str, echeancier: echeancierSchema.echeancierCreate, db: Session = Depends(get_db)):
    db_echeancier = echeancierCRUD.get_echeancier_by_titre_code(db,titre_code)
    if db_echeancier:
        raise HTTPException(status_code=400, detail="Cet échéancier existe déjà")
    return echeancierCRUD.create_titre_echeancier(db, titre_code, echeancier) 

@router.get("/titres/{titre_code}/echeancier",response_model=echeancierSchema.echeancier)
def read_titre_echeancier(titre_code : str, db : Session=Depends(get_db)):
    db_echeancier = echeancierCRUD.get_echeancier_by_titre_code(db,titre_code)
    if db_echeancier is None:
        raise HTTPException(status_code=404, detail="Cet écheancier n'existe pas")
    return db_echeancier

@router.put("/titres/{titre_code}/echeancier")
def change_titre_echeancier(code : str, echeancier : echeancierSchema.echeancierBase, db : Session=Depends(get_db)):
    db_echeancier = echeancierCRUD.get_echeancier_by_titre_code(db,code)
    if db_echeancier:
        return echeancierCRUD.update_echeancier(db, code, echeancier)
    else:
        raise HTTPException(status_code=404, detail="Cet echeancier n'existe pas")

@router.delete("/titres/{titre_code}/echeancier",response_model=echeancierSchema.echeancier)
def destroy_titre_echeancier(code : str,db : Session=Depends(get_db)):
    db_echeancier = echeancierCRUD.get_echeancier_by_titre_code(db,code)
    if db_echeancier:
        return echeancierCRUD.delete_echeancier(code, db)
    if db_echeancier is None:
        raise HTTPException(status_code=404, detail="Cet echeancier n'existe pas")
    



    