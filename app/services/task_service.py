from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import schemas
from app.repositories import TaskRepository
from app.enums import TaskStatus

repo = TaskRepository()
work_follows = [TaskStatus.TODO, TaskStatus.IN_PROGRESS, TaskStatus.DONE]

class TaskService:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return repo.get_all(db, skip, limit)

    def get(self, db: Session, task_id: int):
        task = repo.get(db, task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")    
        return task

    def create(self, db: Session, task: schemas.TaskCreate):
        return repo.create(db, task)

    def update(self, db: Session, task_id: int, task_data: schemas.TaskUpdate):
        task = repo.get(db, task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")    
        
        if task_data.status is not None and task_data.status != task.status:
            current_index = work_follows.index(task.status)
            new_index = work_follows.index(task_data.status)
            if abs(new_index - current_index) != 1:
                raise HTTPException(status_code=400, detail="Invalid status transition")
            
        return repo.update_task(db, task_id, task_data)

    def delete(self, db: Session, task_id: int):
        task = repo.get(db, task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")    
        return repo.delete(db, task_id)
    
    def update_status(self, db: Session, task_id: int, new_status: str):
        task = repo.update_status(db, task_id, new_status)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")    
        return task
