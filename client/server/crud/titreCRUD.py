from sqlalchemy.orm import Session

from ..models import titreModel
from ..schemas import titreSchema

def create_titre(db: Session, titre: titreSchema.titreCreate):
    db_titre = titreModel.Titre(code= titre.code,
                                description= titre.description,
                                nominal= titre.nominal,
                                dateEmission= titre.dateEmission,
                                dateEcheance= titre.dateEcheance,
                                dateJouissance= titre.dateJouissance,
                                tauxFacial= titre.tauxFacial,
                                spread= titre.spread,
                                amort=titre.amort,
                                lastPriceManar= titre.lastPriceManar)
    db.add(db_titre)
    db.commit()
    db.refresh(db_titre)
    return "Titre ajouté à la base Access avec succès"


def get_titre_by_code(db : Session, titre_code: str):
    return db.query(titreModel.Titre).filter(titreModel.Titre.code == titre_code).first()

def get_titre_by_id(db : Session, titre_id: int):
    return db.query(titreModel.Titre).filter(titreModel.Titre.id == titre_id).first()


def get_titres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(titreModel.Titre).offset(skip).limit(limit).all()

def update_titre(db : Session, code_titre: str, titre: titreSchema.titreUpdate):
    db_titre = db.query(titreModel.Titre).filter(titreModel.Titre.code == code_titre).first()
    db_titre.code = titre.code
    db_titre.description= titre.description
    db_titre.nominal= titre.nominal
    db_titre.dateEmission= titre.dateEmission
    db_titre.dateEcheance= titre.dateEcheance
    db_titre.dateJouissance= titre.dateJouissance
    db_titre.tauxFacial= titre.tauxFacial
    db_titre.spread= titre.spread
    db_titre.amort=titre.amort
    db_titre.lastPriceManar= titre.lastPriceManar
    db.commit()
    db.refresh(db_titre)
    return db_titre

def delete_titre(code : str, db : Session):
    titre = db.query(titreModel.Titre).filter(titreModel.Titre.code == code).first()
    db.delete(titre)
    db.commit()
    return "Titre supprimé de la base Access avec succès"


