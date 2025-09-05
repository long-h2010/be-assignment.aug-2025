from sqlalchemy.orm import Session
from app import schemas
from app.repositories import ProjectRepository

repo = ProjectRepository()

class ProjectService:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return repo.get_all(db, skip, limit)

    def get(self, db: Session, prj_id: int):
        return repo.get(db, prj_id)

    def create(self, db: Session, prj: schemas.ProjectCreate):
        return repo.create(db, prj)

    def update(self, db: Session, prj_id: int, prj: schemas.ProjectCreate):
        return repo.update(db, prj_id, prj)

    def delete(self, db: Session, prj_id: int):
        return repo.delete(db, prj_id)
