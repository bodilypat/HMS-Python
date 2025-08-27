# backend/app/schemas/roomtype.py

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, constr, conint, condecimal
    
class RoomTypeBase(BaseModel):
    type_name: constr(min_length=1, max_length=50)
    description: Optional[str] = None 
    base_price: condecimal(ge=0, max_digits=10, decimal_places=2)
    default_capacity: conint(gt=0) = 1
    bed_count: conint(ge=0) = 1
    amenities: Optional[str] = None 
    
class, RoomTypeCreate(RoomTypeBase):
    """Schema for creating a new room type."""
    pass 
    
class RoomTypeUpdate(BaseModel):
    """Schema for updating an existing room type."""
    type_name: Optional[constr(min_length=1, max_length=50)] = None 
    description: Optional[str] = None 
    base_price: Optional[condecimal(ge=0, max_digits=10, decimal_place=2)] = None 
    default_capacity: Optional[conint(gt=0)] = None
    bed_count: Optional[conint(gt=0)] = None
    aminities: Optional[str] = None
    
    class Config:
        orm_mode = True 
        
class RoomTypeOut(BaseModel):
    """Schema for returning room type data."""
    room_type_id: int
    type_name: str
    description: Optional[str]
    base_price: float
    default_capacity: int
    bed_count: int
    amenities: Optional[str]
    created_at: datetime 
    updated_at: datetime 
    
class Config:
    orm_mode: True 
    