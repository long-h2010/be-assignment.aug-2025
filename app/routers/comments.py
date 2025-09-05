from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas
from app.database import get_db
from app.services import CommentService
from app.core.security import get_current_user

router = APIRouter(prefix="/comments", tags=["Comments"])
service = CommentService()

@router.get("/", response_model=List[schemas.CommentOut])
def read_comments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip, limit)

@router.get("/{cmt_id}", response_model=schemas.CommentOut)
def read_comment(cmt_id: int, db: Session = Depends(get_db)):
    return service.get(db, cmt_id)

@router.post("/", response_model=schemas.CommentOut)
def create_comment(cmt: schemas.CommentCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return service.create(db, cmt, current_user.id)

@router.put("/{cmt_id}", response_model=schemas.CommentOut)
def update_comment(cmt_id: int, cmt: schemas.CommentCreate, db: Session = Depends(get_db)):
    return service.update(db, cmt_id, cmt)

@router.delete("/{cmt_id}", response_model=schemas.CommentOut)
def delete_comment(cmt_id: int, db: Session = Depends(get_db)):
    return service.delete(db, cmt_id)
