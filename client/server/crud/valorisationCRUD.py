from sqlalchemy.orm import Session

from ..models import valoModel,echeancierModel
from ..schemas import valoSchema,echeancierSchema
from ..crud import echeancierCRUD


def create_titre_valorisation(db: Session, titre_code :str, valorisation: valoSchema.valoCreate):
    db_echeancier = echeancierCRUD.get_echeancier_by_titre_code(db,titre_code)
    db_valorisation = valoModel.Valorisation(dateValo = valorisation.dateValo,
                                            courbe = valorisation.courbe,
                                            price = valorisation.price,
                                            echeancier_id = db_echeancier.id)
    db.add(db_valorisation)
    db.commit()
    db.refresh(db_valorisation)
    return "Valorisation ajoutée à la base Access avec succès"


def get_valorisation_by_titre_code(db : Session, echeancier_code: str):
    db_echeancier = db.query(echeancierModel.Echeancier).filter(echeancierModel.Echeancier.titre_code == echeancier_code).first()
    return db.query(valoModel.Valorisation).filter(valoModel.Valorisation.echeancier_id == db_echeancier.id).first()


def update_valorisation(db:Session,code:str,valorisation:valoSchema.valoUpdate):
    db_echeancier = echeancierCRUD.get_echeancier_by_titre_code(db,code)
    db_valorisation = db.query(valoModel.Valorisation).filter(valoModel.Valorisation.echeancier_id == db_echeancier.id).first()
    db_valorisation.dateValo = valorisation.dateValo
    db_valorisation.courbe = valorisation.courbe
    db_valorisation.price = valorisation.price
    db.commit()
    db.refresh(db_valorisation)
    


def delete_valorisation(code : str, db : Session):
    db_echeancier = echeancierCRUD.get_echeancier_by_titre_code(db,code)
    db_valorisation = db.query(valoModel.Valorisation).filter(valoModel.Valorisation.echeancier_id == db_echeancier.id).first()
    db.delete(db_valorisation)
    db.commit()
