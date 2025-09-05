from pydantic import BaseModel, EmailStr
from app.enums.user_roles import UserRole
from typing import Optional
from app.schemas.organization import OrganizationOut

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: UserRole = UserRole.MEMBER

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdateOrganization(BaseModel):
    organization_id: int

class UserOut(UserBase):
    id: int
    organization: Optional[OrganizationOut]
    
    class Config:
        orm_mode = True
