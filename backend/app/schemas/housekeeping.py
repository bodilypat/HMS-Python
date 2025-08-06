# backend/app/schemas/housekeeping.py

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field 

class CleaningStatus(str, Enum):
    pending = "Pending"
    in_process = "In Process"
    completed = "Completed"
    
class HousekeepingBase(BaseModel):
    room_id: int 
    staff_id: int 
    cleaning_date: datetime = Field(..., description="Cleaning must be at or before current datetime")
    cleaning_status: CleaningStatus
    
class HousekeepingCreate(HousekeepingBase0:
    pass 
    
class HousekeepinUpdate(BaseModel):
    room_id: Optional[int] = None 
    staff_id: Optional[int] = None 
    cleaning_date: Optional[datetime] = None 
    cleaning_status: Optional[CleaningStatus] = None 
    
class HousekeepinOut(BaseModel):
    housekeeping_id: int 
    room_id: int 
    cleaning_date: datetime
    cleaning_status: CleaningStatus
    
class Config:
    orm_mode = True