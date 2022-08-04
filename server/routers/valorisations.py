from fastapi import APIRouter, Depends, HTTPException
from typing import List

from datetime import date
from schemas import valoSchema
from crud import valorisationCRUD
from db.db_setup import get_db, Session
router = APIRouter()

@router.post("/titres/{titre_code}/echeancier/valorisation",response_model=valoSchema.valoCreate)
def create_titre_valorisation(echeancier_code:str, valorisation: valoSchema.valoCreate, db: Session = Depends(get_db)):
    return valorisationCRUD.create_titre_valorisation(db, echeancier_code, valorisation) 

@router.get("/titres/{titre_code}/echeancier/valorisation",response_model=List[valoSchema.valoBase])
def read_titre_valorisation(titre_code : str, db : Session=Depends(get_db)):
    db_valorisation = valorisationCRUD.get_valorisation_by_titre_code(db,titre_code)
    if db_valorisation is None:
        raise HTTPException(status_code=404, detail="Cette valorisation n'existe pas")
    return db_valorisation

@router.put("/titres/{titre_code}/echeancier/valorisation")
def change_titre_valorisation(code : str, valorisation : valoSchema.valoBase, db : Session=Depends(get_db)):
    db_valorisation = valorisationCRUD.get_valorisation_by_titre_code(db,code)
    if db_valorisation:
        return valorisationCRUD.update_valorisation(db, code, valorisation)
    else:
        raise HTTPException(status_code=404, detail="Cette valorisation n'existe pas")

@router.delete("/titres/{titre_code}/echeancier/valorisation",response_model=valoSchema.valoBase)
def destroy_titre_valorisation(code : str, date : date,db : Session=Depends(get_db)):
    db_valorisation = valorisationCRUD.delete_valorisation(code,db,date)
    if db_valorisation:
        return valorisationCRUD.delete_valorisation(code, db, date)
    if db_valorisation is None:
        raise HTTPException(status_code=404, detail="Cette valorisation n'existe pas")
    



    