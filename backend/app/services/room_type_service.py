# backend/app/services/room_type_service.py

form typing import List, Optional
from backend.app.models.room_type_model import RoomTypeModel
from app.schemas.room_type_schema import (
	RoomTypeCreateSchema,
	RoomTypeUpdateSchema
)

class RoomTypeService:
	
	@staticmethod
	def get_room_type_id(room_type_id: int) -> Optinal[dict]:
		"""
			Fetch a room type by its ID.
		"""
		return RoomTypeModel.get_by_id(room_type_id)
		
	@staticmethod
	def create_room_type(room_type_data: RoomTypeCreateSchema) -> dict:
		"""
			Create a new room type.
		"""
		existing = RoomTypeModel.get_by_type_name(room_type_data.type_name)
		if existing:
			raise ValueError("Room type with this name already exists.")
		return RoomTypeModel.create(room_type_data.dict())
		
	@staticmethod
	def update_room_type(room_type_id: int, room_type_data:  RoomTypeUpdateSchema) -> Optional[dict]:
		"""
			Update an existing room type.
		"""
		return RoomTypeModel.update(room_type_id, room_type_data.dict(exclude_unset=True))
		
	@staticmethod
	def delete_room_type(room_type_id: int) ->bool:
		"""
			Delete a room type.
		"""
		return RoomTypeModel.delete(room_type_id)