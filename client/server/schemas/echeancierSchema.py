from pydantic import BaseModel
from datetime import date
from .valoSchema import valo
from .titreSchema import titre
from typing import List, Optional

class echeancierBase(BaseModel):
    capitalAmorti : float | None
    capitalRestant : float | None
    dateTombee : date | None
    couponBrut : float | None
    titre_code : str | None
    class Config:
        orm_mode = True

class echeancierUpdate(BaseModel):
    capitalAmorti : Optional[float] 
    capitalRestant : Optional[float]
    dateTombee : Optional[date]
    couponBrut : Optional[float]
    class Config:
        orm_mode = True


class echeancierCreate(echeancierBase):
    pass
    class Config:
        orm_mode = True

class echeancier(echeancierBase):
    valorisations : List[valo] 
    class Config:
        orm_mode = True
    
    