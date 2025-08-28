# backend/app/schemas/service_schema.py

from pydantic import BaseModel, condecimal, constr
from typing import Optional
from datetime import datetime 

# Base Schema
class ServiceBase(BaseModel):
	service_type: constr(min_length=1, max_length=100)
	category: Optional[constr(max_length=50) = None 
	description: Optional[str] = None 
	price: condecimal(ge=0, max_digits=10, decimal_places=2)
	is_active: Optional[bool] = True 
	
# Create Schema
class ServiceCreate(ServieBase):
    """
        Schema for creating a new service.
    """
	pass
	 
# Update Schema 
class ServiceUpdate(BaseModel):
    service_type: Optional[constr(min_length=1, max_length=100)] = None 
    category: Optional[constr(max_length=50)] = None 
    description: Optional[str] = None 
    price: Optional[condecimal(ge=0, max_digits=10, decimal_places=2)] = None 
    is_active: Optional[bool] = None 
    
    class Config:
        orm_mode = True
        
class ServiceOut(ServiceBase):
    service_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
class Config:
    orm_mode: True 
    
    
    