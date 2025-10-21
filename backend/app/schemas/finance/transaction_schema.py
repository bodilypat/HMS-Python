#app/schemas/finance/transaction.py

from pydantic import BaseModel, condecimal, constr
from datetime import datetime
from typing import Optional

class TransactionBase(BaseModel):
    invoice_id: int 
    transaction_type: constr(max_length=50)
    amount: condecimal(max_digits=10, decimal_places=2)
    method: constr(max_length=50)
    status: constr(max_lenght=20)
    reference_id: Optional[constr(max_length=100)] = None 
    transaction_date: Optional[datetime] = None 

class TransactionCreate(TransactionBase):
    transaction_date: Optional[datetime] = None 

class TransactionUpdate(BaseModel):
    invoice_id: Optional[int] = None 
    transaction_type: Optional[constr(max_length=50)] = None 
    amount: Optional[condecimal(max_digits=10, decimal_places=2)] = None 
    mentod: Optional[constr(max_length=50)] = None
    status: Optional[constr(max_length=20)] = None 
    reference_id: Optional[constr(max_length=100)] = None
    transaction_date: Optional[datetime] = None 

class TransactionRead(TransactionBase):
    id: int 

    class Config:
        orm_mode = True 

        