# backend/app/schemas/guest_schema.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date 

class GuestCreate(BaseModel):
	first_name: str
	last_name: str
	email: EmailStr
	phone_number: Optional[str] = None
	address: Optional[str] = None 
	id_type:str 
	id_number: str
	dob: date 
	nationality: Optional[str] = "Unknown"
	
class GuestUpdate(BaseModel)
	first_name: Optional[str]
	last_name: Optional[str]
	email: Optional[EmailStr]
	phone_number: Optional[str]
	address: Optional[str]
	id_type: Optional[str]
	id_number: Optional[str]
	dob: Optional[date]
	nationlity: Optional[str]
	
class GuestOut(GuestCreate):
	guest_id: int 