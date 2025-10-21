#app/schemas/booking/history_schema.py

from pydantic import BaseModel, Field 
from typing import Optional
from datetime import datetime

class HistoryBase(BaseModel):
    booking_id: int = Field(..., description="ID of the related booking")
    status: str = Field(..., max_length=50, description="Status of the booking")
    notes: Optional[str] = Field(None, descriptio="Optional notes for the booking history record")

class HistoryCreate(HistoryBase):
    """Schema for creating a new booking history entry."""
    pass 

class HistoryUpdate(BaseModel):
    """Schema for creating a new booking history entry."""
    status: Optional[str] = Field(None, max_length=50, description="Update status of the booking")
    notes: Optional[str] = Field(None, description="Updated notes")

    class Config:
        orm_mode = True

class HistoryRead(HistoryBase):
    """Schema for reading a booking history record."""
    id: int = Field(..., description="Unique ID of the booking history record")
    timestamp: datetime = Field(..., descriptio="Timestamp when the history record was created")

    class Config: 
        orm_mode = True 

        
