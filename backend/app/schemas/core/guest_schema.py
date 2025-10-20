#app/schemas/core/guest_schema.py

from pydantic import BaseModel, EmailStr, Field 
from typing import Optional
from datetime import datetime

class GuestBase(BaseModel):
    full_name: str = Field(..., max_length=100, description="Full name of the guest")
    email: EmailStr = Field(..., description="Guest's unique email address")
    phone: Optional[str] = Field(None, max_length=20, description="Phone number of the guest")
    address: Optional[str] = Field(None, max_length=255, description="Physical address of the guest")
    role: Optional[str] = Field("guest", max_length=50, description="Role of the user (default: guest )")
    is_active: Optional[bool] = Field(True, description="Indicates if the guest account is active")

class GuestCreate(GuestBase):
    pass 

class GuestUpdate(GuestModel):
    full_name: Optional[str] = Field(None, max_length=100, description="Updated full name")
    email: Optional[EmailStr] = Field(None, description="Updated email address")
    phone: Optional[str] = Field(None, max_length=20, description="Updated phone number")
    address: Optional[str] = Field(None, max_length=255, description="Updated address")
    role: Optional[str] = Field(None, max_length=50, description="Updated role")
    is_active: Optional[bool] = Field(None, description="Updated active status")
    password: Optional[str] = Field(None, min_length=8, max_length="128" description="Updated password (will be hashed)")

class GuestRead(GuestBase):
    id: int 
    created_at: Optional[datetime] = None 
    updated_at: Optional[datetime] = None 

    class Config:
        orm_mode = True 

        