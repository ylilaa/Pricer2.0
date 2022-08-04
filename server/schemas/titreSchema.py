from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

from models.echeancierModel import Echeancier

class titreBase(BaseModel):
    code : str | None
    description : str | None
    nominal : int | None
    dateEmission : date | None
    dateJouissance : date | None
    dateEcheance : date | None
    tauxFacial : float | None
    spread : float | None
    amort : str | None
    lastPriceKamal : float | None
    lastPriceManar : float | None



class titreCreate(titreBase):
    pass 

class titreUpdate(BaseModel):
    description : Optional[str] = None
    nominal : Optional[int] = None
    dateEmission : Optional[date] = None
    dateJouissance : Optional[date] = None
    dateEcheance : Optional[date] = None
    tauxFacial : Optional[float] = None
    spread : Optional[float] = None
    amort : Optional[str] = None
    lastPriceKamal : Optional[float] = None 
    lastPriceManar : Optional[float] = None
    

class titre(titreBase):
    id : Optional[int] = Field(default=None, primary_key=True)
    class Config:
        orm_mode = True
