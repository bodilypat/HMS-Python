# backend/app/schemas/feedback.py

from datetime import datetime
from typing import Optional
from pydantic import BaseModel,  Field, conint 

class FeedbackBase(BaseModel):
    guest_id: int 
    reservation_id: int 
    rating: conint(get=1, le=50 = Field(..., description="Rating must be between 1 and 5")
    comments: Optional[str] = None 
    feedback_date: Optional[datetime] = None 
    
    class Config:
        orm_mode = true
    
class FeedbackCreate(FeedbackBase):
    pass 
    
class FeedbackUpdate(BaseModel):
    guest_id: Optional[int] = None 
    reservation_id: Optional[int] = None 
    rating: Optional[conint(get=1, le=5)] = None 
    comment: Optional[str] = None
    feedback_date: Optional[datetime] = None 
    
    class Config:
        orm_mode = True
        
class FeedbackOut(BaseModel):
    feedback_id: int 
    guest_id: int 
    reservation_id: int 
    rating: int 
    comment: Optional[str]
    feedback_date: datetime
    
class Config:
    orm_mode = True 
    
    