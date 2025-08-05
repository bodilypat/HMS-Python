# backend/app/schemas/service.py

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, condecimal, constr 

class ServieBase(BaseModel):
	service_type: constr(min_length=1, max_length=100)
	category: Optional[constr(max_length=50) = None 
	description: Optional[str] = None 
	price: condecimal(ge=0, max_digits=10, decimal_places=2)
	is_active: True 
	
class ServieCreate(ServieBase):
	pass
	 
class ServiceUpdate(BaseModel):
    service_type: Optional(constr(min_length=1, max_length=100)] = None 
    category: Optional[constr(max_length=50)] = None 
    descript: Optional[str] = None 
    price: Optional[condecimal(ge=0, max_digits=10, decimal_places=2)] = None 
    is_active: Optional[bool] = None 
    
class ServiceOut(BaseModel):
    service_id: int
    service_type: str
    category: optional[str]
    price: float 
    is_active: bool
    
class Config:
    orm_mode: True 
    
    
    