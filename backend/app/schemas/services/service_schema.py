# backend/app/schemas/service_schema.py

from pydantic import BaseModel, condecimal, constr
from typing import Optional
from datetime import datetime 

class ServiceBase(BaseModel):
	service_type: constr(min_length=1, max_length=100)
	category: Optional[constr(max_length=50) = None 
	description: Optional[str] = None 
	price: condecimal(ge=0, max_digits=10, decimal_places=2)
	is_active: Optional[bool] = True 
	
class ServiceCreate(ServieBase):
	pass
	 
class ServiceUpdate(BaseModel):
    service_type: Optional[constr(min_length=1, max_length=100)] = None 
    category: Optional[constr(max_length=50)] = None 
    description: Optional[str] = None 
    price: Optional[condecimal(ge=0, max_digits=10, decimal_places=2)] = None 
    is_active: Optional[bool] = None 
    
class ServiceOut(ServiceBase):
    service_id: int
    created_at: datetime
    
class Config:
    orm_mode: True 
