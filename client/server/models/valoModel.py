from sqlalchemy import DateTime, Column, Float,ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..db.db_setup import Base


class Valorisation(Base):
    __tablename__ = "valorisations"

    id = Column(Integer, primary_key=True, index=True)
    dateValo = Column(DateTime)
    courbe = Column(String)
    price = Column(Float)
    echeancier_id = Column(Integer, ForeignKey("echeanciers.id"))
    
    echeancier = relationship("Echeancier", back_populates="valorisations")
    
    