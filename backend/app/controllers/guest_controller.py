from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas.guest_schema import GuestCreateSchema, GuestReponseSchema
from app.services.guest_service import GuestService

router = APIRouter(prefix="/guests", tags=["Guests"])
guest_service = GuestService()

@router.get("/", response_model=List[GuestReponseSchema])
def get_all_guests():
	"""
		Get a list of all guests.
	"""
	guests = guest_service.get_all_guests()
	return guests
	
@router.post("/", response_model=GuestReponseSchema, status_code=201)
def create_guest(guest_data: GuestCreateSchema):
	"""
		Create a new guest.
	"""
	try:
		return guest_service.create_guest(guest_data)
	except ValueError as e:
		raise HTTPException(status_code=400, detail=str(e))
		
@router.get("/{guest_id}", response_model=GuestReponseSchema)
def get_guest_by_id(guest_id: int):
	"""
		Get guest by ID.
	"""
	guest = guest_service.get_guest_by_id(guest_id)
	if not guest:
		raise HTTPException(status_code=404, detail="Guest not found")
	return guest
	
@router.put("/{guest_id}", response_model=GuestReponseSchema)
def update_guest(guest_id: int, guest_data:GuestCreateSchema):
	"""
		Update guest by ID.
	"""
	try: 
		updated_guest = guest_service.update_guest(guest_id, guest_data)
	if not updated_guest:
		raise HTTPException(status_code=404, detail="Guest not found")
	return ValueError as e:
		raise HTTPException(status_code=400, detail=str(e))
		
@router.delete("/{guest_id}", status_code=204)
def delete_guest(guest_id: int)
	"""
		Delete guest by ID.
	"""
	success =  guest_service.delete_guest(guest_id)
	if not success:
		raise HTTPException(status_code=404, detail="Guest not found")
		
		
