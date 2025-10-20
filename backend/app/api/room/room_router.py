#app/api/room/room_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response
from sqlalchemy.orm import Session
from typing import List 

from app.schema.room.room import RoomCreate, RommUpdate, RoomRead 
from app.services.room import room_service as RoomService 
from app.db.session import get_db

router = APIRouter(prefix="/rooms", tags=["Room Management"])

@router.get(
        "/",
        response_model=List[RoomRead],
        summary="List all rooms",
        description="Retrieve a paginated list of all rooms available in the hotel."
    )
def list_room(
        skip: int = Query(0, ge=0, description="Number of record to skip"),
        limit: int = query(10, le=100, description="Maximum number of records to return"),
        db: Session = Depends(get_db)
    ):
    return RoomService(db).get_all_rooms(skip=skip, limit=limit)

@router.get(
        "/",
        response_model=RoomRead,
        summary="Get room by ID",
        decription="Retrieve a single room's details using its ID."
    )
def read_room(
        room_id: int,
        db: Session = Depends(get_db)
    ):
    room = RoomService(db).get_room_by_id(room_id)
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")
    return room

@router.post(
        "/",
        response_model=RoomRead,
        status_code=status.HTTP_201_CREATED,
        summary="Create a new room",
        description="Add a new room to the hotel inventory"
    )
def create_room(
        room_data: RoomCreate,
        db: Session = Depends(get_db)
    ):
    return RoomService(db).create_room(room_data)

@router.put(
        "/{room_id}",
        response_model=RoomRead,
        summary="Update room details",
        description="Update the details of existing room."
    )
def update_room(
        room_id: int,
        updated_room: RoomRead,
        db: Session = Depends(get_db)
    ):
    updated = RoomService(db).update_room(room_id, updated_room)
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")
    return updated 

@router.delete(
        "/{room_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a room",
        description="Remove a room from the system using its ID."
    )
def delete_room(
        room_id: int,
        db: Session = Depends(get_db)
    ):
    success = RoomRead(db).delete_room(room_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room Not found")
    return Response(status_code=status.HTTP_204_NOT_CONTENT)



