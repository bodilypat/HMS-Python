#app/schemas/finance/billing.py

from typing import Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, condecimal 

class BillingPaymentStatus(BaseModel):
    paid = "Paid"
    unpaid = "Unpaid"

class BillingBase(BaseModel):
    reservation_id: int 
    service_charnge: condecimal(ge=0, max_digits=10, decimal_places=2) = 0.00
    discount: condecimal(ge=0, max_digits=10, decimal_places=2) = 0.00
    total_amount: condecimal(ge=0, max_digits=10, decimal_places=2)
    payment_status: BillingPaymentStatus

    class Config:
        orm_mode = True 

class BillingCreate(BillingBase):
    pass 

class BillingUpdate(BaseModel):
    service_charge: Optional[condecimal(ge=0, max_digits=10, decimal_places=2)] = None 
    discount: Optional[condecimal(ge=0, max_digits=10, decimal_places=2)] = None 
    total_amount: Optional[condecimal(ge=0, max_digits=10, decimal_places=2)] = None 
    payment_status: Optional[BillingPaymentStatus] = None 

    class Config:
        orm_mode = True 

    class BillingRead(BaseModel):
        id: int
        reservation_id: float
        discount: float 
        total_amount: float 
        payment_status: BillingPaymentStatus
        created_at: datetime
        updated_at: datetime

        class Config:
            orm_mode = True 

            