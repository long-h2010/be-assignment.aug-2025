from pydantic import BaseModel
from datetime import datetime

class NotificationBase(BaseModel):
    message: str
    to_user_id: int
    
class NotificationCreate(NotificationBase):
    pass

class NotificationOut(NotificationBase):
    id: int
    created_at: datetime
    is_read: int

    class Config:
        orm_mode = True
