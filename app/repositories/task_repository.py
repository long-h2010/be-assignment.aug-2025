from app.models import Task
from app.schemas import TaskCreate, TaskUpdate
from app.repositories.base_repository import BaseRepository
from sqlalchemy.orm import Session

class TaskRepository(BaseRepository[Task, TaskCreate]):
    def __init__(self):
        super().__init__(Task)

    def update_task(self, db: Session, task_id: int, task_data: TaskUpdate) -> Task:
        db_obj = self.get(db, task_id)
        for field, value in task_data.dict(exclude_unset=True).items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj
