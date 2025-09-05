from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReportBase(BaseModel):
    project_id: int
    type: str
    data: Optional[str] = None


class ReportCreate(ReportBase):
    pass


class ReportOut(ReportBase):
    id: int

    class Config:
        orm_mode = True
