from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas
from app.database import get_db
from app.services import TaskService
from app.core.security import require_admin

router = APIRouter(prefix="/tasks", tags=["Tasks"])
service = TaskService()

@router.get("/", response_model=List[schemas.TaskOut])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip, limit)

@router.get("/{task_id}", response_model=schemas.TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    return service.get(db, task_id)

@router.post("/", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), current_user = Depends(require_admin)):
    return service.create(db, task)

@router.put("/{task_id}", response_model=schemas.TaskUpdate)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    return service.update(db, task_id, task)

@router.delete("/{task_id}", response_model=schemas.TaskOut)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return service.delete(db, task_id)
