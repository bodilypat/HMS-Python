# backend/app/controllers/reservation_controller.py

from fastapi import APIRouter, HTTPException
from typing import List
from datetime import date 

from app.services.reservation_service import ReservationService 
from app.schemas.reservation_schema import (
	ReservationCreateSchema,
	ReservationUpdateSchema,
	ReservationResponseSchema
)

router = APIRouter(prefix="/reservations", tags=["Reservations"])
reservation_service = ReservationService()

@router.get("/", response_model=List[ReservationResponseSchema])
def get_all_reservation():
	"""
		Retrieve all reservations.
	"""
	return reservation_service.get_all_reservation()
	
@router.get("/{reservation_id}", response_model=ReservationResponseSchema)
def get_reservation_by_id(reservation_id: int):
    """
        Get a reservation by its ID.
    """
    reservation = reservation_service.get_reservation_by_id(reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, details="Reservation not found")
       return reservation
       
@router.post("/", response_model=ReservationResponseSchema, status_code=201)
def create_reservation(reservation_data: ReservationCreateSchema):
    """
        Create a new reservation.
    """
    try:
        return reservation_service.create_reservation(reservation_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        
@router.put("/{reservation_id}", response_model=ReservationResponseSchema)
def update_reservation(reservation_id: int, reservation_data: ReservationUpdateSchema):
    """
        Update an existing reservation.
    """
    update = reservation_service.update_reservation(reservation_id, reservation_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return updated
  
@router.delete("/{reservation_id}", status_code=204)
def delete_reservation(reservation_id: int):
    """
        Delete a reservation by ID.
    """
    delete = reservation_service.delete_reservation(reservation_id) 
    if not deleted:
        raise HTTPException(status_code=404, detail="Reservation not found")