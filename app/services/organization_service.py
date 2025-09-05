from sqlalchemy.orm import Session
from app import schemas
from app.repositories import OrganizationRepository

repo = OrganizationRepository()

class OrganizationService:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return repo.get_all(db, skip, limit)

    def get(self, db: Session, org_id: int):
        return repo.get(db, org_id)

    def create(self, db: Session, org: schemas.OrganizationCreate):
        return repo.create(db, org)

    def update(self, db: Session, org_id: int, org: schemas.OrganizationCreate):
        return repo.update(db, org_id, org)

    def delete(self, db: Session, org_id: int):
        return repo.delete(db, org_id)
