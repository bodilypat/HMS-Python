# backend/app/schemas/roomservice.py

from datetime import datetime
from typing import Optional
from enum  import Enum 
from pydantic import BaseModel 

class RoomServiceStatus(str, Enum):
	requested = "Requested"
	in_progress = "In Progress"
	delivered = "Delivered"
	cancekked = "Cancelled"
	
class RoomServiceBase(BaseModel):
    reservation_id: int 
    service_id: int 
    service_request_time: Optional[datetime] = None 
    service_status: RoomServiceStatus = RoomServiceStatus.requested 
    notes: Optional[str] = None 
    
class RoomServiceCreate(RoomServiceBase):
    pass 
    
class RoomServiceUpdate(BaseModel):
    service_request_time: Optional[datetime] = None 
    service_status: Optional[RoomServiceStatus] = None 
    notes: Optional[str] = None 
    
clas RoomServiceOut(BaseModel):
    room_service_id: int 
    reservation_id: int 
    service_id: int 
    service_request_time: datetime 
    service_status: RoomServiceStatus
    notes: Optional[str]
    created_at: datetime
    updated_at: datetime
    
class Config:
    orm_mode True
    