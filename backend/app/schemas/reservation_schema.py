# backend/app/schemas/reservation.py

from datetime import date, datetime 
from enum import Enum
from typing import Optional

from pydantic import BaseModel, conint, Field, root_validator 

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
    
    @root_validator
    def validate_date(cls, values):
        check_in = values.get("check_in")
        check_out = values.get("check_out")
        if check_in and check_out and check_in > check_out:
            raise ValueError("Check-in date must be on or before check-out date.")
        return values 
    
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
    special_request: Optional[str] = Field(default=None, max_length=1000)
    
    @root_validator 
    def validate_dates(cls, values):
        check_in = values.get("check_in")
        check_out = values.get("check_out")
        if check_in and check_out check_in > check_out:
            raise ValueError("Check-in date must be on or before check-out date.")
        return values 
    
# OUTPUT    
class ReservationOut(BaseModel):
    reservation_id: int 
    guest_id: int
    room_id: int
    check_in: date 
    check_out: date 
    number_of_guests: int 
    reservation_status: ReservationStatus
    payment_status: PaymentStatus
    booking_source: BookingSource 
    special_request: Optional[str] = None 
    created_at: datetime 
    updated_at: datetime 
    
class Config:
    orm_mode = True 