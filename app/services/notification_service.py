from sqlalchemy.orm import Session
from app import schemas
from app.repositories import NotificationRepository
import redis
import json

repo = NotificationRepository()
r = redis.Redis(host="redis", port=6379, decode_responses=True)

class NotificationService:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return repo.get_all(db, skip, limit)

    def get(self, db: Session, noti_id: int):
        return repo.get(db, noti_id)

    def create(self, db: Session, noti: schemas.NotificationCreate):
        noti_data = repo.create(db, noti)
        payload = {
            "id": noti_data.id,
            "message": noti_data.message,
            "to_user_id": noti_data.to_user_id,
            "created_at": str(noti_data.created_at),
            "is_read": noti_data.is_read
        }
        r.publish(f"user:{noti.to_user_id}:notifications", json.dumps(payload))

    def update(self, db: Session, noti_id: int, noti: schemas.NotificationCreate):
        return repo.update(db, noti_id, noti)

    def delete(self, db: Session, noti_id: int):
        return repo.delete(db, noti_id)
