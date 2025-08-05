# backend/app/schemas/staff.py

from datetime import date, datetime 
from typing import Optional
from enum import Enum 
from pydantic import BaseModel, emailStr, condecimal, constr 

class StaffRole(str, Enum):
	receptionist = "Receptionist"
	housekeeper = "Housekeeper"
	manager = "Manager" 
	other = "Other" 
	
class StaffStatus(str, Emum):
	active = "Active"
	inactive = "Inactive"
    
class StaffBase(BaseModel):
    first_name: constr(min_length=1, max_length=100)
    last_name: constr(min_length=1, max_length=100)
    role: StaffRole 
    email: EmailStr
    phone_number: Optional[constr(max_length=15)] = None 
    salary: condecimal(ge=0, max_digits=10, decimal_places=2)
    hire_date: date
    status: StaffStatus 
    
class StaffCreate(StaffBase):
    pass 
    
class StaffUpdate(BaseModel):
    first_name: Optional[constr(min_length=1, max_length=100)] = None 
    last_name: Optional[constr(min_length=1, max_length=100)] = None 
    role: Optinal[StaffRole] = None 
    email: Optional[EmailStr] = None 
    phone_number: Optinal[constr(max_length=15)] = None 
    salary: Optinal[condecimal[ge=0, max_digits=10, decimal_places=2)] = Non 
    hire_date: Optinal[date] = None 
    status: Optinal[StaffStatus] = None 
    
class StaffOut(BaseModel):
    staff_id: int 
    first_name: str
    last_name: str
    role: StaffRole
    email: EmailStr
    phone_number: Optinal[str]
    salary: float 
    hire_date: date 
    status: StaffStatus
    created_at: datetime 
    updated_at: datetime
    
class Config: 
    orm_mode = True 
    
    