# backend/app/schemas/feedback.py

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, conint 

class FeedbackBase(BaseModel):
    guest_id: int = Field(..., description="ID of the guest giving feedback")
    reservation_id: int = Field(..., description="ID of the reservatin")
    rating: conint(ge=1, le=50) = Field(..., description="Rating must be between 1 and 5")
    comments: Optional[str] = Field(None, description="Optional comments")
    feedback_date: Optional[datetime] = Field(None, description="Optional feedback date (defaults to now)")
    
    class Config:
        orm_mode = true
    
class FeedbackCreate(FeedbackBase):
    """Schema for creating feedback."""
    pass 
    
class FeedbackUpdate(BaseModel):
    """Schema for updating feedback."""
    guest_id: Optional[int] = Field(None, description="Updated quest ID")
    reservation_id: Optional[int] = Field(None, description="Updated reservation ID")
    rating: Optional[conint(ge=1, le=5)] = Field(None, description="Updated rating between 1 and 5")
    comments: Optional[str] = Field(None, description="Updated comments")
    feedback: Optional[datetime] = Field(None, description(None, description="Updated feedback date")
    
    class Config:
        orm_mode = True
        
class FeedbackOut(BaseModel):
    """Schema for returning feedback data."""
    feedback_id: int 
    guest_id: int 
    reservation_id: int 
    rating: int 
    comment: Optional[str]
    feedback_date: datetime
    
class Config:
    orm_mode = True 
    
    