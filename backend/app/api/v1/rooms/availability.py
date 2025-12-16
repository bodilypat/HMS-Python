#app/api/v1/rooms/room_availability.py

from datetime import date
from typing import List 

from fastapi import APIRouter, Query, Depends, HTTPException, status 
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.rooms.availability import AvailabilityResponse
from app.services.rooms.availability_service import AvailabilityService

router = APIRouter(prefix="/rooms", tags=["Room Availability"])

#---------------------------------------
# Get Available Rooms Endpoint
#---------------------------------------
@router.get(
    "/availability",
    response_model=List[AvailabilityResponse],
    summary="Get Available Rooms",
    description="Retrieve a list of available rooms for the specified date range.",
)
def get_available_rooms(
    start_date: date = Query(..., description="Start date for room availability (YYYY-MM-DD)"),
    end_date: date = Query(..., description="End date for room availability (YYYY-MM-DD)"),
    db: Session = Depends(get_db),
):
    if start_date > end_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Start date must be before or equal to end date.",
        )
    
    availability_service = AvailabilityService(db)
    available_rooms = availability_service.get_available_rooms(start_date, end_date)
    
    return available_rooms

#---------------------------------------
# Get Room Availability by ID Endpoint
#---------------------------------------
@router.get(
    "/{room_id}/availability",
    response_model=AvailabilityResponse,
    summary="Get Room Availability by ID",
    description="Retrieve availability details for a specific room by its ID.",
)
def get_room_availability_by_id(
    room_id: int,
    start_date: date = Query(..., description="Start date for room availability (YYYY-MM-DD)"),
    end_date: date = Query(..., description="End date for room availability (YYYY-MM-DD)"),
    db: Session = Depends(get_db),
):
    if start_date > end_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Start date must be before or equal to end date.",
        )
    
    availability_service = AvailabilityService(db)
    room_availability = availability_service.get_room_availability_by_id(room_id, start_date, end_date)
    
    if not room_availability:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Room with ID {room_id} not found or has no availability in the specified date range.",
        )
    
    return room_availability


