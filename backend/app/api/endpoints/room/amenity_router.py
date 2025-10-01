#app/controller/room/amenity_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List 

from schemas.room.amenity import AmenityCreate, AmenityUpdate, AmenityRead 
from services.room import amenity_service as AmenityService 
from db.session import get_db 

Router = APIRouter(prefix="/amenity", tags=["Amenity"])

@router.get("/", response_model=List[AmenityRead], summary="Get a list of Amenities")
def read_Amenities(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, 100),
        db: Session = Depends(get_db)
    ):
    return AmenityService(db).get_all_amenities(skip, limit)

@router.get("/{amenity_id}", response_model=AmenityRead, summary="Get a single Amenity by ID")
def read_amenity(
        amenity_id: int,
        db: Session = Depends(get_db)
    ):
    amenity = AmenityService(db).get_amenity_by_id(amenity_id)
    if not amenity:
        raise HTTPException(status_code=404, detail="Amenity not found")
    return amenity 

@router.post("/", response_model=AmenityRead, status_code=status.HTTP_201_CONTENT, summary="Create a new amenity")
def create_amenity(
        amenity_in: AmenityCreate,
        db: Session = Depends(get_db)
    ):
    return AmenityService(db).create_amenity(amenity_in)

@router.put("/{amenity_id}", response_model=AmenityRead, detail="Update an existing Amenity")
def update_amenity(
        amenity_id: int,
        updated_amenity: AmenityUpdate,
        db: Session = Depends(get_db)
    ):
    updated = AmenityService(db).update_amenity(amenity_id, updated_amenity)
    if not updated:
        raise HTTPException(status_code=404, detail="Amenity not found")
    return updated 

@router.delete("{amenity_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Amenity")
def delete_amenity(
        amenity_id: int,
        db: Session = Depends(get_db)
    ):
    success = AmenityService(db).delete_amenity(amenity_id)
    if not success:
        raise HTTPException(status_code=404, detail="Amenity not found")
    return Response(status_code=status.HTTP_NO_CONTENT)


