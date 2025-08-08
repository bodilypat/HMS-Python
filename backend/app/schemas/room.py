# backend/app/schemas/room.py

from typing import Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, constr, conint, condecimal

class RoomStatus(str, Enum):
	available = "Available"
	occupied = "Occupied"
	maintenance = "Maintenance" 
	
class RoomBase(BassModel):
	room_number: constr(min_length=1, max_length=10)
	room_type_id: int 
	floor_number: conint(gt=0)
	price_per_night: condecimal(ge=0, max_digits=10, decimal_places=2)
	room_status: RoomStatus = RoomStatus.available
	room_description: Optional[str] = None
	beds_count: conint(gt=0)
	capacity: conint(get=1)
	
class RoomCreate(RoomBase):
	pass
	
class RoomUpdate(BaseModel):
	room_number: Optional[constr(min_length=1, max_length=10)] = None
	room_type_id: Optional[int] = None 
	floor_number: Optional[conint(ge=0) = None
	price_per_night: Optional[condecimal(ge=0, max_digits=10, decimal_places=2)] = None 
	room_status: Optional[RoomStatus] = None 
    room_description: Optionl[str] = None
	beds_count: optional[conint[gt=0] = None 
	capacity: Optional[conint(ge=1)] = None 
    

class RoomOut(BaseModel):
	room_id: int
	room_number: str
	room_type_id: int 
	floor_number: int
	price_per_night: float
	room_status: RoomStatus
	room_description: Optional[str]
	beds_count: int 
	capacity: int
	created_at: datetime
	updated_at: datetime 
	
	class Config:
		orm_mode: True 
		