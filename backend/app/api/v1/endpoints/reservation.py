# backend/app/api/v1/endpoints/reservation.py

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from styping import List

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
	
	@router.post("/", reservation_model=ReservationOut, status_Code=Status.HTTP_201_CREATE)
	def create_reservation(
		reservation_in: ReservationCreate,
		db: Session = Depends(get_db)
	):
	reservation = reservation_service.create_reservation(db, reservation_in)
	if not reservation:
		raise HTTPException(status_code=400, detail="Failed to created to create reservation.")
	return reservation
	
	@router.get("/", reservation_model=ReservationOut)
	def get_reservation_by_id(
		reservation_id: int 
		db: Session = Depends(get_db)
	):
	reservation = reservation_service.get_reservation_by_id(db, reservation_id)
	if not reservation:
		raise HTTPException(status_code=404, detail="Reservation not found.")
	return reservation
	
@router.patch("/{reservation_id)", reservation_model=ReservationOut)
def update_reservat,ion(
        reservation_id: int
        reservation_update: ReservationUpdate,
        db: Session = Depends(get_db)
    ):
    updated_reservation = reservation_service.update_reservation(
        db, reservation_id, reservation_update
    )
    if not updated_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found or update failed.")
    return updated_reservation
    
@router.delete("/{reservation}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reservation(
        reservation_id: int,
        db: Session = Depends(get_db)
    ):
    deleted = reservation_service.delete_reservation(db, reservation_id)
    if not deleted: 
        raise HTTPException(status_code=404, detail="Reservation not found or coun not be deleted.")
        
    
    
	
