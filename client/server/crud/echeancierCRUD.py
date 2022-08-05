from sqlalchemy.orm import Session

from ..models import echeancierModel
from ..schemas import echeancierSchema


def create_titre_echeancier(db: Session, code :str, echeancier: echeancierSchema.echeancierCreate):
    db_echeancier = echeancierModel.Echeancier(capitalAmorti = echeancier.capitalAmorti,
                                                capitalRestant = echeancier.capitalRestant,
                                                dateTombee = echeancier.dateTombee,
                                                couponBrut = echeancier.couponBrut,
                                                source = "Kamal",
                                                titre_code = code,)
                                                
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
    db_echeancier.source = "kamal"
    db.commit()
    db.refresh(db_echeancier)
    


def delete_echeancier(code : str, db : Session):
    db_echeancier = db.query(echeancierModel.Echeancier).filter(echeancierModel.Echeancier.titre_code == code).first()
    db.delete(db_echeancier)
    db.commit()
