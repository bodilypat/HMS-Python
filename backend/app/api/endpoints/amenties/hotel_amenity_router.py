#app/api/endpoint/amenities/hotel_amenity_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response
from sqlalchemy.orm import Session
from typing import List 

from schemas.amenities import HotelAmenityCreate, HotelAmenityRead, HotelAmenityUpdate
from db.session import get_db
from services.amenities import hotel_amenity_service as HotelAmenityService

router = APIRouter(prefix="/amenities", tags=["Amenities"])

@router.get("/", response_model=HotelAmenityRead, summary="List all hotel amenities")
def list_hotel_amenities(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    """ Retrieve a paginated list of hotel amenities."""
    return HotelAmenityService(db).get_all_hotel_amenities(skip=skip, limit=limit)

@router.get("{amenity_id}", response_model=HotelAmenityRead, summary="Get a hotel amenity by ID.")
def get_hotel_amenity(
        amenity_id: int,
        db: Session = Depends(get)
    ):
    """ Retrieve a single hotel amenity by its ID."""
    amenity = HotelAmenityService(db).get_hotel_amenity_by_id(amenity_id)
    if not amenity:
        raise HTTPException(status_code=404, detail="Hotel amenity not found.")
    return amenity

@router.post("/", response_model=HotelAmenityRead, status_code=status.HTTP_201_CREATED, summary="Create a new hotel amenity")
def create_hotel_amenity(
        amenity_data: HotelAmenityCreate,
        db: Session = Depends(get_db)
    ):
    """ Create a new hotel amenity."""
    return HotelAmenityService(db).create_hotel_amenity(amenity_data)

@router.put("/{amenity_id}", response_model=HotelAmenityRead, summary="Update a hotel amenity")
def update_hotel_amenity(
        amenity_id: int,
        updated_aminity: HotelAmenityUpdate,
        db: Session = Depends(get_db)
    ):
    """ Update an existing hotal amenity by ID."""
    updated = HotelAmenityService(db).update_hotel_amenity(amenity_id, updated_aminity)
    if not updated:
        raise HTTPException(status_code=404, detail="Hotel amenity not found")
    return updated 

@router.delete("/{amenity}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a hotel amenity")
def delete_hotel_amenity(
        amenity_id: int,
        db: Session = Depends(get_db)
    ):
    """ Delete a hotel amenity by ID."""
    success = HotelAmenityService(db).delete_hotel_amenity(amenity_id)
    if not success:
        raise HTTPException(status_code=404, detail="Hotel amenity not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
