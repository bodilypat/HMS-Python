# backend/app/controllers/core/guest_controller.py

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from typing import List

from app.schemas import guest as guest_schemas
from app.services import guest_service
from app.api.deps import get_db 

router = APIRouter(prefix="/guests", tags=["Guests"])

@router.post("/", response_model=guest_schemas.GuestOut, status_code=status.HTTP_201_CREATED)
def create_guest(guest_in: guest_schemax.GuestCreate, db: Session = Depends(get_db)):
    """
        Create a new guest record.
    """
    return guest_service.create_guest(db, guest_in)
    
@router.get("/", response_model=List[guest_schemas.GuestOut)
    def get_all_guest(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
        """
            Retrieve all guest records (paginated).
        """
        return guest_service.get_guest(db, skip=skip, limit=limit)
        
@router.get("/{guest_id}", response_model=guest_schemas.GuestOut)
    def get_guest_by_id(guest_id: int, db: Session = Depends(get_db):
    """
        Retrieve a single guest by ID.
    """
    guest = guest_service.get_guest_by_id(db, guest_id)
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return guest 

@router.put("/{guest_id}", response_model=guestt_schemas.GuestOut)
    def update_guest(guest_id: int, guest_in: guest_schemax.GuestUpdate, db: Session = Depends(get_db)
    """
        Update an exiting guest.
    """
    updated_guest = guest_service.update_guest(db, guest_id, guest_in)
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found or update failed")
    return guest 
    
@router.delete("/{guest_id)", status_code=status.HTTP_204_NO_CONTENT)
    def delete_guest(guest_id: int, db: Session = Depends(get_db)):
    """
        Delete a guest by ID.
    """
    success = guest_service.delete_guest(db_guest_id)
    if not success:
        raise HTTPException(status_code=404, detail="Guest not found or already deleted")
    return
