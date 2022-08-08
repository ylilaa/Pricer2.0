from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..models import echeancierModel
from ..schemas import echeancierSchema
from ..crud.titreCRUD import get_titre_by_code

def create_titre_echeancier(db: Session, code :str, echeancier: echeancierSchema.echeancierCreate):
    isCode = get_titre_by_code(db, code)
    if isCode is None:
        raise HTTPException(status_code=404, detail="Ce titre n'existe pas dans la base, cet échéancier sera ignoré ")
        return {"code du titre": code}

    db_echeancier = echeancierModel.Echeancier(capitalAmorti = echeancier.capitalAmorti,
                                                capitalRestant = echeancier.capitalRestant,
                                                dateTombee = echeancier.dateTombee,
                                                couponBrut = echeancier.couponBrut,
                                                titre_code = echeancier.titre_code,)
                                                
    db.add(db_echeancier)
    db.commit()
    db.refresh(db_echeancier)
    return "Echeancier ajouté à la base Access avec succès"


def get_echeancier_by_titre_code(db : Session, titre_code: str):
    return db.query(echeancierModel.Echeancier).filter(echeancierModel.Echeancier.titre_code == titre_code).first()


def update_echeancier(db:Session,code:str,echeancier:echeancierSchema.echeancier):
    db_echeancier = db.query(echeancierModel.Echeancier).filter(echeancierModel.Echeancier.titre_code == code).first()
    db_echeancier.capitalAmorti = echeancier.capitalAmorti
    db_echeancier.capitalRestant = echeancier.capitalRestant
    db_echeancier.dateTombee = echeancier.dateTombee
    db_echeancier.couponBrut = echeancier.couponBrut
    db.commit()
    db.refresh(db_echeancier)
    


def delete_echeancier(code : str, db : Session):
    db_echeancier = db.query(echeancierModel.Echeancier).filter(echeancierModel.Echeancier.titre_code == code).first()
    db.delete(db_echeancier)
    db.commit()
