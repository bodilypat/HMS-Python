#app/controllers/room/room_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List 

from schemas.room.room import RoomCreate, RoomRead, RoomUpdate 
from services.room.room import RoomService 
from dependancies  import get_db

router = APIRouter(prefix="/rooms", tags=["Rooms Managemet"])

@router.get("/", response_model=List[RoomRead], summary="Get a list of Rooms")
def read_rooms(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return RoomService(db).get_all_rooms(skip, limit)

@router.get("{room_id}", response_model=RoomRead, summary="Get a single Room by ID")
def read_room(
        room_id: int,
        db: Session = Depends(get_db)
    ):
    room = RoomService(db).get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@router.post("/", response_model=RoomRead, status_code=status.HTTP_201_CREATED, summary="Create a new Room")
def create_room(    
        room_in: RoomCreate,
        db: Session = Depends(get_db)
    ):
    return RoomService(db).create_room(room_in)

@router.put("/{room_id}", response_model=RoomRead, summary="Update an existing Room")
def update_room(
        room_id: int,
        updated_room: RoomUpdate,
        db: Session = Depends(get_db)
    ):
    updated = RoomService(db).update_room(room_id, updated_room)
    if not updated:
        raise HTTPException(status_code=404, detail="Room not found")
    return updated 

@router.delete("/{room_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Room")
def delete_room(
        room_id: int,
        db: Session = Depends(get_db)
    ):
    room = RoomService(db).delete(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return Response(status_code=status_HTTP_NO_CONTENT)


