#app/api/v1/rooms/rooms.py

from fastapi import APIRouter, Depends, Query
from typing import Optional, List 

from app.schemas.rooms import RoomCreate, RoomUpdate, RoomResponse 
from app.sevices.rooms.room_service import RoomService 

router = APIRouter()

#--------------------------------------
# Get All Rooms 
#--------------------------------------
@router.get("/", response_model=List[RoomResponse])
async def get_all_rooms(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    room_type_id: Optional[int] = None,
    status: Optional[str] = None,
    room_service: RoomService = Depends()
):
    """ 
    Retrieve all rooms with optional filters and pagination.
    """
    return await service.get_all_rooms(
        page=page,
        page_size=page_size,
        room_type_id=room_type_id,
        status=status 
    )

#------------------------------
# Get Room by ID
#------------------------------
@router.get("/{room_id}", response_model=RoomResponse)
async def get_room_by_id(
    room_id: int,
    room_service: RoomService = Depends()
):
    """
    Retrieve a room by its ID.
    """
    return await room_service.get_room_by_id(room_id=room_id)
#-------------------------------
# Create a Room
#-------------------------------
@router.post("/", response_model=RoomResponse)
async def create_room(
    room: RoomCreate,
    room_service: RoomService = Depends()
):
    """ 
    Create a new room with the provided details.
    """
    return await room_service.create_room(room=room)

#-------------------------------
# Update a Room
#-------------------------------
@router.put("/{room_id}", response_model=RoomResponse)
async def update_room(
    room_id: int,
    room: RoomUpdate,
    room_service: RoomService = Depends()
):
    """
    Update an existing room with the provided details.
    """
    return await room_service.update_room(room_id=room_id, room=room)

#-------------------------------
# Delete a Room
#-------------------------------
@router.delete("/{room_id}", response_model=RoomResponse)
async def delete_room(
    room_id: int,
    room_service: RoomService = Depends()
):
    """
    Delete a room by its ID.
    """
    await room_service.delete_room(room_id=room_id)
    return {"message": "Room deleted successfully"}


