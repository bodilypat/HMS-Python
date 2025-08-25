# backend/app/schemas/guest.py

from datetime import date, datetime 
from enum import Enum
from typing import Optional
from pydantic import BaseModel, constr, EmailStr 

class IDType(str, Enum):
    passport = "Passport"
    national_id = "National ID"
    driver_license = "Driver License"
    
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
    
# Schema for creating a guest    
class GuestCreate(GuestBase):
    pass
    
# Schema for updating guest info (all fields optional)
class GuestUpdate(BaseModel):
    first_name: Optional[constr(min_length=1, max_length=100)] = None
    last_name: Optional[constr(min_length=1, max_length=100)] = None
    email: Optiona[EmailStr] = None
    phone_number: optional[constr(max_length=20)] = None
    address: Optional[str] = None
    id_type: Optional[IDType] = None
    id_number: Optional[constr(min_length=3, max_length=50) = None
    dob: Optional[date] = None
    nationality: Optional[constr(max_length=50)] = None 
    
# Schema for returing guest data
class GuestOut(BaseModel):
    guest_id: int
    created_at: datetime
    updated_at: datetime 
    
class Config:
    orm_mode = True 
    