from pydantic import BaseModel
from typing import Optional

class fundInputForm(BaseModel):
    name : Optional[str]
    AN : Optional[str]
    SR : Optional[str]
    PEncours : Optional[str]
    CEncours : Optional[str]
    Agios : Optional[str]
    FdG : Optional[str]
    Banque : Optional[str]
    Levier : Optional[str]
    RREPO : Optional[str]
    BDC : Optional[str]