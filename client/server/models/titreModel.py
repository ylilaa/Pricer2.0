from sqlalchemy import DateTime, Column, Float,ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..db.db_setup import Base
from ..models.echeancierModel import Echeancier


class Titre(Base):
    __tablename__ = "titres"

    id = Column(Integer, index=True)
    code = Column(String, unique=True, primary_key=True)
    description = Column(String)
    nominal = Column(Integer)
    dateEmission = Column(DateTime)
    dateJouissance = Column(DateTime)
    dateEcheance = Column(DateTime)
    tauxFacial = Column(Float)
    spread = Column(Float)
    amort = Column(String)
    lastPriceKamal = Column(Float)
    lastPriceManar = Column(Float)

    echeancier = relationship("Echeancier",back_populates="titre")
    
