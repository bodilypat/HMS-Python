from datetime import datetime 
from enum import Enum
from pydamic import BaseModel, EmailStr, constr
from typing import Optional

class UserRole(str, Enum):
	admin = "Amin"
	manager = "Manager"
	receptionist = "Receptionist"
	staff = "Staff"
	guest = "Guest"
	
class UserStatus(str, Enum):
	active = "Active"
	inactive = "Inactive"
	
class UserBase(BaseModel):
	full_name: constr(min_length=1, max_length=100)
	username: constr(min_length=3, max_length=50)
	email: EmailStr
	phone_number: Optional[constr(max_length=20)] = None
	role: UserRole = UserRole.guest
	status: UserStatus = UserStatus.active
	
class UserCreate(UserBase):
	password: constr(min_length=6, max_length=128)
    
class UserUpdate(BaseModel):
    full_name: Optional[constr(min_length=1, max_length=100)] = None 
    username: Optional[constr(min_length=3, max_length=50)] = None
    email: Optional[EmailStr] = None 
    phone_number: Optional[constr(max_length=20)] = None
    role: Optional[UserStatus] = None 
    password: Optional[constr(min_length=6, max_length=128)] = None
    
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
        
    class UserInDB(UserOut):
        password_hash: str 
        