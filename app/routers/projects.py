from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas
from app.database import get_db
from app.services import ProjectService

router = APIRouter(prefix="/projects", tags=["Projects"])
service = ProjectService()

@router.get("/", response_model=List[schemas.ProjectOut])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip, limit)

@router.get("/{prj_id}", response_model=schemas.ProjectOut)
def read_project(prj_id: int, db: Session = Depends(get_db)):
    db_prj = service.get(db, prj_id)
    if db_prj is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_prj

@router.post("/", response_model=schemas.ProjectOut)
def create_project(prj: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return service.create(db, prj)

@router.put("/{prj_id}", response_model=schemas.ProjectOut)
def update_project(prj_id: int, prj: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_prj = service.update(db, prj_id, prj)
    if db_prj is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_prj

@router.delete("/{prj_id}", response_model=schemas.ProjectOut)
def delete_project(prj_id: int, db: Session = Depends(get_db)):
    db_prj = service.delete(db, prj_id)
    if db_prj is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_prj
