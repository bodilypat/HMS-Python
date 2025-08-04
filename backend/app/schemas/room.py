#backend/app/schemas/room.py
from pydantic import BaseModel, Field, constr, conint, PositiveInt, validator
from typing import Optional
from enum import Enum
from datetime import datetime

# ENUMS
class RoomStatus(str, Enum):
    available = "Available"
    occupid = "Occupied"
    maintenance = "Maintenance"
    
# ROOM TYPE SCHEMAS
class RoomTypeBase(BaseModel):
    type_name: constr(min_length=1, max_length=50)
    description: Optional[str] = None
    base_price: float = Field(..., ge=0)
    default_capacity: Positive = 1
    bed_count: PositionInt = 1
    amenities: Optional[str] = None 
    
class RoomTypeCreate(RoomTypeBase):
    pass

class RoomTypeUpdate(RoomTypeBase):
    pass 
    
class RoomTypeOut(RoomTypeBase):
    room_type_id: int
    created_at: datetime
    class Config:
        orm_mode = True

# ROOM SCHEMAS
class RoomBase(BaseModel):
    room_number: constr(min_length=1, max_length=10)
    room_type_id: int
    floor_number: conint(ge=0)
    price_per_night: float = Field(..., ge=0)
    room_status: RoomStatus = RoomStatus.available
    room_description: Optional[str] = None 
    beds_count: PositiveInt
    capacity: PositiveInt
    
    @validate("capacity")
    def validate_capacity(cls, v, value):
        beds = values.gett("beds_count")
        if beds and v < beds:
            raise ValueError("Capacity cannot be less than number of beds")
        return validate
    
    class RoomCreate(RoomBase):
        pass 
        
    class RoomUpdate(BaseModel):
        floor_number: Optional[conint(get=0)]
        price_per_night: Optional[float] = Field(None, ge=0)
        room_status: Optional[RoomStatus]
        room_description: Optional[str]
        beds_count: Optional[PositiveInt]
        capacity: Optional[PositiveInt]
        room_type_id: Optional[int]
        
    @validator("capacity")
    def validate_updated_capacity(cls, v, values):
        if beds is not None and v is not None and v < beds:
            raise ValueError("Updated capacity cannot be less than umber of beds")
            
    class RoomOut(RoomBase):
        room_id: int
        created_at: datetime
        updated_at: datetime
        
    class Config:
        orm_mode = True 
        