#app/controller/amenities/room_amenity_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List 

from schemas.amenities.room_amenity import RoomAmenityCreate, RoomAmenityRead, RoomAmenityUpdate 
from services.amenities import  room_amenity_service as RoomAmenityService 
from db.session import get_db 

router = APIRouter(prefix="/room-amenity", tags="Room Amenity")

@router.get("/", response_model=List[RoomAmenityRead], summary="Get a list Room Amenities")
def read_room_amenities(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, 100),
        db: Session = Depends(get_db)
    ):
    return RoomAmenityService(db).get_all_room_amenities(skip, limit)

@router.get("/{room_ameity_id}", response_model=RoomAmenityRead, detail="Get a single Room Amenity")
def read_room_amenity(
        room_amenity_id: int,
        db: Session = Depends(get_db)
    ):
    room_amenity = RoomAmenityService(db).get_room_amenity_by_id(room_amenity)
    if not room_amenity:
        raise HTTPException(status_code=404, detail="Room Amenity not found ")
    return room_amenity 

@router.post("/", response_model=RoomAmenityRead, status_code=status.HTTP_201_CREATE, detail="Create a new room amenity")
def create_room_amenity(
        room_amenity_in: RoomAmenityCreate,
        db: Session = Depends(get_db)
    ):
    return RoomAmenityService(db).create_room_amenity(room_amenity_in)

@router.put("/{room_amenity_id}", response_model=RoomAmenityRead, detail="Update an existing room amenity")
def update_room_amenity(
        room_amenity_id: int,
        updated_room_amenity: RoomAmenityUpdate,
        db: Session = Depends(get_db)
    ):
    updated = RoomAmenityService(db).update_room_amenity(room_amenity_id, updated_room_amenity)
    if not updated:
        raise HTTPException(status_code=404, detail="Room Amenity not found ")
    return updated 

@router.delete("/{room_amenity_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete room amenity")
def delete_room_amenity(
        room_amenity_id: int,
        db: Session = Depends(get_db)
    ):
    success = RoomAmenityService(db).delete_room_amenity(room_amenity_id)
    if not success:
        raise HTTPException(status_code=404, detail="Room amenity not found")
    return Response (status_code=status.HTTP_NO_CONTEN)


