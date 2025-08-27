# backend/app/schemas/booking/booking_schema.py

from typing import optional
from datetime import datetime 
from pydantic import BaseModel, Field

# Base Schema
class BookingBase(BaseModel):
	reservation_id: int = Field(..., description="ID of the related reservation")
	staff_id: int = Field(..., description="ID of the staff member who made the booking")
	notes: optional[str] = Field(None, description="Optional notes or comments about the booking")

# Schema used for creating a booking 
class BookingCreate(BookingBase):
	pass
	
# Schema for reading/retrieving booking data 
class BookingRead(BookingBase):
	booking_id: int 
	boking_time: datetime = Field(...,description="Timestamp when the booking was created")
	
	class Config:
		orm_mode = True 
		
# Schema used for partial updates
class BookingUpdate(BaseModel):
	reservation_id: Optional[int] = None
	staff_id: Optional[int] = None 
	notes: Optional[str] = None 
	
	