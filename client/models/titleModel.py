from pydantic import BaseModel
from typing import Optional
from datetime import datetime




class titleInputForm(BaseModel):
    code : Optional[str]
    dateValo : Optional[str]
    courbeBAM : Optional[str]
    courbeCustom : Optional[str]

