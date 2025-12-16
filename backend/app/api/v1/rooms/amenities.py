#app/api/v1/rooms/amenities.py
"""
CRUD endpoint for managing room amenities in the Hotel Management System. 
"""
from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from typing import List

from app.database.session import get_db
from app.schemas.rooms.amenity import AmenityCreate, AmenityUpdate, AmenityOut
from app.services.rooms.amenity_service import AmenityService

router = APIRouter()
amenity_service = AmenityService()
#---------------------------------
# Create Amenity
#---------------------------------
@router.post(
        "/", 
        response_model=AmenityOut, 
        status_code=status.HTTP_201_CREATED
    )
def create_amenity(
    amenity_in: AmenityCreate,
    db: Session = Depends(get_db)
):
    """
    Docstring for create_amenity
    
    :param amenity_in: Description
    :type amenity_in: AmenityCreate
    :param db: Description
    :type db: Session
    """
    amenity = amenity_service.create_amenity(db, amenity_in)
    if not amenity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Amenity could not be created"
        )
    return amenity

#---------------------------------
# Get All Amenities
#---------------------------------
@router.get(
        "/", 
        response_model=List[AmenityOut]
        status_code=status.HTTP_200_OK
    )
def get_amenities(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """
    Docstring for get_amenities
    :param skip: Description
    :type skip: int
    :param limit: Description
    :type limit: int
    :param db: Description
    :type db: Session
    :return: Description
    :rtype: List[AmenityOut]

    """
    amenities = amenity_service.get_amenities(db, skip=skip, limit=limit)
    return amenities

#---------------------------------
# Get Amenity by ID
#---------------------------------
@router.get(
        "/{amenity_id}", 
        response_model=AmenityOut, status_code=status.HTTP_200_OK
    )
def get_amenity(
    amenity_id: int,
    db: Session = Depends(get_db)
):
    """
    Docstring for get_amenity
    
    :param amenity_id: Description
    :type amenity_id: int
    :param db: Description
    :type db: Session
    """
    amenity = amenity_service.get_amenity_by_id(db, amenity_id)
    if not amenity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Amenity not found")
    return amenity

#---------------------------------
# Update Amenity
#---------------------------------
@router.put(
        "/{amenity_id}", 
        response_model=AmenityOut,
        status_code=status.HTTP_200_OK)
def update_amenity(
    amenity_id: int,
    amenity_in: AmenityUpdate,
    db: Session = Depends(get_db)
):
    """
    Docstring for update_amenity
    
    :param amenity_id: Description
    :type amenity_id: int
    :param amenity_in: Description
    :type amenity_in: AmenityUpdate
    :param db: Description
    :type db: Session
    """
    amenity = amenity_service.update_amenity(db, amenity_id, amenity_in)
    if not amenity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Amenity not found")
    return amenity

#---------------------------------
# Delete Amenity
#---------------------------------
@router.delete(
        "/{amenity_id}", 
        status_code=status.HTTP_204_NO_CONTENT
    )
def delete_amenity(
    amenity_id: int,
    db: Session = Depends(get_db)
):
    """
    Docstring for delete_amenity
    
    :param amenity_id: Description
    :type amenity_id: int
    :param db: Description
    :type db: Session
    """
    success = amenity_service.delete_amenity(db, amenity_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Amenity not found")
    return None

