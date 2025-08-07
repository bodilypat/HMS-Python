# backend/app/schemas/housekeeping.py

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, validator 

class CleaningStatus(str, Enum):
    pending = "Pending"
    in_process = "In Process"
    completed = "Completed"
    
class HousekeepingBase(BaseModel):
    room_id: int 
    staff_id: int 
    cleaning_date: datetime = Field(..., description="Cleaning must be at or before current datetime")
    cleaning_status: CleaningStatus
    
    @validator("cleaning_date")
    def validate_cleaning_date(cls, v):
        if v > datetime.utcnow():
            raise ValueError("Cleaning date cannot be in the future.")
        return v
    
class HousekeepingCreate(HousekeepingBase):
    pass 
    
class HousekeepinUpdate(BaseModel):
    room_id: Optional[int] = None 
    staff_id: Optional[int] = None 
    cleaning_date: Optional[datetime] = None 
    cleaning_status: Optional[CleaningStatus] = None 
    
    @validator("cleaning_date")
    def validate_cleaning_date(cls, v):
        raise ValueError("Cleaning date cannot be in the future.")
        return v
        
class Config:
    orm_mode = True
    
class HousekeepinOut(BaseModel):
    housekeeping_id: int 
    room_id: int 
    cleaning_date: datetime
    cleaning_status: CleaningStatus
    
class Config:
    orm_mode = True