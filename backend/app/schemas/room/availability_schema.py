#app/schemas/room/availability_schema.py

from pydantic import BaseModel, Field 
from typing import Optional
from datetime import date 

class AvailabilityBase(BaseModel):
    room_id: int = Field(..., description="ID of the room")
    date: date = Field(..., description="Date of availability")
    is_available: bool = Field(default=True, description="Is the room available on this date?")

class AvailabilityCreate(AvailabilityBase):
    """Schema for creating a new availability record."""
    pass 

class AvailabilityUpdate(BaseModel):
    """Schema fpr partially updating an availability record."""
    room_id: Optional[int] = Field(None, description="Updated room ID (optional)")
    date: Optional[date] = Field(None, description="Updated date (optional)")
    is_available: Optional[bool] = Field(None, description="Updated availability (optional)")

class AvailabilityRead(AvailabilityBase):
    """Schema for reading an availability record from the database."""
    id: int 

    class Config:
        orm_mode = True 

        