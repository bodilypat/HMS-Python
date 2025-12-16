#app/api/v1/guests/guest.py 

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.guest import GuestCreate, GuestResponse, GuestUpdate
from app.services.guest_service import guest_service as GuestService

router = APIRouter(prefix="/guests", tags=["Guests"])

#================= Create Guest =================#

@router.post("/", response_model=GuestResponse, status_code=status.HTTP_201_CREATED)
def create_guest(guest: GuestCreate, db: Session = Depends(get_db)):
    db_guest = GuestService.get_guest_by_email(db, email=guest.email)
    if db_guest:
        raise HTTPException(status_code=400, detail="Email already registered")
    return GuestService.create_guest(db=db, guest=guest)
#================= List Guests =================#

@router.get("/", response_model=list[GuestResponse])
def list_guests(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    guests = GuestService.get_guests(db, skip=skip, limit=limit)
    return guests

#================= Get Guest by ID =================#

@router.get("/{guest_id}", response_model=GuestResponse)
def get_guest(guest_id: int, db: Session = Depends(get_db)):
    db_guest = GuestService.get_guest_by_id(db, guest_id=guest_id)
    if not db_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return db_guest

#================== Update Guest =================#

@router.put("/{guest_id}", response_model=GuestResponse)
def update_guest(guest_id: int, guest: GuestUpdate, db: Session = Depends
(get_db)):
    db_guest = GuestService.get_guest_by_id(db, guest_id=guest_id)
    if not db_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return GuestService.update_guest(db=db, guest_id=guest_id, guest=guest)

#================= Delete Guest =================#

@router.delete("/{guest_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_guest(guest_id: int, db: Session = Depends(get_db)):
    db_guest = GuestService.get_guest_by_id(db, guest_id=guest_id)
    if not db_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    GuestService.delete_guest(db=db, guest_id=guest_id)
    return None

