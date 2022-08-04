from pydantic import BaseModel
from typing import Optional

class TitleListInputForm(BaseModel):
    list : Optional[str] ## un path fichier ?
    dateValo : Optional[str]
    courbeBAM : Optional[bool] 
    courbeCustom : Optional[bool] ## un path fichier ?