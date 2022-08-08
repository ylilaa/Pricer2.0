from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

from ..models.echeancierModel import Echeancier

class titreBase(BaseModel):
    code : str | None
    description : str | None
    nominal : Optional[int] | None
    dateEmission : Optional[date] | None
    dateJouissance : Optional[date] | None
    dateEcheance : Optional[date] | None
    tauxFacial : Optional[float] | None
    spread : Optional[float] | None
    amort : Optional[str] | None
    lastPriceKamal : Optional[float] | None
    lastPriceManar : Optional[float] | None
    class Config:
        orm_mode = True



class titreCreate(titreBase):
    pass

class titreUpdate(BaseModel):
    code : Optional[str] | None
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
    class Config:
        orm_mode = True


class titre(titreBase):
    id : Optional[int] = Field(default=None, primary_key=True)
    