#app/ap/v1/rooms/room_types.py

"""
CRUD endpoints for managing room typs in the Hotel Management System.
Include creating, reading, updating and deleting
"""

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.rooms.room_type import RoomTypeCreate, RoomTypeUpdate, RoomTypeResponse
from app.services.rooms.room_type_service import RoomTypeService

router = APIRouter()
room_type_service = RoomTypeService()

#---------------------------
# Create Room Type
#---------------------------
@router.post(
        "/", 
        response_model=RoomTypeResponse, 
        status_code=status.HTTP_201_CREATED
    )
def create_room_type(
    room_type: RoomTypeCreate,
    db: Session = Depends(get_db)
):
    """
    Docstring for create_room_type
    
    :param room_type: Description
    :type room_type: RoomTypeCreate
    :param db: Description
    :type db: Session
    """
    created_room_type = room_type_service.create_room_type(db, room_type)
    if not created_room_type:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create room type")
    return created_room_type

#---------------------------
# Get All Room Types
#---------------------------
@router.get(
        "/", 
        response_model=List[RoomTypeResponse],
        status_code=status.HTTP_200_OK
    )
def get_all_room_types(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """
    Docstring for get_all_room_types
    
    :param skip: Description
    :type skip: int
    :param limit: Description
    :type limit: int
    :param db: Description
    :type db: Session
    """
    room_type = room_type_service.get_all_room_types(db, skip=skip, limit=limit)
    return room_type

#---------------------------
# Get Room Type by ID
#---------------------------
@router.get(
        "/{room_type_id}", 
        response_model=RoomTypeResponse,
        status_code=status.HTTP_200_OK
    )
def get_room_type_by_id(
    room_type_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve a room type by its ID.
    
    :param room_type_id: Description
    :type room_type_id: int
    :param db: Description
    :type db: Session
    """
    room_type = room_type_service.get_room_type_by_id(db, room_type_id)
    if not room_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room type not found")
    return room_type

#---------------------------
# Update Room Type
#---------------------------
@router.put(
        "/{room_type_id}", 
        response_model=RoomTypeResponse,
        status_code=status.HTTP_200_OK
    )
def update_room_type(
    room_type_id: int,
    room_type_update: RoomTypeUpdate,
    db: Session = Depends(get_db)
):
    """
    Docstring for update_room_type
    
    :param room_type_id: Description
    :type room_type_id: int
    :param room_type_update: Description
    :type room_type_update: RoomTypeUpdate
    :param db: Description
    :type db: Session
    """
    updated_room_type = room_type_service.update_room_type(db, room_type_id, room_type_update)
    if not updated_room_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room type not found")
    return updated_room_type

#---------------------------
# Delete Room Type
#---------------------------
@router.delete(""
"       /{room_type_id}", 
        status_code=status.HTTP_204_NO_CONTENT,
        status_code=status.HTTP_204_NO_CONTENT)
def delete_room_type(
    room_type_id: int,
    db: Session = Depends(get_db)
):
    """
    Docstring for delete_room_type
    :param room_type_id: Description
    :type room_type_id: int
    :param db: Description
    :type db: Session
    """
    deleted = room_type_service.delete_room_type(db, room_type_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room type not found")
    return None







