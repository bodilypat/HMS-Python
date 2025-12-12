#app/schemas/billings.py

from pydantic import BaseModel 
from typing import Optional
from datetime import date 

class BillingCreate(BaseModel):
    guest_id: int 
    booking_id: int 
    amount: float 
    status: Optional[str] = None 
    payment_method: Optional[str] = None
    billing_date: Optional[date] = None

class BillingUpdate(BaseModel):
    amount: Optional[float]
    status: Optional[str]
    payment_method: Optional[str]
    billing_date: Optional[date]

class BillingResponse(BaseModel):
    id: int 
    guest_id: int 
    booking_id: int 
    amount: float 
    status: str 
    payment_method: Optional[str] 
    billing_date: Optional[date]

    class Config: 
        orm_mode = True 

        