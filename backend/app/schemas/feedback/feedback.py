#app/schemas/feedback/feedback.py

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class FeedbackBase(BaseModel):
    user_name: str = Field(..., max_length=100, description="Name of the user providing feedback")
    email: Optional[EmailStr] = Field(None, descript="Optional email address of the user")
    message: str = Field(..., min_length=5, description="Feedback message content")
    rating: Optional[int] = Field(None, ge=1, le=5, description="Optional rating from 1 to 5")

class FeedbackCreat(FeedbackBase):
        pass

class FeedbackUpdate(BaseModel):
      user_name: Optional[str] = Field(None, max_length=100)
      email:Optional[EmailStr] = None 
      message: Optional[str] = Field(None, min_length=5)
      rating: Optional[int] = Field(None, ge=1, le=5)

class FeedbackRead(FeedbackBase):
      id: int
      created_at: datetime

class Config:
      orm_mode = True
      