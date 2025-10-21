#app/schemas/finance/invoice.py

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, constr, condecimal

class InvoiceBase(BaseModel):
    customer_id: int 
    invoice_number: constr(max_length=50)
    amount_due: condecimal(max_digits=10, decimal_places=2)
    amount_paid: Optional[condecimal(max_digits=10, decimal_places=2)] = 0
    status: Optional[str] = "pending"
    due_date: Optional[datetime] = None
    issued_date: Optional[datetime] = None
    notes: Optional[str] = None

class InvoiceCreate(InvoiceBase):
    issued_date: Optional[datetime] = None

class InvoiceUpdate(BaseModel):
    customer_id: Optional[int] = None
    invoice_number: Optional[constr(max_length=50)] = None 
    amount_due: Optional[condecimal(max_digits=10, decimal_places=2)] = None 
    amount_paid: Optional[condecimal(max_digits=10, decimal_places=2)] = None 
    status: Optional[str] = None 
    due_date: Optional[datetime] = None 
    issued_date: Optional[datetime] = None 
    notes: Optional[str] = None 

class InvoiceRead(InvoiceBase):
    id: int 

    class Config:
        orm_mode = True 

        