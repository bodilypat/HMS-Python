# backend/app/controllers/guest_controller.py

from fastapi import APIRouter, HTTPException, status
from backend.app.services.guest_service import GuestService
from backend.app.schemas.guest_schema import GuestCreate, GuestUpdate, GuestOut

router = APIRouter(prefix="/guests", tags=["Guests"])

@router.get("/", response_model=List[GuestOut])
def get_all_guests():
	"""
		Retrieve all guest records.
	"""
	guests = GuestService.get_all_guests()
	return guests
	
@router.get("/{guest_id}", response_model=GuestOut)
def get_guest_by_id(guest_id: int):
	"""
		Retrieve a guest by their unique ID.
	"""
	guest = GuestService.get_guest_by_id(guest_id)
	if not guest:
		raise HTTPException(status_code=404, detail="Guest not found")
	return guest

@router.post("/", response_model=GuestOut, status_code=status.HTTP_201_CREATED)
def create_guest(guest_data: GuestCreate):
	"""
		Create a new guest record.
	"""
    guest_id = GuestService.create_guest(guest_data.dict())
    if not guest_id:
        raise HTTPException(status_code=500, detail="Failed to create guest.")
    return GuestService.get_guest_by_id(guest_id)	
	
@router.put("/{guest_id}", response_model=GuestOut)
def update_guest(guest_id: int, guest_data:GuestUpdate):
	"""
		Update an existing guest's information.
	"""
    success = GuestService.update_guest(guest_id, guest_data.dict(exclude_unset=True))
    if not success:
        raise HTTPException(status_code=404, detial="Guest not found or update failed.")
    return GuestService.get_guest_by_id(guest_id)
		
@router.delete("/{guest_id}", status_code=status.204_NO_CONTENT)
def delete_guest(guest_id: int)
	"""
		Delete guest by ID.
	"""
	success = GuestService.delete_guest(guest_id)
	if not success:
		raise HTTPException(status_code=404, detail="Guest not found or delete failed.")
    return None
    
		
		