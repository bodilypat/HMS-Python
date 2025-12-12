#app/api/v1/staff.py

from fastapi import APIRouter, Depends, Query 
from typing import Optional, List
from app.schemas.staff import (
    StaffCreate,
    StaffUpdate,
    StaffOut
)
from app.services.staff.staff_service import StaffService 

router = APIRouter()

#-----------------------
# Get All Staff (with filters & pagination)
@router.get("/", response_model=List[StaffOut], tags=["Staff"])
async def get_all_staff(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    name: Optional[str] = None,
    email: Optional[str] = None,
    role: Optional[str] = None,
    active: Optional[bool] = None,
    staff_service: StaffService = Depends(),
):
    """ 
    Retrieve all staff members with optional filters and pagination.
    """
    return await staff_service.get_all_staff(
        page=page,
        page_size=page_size,
        name=name,
        email=email,
        role=role,
        active=active
    )

#-----------------------------
# Get Staff by ID
#-----------------------------
@router.get("/{staff_id}", response_model=StaffOut, tags=["Staff"])
async def get_staff_by_id(
    staff_id: int,
    staff_service: StaffService = Depends(),
):
    """
    Retrieve a staff member by their ID.
    """
    return await staff_service.get_staff_by_id(staff_id=staff_id)

#------------------------------
# Create a New Staff Member
#------------------------------
@router.post("/", response_model=StaffOut, tags=["Staff"])
async def create_staff(
    staff: StaffCreate,
    staff_service: StaffService = Depends(),
):
    """ 
    Create a new staff member.
    """
    return await staff_service.create_staff(staff=staff)

#------------------------------
# Update Staff Member
#------------------------------
@router.put("/{staff_id}", response_model=StaffOut, tags=["Staff"])
async def update_staff(
    staff_id: int,
    staff: StaffUpdate,
    staff_service: StaffService = Depends(),
):
    """ 
    Update an existing staff member by their ID.
    """
    return await staff_service.update_staff(staff_id=staff_id, staff=staff)

#------------------------------
# Delete Staff Member
#------------------------------
@router.delete("/{staff_id}", response_model=StaffOut, tags=["Staff"])
async def delete_staff(
    staff_id: int,
    staff_service: StaffService = Depends(),
):
    """ 
    Delete a staff member by their ID.
    """
    await staff_service.delete_staff(staff_id=staff_id)
    return {"message": "Staff member deleted successfully."}


