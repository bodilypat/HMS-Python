#app/api/v1/staff/staff.py
from typing import List 

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.staff import StaffCreate, StaffResponse, StaffUpdate
from app.services.staff import stafff_service as BookingService

router = APIRouter(prefix="/staff", tags=["Staff"])

#==================Create Staff Member==================#
@router.post("/", response_model=StaffResponse, status_code=status.HTTP_201_CREATED)
def create_staff(
    staff: StaffCreate,
    db: Session = Depends(get_db)
):
    db_staff = BookingService.get_staff_by_email(db, email=staff.email)
    if db_staff:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Staff member with this email already exists."
        )
    return BookingService.create_staff(db=db, staff=staff)

#==================Get All Staff Members==================#
@router.get("/", response_model=List[StaffResponse])
def get_all_staff(
    db: Session = Depends(get_db)
):
    return BookingService.get_all_staff(db)
#==================Get Staff Member by ID==================#
@router.get("/{staff_id}", response_model=StaffResponse)
def get_staff_by_id(
    staff_id: int,
    db: Session = Depends(get_db)
):
    db_staff = BookingService.get_staff_by_id(db, staff_id=staff_id)
    if not db_staff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff member not found."
        )
    return db_staff 
#==================Update Staff Member==================#
@router.put("/{staff_id}", response_model=StaffResponse)
def update_staff(
    staff_id: int,
    staff: StaffUpdate,
    db: Session = Depends(get_db)
):
    db_staff = BookingService.get_staff_by_id(db, staff_id=staff_id)
    if not db_staff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff member not found."
        )
    return BookingService.update_staff(db=db, staff_id=staff_id, staff=staff)
#==================Delete Staff Member==================#
@router.delete("/{staff_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_staff(
    staff_id: int,
    db: Session = Depends(get_db)
):
    db_staff = BookingService.get_staff_by_id(db, staff_id=staff_id)
    if not db_staff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff member not found."
        )
    BookingService.delete_staff(db=db, staff_id=staff_id)
    return None
