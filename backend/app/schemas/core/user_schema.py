# backend/app/schemas/user.py 

from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from enum import Enum
from datetime import datetime 

class UserRole(str, Enum):
	admin = "Admin"
	manager = "Manager"
	receptionist = "Receptionist"
	staff = "Staff"
	guest = "Guest"
	
class UserStatus(str, Enum):
	active = "Active"
	inactive = "Inactive"
	
# Shared base schema
class UserBase(BaseModel):
	full_name: constr(min_length=1, max_length=100)
	username: constr(min_length=3, max_length=50)
	email: EmailStr
	phone_number: Optional[constr(max_length=20)] = None
	role: Optional[UserRole] = UserRole.guest
    status: Optional[UserStatus] = UserStatus.active

# Schema for updating a new user (includes password)	
class UserCreate(UserBase):
	password: constr(min_length=6, max_length=128)
    
# Schema for updating existing user fields (all optional)
class UserUpdate(BaseModel):
    full_name: Optional[constr(min_length=1, max_length=100)] = None 
    username: Optional[constr(min_length=3, max_length=50)] = None
    email: Optional[EmailStr] = None 
    phone_number: Optional[constr(max_length=20)] = None
    role: Optional[UserRole] = None 
    status: Optional[UserStatus] = None
    password: Optional[constr(min_length=6, max_length=128)] = None
    
# Schema for returning user data to clients
class UserOut(BaseModel):
    user_id: int 
    full_name: str
    username: str
    email: EmailStr 
    phone_number: Optional[str] = None 
    role: UserRole
    status: UserStatus
    create_at: datetime 
    updated_at: datetime 
    
    class Config:
        orm_mode = True 
        
# Internal schema for accessing hashed passwords
    class UserInDB(UserOut):
        password_hash: str 
