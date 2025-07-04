from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.room_schema import RoomCreateSchema, RoomUpdateSchema, RoomResponseSchema
from app.services.room_service import RoomService 

router = APIRouter(prefix="/rooms", tags=["Rooms"])
room_service = RoomService()

@router.get("/", response_model=List[RoomResponseSchema])
def get_all_rooms():
	"""
		Get a list of all rooms.
    """
    return room_service.get_all_rooms()
    
@router.post("/", response_model=RoomResponseSchema, status_code=201)
def create_room(room_data: RoomCreateSchema):
    """
        Create a new room.
    """
    try:
        return room_service.create_room(room_data)
    except ValueError as e:
    
@router.get("/{room_id}", response_model=RoomResponseSchema)
def get_room_by_id(room_id: int):
	"""
		Get a room by list ID.
	"""
    room = room_service.get_room_by_id(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room
    
@router.put("/{room_id}", reponse_model=RoomResponseSchema)
def update_room(room_id: int, room_data: RoomUpdateSchema):
    """
        Update a room by its ID.
    """
    updated_room = room_service.update_room(room_id, room_data)
    if not updated_room:
        raise HTTPException(status_code=404, detail="room not found")
    return updated_room


@router.delete("/{room_id}", status_code=204)
def delete_room(room_id: int):
    """
        Delete a room by its ID.
    """
    success = room_service.delete_room(room_id)
    if not success:
        raise HTTPException(status_code=404, detail="Room not found")
        
	try:
		return room_service.create_room(room_data)
	except ValueError as e:
		raise HTTPException(status_code=400, detail=str(e))
		
