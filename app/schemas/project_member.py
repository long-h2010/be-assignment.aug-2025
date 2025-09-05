from pydantic import BaseModel
from datetime import datetime

class ProjectMemberBase(BaseModel):
    project_id: int
    user_id: int

class ProjectMemberCreate(ProjectMemberBase):
    pass

class ProjectMemberOut(ProjectMemberBase):
    id: int
    joined_at: datetime

    class Config:
        orm_mode = True
