from app.models import User
from app.schemas import UserCreate
from app.repositories.base_repository import BaseRepository
from sqlalchemy.orm import Session
from typing import Optional

class UserRepository(BaseRepository[User, UserCreate]):
    def __init__(self):
        super().__init__(User)

    def get_user_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()
    
    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def verify_password(self, pwd_context, plain_pw: str, hashed_pw: str) -> bool:
        return pwd_context.verify(plain_pw, hashed_pw)
    
    def add_to_organization(self, db: Session, user_id: int, organization_id: int) -> Optional[User]:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.organization_id = organization_id
            db.commit()
            db.refresh(user)
        return user
