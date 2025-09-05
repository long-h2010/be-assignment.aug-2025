from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.repositories import UserRepository, OrganizationRepository

user_repo = UserRepository()
user_repo = OrganizationRepository()

class UserService:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return user_repo.get_all(db, skip, limit)

    def get(self, db: Session, user_id: int):
        user = user_repo.get(db, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def create(self, db: Session, user: schemas.UserCreate):
        return user_repo.create(db, user)

    def update(self, db: Session, user_id: int, user: schemas.UserCreate):
        user = user_repo.get(db, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user_repo.update(db, user_id, user)

    def delete(self, db: Session, user_id: int):
        user = user_repo.get(db, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user_repo.delete(db, user_id)
    
    def add_to_useranization(self, db: Session, user_id: int, org_id: int):
        if user_repo.get(db, user_id) is None:
            raise HTTPException(status_code=400, detail="User does not exist")
        
        if user_repo.get(db, org_id) is None:
            raise HTTPException(status_code=400, detail="Organization does not exist") 
        
        return user_repo.add_to_useranization(db, user_id, user_id)
