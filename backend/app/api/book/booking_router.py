#app/api/booking/booking_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List

from schemas.booking.booking_schema import BookingCreate, BookingUpdate, BookingRead 
from services.booking import booking_service as BookingService 
from db.session import get_db

router = APIRouter(prefix="/booking", tags=["Booking"])

@router.get(
        "/",
        response_model=List[BookingRead],
        summary="List all bookings",
        description="Retrieve a paginated list of all bookings"
    )
def list_booking(
        skip: int = Query(0, ge=0, description="Number of records to skip"),
        limit: int = Query(10, le=100, descriptiom="Maximum number of records to return"),
        db: Session = get_db                           
    ):
    """
    Get a paginated list of bookings.
    """
    return BookingService(db).get_all_booking(skip=skip, limit=limit)

@router.get(
        "/{booking_id}",
        response_model=BookingRead,
        summary="Get booking by ID",
        description="Retrieve a booking by its ID."
    )
def get_booking_by_id(
        booking_id: int,
        db: Session = Depends(get_db)
    ):
    """
    Retrieve a single booking entry by ID.
    """
    booking = BookingService(db).get_booking_by_id(booking_id)
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    return booking 

@router.post(
        "/",
        response_model=BookingRead,
        status_code=status.HTTP_201_CREATED,
        summary="Create a new booking",
        description="Create a new booking in the system"
    )
def create_booking(
        booking_data: BookingCreate,
        db: Session = Depends(get_db)
    ):
    return BookingService(db).create_booking(booking_data)

@router.put(
        "/{booking_id}",
        response_model=BookingRead,
        summary="Update booking",
        description="Update a existing booking by its ID"
    )
def update_booking(
        booking_id: int,
        updated_booking: BookingUpdate,
        db: Session = Depends(get_db)
    ):
    updated = BookingService(db).update_booking(booking_id, updated_booking)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    return updated 

@router.delete(
        "/{booking_id}", 
        status_code=status.HTTP_NO_CONTENT,
        summary="Deleting booking",
        description="Delete a booking by its ID."
    )
def delete_booking(
        booking_id: int,
        db: Session = Depends(get_db)
    ):
    deleted = BookingService(db).delete_booking(booking_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
