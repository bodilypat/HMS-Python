#app/schemas/core/staff_schema.py

from pydantic import BaseModel, EmailStr, Field 
from typing import Optional
from datetime import datetime

class StaffBase(BaseModel):
    full_name: str = Field(..., max_length=100, description="Full name of the staff member")
    email: EmailStr = Field(..., description="unique email address of the member")
    phone: Optional[str] = Field(None, max_length=20, description="Contact phone number")
    role: Optional[str] = Field("staff", max_length=50, description="Role/position of teh staff member")
    is_active: Optional[bool] = Field(True, description="Is the staff member currently active")

class StaffCreate(StaffBase):
    password: str = Field(..., min_length=8, max_length=100, description="Password for the staff member (will be hashed)")


class StaffUpdate(BaseModel):
    full_name: Optional[str] = Field(None, description="Updated full name")
    email: Optional[EmailStr] = Field(None, description="Updated email address")
    phone: Optional[str] = Field(None, max_length=20, description="Update contact phone number")
    role: Optional[str] = Field(None, max_length=50, description="Updated role")
    is_active: Optional[bool] = Field(None, description="Updated active status")
    password:  Optional[str] = Field(None, min_length=8, max_length=128, description="Updated password (will be hashed)")

class StaffRead(StaffBase):
    id: int 
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None 

    class Config: 
        orm_mode = True 

        