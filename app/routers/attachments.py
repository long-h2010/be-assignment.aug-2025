from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from typing import List
from pathlib import Path
from app import schemas
from app.database import get_db
from app.services import AttachmentService
from app.config import settings

router = APIRouter(prefix="/attachments", tags=["attachments"])
service = AttachmentService()

UPLOAD_DIR = Path(settings.UPLOAD_DIR)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

MAX_FILE_SIZE = settings.MAX_FILE_SIZE 
MAX_FILE_PER_TASK = settings.MAX_FILE_PER_TASK

@router.post("/task/{task_id}", response_model=List[schemas.AttachmentOut])
async def upload_attachments(task_id: int, files: List[UploadFile] = File(...), db: Session = Depends(get_db)):
    if len(files) + service.count_by_task(db, task_id) > MAX_FILE_PER_TASK:
        raise HTTPException(status_code=400, detail=f"Cannot upload more than {MAX_FILE_PER_TASK} files per task")
    
    for file in files:
        if len(file) > MAX_FILE_SIZE:
            raise HTTPException(status_code=400, detail=f"File size exceeds the maximum limit of {MAX_FILE_SIZE} bytes")
    
    return service.upload_files(db, task_id, files, UPLOAD_DIR)
