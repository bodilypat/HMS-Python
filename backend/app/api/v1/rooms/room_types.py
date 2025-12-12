#app/api/v1/rooms/room_types.py

from fastapi import APIRouter, Depends, Query
from typing import Optional, List 

from app.schemas.rooms import RoomTypeCreate, RoomTypeUpdate, RoomTypeResponse 
from app.services.rooms.room_type_service import RoomTypeService 

router = APIRouter()

#----------------------------
# Get All Room Type 
#----------------------------
@router.get("/", response_model=List[RoomTypeResponse])
async def get_all_room_types(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    name: Optional[str] = None,
    service: RoomTypeService = Depends(),
):
    """ 
    Retrieve all room types with optional filtering by name and pagination.
    """
    return await service.get_all_room_types(
        page=page, 
        page_size=page_size,
        name=name
    )

#--------------------------------
# Get Room Type By ID
#--------------------------------
@router.get("/{room_type_id}", response_model=RoomTypeResponse)
async def get_room_type_by_id(
    room_type_id: int,
    service: RoomTypeService = Depends(),
):
    """ 
    Retrieve a room type by its ID.
    """
    return await service.get_room_type_by_id(room_type_id=room_type_id)

#--------------------------------
# Create Room Type
#--------------------------------
@router.post("/", response_model=RoomTypeResponse)
async def create_room_type(
    room_type: RoomTypeCreate,
    service: RoomTypeService = Depends(),
):
    """ 
    Create a new room type.
    """
    return await service.create_room_type(room_type=room_type)

#--------------------------------
# Update Room Type
#--------------------------------
@router.put("/{room_type_id}", response_model=RoomTypeResponse)
async def update_room_type(
    room_type_id: int,
    room_type: RoomTypeUpdate,
    service: RoomTypeService = Depends(),
):
    """ 
    Update an existing room type by its ID.
    """
    return await service.update_room_type(room_type_id=room_type_id, room_type=room_type)

#--------------------------------
# Delete Room Type
#--------------------------------
@router.delete("/{room_type_id}", response_model=RoomTypeResponse)
async def delete_room_type(
    room_type_id: int,
    service: RoomTypeService = Depends(),
):
    """ 
    Delete a room type by its ID.
    """
    await service.delete_room_type(room_type_id=room_type_id)
    return {"message": "Room type deleted successfully"}


