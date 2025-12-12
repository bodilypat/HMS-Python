#api/v1/guests.py

from fastapi import APIRouter, Depends, Query
from typing import Optional, List 

from app.schemas.guests import (
    GuestCreate,
    GuestUpdate,
    GuestOut
)
from app.services.guests.guest_service import GuestService

router = APIRouter()

#--------------------------------------------
# Get All Guests (with filters & pagination)
#--------------------------------------------
@router.get("/", response_model=List[GuestOut], tags=["Guests"])
async def get_all_guests(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    name: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    guest_service: GuestService = Depends()
):
    """ 
    Retrieve all guests with optional filters and pagination.
    """
    return await guest_service.get_all_guests(
        page=page, 
        page_size=page_size, 
        name=name, 
        email=email, 
        phone=phone
    )

#--------------------------------
# Get Guest by ID
#--------------------------------
@router.get("/{guest_id}", response_model=GuestOut, tags=["Guests"])
async def get_guest_by_id(
    guest_id: int,
    guest_service: GuestService = Depends()
):
    """ 
    Retrieve a guest by their ID. 
    """
    return await guest_service.get_guest_by_id(guest_id=guest_id)

#--------------------------------
# Create Guest 
#--------------------------------
@router.post("/", response_model=GuestOut, tags=["Guests"])
async def create_guest(
    guest: GuestCreate,
    guest_service: GuestService = Depends()
):
    """ 
    Create a new guest. 
    """
    return await guest_service.create_guest(guest=guest)

#---------------------------------
# Update Guest
#---------------------------------
@router.put("/{guest_id}", response_model=GuestOut, tags=["Guests"])
async def update_guest(
    guest_id: int,
    guest: GuestUpdate,
    guest_service: GuestService = Depends()
):
    """ 
    Update an existing guest by their ID. 
    """
    return await guest_service.update_guest(guest_id=guest_id, guest=guest)

#---------------------------------
# Delete Guest
#---------------------------------
@router.delete("/{guest_id}", response_model=GuestOut, tags=["Guests"])
async def delete_guest(
    guest_id: int,
    guest_service: GuestService = Depends()
):
    """ 
    Delete a guest by their ID. 
    """
    await guest_service.delete_guest(guest_id=guest_id)
    return {"message": "Guest deleted successfully"}


