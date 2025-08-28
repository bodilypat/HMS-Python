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
        default=None, 
        description="Time when service was requested (optional)"
    )
    service_status: RoomServiceStatus = Field (
        default=RoomServiceStatus.requested, 
        description="Current status of the service request."
    )
    notes: Optional[str] = Field(
        default=None, 
        max_length = 1000
        description="Optional notes or special instructuons for the service."
    )
    
# CREATE SCHEMA
class RoomServiceCreate(RoomServiceBase):
    """
        Schema used then creating a new rom service request.
    """
    pass 

# UPDATE SCHEMA    
class RoomServiceUpdate(BaseModel):
    service_request_time: Optional[datetime] = Field (
        default=None,
        description="Updated request time, if changed." 
    ) 
    service_status: Optional[RoomServiceStatus] = Field (
        default=None,
        description="Updated service status."
    )
    notes: Optional[str] = Field(
        default=None, 
        max_length=1000,
        description="Updated notes, if any."
    )
    
# OUTPUT / RESPONSE SCHEMA
class RoomServiceOut(BaseModel):
    room_service_id: int 
    reservation_id: int,
    service_id: int
    service_request_time: datetime
    service_status: RoomServiceStatus
    notes: Optional[str] = None 
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = Ture

