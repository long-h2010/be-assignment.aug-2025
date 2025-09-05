from sqlalchemy.orm import Session
from app import schemas
from app.repositories import ReportRepository

repo = ReportRepository()

class ReportService:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return repo.get_all(db, skip, limit)

    def get(self, db: Session, rp_id: int):
        return repo.get(db, rp_id)

    def create(self, db: Session, rp: schemas.ReportCreate):
        return repo.create(db, rp)

    def update(self, db: Session, rp_id: int, rp: schemas.ReportCreate):
        return repo.update(db, rp_id, rp)

    def delete(self, db: Session, rp_id: int):
        return repo.delete(db, rp_id)
