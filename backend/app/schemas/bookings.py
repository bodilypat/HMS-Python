#app/schemas/bookings.py

from pydantic import BaseModel 
from typing import Optional
from datetime import date 

class ReservationCreate(BaseModel):
    guest_id: int
    room_id: int 
    check_in: date 
    check_out: date 
    status: str = "pending"

class ReservationUpdate(BaseModel):
    room_id: Optional[int]
    check_in: Optional[date]
    check_out: Optional[date]
    status: Optional[str]

class ReservationResponse(BaseModel):
    id: int
    guest_id: int 
    check_in: date
    check_out: date 
    status: str 

    class Config: 
        orm_mode = True 

class PaymentCreate(BaseModel):
    reservation_id: int
    amount: float 
    payment_method: str 

class PaymentResponse(BaseModel):
    id: int
    reservation_id: int
    amount: float
    payment_method: str
    status: str

    class Config:
        orm_mode = True