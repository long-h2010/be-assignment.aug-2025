from app.models import Notification
from app.schemas import NotificationCreate
from app.repositories.base_repository import BaseRepository

class NotificationRepository(BaseRepository[Notification, NotificationCreate]):
    def __init__(self):
        super().__init__(Notification)

    def mark_as_read(self, db, noti_id: int):
        noti = db.query(Notification).filter(Notification.id == noti_id).first()
        if noti:
            noti.is_read = True
            db.commit()
            db.refresh(noti)
        return noti
