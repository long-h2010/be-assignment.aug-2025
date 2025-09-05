from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.user import UserCreate
from typing import Optional
from passlib.context import CryptContext
from .user_repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
user_repository = UserRepository()

class AuthRepository:
    def create_user(self, db: Session, user_in: UserCreate) -> User:
        hashed_pw = pwd_context.hash(user_in.password)
        user_in.password = hashed_pw
        return user_repository.create(db, user_in)

    def get_user_by_username(self, db: Session, username: str) -> Optional[User]:
        return user_repository.get_user_by_username(db, username)
    
    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        return user_repository.get_user_by_email(db, email)

    def verify_password(self, plain_pw: str, hashed_pw: str) -> bool:
        return user_repository.verify_password(pwd_context, plain_pw, hashed_pw)
