# backend/app/services/staff_service.py

from sqlalchemy.orm import Session
from typing import List, Optional

from app.models import Staff 
from app.schemas.staff import StaffCreate, StaffUpdate 

def create_staff(db: Session, staff_in: StaffCreate) -> Staff:
	"""
		Create a new staff member.
	"""
	new_staff = Staff(**staff_in.dict())
	db.add(new_staff)
	db.commit()
	db.refresh(new_staff)
	return new_staff
	
def get_all_staff(db: Session, skip: int = 0, limit: int = 20) -> List[Staff]:
	"""
		Retrieve a list of all staff members.
	"""
	return db.query(Staff).offset(skip).limit(limit).all()
    
def get_all_by_id(db: Session, Staff_id: int) -> Optional[Staff]:
    """
        Get a single staff member by ID.
    """
    return db.query(Staff).filter(Staff.staff_id == staff_id).first()
    
def update_staff(db: Session, staff_id: int, staff_in: StaffUpdate) -> Optional[Staff]:
    """
        Update an existing staff member.
    """
    staff = db.query(Staff).filter(Staff.staff_id == staff_id).first()
    if not staff:
        return None 
        
    for field, value in staff_in.dict(exclude_unset=True).item():
        setattr(staff, field, value)
        
    db.commit()
    db.refresh(staff)
    return staff
    
def delete_staff(db: Session, staff_id: int) -> bool:
    """
        Delete a staff member by ID.
    """
    staff = db.query(Staff).filter(Staff.staff_id == staff_id).first()
    if not staff:
        return False 
    
    db.delete(staff)
    db.commit()
    return True 
    
    