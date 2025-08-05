# backend/app/schemas/billing.py

from typing import Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, condecimal

class BillingPaymentStatus(str, Enum):
	paid = "Paid"
	unpaid = "Unpaid"
	
class BillingBase(BaseModel):
    reservation_id: int 
    service_charge: condecimal(ge=0, max_digits=10, decimal_places=2) = 0.00
    discount: condecimal(ge=0, max_digits=10, decimal_places=2) = 0.00
    total_amount: condecimal(ge=0, max_digits=10, decimal_places=2)
    payment_status: BillingPaymentStatus
    
class BillingCreate(BillingBase):
    pass 
    
class BillingUpdate(BaseModel):
    service_charge: Optional[condecimal(ge=0, max_digits=10, decimal_places=2)] = None
    discount: Optional[condecimal(ge=0, max_digits=10, decimal_places=2)] = None
    total_amount: Optional[condecimal[condecimal(ge=0, max_digits=10, decimal_places=2)] = None 
    payment_status: Optional[BillingPaymentStatus] = None 
    
class BillingOut(BaseModel):
    billing_id: int
    reservation_id: int 
    service_charge: float 
    discount: float 
    total_amount: float 
    payment_status: BillingPaymentStatus
    created_at: datetime 
    
class Config:
    orm_mode = True 
    