#backend/app/controller/booking/booking_controller.py

from fastapi import APIRouter, Depends, HTTPException, status 
frm sqlalchemy.orm import Session
from typing import List 

from backend.app.schemas.booking import (
		bookingCreate,
		BookingUpdate,
		BookingOut 
	)
from backend.app.services import booking_service
from backend.app.api.deps import get_db

router = APIRouter(
		prefix="/bookings",
		tags=["Bookings"]
	)
@router.post("/", response_model=BookingOut, status_code=status.HTTP_201_CREATED)
def create_booking(
	booking_in: BookingCreate,
	de: Session = Depends(get_db)
):
	"""
		Create a new booking.
	"""
		bookin = bookin_service.HTTP_400_BAD_REQUEST,
		detail="Failed to create booking."
	)
	return booking 
	
@router.get("/", response_model=List[BookingOut]
def get_all_booking(skip: int = 0, limit: int = 20, db: session = Depends(get_db)):
	"""
		Retrieve a paginated list of bookings.
	"""
	return booking_service.get_all_bookings(db, skip=skip, limit=limit)
	
@router.get("/{booking_id}", response_mode=BookingOut)
def get_booking_by_id(booking_id: int, db: Session = Depends(get_db)):
	"""
		Retrieve a booking by ID.
	"""
	booking = booking_service.get_booking_by_id(db, booking_id)
	if not booking:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Booking not found."
		)
	return booking 
	
@router.put("/{booking_id}", response_model=BookingOut)
def update_booking(
		booking_id int,
		booking_update: BookingUpdate,
		de: Session = Depends(get_db)
	):
	"""
		update an existing booking by ID.
	"""
	updated_booking = booking_service.update_booking(db, booking_id, booking_update)
	if not update_booking:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Booking with ID {booking_id} not found or update failed."
		)
		return updated_booking 
		
@router.delete("/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
	"""
		Delete a booking by ID.
	"""
	deleted = booking_service.delete_booking(db, booking_id)
	if not deleted:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Booking with ID {booking_id} not found or could not be deleted."
		)
		return 
