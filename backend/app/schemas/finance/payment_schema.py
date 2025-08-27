# backend/app/schemas/payment.py

from typing import optional
from datetime import datetime 
from enum import Enum
from paydantic import BaseModel, condecimal, constr, Field

# ENUMS
class PaymentMethod(str, Enum):
	credit_card = "Credit Card"
	cash = "Cash"
	online_transfer = "Online Transfer"
	other = "Other"
	
class PaymentStatus(str, Enum):
    completed = "Completed"
    pending = "Pending"
    failed = "Failed"
    
# BASE   SCHEMA
class PaymentBase(BaseModel):
    reservation_id: int
    amount_paid: condecimal(ge=0, max_digits=10, decimal_places=2)
    currency: constr(min_length=3, max_length=3) = Field(default="USD", description="ISO 4217 currency code")
    is_active: bool = True 
    payment_method: PaymentMethod 
    payment_status: PaymentStatus = PaymentStatus.pending
    transaction_reference: Optional[constr(max_length=100)] = None
    
    class Config:
        orm_mode = True
    
# CREATE SCHEMA
class PaymentCreate(PaymentBase):
    pass
    
# UPDATE SCHEMA
class PaymentUpdate(BaseModel):
    amount_paid: Optional[condecimal(ge=0, max_digits=10, decimal_places=2)] = None 
    currency: optional[constr(min_length=3, max_length=3)] = None 
    is_active: Optional[bool] = None 
    payment_method: Optional[PaymentMethod] = None 
    payment_status: Optional[PaymentStatus] = None
    transaction_reference: Optional[constr(max_length=100)] = None 
    
    class Config:
        orm_mode = Ture

# OUTPUT SCHEMA    
class PaymentOut(BaseModel):
    payment_id: int 
    reservation_id: int 
    amount_paid: float
    currency: str
    is_active: bool
    payment_date: datetime 
    payment_method: PaymentMethod
    payment_status: PaymentStatus
    transaction_reference: Optional[str] = None
    created_at: datetime 
    updated_at: datetime 
    
class Config:
    orm_mode = True 
