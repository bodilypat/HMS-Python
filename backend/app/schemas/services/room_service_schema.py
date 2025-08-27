# backend/app/schemas/roomservice.py

from datetime import datetime
from typing import Optional
from enum  import Enum 

from pydantic import BaseModel, Field

# ENUM for service status
class RoomServiceStatus(str, Enum):
	requested = "Requested"
	in_progress = "In Progress"
	delivered = "Delivered"
	cancelled = "Cancelled"

# BASE SCHEMA	
class RoomServiceBase(BaseModel):
    reservation_id: int 
    service_id: int 
    service_request_time: Optional[datetime] = Field (
        default=None, description="Time when service was requested (optional)"
    )
    service_status: RoomServiceStatus = Field (
        default=RoomServiceStatus.requested, description="Current status of the service"
    )
    notes: Optional[str] = Field(default=None, max_length = 1000)
    
# CREATE SCHEMA
class RoomServiceCreate(RoomServiceBase):
    pass 

# UPDATE SCHEMA    
class RoomServiceUpdate(BaseModel):
    service_request_time: Optional[datetime] = None 
    service_status: Optional[RoomServiceStatus] = None 
    notes: Optional[str] = Field(default=None, max_length=1000)
    
    class Config:
        orm_mode = Ture

# OUTPUT SCHEMA    
class RoomServiceOut(BaseModel):
    room_service_id: int 
    reservation_id: int 
    service_id: int 
    service_request_time: datetime 
    service_status: RoomServiceStatus
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
class Config:
    orm_mode = True
    