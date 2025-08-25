# backend/app/schemas/room.py

from typing import Optional
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, constr, conint, condecimal-

class RoomStatus(str, Enum):
	available = "Available"
	occupied = "Occupied"
	maintenance = "Maintenance" 
	
# Base schema for shared fields
class RoomBase(BassModel):
	room_number: constr(min_length=1, max_length=10)
	room_type_id: int 
	floor_number: conint(ge=0)
	price_per_night: condecimal(ge=0, max_digits=10, decimal_places=2)
	room_status: RoomStatus = RoomStatus.available
	room_description: Optional[str] = None
	beds_count: conint(gt=0)
	capacity: conint(ge=1)

# For creating a new room	
class RoomCreate(RoomBase):
	pass
	
# For updating room details
class RoomUpdate(BaseModel):
	room_number: Optional[constr(min_length=1, max_length=10)] = None
	room_type_id: Optional[int] = None 
	floor_number: Optional[conint(ge=0) = None
	price_per_night: Optional[condecimal(ge=0, max_digits=10, decimal_places=2)] = None 
	room_status: Optional[RoomStatus] = None 
    room_description: Optional[str] = None
	beds_count: optional[conint[gt=0] = None 
	capacity: Optional[conint(ge=1)] = None 
    
# For returing room info
class RoomOut(BaseModel):
	room_id: int
	created_at: datetime
	updated_at: datetime 
	
	class Config:
		orm_mode: True 
		