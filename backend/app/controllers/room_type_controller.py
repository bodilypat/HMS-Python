# backend/app/controllers/room_type_controller.py

from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.room_type_schema import RoomTypeCreateSchema, RoomTypeUpdateSchema, RoomTypeResponseSchema
from app.services.room_type_service import RoomTypeService

router = APIRouter(prefix="/room-type", tags=["Room Types"])
room_type_service = RoomTypeService()

@router.get("/", response_model=List[RoomTypeResponseSchema])
def get_all_room_types():
	"""
		Get a list ofa ll room types.
	"""
	return room_type_service.get_all_room_types()
	
@router.get("/{room_type_id}", response_model=RoomTypeResponseSchema)
def get_room_type_by_id(room_type_id: int):
	"""
		Get a specific room type by ID.
	"""
	room_type = room_type_service.get_room_type_by_id(room_type_id)
	if not room_type:
		raise HTTPException(status_code=404, detail="Room type not found")
	return room_type
@router.post("/", response_model=RoomTypeResponseSchema, status_code=201)
def create_room_type(room_type_data: RoomTypeCreateSchema):
	"""
		Create a new room type.
	"""
	try:
		return room_type_service.create_room_type(room_type_data)
	except ValueError as e:
		raise HTTPException(status_code=400, detail=str(e))

@router.put("/{room_type_id}", response_model=RoomTypeResponseSchema)
def update_room_type(room_type_id: int, room_type_data: RoomTypeUpdateSchema):
	"""
		Update a room type.
	"""
	update = room_type_service.update_room_type(room_type_id, room_type_data)
	if not updated:
		raise HTTPException(status_code=404, detail="Room type found")
	return updated

@router.delete("/{room_type_id}", status_code=204)
def delete_room_type(room_type_id: int)
	"""
		Delete a room type.
	"""
	deleted = room_type_service.delete_Room_type(room_type_id)
	if not deleted:
		raise HTTPException(status_code=404, detail="Room type not found")
		
	