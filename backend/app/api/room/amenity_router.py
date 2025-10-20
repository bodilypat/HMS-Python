#app/api/room/amenity_router.py

from fastapi import APIRouter, Depends, HTTPException, status, query, Response 
from sqlalchemy.orm import Session 
from typing import List 

from schemas.amenities.amenity_schema import AmenityCreate, AmenityUpdate, AmenityRead 
from services.amenities import amenity_service as AmenityService 
from db.session import get_db 

router = APIRouter(prefix="/amenities", tags=["Amenties"])

@router.get(
        "/",
        response_model=List[AmentiyRead],
        summary="",
        description=""
    )
def list_amenties(
        skip: int = Query(0, ge=0, description=""),
        limit: int = Query(10, le=100, description=""),
        db: Session = Depends(get_db)
    ):
    return AmenityService(db).get_all_amenities(skip=skip, limit=limit)

@router.get(
        "/{amenity_id}",
        response_mode=AmenityRead,
        summary="",
        description=""
    )
def read_amenity(
        amenity_id: int,
        db: Session = Depends(get_db)
    ):
    amenity = AmenityService(db).get_amenity_by_id(amenity_id)
    if not amenity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Amenity not found")
    return amenity 

@router.post(
        "/",
        response_model=AmenityRead,
        status_code=status.HTTP_201_CREATED,
        summary="",
        description=""
    )
def create_amenity(
        amenity_data: AmenityCreate,
        db: Session = Depends(get_db)
    ):
    try:
        return AmenityService(db).create_amenity(amenity_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post(
        "/{amenity_id}",
        response_model=AmenityRead,
        summary="",
        description=""
    )
def update_amenity(
        amenity_id: int,
        updated_amenity: AmenityUpdate,
        db: Session = Depends(get_db)
    ):
    updated = AmenityService(db).update_amenity(amenity_id, updated_amenity)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Amenity not found")
    return updated 

@router.delete(
        "/{amenity_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="",
        description=""
    )
def delete_amenity(
        amenity_id: int,
        db: Session = Depends(get_db)
    ):
    success = AmenityService(db).delete_amenity(amenity_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Amenity not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


