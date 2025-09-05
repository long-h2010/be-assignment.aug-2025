from pydantic import BaseModel
from app.schemas.organization import OrganizationOut

class ProjectBase(BaseModel):
    name: str

class ProjectCreate(ProjectBase):
    organization_id: int

class ProjectOut(ProjectBase):
    id: int
    organization: OrganizationOut

    class Config:
        orm_mode = True
