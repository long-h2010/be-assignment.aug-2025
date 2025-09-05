from sqlalchemy.orm import Session
from app import schemas
from app.repositories import CommentRepository, TaskRepository

cmt_repo = CommentRepository()
task_repo = TaskRepository()

class CommentService:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return cmt_repo.get_all(db, skip, limit)

    def get(self, db: Session, cmt_id: int):
        return cmt_repo.get(db, cmt_id)

    def create(self, db: Session, cmt: schemas.CommentCreate, user_id: int):
        if task_repo.get(db, cmt.task_id) is None:
            raise ValueError("Task does not exist")
        
        cmt_data = cmt.dict()
        cmt_data['user_id'] = user_id
        return cmt_repo.create(db, cmt_data)

    def update(self, db: Session, cmt_id: int, cmt: schemas.CommentCreate):
        return cmt_repo.update(db, cmt_id, cmt)

    def delete(self, db: Session, cmt_id: int):
        return cmt_repo.delete(db, cmt_id)
