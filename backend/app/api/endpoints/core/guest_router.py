#app/controller/core/guest_router.py

from fastap import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List

from dependencies import get_db
from schemas.core.guest import GuestCreate, GuestRead, GuestUpdate
from services.core.guest import GuestService

router = APIRouter(prefix="/users", tags=["User Management"])

@router.get("/", response_model=List[GuestRead], summary="Get a list of Guests" )
def read_guests(
        skip: int = Query(0, ge=0),
        limit: int = Query(10,le=100),
        db: Session = Depends(get_db)
    ):
    return GuestService(db).get_all_guests(skip,limit)

@router.get("/{guest_id}", response_model=GuestRead, summary="Get a single Guest by ID")
def read_guest(
        guest_id: int,
        db: Session = Depends(get_db)
    ):
    guest = GuestService(db).get_guest_by_id(guest_id)
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return guest 
@router.post("/", response_model=GuestRead, status_code=status.HTTP_201_CREATED, summary="Create a new guest")
def create_guest(
        guest_in: GuestCreate,
        db: Sesssion = Depends(get_db)
    ):
    new_guest = GuestService(db)
    if new_guest.get_guest_by_email(guest_in.email):
        raise HTTPException(status_code=404, detail="Guest not found")
    return new_guest.create_guest(guest_in)
@router.put("/{guest_id}", response_model=GuestRead, summary="Update an existing Guest")
def update_guest(
    guest_id: int,
    updated_guest: GuestUpdate,
    db: Session = Depends(get_db)
    ):
    updated = GuestService(db).update_guest(guest_id, updated_guest)
    if not updated:
        raise HTTPException(status_code=404, detail="Guest not found")
    return updated

@router.delete("/{guest_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Guest")
def delete_guest(
        guest_id: int,
        db: Session = Depends(get_d)
    ):
    guest = GuestService(db).delete_guest(guest_id)
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return Response(status_code=status.HTTP_NO_CONTENT)

