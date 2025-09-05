from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])
service = AuthService()

@router.post("/register", response_model=schemas.user.UserOut)
def register(user_in: schemas.user.UserCreate, db: Session = Depends(get_db)):
    return service.register(db, user_in)

@router.post("/login")
def login(user_in: schemas.user.UserLogin, db: Session = Depends(get_db)):
    return service.login(db, user_in.username, user_in.password)
