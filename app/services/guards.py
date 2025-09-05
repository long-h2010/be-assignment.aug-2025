from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.users import User
from app.enums import UserRole, TaskStatus

def ensure_assign_permission(assignee_id: int, actor: User):
    if actor.role in (UserRole.admin, UserRole.manager):
        return
    if assignee_id != actor.id:
        raise HTTPException(status_code=403, detail="Members can assign only to themselves")

def ensure_due_date_future(due_dt):
    from datetime import datetime
    if due_dt and due_dt < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Due date must be today or in the future")

def ensure_forward_status(old: TaskStatus, new: TaskStatus):
    order = [TaskStatus.todo, TaskStatus.in_progress, TaskStatus.done]
    if order.index(new) < order.index(old):
        raise HTTPException(status_code=400, detail="Status can only move forward")
