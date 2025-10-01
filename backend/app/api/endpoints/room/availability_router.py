#app/api/room/availability_router.py 

from fastapi import APIRouter, Depends, HTTPException, Query, Response , status
from sqlalchemy.orm import Session 
from typing import List 

from schemas.room.availability import AvailabilityCreate, AvailabilityUpdate, AvailabilityRead
from db.session import get_db
from services.room import availability_service 

router = APIRouter(prefix="/availabilities", tags=["Availabilities"])

@router.get("/", response_model=List[AvailabilityRead], summary="Get a list all Availabiities" )
def read_availabilities(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return availability_service.get_all_availabilities(db, skip, limit)

@router.get("/{availability_id}", response_model=AvailabilityRead, summary="get a single Availabity by ID")
def read_availability(
        availability_id: int,
        db: Session = Depends(get_db)
    ):
    availability = availability_service.get_availability_by_id(db, availability_id)
    if not availability:
        raise HTTPException(status_code=404, detail="Availability not found")
    return availability

@router.post("/", response_model=AvailabilityRead, status_code=status.HTTP_201_CREATED, summary="Create a new availability")
def create_availability(
        availability_data: AvailabilityCreate,
        db: Session = Depends(get_db)
    ):
    return availability_service.create_availability(db, availability_data)

@router.put("/{availability_id}", response_model=AvailabilityRead, summary="Update an existing availability")
def update_availability(
        availability_id: int,
        updated_availability: AvailabilityUpdate,
        db: Session = Depends(get_db)
    ):
    updated = availability_service.update_availability(db, availability_id, updated_availability)
    if not updated:
        raise HTTPException(status_code=404, detail="Availability not found")
    return updated

@router.delete("/{availability_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete an availability")
def delete_availability(
        availability_id: int,
        db: Session = Depends(get_db)
    ):
    success = availability_service.delete_availability(db, availability_id)
    if not success:
        raise HTTPException(status_code=404, detail="Availability not found")
    return Response(status_code=status.HTTP_NO_CONTENT)
    
