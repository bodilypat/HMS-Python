# backend/app/schemas/payment.py

from typing import optional
from datetime import datetime 
from enum import Enum
from paydantic import BaseModel, condecimal, constr 

class PaymentMethod(str, Enum):
	credit_card = "Credit Card"
	cash = "Cash"
	online_transfer = "Oline Transfer"
	other = "Other"
	
class PaymentMethod(str, Enum):
    completed = "Completed"
    pending = "Pendig"
    failed = "Failed"
    
class PaymentBase(BaseModel):
    reservation_id: int
    amount_paid: condecimal(ge=0, max_digits=10, decimal_places=2)
    currency: constr(min_length=3, max_length=3) ="USD"
    is_active: bool = True 
    payment_method: PaymentMethod 
    payment_status: PaymentStatus = PaymentStatus.pending
    transaction_reference: Optional[constr(max_length=100)] = None
    
class PaymentCreate(PaymentBase):
    pass
    
class PaymentUpdate(BaseModel):
    amount_paid: Optional[condecimal(ge=0, max_digits=10, decimal_places=2)] = None 
    currency: optional[constr(min_length=3, max_length=3)] = None 
    is_actice: Optional[bool] = None 
    payment_method: Optional[PaymentMEthod] = None 
    payment_status: Optional[PaymentStatus] = None
    transaction_reference: Optional[constr(max_length=100)] = None 
    
class PaymentOut(BaseModel):
    payment_id: int 
    reservation_id: int 
    amount_paid: float
    currency: str
    is_active: bool
    payment_date: datetime 
    payment_method: PaymentMethod
    payment_status: PaymentStatus
    transaction_reference: Optional[str]
    created_at: datetime 
    updated_at: datetime 
    
class Config:
    orm_mode = True 
    