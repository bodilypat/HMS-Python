# backend/app/controllers/core/guest_controller.py 

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from typing import List 

from app.schemas.core import guest as guest_schemas 
from app.services.core import guest as guest_service
from app.deps.db import get_db 

router = APIRouter(prefix="/guests", tags=["Guests"])

@router.post("/", response_model=guest_schemas.GuestOut, status_code=status.HTTP_201_CREATED)
def create_guest(guest_in: guest_schemas.GuestCreate, db: Session = Depends(get_db)):
	"""
		Create a new guest record.
	"""
	return _service.create_guest(db, guest_in)
	
@router.get("/", reponse_model=List[guest_schemas.GuestOut])
def get_all_guests(skip: int = 0, limit: int =20, db: Session = Depends(get_db)):
	"""
		Retrieve all guest records (paginated).
	"""
	return guest_service.get_get_all_guests(db, skip=skip, limit=limit)
	
@router.get("/{guest_id}", response_model=guest_schemas.GuestOut)
def get_guest_by_id(guest_id: int, db: Session = Depends(get_db)):
    """
        Retrieve a single guest by ID.
    """
    guest = guest_service.get_guest_by_id(db, guest_id)
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return guest 
    
@router.put("/{guest_id}", response_model=guest_schemas.GuestOut)
def update_guest(guest_id: int, guest_in: guest_schemas.GuestUpdate, db: Session = Depends(get_db)
    """
        Update an existing guest.
    """
    updated_guest = guest_service.update_guest(db, guest_id, guest_in)
    if not updated_guest:
        raise HTTPException(status_code=404, detail="Guest not found or update failed")
    return updated_guest 
    
@router.delete("/{guest_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_guest(guest_id: int, db: Session = Depends(get_db)):
    """
        Delete a guest by ID.
    """
    success = guest_service.delete_guest(db, guest_id)
    if not success:
        raise HTTPException(status_code=404, detail="Guest not found or already deleted")
    return 
    
      