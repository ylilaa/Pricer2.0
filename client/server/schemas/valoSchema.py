from pydantic import BaseModel
from datetime import date
from typing import Optional

class valoBase(BaseModel):
    dateValo : date
    courbe : str
    price : float
    class Config:
        orm_mode = True
    

class valoCreate(valoBase):
    pass

class valoUpdate(BaseModel):
    dateValo : Optional[date]
    courbe : Optional[str]
    price : Optional[float]
    class Config:
        orm_mode = True


class valo(valoBase):
    id : int
    echeancier_id : int
    class Config:
        orm_mode = True
