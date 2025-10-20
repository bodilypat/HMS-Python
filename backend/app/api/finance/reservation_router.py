#app/api/booking/reservation_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List 

from schemas.booking.reservation_schema import ReservationCreate, ReservationUpdate, ReservationRead 
from services.booking import reservation_service as ReservationService 
from db.session import get_db 

router = APIRouter(prefix="reservations", tags=["Reservations"])

@router.get(
        "/",
        response_model=List[ReservationRead],
        summary="List all reservations",
        description="Retrieve a paginated list of all reservations."
    )
def list_reservations(
        skip: int = Query(0, ge=0, descrption="Item to skip"),
        limit: int = Query(10, le=100, description="Maximum number of items to return"),
        db: Session = Depends(get_db)
    ):
    return ReservationService(db).get_all_reservations(skip=skip, limit=limit)


@router.get(
        "/{reservation_id}",
        response_model=ReservationRead,
        summary="Get reservation by ID",
        description="Retrieve details of a reservation by its ID."
    )
def read_reservation(
        reservation_id: int,
        db: Session = Depends(get_db)
    ):
    reservation = ReservationService(db).get_reservation_by_id(reservation_id)
    if not reservation:
        raise HTTPException(status_code=status.HTTP_404_NOT_fOUND, detail="Reservation not found")
    return reservation 

@router.post(
        "/",
        response_model=ReservationRead,
        summary="Create a reservation",
        description="Create a new reservation in the system"
    )
def create_reservation(
        reservation_data: ReservationCreate,
        db: Session = Depends(get_db)
    ):
    return ReservationService(db).create_reservation(reservation_data)

@router.put(
        "/{reservation_id}",
        response_model=ReservationRead,
        summary="Update a reservation",
        description="Update an existing reservation by its ID."
    )
def update_reservation(
        reservation_id: int,
        updated_reservation: ReservationUpdate,
        db: Session = Depends(get_db)
    ):
    updated = ReservationService(db).update_reservation(reservation_id, updated_reservation)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found")
    return updated 

@router.delete(
        "/{reservation_id}"
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a reservation",
        description="Delete a reservation by its ID."
    )
def delete_reservation(
        reservation_id: int,
        db: Session = Depends(get_db)
    ):
    success = ReservationService(db).delete_reservation(reservation_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)