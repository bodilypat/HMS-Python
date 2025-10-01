#app/controllers/booking/reservation_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List 

from schemas.booking.reservation import ReservationCreate, ReservationRead, ReservationUpdate
from services.booking import reservation_service as ReservationService
from db.session import get_db 

router = APIRouter(prefix="/reservations", tags=["Reservations"])

@router.get("/", response_model=List[ReservationRead], summary="List all reservations" )
def list_reservations(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, 100),
        db: Session = Depends(get_db)
    ):
    """ Retrieve a paginated list of all reservations."""
    return ReservationService(db).get_all_reservations(db, skip=skip, limit=limit)

@router.get("/{reservation_id}", response_model=ReservationRead, summary="Get reservation by ID.")
def get_reservation(
        reservation_id: int,
        db: Session = Depends(get_db)
    ):
    """ Retrieve a reservation by its ID."""
    reservation = ReservationService.get_reservation_by_id(reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail=" Reservation not found")
    return reservation 

@router.post("/", response_model=ReservationRead, status_code=status.HTTP_201_CREATED, summary="Create reservation")
def create_reservation(
        reservation_data: ReservationCreate,
        db: Session = Depends(get_db)
    ):
    """ Create new reservation."""
    return ReservationService(db).create_reservation(reservation_data)

@router.put("/{reservation_id}", response_model=ReservationRead, summary="Update resevation")
def update_reservation(
        reservation_id: int,
        updated_data: ReservationUpdate,
        db: Session = Depends(get_db)
    ):
    """ Update an existing reservation by ID."""
    updated = ReservationService(db).update_reservation(reservation_id, updated_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return updated 

@router.delete("/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a reservation")
def delete_reservation(
        reservation_id: int,
        db: Session = Depends(get_db)
    ):
    """ Delete a reservation by ID."""
    success = ReservationService(db).delete_reservation(reservation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)