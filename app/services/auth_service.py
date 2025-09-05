from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.auth_repository import AuthRepository
from app.schemas.user import UserCreate
from app.core import security

repo = AuthRepository()

class AuthService:
    def register(self, db: Session, user_in: UserCreate):
        existing_username = repo.get_user_by_username(db, user_in.username)
        if existing_username:
            raise HTTPException(status_code=400, detail="Username already exists")
        
        existing_email = repo.get_user_by_email(db, user_in.email)
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        return repo.create_user(db, user_in)

    def login(self, db: Session, username: str, password: str):
        user = repo.get_user_by_username(db, username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if not repo.verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = security.create_access_token({"sub": str(user.id)})
        return {"access_token": token, "token_type": "bearer", "user": user}
