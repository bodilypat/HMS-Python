#app/controllers/booking/availability_check_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Respomse
from sqlalchemy.orm import Session
from typing import List 

from schemas.booking.availability import AvaialbilityCreate, AvailablityUpdate, AvailabilityRead
from services.booking import availability_service as AvailabilityService
from db.session import get_db

router = APIRouter(prefix="/availability", tags=["Availability"])

@router.get("/", response_model=List[AvailabilityRead], summary="Get a list of room availabilities")
def read_availabilities(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    """ REtrieve a paginated list of room avaiabilities (skip, list)"""
    return AvailabilityService(db).get_all_availabilities(skip, limit)

@router.get("/{room_id}", response_model=AvailabilityRead, summary="Get room availability by ID")
def read_Availability(
        room_id: int,
        db: Session = Depends(get_db)
    ):
    """ Retrieve a single room availability by ID"""
    availability = AvailabilityService(db).get_availability_by_id(room_id)
    if not availability:
        raise HTTPException(status_code=404, detail="Room availability not found")
    return availability

@router.post("/", response_model=AvailabilityRead, status_code=status.HTTP_201_CREATED, summary="Create room availability")
def create_availability(
        room_availability: AvaialbilityCreate,
        db: Session = Depends(get_db)
    ):
    """ Create a new room availability etry."""
    return AvailabilityService(db).create_available(room_availability)

@ router.put("/{room_id}", response_model=AvailabilityRead, summary="Update room availability")
def update_availability(
        room_id: int,
        updated_availability: AvailablityUpdate,
        db: Session = Depends(get_db)
    ):
    """ Update an existing room availability by ID"""
    updated = AvailabilityService(db).update_able_room(room_id, updated_availability)
    if not updated:
        raise HTTPException(status_code=404, detail="Room availability not found")
    return updated 

@router.delete("/{room_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete room availability")
def delete_availability(
        room_id: int,
        db: Session = Depends(get_db)
    ):
    """ Delete a room avaiability by ID."""
    success = AvailabilityService(db).delete_able_room(room_id)
    if not success:
        raise HTTPException(status_code=404, detail="Room availability not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)