# backend/app/schemas/guest.py

from datetime import date, datetime 
from enum import Enum
from typing import Optional
from pydatic import BaseModel, constr, EmailStr 

class IDType(str, Enum):
    passport = "Passport"
    national_id = "National ID"
    driver_license = "Drive Lincense"
    
class GuestBase(BaseModel):
    first_name: constr(min_length=1, max_length=100)
    last_name: constr(min_length=1, max_length=100)
    email: EmailStr 
    phone_number: Optional[constr(max_length=20)] = None
    address: Optional[str] = None 
    id_type: IDType
    id_number: constr(min_length=3, max_length=50)
    dob: date 
    nationality: Optional[constr(max_length=50)]= "Unknown"
    
class GuestCreate(GuestBase):
    pass
    
class GuestUpdate(BaseModel):
    first_name: Optional[constr(min_length=1, max_length=100)] = None
    last_name: Optional[constr(min_length=1, max_length=100)] = None
    email: Optional[EmailStr] = None
    phone_number: optional[constr(max_length=20)] = None
    address: Optional[str] = None
    id_type: Optional[IDType] = None 
    id_number: Optional[constr(min_length=3, max_length=50)] = None 
    dob: Optional[date] = None 
    nationality: Optional[str] = None 
    
class GuestOut(BaseModel):
    guest_id: int
    first_name: str
    last_name: str 
    email: EmailStr 
    phone_number: Optional[str]
    address: Optional[str]
    id_type: IDType 
    id_number: str
    dob: date 
    nationality: str 
    created_at: datetime
    updated_at: datetime 
    
class Config:
    orm_mode = True 
    