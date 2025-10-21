#app/api/booking/availability_check_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List 

from schemas.booking.availability_schema import(
        AvailabilityCreate,
        AvailabilityUpdate,
        AvailabilityRead
    )
from services.booking.availability_service import AvailabilityService
from db.session import get_db 

router = APIRouter(
        prefix="/availability", 
        tags=["Availability"], 
        response={404: {"description": "Not found"}}
    )
def get_service(db: Session = Depends(get_db)) -> AvailabilityService:
    return AvailabilityService(db)

@router.get(
        "/",
        response_model=List[AvailabilityRead],
        summary="List all room availabilities",
        description="Retrieve a paginatged list of available rooms and their availability status."
    )
def list_availabilities(
        skip: int = Query(0, g=0, description="Number of records to skip"),
        limit: int = Query(10, le=100, description="Maximum number of record to return"),
        service: AvailabilityService = Depends(get_service)
    ):
    return service.get_all_availabilities(skip, limit)

@router.get(
        "/{room_id}",
        response_model=AvailabilityRead,
        summary="Get acailability for a specific room",
        description="Fetch availability details for a specific room by its ID."
    )
def read_availability(
        room_id: int,
        service: AvailabilityService = Depends(get_service)
    ):
    availability = service.get_availability_by_id(room_id)
    if not availability:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Availability not found for room ID {room_id}")
    return availability 

@router.post(
        "/",
        response_model=AvailabilityRead,
        status_code=status.HTTP_201_CREATED,
        summary="Create a room availability record.",
        description="Create a new availability record for a room indicating avaiable dates.",
    )
def create_Availability(
        room_availability: AvailabilityCreate,
        service: AvailabilityService = Depends(get_service)
    ):
    return service.create_availability(room_availability)

@router.put(
        "/{room_id}",
        response_model=AvailabilityRead,
        summary="Update room availability",
        description="Modify the availability details for a specific room.",
    )
def update_availability(
        room_id: int,
        updated_availability: AvailabilityUpdate,
        service: AvailabilityService = Depends(get_service),
    ):
    updated = service.update_availability(room_id, updated_availability)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Availability not found room id {room_id}")
    return updated 

@router.delete(
        "/{room_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete room avaiability",
        description="Remove the availability record for a room by its ID.",
    )
def delete_availability(
        room_id: int,
        service: AvailabilityService = Depends(get_service)
    ):
    success = service.delete_availability(room_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Availability not found for room ID {room_id}")
    return Response(status_code=status.HTTP_204_NO_CONTENT)






