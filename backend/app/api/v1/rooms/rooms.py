#app/api/v1/rooms/rooms.py

"""
CRUD endpoints for managing rooms in the Hotl Management System.
Includes creating, reading and updating, and deleting rooms.
"""

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.rooms.room import RoomCreate, RoomResponse, RoomUpdate
from app.services.rooms.room_service import RoomService

router = APIRouter()
room_service = RoomService()

#-----------------------------
# Endpoint to create a new room
#-----------------------------
@router.post(
        "/rooms/", 
        response_model=RoomResponse, 
        status_code=status.HTTP_201_CREATED
    )
def create_room(
        room: RoomCreate, 
        db: Session = Depends(get_db)
    ):
    """
    Create a new room.
    """
    db_room = room_service.create_room(db, room)
    if db_room is None:
        raise HTTPException(status_code=400, detail="Room could not be created.")
    return db_room

#-----------------------------
# Endpoint to get all rooms
#-----------------------------
@router.get(
        "/rooms/", 
        response_model=List[RoomResponse], 
        status_code=status.HTTP_200_OK
    )
def get_rooms(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
    ):
    """
    Retrieve all rooms.
    """
    rooms = room_service.get_all_rooms(db, skip=skip, limit=limit)
    return rooms

#-----------------------------
# Endpoint to get a room by ID
#-----------------------------
@router.get(
        "/rooms/{room_id}", 
        response_model=RoomResponse, 
        status_code=status.HTTP_200_OK
    )
def get_room_by_id(
        room_id: int, 
        db: Session = Depends(get_db)
    ):
    """
    Retrieve a room by its ID.
    """
    db_room = room_service.get_room_by_id(db, room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found.")
    return db_room

#-----------------------------
# Endpoint to update a room by ID
#-----------------------------
@router.put(
        "/rooms/{room_id}", 
        response_model=RoomResponse, 
        status_code=status.HTTP_200_OK
    )
def update_room(

        room_id: int, 
        room: RoomUpdate, 
        db: Session = Depends(get_db)
    ):
    """
    Update a room by its ID.
    """
    db_room = room_service.update_room(db, room_id, room)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found.")
    return db_room

#-----------------------------
# Endpoint to delete a room by ID
#-----------------------------
@router.delete(
        "/rooms/{room_id}", 
        status_code=status.HTTP_204_NO_CONTENT
    )
def delete_room(
        room_id: int, 
        db: Session = Depends(get_db)
    ):
    """
    Delete a room by its ID.
    """
    success = room_service.delete_room(db, room_id)
    if not success:
        raise HTTPException(status_code=404, detail="Room not found.")
    return None




