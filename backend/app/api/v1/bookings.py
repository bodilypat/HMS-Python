#api/v1/bookings.py

# Bookings API endpoints

from fastapi import APIRouter, Depends, Query
from typing import Optional, List 

from app.schemas.bookings import (
    BookingCreate,
    BookingUpdate,
    BookingOut
)
from app.services.bookings.booking_service import BookingService

router = APIRouter()

#-------------------
# Get All Bookings 
#-------------------

@router.get("/", response_model=List[BookingOut], tags=["Bookings"])
async def get_all_bookings(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    guest_id: Optional[int] = None,
    room_id: Optional[int] = None,
    status: Optional[str] = None,
    booking_service: BookingService = Depends()
):
    """ 
    Retrieve paginated and filterable list of booking 
    """
    return await booking_service.get_all_bookings(
      page=page, 
      page_size=page_size, 
      guest_id=guest_id, 
      room_id=room_id, 
      status=status
    )

#-----------------------
# Get Booking by ID
#-----------------------
@router.get("/{booking_id}", response_model=BookingOut, tags=["Bookings"])
async def get_booking_by_id(
    booking_id: int,
    booking_service: BookingService = Depends()
):  
    """ 
    Retrieve a booking by its ID
    """
    return await booking_service.get_booking_by_id(booking_id=booking_id)

#-----------------------
# Create New Booking 
#-----------------------
@router.post("/", response_model=BookingOut, tags=["Bookings"])
async def create_booking(
    booking: BookingCreate,
    booking_service: BookingService = Depends()
):
    """ 
    Create a new booking (including date validation & availability checks).
    """
    return await booking_service.create_booking(booking=booking)

#-----------------------
# Update Booking by ID
#-----------------------
@router.put("/{booking_id}", response_model=BookingOut, tags=["Bookings"])
async def update_booking(
    booking_id: int,
    booking: BookingUpdate,
    booking_service: BookingService = Depends()
):
    """ 
    Update an existing booking by its ID (including date validation & availability checks).
    """
    return await booking_service.update_booking(booking_id=booking_id, booking=booking)

#-----------------------
# Cancel Booking
#-----------------------
@router.delete("/{booking_id}", response_model=BookingOut, tags=["Bookings"])
async def cancel_booking(
    booking_id: int,
    booking_service: BookingService = Depends()
):
    """ 
    Cancel an existing booking by its ID.
    """
    await booking_service.cancel_booking(booking_id=booking_id)
    return {"message": "Booking cancelled successfully."}


