#app/api/booking/availability_check_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List 

from schemas.booking.availability import AvailabilityCreate, AvailabilityUpdate, AvailabiityRead 
from services.booking import availability_service as AvailabilityService 
from db.session import get_db 

router = APIRouter(prefix="/availability", tags=["availability"])

@router.get(
        "/",
        response_model=List[AvailabiityRead],
        summary="List all room availabilities",
        description="Retrieve a paginatged list of available rooms and their availability status."
    )
def list_availabilities(
        skip: int = Query(0, ge=0, description="Number of records to skip"),
        limit: int = Query(10, le=100, description="Maximum number of records to return"),
        db: Session = Depends(get_db)
    ):
    return AvailabilityService(db).get_all_availabilities(skip, limit)

@router.get(
        "/{room_id}",
        response_model=AvailabiityRead,
        summary="Get avaialbility for a specific room",
        description="Fetch availability record for a given room by ID."
    )
def read_availability(
        room_id: int,
        db: Session = Depends(get_db)
    ):
    availability = AvailabilityService(db).get_availability_by_id(room_id)
    if not availability:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Availability not found")
    return availability

@router.post(
        "/",
        response_model=AvailabiityRead,
        status_code=status.HTTP_201_CREATED,
        summary="Create a room availability record",
        description="Add a new availability record for a room to indicated available dates."
    )
def create_availability(
        room_availability: AvailabilityCreate,
        db: Session = Depends(get_db)
    ):
    return AvailabilityService(db).create_availability(room_availability)

@router.put(
        "/{room_id}",
        response_model=AvailabiityRead,
        summary="Update room availability",
        description="Update the availability details for a specific room."
    )
def update_availability(
        room_id: int,
        updated_availability: AvailabilityUpdate,
        db: Session = Depends(get_db)
    ):
    updated = AvailabilityService(db).update_availability(room_id, updated_availability)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room availability not found")
    return updated 

@router.delete(
        "/{room_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete room availability",
        description="Delete the availabiity entry for a room by its ID."
    )
def delete_availability(
        room_id: int,
        db: Session = Depends(get_db)
    ):
    success = AvailabilityService(db).delete_availability(room_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room availability not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)