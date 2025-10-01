#app/controllers/core/staff_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from dependancies import get_db 

from schemas.core.staff import StaffCreate, StaffRead, StaffUpdate 
from services.core.staff import StaffService 
from typing import List 

router = APIRouter(prefix="/users", tags=["User Management"])

@router.get("/", response_model=List[StaffRead], summary="Get a list of Staff")
def read_staff(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return StaffService(db).get_all_staffs(skip, limit)

@router.get("/{staff_id}", response_model=StaffRead, summary="Get a single of staff by ID")
def read_staff(
        staff_id: int,
        db: Session = Depends(get_db)
    ):
    staff = StaffService(db).get_staff_by(staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff 

@router.post("/", response_model=StaffRead, status_code=status.HTTP_201_CREATED, summary="Create a new Staff")
def create_staff(
        staff_in: StaffCreate,
        db: Session = Depends(get_db)
    ):
    new_staff = StaffService(db)
    if new_staff.get_user_by_email(staff_in.email):
        raise HTTPException(status_code=404, detail="Email already registed")
    return new_staff.create_staff(staff_in)

@router.put("{staff_id}", response_model=StaffRead, summary="Update existing Staff")
def update_staff(
        staff_id: int,
        updated_staff: StaffUpdate,
        db: Session = Depends(get_db)
    ):
    updated = StaffService(db).update_staff(staff_id, updated_staff)
    if not updated:
        raise HTTPException(status_code=404, detail="Staff not found")
    return updated 

@router.delete("{staff_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Staff")
def delete_staff(
        staff_id: int,
        db: Session = Depends(get_db)
    ):
    staff = StaffService(db).delete_staff(staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return None

