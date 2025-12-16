#app/api/v1/bookings/bookings.py

from typing import List 

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.bookings.booking import BookingCreate, BookingResponse, BookingUpdate
from app.services.bookings import BookingService


router = APIRouter()

# Dependency-injected service (testable & overrideable)
def get_booking_service(db: Session = Depends(get_db)) -> BookingService:
    return BookingService()

@router.post(
    "/", 
    response_model=BookingResponse, 
    status_code=status.HTTP_201_CREATED,
    summary="Create a new booking"
)
def create_booking(
    booking: BookingCreate, 
    db: Session = Depends(get_db),
    booking_service: BookingService = Depends(get_booking_service)
) -> BookingResponse:
    """
    Create a new booking with the provided details.
    """
    return booking_service.create_booking(db=db, booking=booking)

#------------------------------------
#  Get all bookings
#------------------------------------
@router.get(
    "/", 
    response_model=List[BookingResponse], 
    status_code=status.HTTP_200_OK,
    summary="Get all bookings"
)
def get_all_bookings(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    booking_service: BookingService = Depends(get_booking_service),
) -> List[BookingResponse]:
    """
    Retrieve a list of all bookings with pagination support.
    """
    booking = booking_service.get_all_bookings(db=db, skip=skip, limit=limit)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No bookings found."
        )
    return booking
#------------------------------------
#  Get booking by ID
#------------------------------------
@router.get(
    "/{booking_id}", 
    response_model=BookingResponse, 
    status_code=status.HTTP_200_OK,
    summary="Get booking by ID"
)
def get_booking_by_id(
    booking_id: int,
    db: Session = Depends(get_db),
    booking_service: BookingService = Depends(get_booking_service),
) -> BookingResponse:
    """
    Retrieve a booking by its ID.
    """
    booking = booking_service.get_booking_by_id(db=db, booking_id=booking_id)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Booking with ID {booking_id} not found."
        )
    return booking

#------------------------------------
#  Update booking by ID
#------------------------------------
@router.put(
    "/{booking_id}", 
    response_model=BookingResponse, 
    status_code=status.HTTP_200_OK,
    summary="Update booking by ID"
)
def update_booking_by_id(
    booking_id: int,
    booking_update: BookingUpdate,
    db: Session = Depends(get_db),
    booking_service: BookingService = Depends(get_booking_service),
) -> BookingResponse:
    """
    Update a booking by its ID with the provided details.
    """
    updated_booking = booking_service.update_booking_by_id(
        db=db, 
        booking_id=booking_id, 
        booking_update=booking_update
    )
    if not updated_booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Booking with ID {booking_id} not found."
        )
    return updated_booking

#------------------------------------
#  Delete booking by ID
#------------------------------------
@router.delete(
    "/{booking_id}", 
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete booking by ID"
)
def delete_booking_by_id(
    booking_id: int,
    db: Session = Depends(get_db),
    booking_service: BookingService = Depends(get_booking_service),
) -> None:
    """
    Delete a booking by its ID.
    """
    success = booking_service.delete_booking_by_id(db=db, booking_id=booking_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Booking with ID {booking_id} not found."
        )
    return None
