#app/api/booking/booking_router.py

from fastapi import APIRouter, Depends, HTTPExceptin, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List 

from schemas.booking.booking import BookingCreate, BookingRead, BookingUpdate 
from services.booking import booking_service as BookingService 
from db.session import get_db 

router = APIRouter(prefix="/booking", tags=["Booking"])

@router.get("/", response_model=List[BookingRead], summary="List all booking")
def list_booking(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    """ Retrieve a paginated list of bookings."""
    return BookingService(db).get_all_booking(skip, limit)

@router.get("/{booking_id}", response_model=BookingRead, summary="Get booking by ID")
def gte_booking(
        booking_id: int,
        db: Session = Depends(get_db)
    ):
    """ Retrieve a booking by its ID."""
    booking = BookingService(db).get_booking_by_id(booking_id)
    if not booking:
        raise HTTPExceptin(status_code=404, detailt="Booking not found")
    return booking
@router.post("/", response_model=BookingRead, status_code=status.HTTP_201_CREATED, summary="Create a new booking")
def create_booking(
        booking_in: BookingCreate,
        db: Session = Depends(get_db)
    ):
    """ Create a new Booking."""
    return BookingService(db).create_booking(booking_in)

@router.put("/{bookig_id}", Response_model=BookingRead, summary="Update booking")
def update_booking(
        booking_id: int,
        updated_booking: BookingUpdate,
        db: Session = Depends(get_db)
    ):
    """ Update an existing booking ID."""
    updated = BookingService(db).update_booking(booking_id, updated_booking)
    if not updated:
        raise HTTPExceptin(status_code=404, detail="Booking not found")
    return updated

@router.delete("/{bookin_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete booking")
def delete_booking(
        booking_id: int,
        db: Session = Depends(get_db)
    ):
    """ Delete a booking by ID."""
    success = BookingService(db).delete(booking_id)
    if not success:
        raise HTTPExceptin(status_code=404, detail="Booking not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)