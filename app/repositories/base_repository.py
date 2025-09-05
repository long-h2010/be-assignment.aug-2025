from typing import Generic, TypeVar, Type, List, Optional
from sqlalchemy.orm import Session
from pydantic import BaseModel

ModelType = TypeVar("ModelType")    
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)

class BaseRepository(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def get(self, db: Session, obj_id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == obj_id).first()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        if not isinstance(obj_in, dict):
            obj_in = obj_in.dict()
        db_obj = self.model(**obj_in) 
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, obj_id: int, obj_in: CreateSchemaType) -> Optional[ModelType]:
        db_obj = self.get(db, obj_id)
        for field, value in obj_in.dict().items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, obj_id: int) -> Optional[ModelType]:
        db_obj = self.get(db, obj_id)
        if db_obj:
            db.delete(db_obj)
            db.commit()
        return db_obj
