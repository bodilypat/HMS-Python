# backend/app/schemas/reservation.py

from datetime import date, datetime 
from enum import Enum
from typing import Optional
from pydantic import BaseModel, conint, constr

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
    
class BookingSource(str, Enum)
    website = "Website"
    phone = "Phone"
    walk_in = "Walk-in"
    travel_agency  = "Travel Agency"
    ota = "OTA"
    
class ReservationBase(BaseModel):
    guest_id: int 
    room_id: int 
    check_in: date 
    check_out: date
    number_of_guests: comint(gt=0) = 1 
    reservation_status: ReservationStatus = ReservatinStatus.pending
    payment_status: PaymentStatus = PaymentStatus.pending
    booking_source: BookingSourcee = BookingSource.website
    special_request: Optional[str] = None 
    
class ReservationCreate(ReservationBase):
    pass
    
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
    special_request: Optional[str]
    created_at: datetime 
    updated_at: datetime 
    
class config:
    orm_mode = True 