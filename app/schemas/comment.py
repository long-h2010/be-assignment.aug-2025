from pydantic import BaseModel
from datetime import datetime

class CommentBase(BaseModel):
    content: str
    task_id: int

class CommentCreate(CommentBase):
    pass

class CommentOut(CommentBase):
    id: int
    created_at: datetime
    user_id: int

    class Config:
        orm_mode = True
