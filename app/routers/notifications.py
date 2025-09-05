from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas
from app.database import get_db
from app.services import NotificationService

router = APIRouter(prefix="/Notifications", tags=["Notifications"])
service = NotificationService()

@router.get("/", response_model=List[schemas.NotificationOut])
def read_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip, limit)

@router.get("/{noti_id}", response_model=schemas.NotificationOut)
def read_notification(noti_id: int, db: Session = Depends(get_db)):
    return service.get(db, noti_id)

@router.post("/", response_model=schemas.NotificationOut)
def create_notification(noti: schemas.NotificationCreate, db: Session = Depends(get_db)):
    return service.create(db, noti)

@router.delete("/{noti_id}", response_model=schemas.NotificationOut)
def delete_notification(noti_id: int, db: Session = Depends(get_db)):
    return service.delete(db, noti_id)

