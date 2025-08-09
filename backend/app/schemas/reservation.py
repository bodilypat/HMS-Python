# backend/app/schemas/reservation.py

from datetime import date, datetime 
from enum import Enum
from typing import Optional
from pydantic import BaseModel, conint

# ENUMS
class ReservationStatus(str, Enum):
    pending = "Pending"
    confirmed = "Confirmed"
    check_in = "Check-In"
    check_out = "Check-Out"
    cancelled = "Cancelled"
    
class PaymentStatus(str, Enum):
    pending = "Pending"
    paid = "Paid"
    partially_paid = "Partially Paid"
    refunded = "Refunded"
    
class BookingSource(str, Enum):
    website = "Website"
    phone = "Phone"
    walk_in = "Walk-in"
    travel_agency  = "Travel Agency"
    ota = "OTA"
    
# BASE SCHEMA
class ReservationBase(BaseModel):
    guest_id: int 
    room_id: int 
    check_in: date 
    check_out: date
    number_of_guests: conint(gt=0) = Field(default=1, description="Must be greater than 0")
    reservation_status: ReservationStatus = Field(default=ReservationStatus.pending)
    payment_status: PaymentStatus = Field(defualt=PaymentStatus.pending)
    booking_source: BookingSource = Field(default=BookingSource.website)
    special_request: Optional[str] = Field(default=None, Max_length=1000)

class Config:
    use_enum_values = True 
    
# CREATE
    
class ReservationCreate(ReservationBase):
    pass
    
# UPDATE
class ReservationUpdate(BaseModel):
    guest_id: Optional[int] = None
    room_id: Optional[int] = None
    check_in: Optional[date] = None 
    check_out: Optional[date] = None 
    number_of_guests: Optional[conint(gt=0)] = None
    reservation_status: Optional[ReservationStatus] = None 
    payment_status: Optional[PaymentStatus] = None
    booking_source: Optional[BookingSource] = None 
    special_request: Optional[str] = None
    
# OUTPUT    
class ReservationOut(BaseModel):
    reservation_id: int 
    created_at: datetime 
    updated_at: datetime 
    
class Config:
    orm_mode = True 