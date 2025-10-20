#app/schemas/room/room_schema.py

from pydantic import BaseModel, Field, condecimal
from typing import Optional
from datetime import datetime 
from enum import Enum

class RoomStatusEnum(str, Enum):
    available = "available"
    occupied = "occupied"
    maintenance = "maintenance"
    reserved = "reserved"

# Base schema shared accorss Create/Read/Update 
class RoomBase(BaseModel):
    number: str = Field(..., description="Room number")
    category_id: Optional[int] = Field(None, description="ID of the room category")
    floor: Optional[int] = Field(None, description="Floor number")
    is_available: Optional[bool] = Field(True, description="Is room available?")
    status: Optiona[RoomStatusEnum] = Field(default=RoomStatusEnum.available)
    base_price: Optional[condecimal(max_digits=10, decimal_places=2)] = Field(None, description="Base price for the room")

    class Config:
        orm_mode = True 

# Create schema
class RoomCreate(RoomBase):
    pass 

# Update schema
class RoomUpdate(BaseModel):
    number: Optional[str] = None 
    category: Optional[int] = None 
    floor: Optional[int] = None 
    is_available: Optional[bool] = None
    status: Optional[RoomStatusEnum] = None 
    base_price: Optional[condecimal(max_digits=10, decimal_places=2)] = None 

    class Config:
        orm_mode = True 

# Read Schema 
class RoomRead(RoomBase):
    id : int 
    created_at: Optional[datetime] = None 
    updated_at: Optional[datetime] = None 

    class Config:
        orm_mode = True 

        
