#app/schemas/staff.py

from pydantic import BaseModel, EmailStr 
from typing import Optional 

class StaffCreate(BaseModel):
    full_name: str 
    email: EmailStr
    role: str 
    phone: Optional[str] = None 
    is_active: bool = True 

class StaffUpdate(BaseModel):
    full_name: Optional[str]
    email: Optional[EmailStr]
    role: Optional[str]
    phone: Optional[str]
    is_active: Optional[bool]

class StaffResponse(BaseModel):
    id: int 
    full_name: str 
    email: EmailStr
    role: str 
    phone: Optional[str]
    is_active: bool

    class Config:
        orm_mode = True 

        