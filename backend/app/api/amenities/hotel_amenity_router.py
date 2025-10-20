#app/api/amenities/hotel_amenity_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List 

from schemas.amenities.hotel_amenity_router import HotelAmenityCreate, HotelAmenityRead, HotelAmenityUpdate 
from services.amenties import hotel_service as HotelAmenityService
from db.session import get_db


router = APIRouter(prefix="/amenities", tags=["Hotel Amenities"])

@router.get(
        "/",
        response_model=List[HotelAmenityRead],
        summary="List all hotel amenties",
        description="Retrieve a paginated list of all hotel amenties available."
    )
def list_hotel_amenities(
        skip: int = Query(0, ge=0, description="Number of records to skip."),
        limit: int = Query(10, le=100, description="Maximum number of record to return"),
        db: Session = Depends(get_db)
    ):
    return HotelAmenityService(db).get_all_hotel_amenities(skip, limit)

@router.get(
        "/{amenity_id}",
        response_model=HotelAmenityRead,
        summary="Get a amenity by ID.",
        description="Retrieve a single hotel amenity by its unique ID."
    )
def get_hotel_amenity(
        amenity_id: int,
        db: Session = Depends(get_db)
    ):
    hotel_amenity = HotelAmenityService(db).get_hotel_amenity(amenity_id)
    if not hotel_amenity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hotel Amenity not found")
    return hotel_amenity

@router.post(
        "/",
        response_model=HotelAmenityRead,
        summary="Create a new hotel amenity",
        description="Add a new amenity to be available in the hotel."
    )
def create_hotel_amenity(
        hotel_amenity_data: HotelAmenityCreate,
        db: Session = Depends(get_db)
    ):
    return HotelAmenityService(db).create_hotel_amenity(hotel_amenity_data)

@router.put(
        "/{amenity_id}",
        response_model=HotelAmenityUpdate,
        summary="Update a hotel amenity",
        description="Update an existing amenity by its ID."
    )
def update_hotel_amenity(
        amenity_id: int,
        updated_hotel_amenity: HotelAmenityUpdate,
        db: Session = Depends(get_db)
    ):
    updated = HotelAmenityService(db).update_hotel_amenity(amenity_id, updated_hotel_amenity)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hotel Amenity not found")
    return updated 

@router.delete(
        "/{amenity_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a hotel amenity.",
        description="Remove a hotel amenty from the system using its ID."
    )
def delete_hotel_amenity(
        amenity_id: int,
        db: Session = Depends(get_db)
    ):
    success = HotelAmenityService(db).delete_hotel_amenity(amenity_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hotel Amenity not found")
    return Response(status_code=status.HTTp_204_NO_CONTENT)