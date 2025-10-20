#app/api/room/availability_router.py

from fastapi import APIRouter, Depends, HTTPException, Query, Response
from sqlalchemy.orm import Session
from typing import List 

from schemas.room.availability import(
        AvailabilityCreate,
        AvailabilityUpdate,
        AvailabilityRead,
    )
from db.session import get_db
from service.room import AvailabilityService 

router = APIRouter(prefix="/availabilities", tags=["Availabilities"])

@router.get("/", response_model=List[AvailabilityRead], summary="List all availabilities", description="Retrieve a paginated list of all room availabilities.")
def list_availabilities(
        skip: int = Query(0, ge=0, description="Number of records to skip"),
        limit: int = Query(10, le=100, description="Maximum number of records to return"),
        db: Session = Depends(get_db)
    ):
    """
        Get a list all room availabilities.
    """
    return AvailabilityService(db).get_all_availabilities(skip=skip, limit=limit)

@router.get(
        "/{availability_id}", 
        response_model=AvailabilityRead, summary="Get availability by ID", 
        description="Retrieve a specific availability entry by its ID."
    )
def read_availability(
        availability_id: int, 
        db: Session = Depends(get_db)
    ):
    """ 
        Get a specific avaiability by its ID.
    """
    availability = AvailabilityService(db).get_availability_by_id(availability_id)
    if not availability:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Availability not found")
    return availability

@router.post(
        "/",
        response_model=AvailabilityRead,
        status_code=status.HTTP_201_CREATED,
        summary="Create a new availability",
        description="Create a new availability record for a room."
    )
def create_availability(
        availability_data: AvailabilityCreate,
        db: Session = Depends(get_db)
    ):
    """
        Create a new availability entry.
    """
    return AvaiablityService(db).create_availability(availability_data)

@router.put(
        "/{availability_id}",
        response_model=AvailabilityRead,
        summary="Update availability",
        description="Update an existing availability by ID."
    )
def update_availability(
        availability_id: int,
        updated_availability: AvailabilityUpdate,
        db: Session = Depends(get_db)
    ):
    """
        Update an existing availability entry.
    """
    updated = AvailabilityService(db).update_availability(availability_id, updated_availability)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Availability not found")
    return updated

@router.delete(
        "/{availability_id}",
        status_code=status.HTTP_204_NO_FOUND,
        summary="Delete availability",
        description="Delete an availability record by ID."
    )
def delete_availability(
        availability_id: int,
        db: Session = Depends(get_db)
    ):
    """
        Delete an availability entry by its ID.
    """
    success = AvailabilityService(db).delete_availability(availability_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AVailability not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
