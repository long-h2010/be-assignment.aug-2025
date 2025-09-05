from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.config import settings
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.users import User, UserRole
from app.models.tasks import Task

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE = settings.ACCESS_TOKEN_EXPIRE
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def create_access_token(data: dict, minutes: int = ACCESS_TOKEN_EXPIRE):
    to_encode = {**data, "exp": datetime.utcnow() + timedelta(minutes=minutes)}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    credentials_exc = HTTPException(status_code=401, detail="Could not validate credentials")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        uid = int(payload.get("sub"))
    except (JWTError, ValueError):
        raise credentials_exc
    
    user = db.query(User).get(uid)
    if not user:
        raise credentials_exc
    return user

def require_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Only admins can perform this action")
    return current_user

def check_task_ownership(task: Task, current_user: User = Depends(get_current_user)):
    if task.assignee_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this task")
    return True
