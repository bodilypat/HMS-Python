#app/schemas/finance/discount.py

from pydantic import BaseModel, Field, condecimal, constr 
from typing import Optional
from datetime import datetime

class DiscountBase(BaseModel):
    name: constr(min_length=1, max_length=100) = Field(..., description="Name of the discount")
    description: Optional[constr(max_length=255)] = Field(None, description="Description of the discount")
    percentage: condecimal(gt=0, lt=100) = Field(..., description="Discount percentage between 0 and 100")
    is_active: bool = Field(default=True, description="Indicates if the discount is active")

    class Config:
        orm_mode = True 

class DiscountCreate(DiscountBase):
    pass

class DiscountUpdate(BaseModel):
    name: Optional[constr(min_length=1, max_length=100)] = None 
    description: Optiona[constr(max_length=255)] = None 
    percentage: Optional[condecimal(gt=0, lt=100)] = None 
    is_active: Optional[bool] = None
    
    class Config:
        orm_mode = True 

class DiscountRead(DiscountBase):
    id: int 
    created_at: Optional[datetime] = None 
    updated_at: Optional[datetime] = None 

    
    