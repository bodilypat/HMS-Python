#app/schemas/finance/payment.py 

from pydantic import BaseModel, constr, condecimal 
from datetime import datetime
from typing import Optional

class PaymentBase(BaseModel):
    invoice_id: int 
    payment_method: constr(regex=r'^(cash|card|online|wallet)$')
    amount_paid: condecimal(max_digits=10, decimal_places=2)
    transaction_id: Optional[str] = None 

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    payment_method: Optional[constr(regex=r'^(cash|card|online|wallet)$')] = None
    amount_paid: Optional[condecimal(max_digits=10, decimal_places=2)] = None
    transaction_id: Optional[str] = None

class PaymentResponse(PaymentBase):
    id: int
    paid_at: datetime

    class Config:
        orm_mode = True 
        