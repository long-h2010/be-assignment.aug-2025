from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas
from app.database import get_db
from app.services import ReportService

router = APIRouter(prefix="/reports", tags=["Reports"])
service = ReportService()

@router.get("/", response_model=List[schemas.ReportOut])
def read_reports(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip, limit)

@router.get("/{rp_id}", response_model=schemas.ReportOut)
def read_report(rp_id: int, db: Session = Depends(get_db)):
    db_rp = service.get(db, rp_id)
    if db_rp is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return db_rp

@router.post("/", response_model=schemas.ReportOut)
def create_report(rp: schemas.ReportCreate, db: Session = Depends(get_db)):
    return service.create(db, rp)

@router.put("/{rp_id}", response_model=schemas.ReportOut)
def update_report(rp_id: int, rp: schemas.ReportCreate, db: Session = Depends(get_db)):
    db_rp = service.update(db, rp_id, rp)
    if db_rp is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return db_rp

@router.delete("/{rp_id}", response_model=schemas.ReportOut)
def delete_report(rp_id: int, db: Session = Depends(get_db)):
    db_rp = service.delete(db, rp_id)
    if db_rp is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return db_rp
