from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas
from app.database import get_db
from app.services import UserService
from app.core.security import require_admin

router = APIRouter(prefix="/users", tags=["Users"])
service = UserService()

@router.get("/", response_model=List[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip, limit)

@router.get("/{user_id}", response_model=schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return service.get(db, user_id)

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.create(db, user)

@router.put("/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.update(db, user_id, user)

@router.delete("/{user_id}", response_model=schemas.UserOut)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return service.delete(db, user_id)

@router.put("/{user_id}/add-to-organization", response_model=schemas.UserOut)
def add_user_to_organization(user_id: int, organization: schemas.UserUpdateOrganization, db: Session = Depends(get_db), current_user = Depends(require_admin)):
    return service.add_to_organization(db, user_id, organization.organization_id)
