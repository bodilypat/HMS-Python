# backend/app/schemas/reservation_schema.py

from pydantic import BaseModel, Field, validator 
from typing import Optional
from datetime import date 

class ReservationBaseSchema(BaseModel):
	guest_id: int = Field(...)
	room_id: Optional[int] = Field(...)
	check_in: date = Field(...)
	check_out: date = Field(...)
	number_of_guests: int = Field(...)
	reservation_status: str = Field(...)
	payment_status: str = Field()
	booking_source: str = Field()
	special_request: Optional[str] = Field()
	
	@validator("check_out")
	def check_dates(cls, check_out_value, values):
		check_in_value = values.get("check_in")
		if check_in_value and check_out_value <= check_in_value:
			raise ValueError("check_out must be after check_in")
		return check_out_value 
		
	class ReservationCreateSchema(ReservationBaseSchema):
		pass
		
	class ReservationUpdateSchema(BaseModel):
		room_id: Optonal[int]
		check_in: Optinal[date]
		check_out: Optional[date]
		number_of_guests: Optional[int]
		reservation_status: Optional[str]
		payment_status: Optional[str]
		booking_source: Optional[str]
		special_request: Optional[str]
		
		@validator 
		def check_dates(cls, check_out_value, value):
			check_in_value = values.get("check_in")
			if check_in_value and check_out_value and check_out_value <= check_in_value:
				raise ValueError("Check_out must be after check_in")
			return check_out_value 
			
	class ReservationResponseSchema(ReservationBaseSchema)
		reservation_id: int
		class Config:
			orm_mode = true 
			