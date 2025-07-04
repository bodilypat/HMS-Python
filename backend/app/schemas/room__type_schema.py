# backend/app/schemas/room_schema.py

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class RoomStatus(str, Enum):
	available = "Available"
	occupied = "Occupied"
	maintenance = "Maintenance"
	
class RoomCreateSchema(BaseModel):
	room_number: str
	room_type_id: int
	floor_number: int
	price_per_night: float
	room_status: RoomStatus = RoomStatus.available
	room_description: Optinal[str] = None
	beds_count: int
	capacity: int 
	
class RoomCreateSchema(RoomCreateSchema):
	pass

class RoomResponseSchema(RoomCreateSchema):
	room_id: int
	
	class Config:
		orm_mode = True
		