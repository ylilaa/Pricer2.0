from pydantic import BaseModel
from datetime import date
from typing import Optional

class valoBase(BaseModel):
    dateValo : date | None
    courbe : str | None
    price : float | None
    class Config:
        orm_mode = True

    

class valoCreate(valoBase):
    pass

class valoUpdate(BaseModel):
    dateValo : Optional[date]
    courbe : Optional[str]
    price : Optional[float]


class valo(valoBase):
    id : int
    echeancier_id : int
    class Config:
        orm_mode = True
