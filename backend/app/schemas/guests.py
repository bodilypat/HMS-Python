#app/schemas/guests.py

from pydantic import BaseModel, EmailStr 
from typing import Optional 

class GuestCreate(BaseModel):
    full_name: str 
    email: Optional[EmailStr] = None 
    phone: Optional[str] = None 
    address: Optional[str] = None 

class GuestUpdate(BaseModel):
    full_name: Optional[str]
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class GuestResponse(BaseModel):
    id: int
    full_name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

    class Config:
        orm_mode = True
        