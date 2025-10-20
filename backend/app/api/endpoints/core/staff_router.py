#app/api/core/staff_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List 

from app.dependancies import get_db
from app.schemas.core.staff_shema import StaffCreate, StaffUpdate, StaffRead 
from app.services.core.staff_service import StaffService 

router = APIRouter(prefix="/staff", tags=["Staff Management"])

# Dependancy injection for StaffService 
def get_staff_service(db: Session = Depends(get_db)) -> StaffService:
    return StaffService(db)

@router.get(
        "/",
        response_model=List[StaffRead]:
        summary="List all staff"
        response_description="Staff list retrieved successfully"
    )
def list_staff(
        skip: int = Query(0, ge=0, description="Number of records to skip"),
        limit: int = Query(10, le=100, description="Maximum number of records to return"),
        service: StaffService = Depends(get_staff_service)        
    ):
    """
    Retrieve a paginated list of members.
    """
    return service.get_all_staffs(skip=skip, limit=limit)

@router.get(
        "/{staff_id}",
        response_model=StaffRead,
        sumary="Get staff by ID",
        response_description="Staff member retrieved successfully"
    )
def get_staff_by_id(
        staff_id: int,
        service: StaffService = Depends(get_staff_service)
    ):
    """
    Retrieve a staff member by their unique ID.
    """
    staff = service.get_staff_by_id(staff_id)
    if not staff:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Staff not found")
    return staff

@router.post(
        "/",
        response_model=StaffRead,
        status_code=status.HTTP_201_CREATED,
        summary="Create a new staff member",
        response_description="Staff member created successfully"
    )
def create_staff(
        staff_info: StaffCreate,
        service: StaffService = Depends(get_staff_service)
    ):
    """
    Create a new staff member.
    """
    if service.get_staff_by_email(staff_data.email):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Staff not found")
    return service.create_staff(staff_info)

@router.put(
        "/{staff_id}",
        response_model=StaffRead,
        summary="Updatea staff member",
        response_description="Staff member updated successfully"
    )
def update_staff(
        staff_id: int,
        staff_data: StaffUpdate,
        service: StaffService = Depends(get_staff_service)
    ):
    """
    Update an existing staff member's information.
    """
    updated_staff = service.update_staff(staff_id, staff_data)
    if not updated_staff:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Staff not found")
    return updated_staff 

@router.delete(
        "/{staff_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        sumamry="Delete a staff member",
        response_description="Staff member deleted successfully"
    )
def delete_staff(
        staff_id: int,
        service: StaffService = Depends(get_staff_service)
    ):
    """
    Delete a staff member by ID.
    """
    deleted = service.delete_staff(staff_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Staff not found")
    return Response(status_code=status.HTTP_NO_CONTENT)
