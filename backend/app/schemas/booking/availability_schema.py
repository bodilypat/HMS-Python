#app/schemas/booking/availability_schema.py

from pydantic import BaseModel, Field, root_validator 
from typing import Optional 
from datetime import date 

class AvailabilityBase(BaseModel):
    room_id: int = Field(..., description="The ID of the room")
    available_from: date = Field(..., description="Start date of availability")
    available_to: date = Field(..., description="End date of availability")
    is_available: bool = Field(default=True, description="Room availability status")

    @root_validator
    def validate_dates(cls, value):
        start = values.get("availble_from")
        end = values.get("available_to")
        if start and end and start >= end: 
            raise ValueError("available_from must be before available_to")
        return values
    
    class Config:
        orm_mode = True

class AvailabilityCreate(AvailabilityBase):
    """Schema for creating a new room availability."""
    pass 

class AvailabilityUpdate(BaseModel):
    available_from: Optional[date] = Field(None, description="Update start date to availability")
    available_to: Optional[date] = Field(None, description="Updated end date of availability")
    is_available: Optional[bool] = Field(None, description="Updated availabiity status")
    
    @root_validator
    def validate_dates(cls, values):
        start = values.get("available_from")
        end = values.get("available_to")
        if start and end and start >=end:
            raise ValueError("available_from must be before available_to")
        return values 
    
        class Config:
            orm_mode = True 

class AvailabilityRead(AvailabilityBase):
    id : int = Field(None, description="The unique ID of the availability record")

    class Config:
        orm_made = True 

        