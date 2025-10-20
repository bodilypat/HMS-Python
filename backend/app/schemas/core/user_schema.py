#app/models/core/user_schema.py

from enum import Enum
from typing import Optional 
from pydantic import BaseModel, EmailStr, Field 
from datetime import datetime

class UserRole(str, Enum):
    admin = "Admin"
    staff = "staff"
    guest = "guest"

class UserBase(BaseModel):
    full_name: str = Field(..., max_length=100, description="Full name of the user")
    email: EmailStr = Field(..., description="Unique email address of the user")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="User password (will be hashed)")
    role: UserRole = Field(default=UserRole.guest, description="Role assigned to the user")
    is_active: Optional[bool] = Field(default=True, description="Is the user account active")

class UserUpdate(BaseModel):
    full_name: Optional[str] = Field(None, max_length=100, description="Updated full name")
    email: Optional[EmailStr] = Field(None, description="Updated email address")
    password: Optional[str] = Field(None, min_length=6, description="New password (will be hashed)")
    role: Optional[UserRole] = Field(None, description="Updated user role")
    is_active: Optional[bool] = Field(None, description="Aactive/deactivate user")

class UserRead(UserBase):
    id: str 
    role: UserRole
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True 
        