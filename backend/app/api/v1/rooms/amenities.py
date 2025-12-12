#app/api/v1/rooms/amenities.py

from fastapi import APIRouter, Depends, Query
from typing import Optional, List 

from app.schemas.rooms import AmenityCreate, AmenityUpdate, AmenityResponse 
from app.services.rooms.ameknity_service import AmenityService 

router = APIRouter()

#----------------------------
# Get All Amenities
#----------------------------
@router.get("/", response_model=List[AmenityResponse])
async def get_all_amenities(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    name: Optional[str] = None,
    service: AmenityService = Depends(),
):
    """ 
    Retrieve all amenities with optional filtering by name and pagination.
    """
    return await service.get_all_amenities(
        page=page, 
        page_size=page_size,
        name=name
    )

#-----------------------------
# Get Amenity By ID
#-----------------------------
@router.get("/{amenity_id}", response_model=AmenityResponse)
async def get_amenity_by_id(
    amenity_id: int,
    service: AmenityService = Depends(),
):
    """ 
    Retrieve a single amenity by its ID.
    """
    return await service.get_amenity_by_id(amenity_id=amenity_id)

#---------------------------
# Create New Amenity
#---------------------------
@router.post("/", response_model=AmenityResponse)
async def create_amenity(
    amenity: AmenityCreate,
    service: AmenityService = Depends(),
):
    """ 
    Create a new amenity with the provided details.
    """
    return await service.create_amenity(amenity=amenity)

#----------------------------
# Update Amenity
#----------------------------
@router.put("/{amenity_id}", response_model=AmenityResponse)
async def update_amenity(
    amenity_id: int,
    amenity: AmenityUpdate,
    service: AmenityService = Depends(),
):
    """ 
    Update an existing amenity with the provided details.
    """
    return await service.update_amenity(amenity_id=amenity_id, amenity=amenity)

#----------------------------
# Delete Amenity
#----------------------------
@router.delete("/{amenity_id}", response_model=AmenityResponse)
async def delete_amenity(
    amenity_id: int,
    service: AmenityService = Depends(),
):
    """ 
    Delete an existing amenity by its ID.
    """
    await service.delete_amenity(amenity_id=amenity_id)
    return {"message": "Amenity deleted successfully"}



