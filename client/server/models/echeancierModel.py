from sqlalchemy import DateTime, Column, Float,ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..db.db_setup import Base



class Echeancier(Base):
    __tablename__ = "echeanciers"

    id = Column(Integer, primary_key=True, index=True)
    capitalAmorti = Column(Float)
    capitalRestant = Column(Float)
    dateTombee = Column(DateTime)
    couponBrut = Column(Float)
    source = Column(String)
    titre_code = Column(String, ForeignKey("titres.code"))
    titre = relationship("Titre", back_populates="echeancier")
    valorisations = relationship("Valorisation",back_populates="echeancier")