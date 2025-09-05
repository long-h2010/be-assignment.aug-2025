from pydantic import BaseModel
from datetime import datetime

class AttachmentBase(BaseModel):
    file_path: str
    task_id: int
    user_id: int

class AttachmentCreate(AttachmentBase):
    pass

class AttachmentOut(AttachmentBase):
    id: int
    uploaded_at: datetime

    class Config:
        orm_mode = True
