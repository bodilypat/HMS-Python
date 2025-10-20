#app/api/amenities/room_amenity_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List 

from schemas.amenities.room_amenity import RoomAmenityCreate, RoomAmenityRead, RoomAmenityUpdate
from services.amenities import room_amenity_service as RoomAmenityService 
from db.session import get_db 

router = APIRouter(prefix="/room-amenities", tags=["Room Amenities"])

@router.get(
        "/",
        response_model=List[RoomAmenityRead],
        summary="List all amenities",
        description="Retrieve a paginated list of all room amenities available."
    )
def list_room_amenities(
        skip: int = Query(0, ge=0, description="Number of records to skip"),
        limit: int = Query(10, le=100, descriptin="Maximum number of records to return."),
        db: Session = Depends(get_db)
    ):
    return RoomAmenityService(db).get_all_room_amenities(skip=skip, limit=limit)

@router.get(
        "/{room_amenity_id}",
        response_model=RoomAmenityRead,
        summary="Get a single room amenity",
        description="Retrieve a specific room amenity by its ID."
    )
def get_room_amenity(
        room_amenity_id: int,
        db: Session = Depends(get_db)
    ):
    room_amenity = RoomAmenityService(db).get_room_amenity_by_id(room_amenity_id)
    if not room_amenity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room Amenity not found")
    return room_amenity

@router.post(
        "/",
        response_model=RoomAmenityRead,
        status_code=status.HTTP_201_CREATED,
        summary="Create a new room amenity",
        description="Add a new room amenity to the system."
    )
def create_room_amenity(
        room_amenity_data: RoomAmenityCreate,
        db: Session = Depends(get_db)
    ):
    return RoomAmenityService(db).create_room_amenity(room_amenity_data)

@router.put(
        "/{room_amenity_id}",
        response_model=RoomAmenityRead,
        summary="Update a room amenity",
        description="Update the details of an existing room amenity by its ID."
    )
def update_room_amenity(
        room_amenity_id: int,
        updated_room_amenity: RoomAmenityUpdate,
        db: Session = Depends(get_db)
    ):
    updated = RoomAmenityService(db).update_room_amenity(room_amenity_id, updated_room_amenity)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room Amenity not found")
    return updated 

@router.delete(
        "/{room_mainity_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a room amenity",
        description="Delete a room amenity by its ID."
    )
def delete_room_amenity(
        room_amenity_id: int,
        db: Session = Depends(get_db)
    ):
    success = RoomAmenityService(db).delete_room_amenity(room_amenity_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room Amenity not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)