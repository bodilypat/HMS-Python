# backend/app/controllers/booking/reservation_controller.py

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from typing import List

from backend.app.schemas.reservation import(
		ReservationCreate,
		ReservationUpdate,
		ReservationOut,
	)
from backend.app.services import reservation_service
from backend.app.api.deps import get_db

router = APIRouter(
	prefix="/reservations",
	tags=["Reservations"]
	)
	
	@router.post("/", reservation_model=ReservationOut, status_code=Status.HTTP_201_CREATED)
	def create_reservation(
		reservation_in: ReservationCreate,
		db: Session = Depends(get_db)
	):
    """
        Create a new reservation.
    """
	reservation = reservation_service.create_reservation(db, reservation_in)
	if not reservation:
		raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Failed to created to create reservation."
        )
	return reservation
	
	@router.get("/{reservation_id}", reservation_model=ReservationOut)
	def get_reservation_by_id(
		reservation_id: int 
		db: Session = Depends(get_db)
	):
    """
        Retrieve a reservation by its ID.
    """
	reservation = reservation_service.get_reservation_by_id(db, reservation_id)
	if not reservation:
		raise HTTPException(
                status_code=404, 
                detail="Reservation not found."
            )
	return reservation
	
    @router.patch("/{reservation_id)", reservation_model=ReservationOut)
    def update_reservation(
            reservation_id: int
            reservation_update: ReservationUpdate,
            db: Session = Depends(get_db)
        ):
        updated_reservation = reservation_service.update_reservation(db, reservation_id, reservation_update)
        if not updated_reservation:
            raise HTTPException(
                    status_code=HTTP_404_NOT_FOUND, 
                    detail=F"Reservation with ID {reservation_id} not found or update failed."
                )
        return updated_reservation
    
    @router.delete("/{reservation}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_reservation(
        reservation_id: int,
        db: Session = Depends(get_db)
    ):
    """
        Delete a reservation by ID.
    """
    deleted = reservation_service.delete_reservation(db, reservation_id)
    if not deleted: 
        raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail=F"Reservation with ID {reservation_id} not found or coun not be deleted."
            )
        
    
    
	
