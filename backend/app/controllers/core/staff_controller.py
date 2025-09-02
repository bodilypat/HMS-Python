#backend/app/controllers/core/staff_controller.py

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from typing import List 

from app.schemas.core import staff as staff_schemas
from app.services.core import staff as staff_service 
from app.deps.db import get_db 

router = APIRouter(prefix="/staff", tags=["Staff"])

@router.post("/", response_model=staff_schemas.StaffOut, status_code=status.HTTP_201_CREATED)
def create_staff(staff_in: staff-schemas.StaffCreate, db: Session = Depends(get_db)):
	"""
		Create a new staff member.
	"""
	return staff_service.create_staff(db, staff_in)
	
@router.get("/", response_model=List[staff_schemas=StaffOut])
def get_all_staff(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
	"""
		Retrieve a paginated list of all staff member.
	"""
	return staff_sevice.get_all_staff(db, skip=skip, limit=limit)
	
@router.get("/{staff_id}", response_model=staff_schemas.StaffOut)
def get_staff_by_id(staff_id: int, db: Session = Depends(get_db)):
	"""
		Retrieve a single staff member by ID.
	"""
	staff = staff_service.get_staff_by_id(db, staff_id)
	if not staff:
		raise HTTPException(status_code=404, detail="Staff member not fpound")
	return staff 
	
@router.put("/{staff_id}", response_model=staff_schemas.StaffOut)
def update_staff(staff_id: int, staff_in: staff_schemas.StaffUpdate, db: Session = Depends(get_db)):
	"""
		Update ane existing staff member by ID.
	"""
	update_staff = staff_service.update_staff(db, staff_id, staff_in)
	if not update_staff:
		raise HTTPException(status_code=404, detail="staff member not found or update failed")
	return updated_staff 
	
@router.delete("/{staff_id}", response_model=status.HTTP_204_NO_CONTENT)
def delete_staff(staff_id: int, db: Session = Depends(get_db)):
	"""
		Delete a staff member by ID.
	"""
	success = staff_service.delete_staff(db, staff_id)
	if not success:
		raise HTTPException(status_code=404, detail="Staff member not found or already deleted")
	return 
	
	