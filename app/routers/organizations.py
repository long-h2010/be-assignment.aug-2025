from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas
from app.database import get_db
from app.services import OrganizationService
from app.core.security import require_admin

router = APIRouter(prefix="/organizations", tags=["Organizations"])
service = OrganizationService()

@router.get("/", response_model=List[schemas.OrganizationOut])
def read_organizations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip, limit)

@router.get("/{org_id}", response_model=schemas.OrganizationOut)
def read_organization(org_id: int, db: Session = Depends(get_db)):
    db_org = service.get(db, org_id)
    if db_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_org

@router.post("/", response_model=schemas.OrganizationOut)
def create_organization(org: schemas.OrganizationCreate, db: Session = Depends(get_db), current_user = Depends(require_admin)):
    return service.create(db, org)

@router.put("/{org_id}", response_model=schemas.OrganizationOut)
def update_organization(org_id: int, org: schemas.OrganizationCreate, db: Session = Depends(get_db)):
    db_org = service.update(db, org_id, org)
    if db_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_org

@router.delete("/{org_id}", response_model=schemas.OrganizationOut)
def delete_organization(org_id: int, db: Session = Depends(get_db)):
    db_org = service.delete(db, org_id)
    if db_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_org
