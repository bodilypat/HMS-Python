#app/api/core/guest_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from typing List 

from app.dependancies import get_db 
from app.schemas.core.guest_schema import GuestCreate, GuestUpdate, GuestRead 
from app.services.core.guest_service import GuestService 

router = APIRouter(prefix="/guests", tags=["Guest Management"])

# Dependancy injection for GuestService
def get_guest_service(db: Session = Depends(get_db)) -> GuestService:
    return GuestService(db)

@router.get(
        "/",
        response_model=List[GuestRead],
        summary="List all guests"
        response_description="List of guests returned successfully"
    )
def list_guests(
        skip: int = Query(0, ge=0, description="Number of record to skip"),
        limit: int = Query(10, le=100, description="MAximum number of records to return"),
        service: GuestService = Depends(get_guest_service)
    ):
    """
    Retrieve a paginated list of guests.
    """
    return service.get_all_guest(skip=skip, limit=limit)

@router.get(
        "/{guest_id}",
        response_model=GuestRead,
        summary="Get guest by ID",
        response_description="Guest retrieved successfully"
    )
def gt_guest_by_id(
        guest_id: int,
        service: GuestService = Depends(get_db)
    ):
    """
    Retrieve a guest by their unique ID.
    """
    guest = service.filter(guest_id)
    if not guest:
        raise HTTPException(status_code=status.HTTP_NOT_FOUND, detail="Guest not found")
    return guest 

@router.post(
        "/",
        response_model=GuestRead,
        status_code=status.HTTP_201_CREATED,
        summary="Create a new guest",
        response_description="Guest created successfully"
    )
def create_guest(
        guest_info: GuestCreate,
        service: GuestService = Depends(get_db)
    ):
    if service.get_guest_by_email(guest_info.email):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Guest not found")
    return service.create_guest(guest_data)

@router.put(
        "/{guest_id}",
        response_model=GuestRead,
        summary="Update guest information",
        response_description="Guest updated successfully"
    )
def update_guest(
        guest_id: int,
        guest_data: GuestUpdate,
        service: GuestService = Depends(get_db)
    ):
    """
    Update an existing guest's information.
    """
    updated_guest = service.update_guest(guest_id, guest_data)
    if not updated_guest:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detailt="Guest not found")
    return updated_guest

@router.delete(
        "/{guest_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a guest",
        response_description="Guest deleted successfully"
    )
def delete_guest(
        guest_id: int,
        service: GuestService = Depends(get_guest_service)
    ):
    """
    Delete a guest by their ID.
    """
    deleted = service.delete_guest(guest_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Guest not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


