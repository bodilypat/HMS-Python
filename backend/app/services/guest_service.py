# backend/app/services/guest_service.py

from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.GuestModel import Guest
from app.schemas.guest import GuestCreate, GuestUpdate


def create_guest(db: Session, guest_in: GuestCreate) -> Guest:
    """
    Create a new guest record.
    """
    new_guest = Guest(**guest_in.dict())
    db.add(new_guest)
    db.commit()
    db.refresh(new_guest)
    return new_guest


def get_guests(db: Session, skip: int = 0, limit: int = 20) -> List[Guest]:
    """
    Retrieve a list of guests with pagination.
    """
    return db.query(Guest).offset(skip).limit(limit).all()


def get_guest_by_id(db: Session, guest_id: int) -> Optional[Guest]:
    """
    Get a guest by ID.
    """
    return db.query(Guest).filter(Guest.guest_id == guest_id).first()


def update_guest(db: Session, guest_id: int, guest_in: GuestUpdate) -> Optional[Guest]:
    """
    Update guest information.
    """
    guest = db.query(Guest).filter(Guest.guest_id == guest_id).first()
    if not guest:
        return None
    
    update_data = guest_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(guest, field, value)
        
    db.commit()
    db.refresh(guest)
    return guest


def delete_guest(db: Session, guest_id: int) -> bool:
    """
    Delete a guest by ID.
    """
    guest = db.query(Guest).filter(Guest.guest_id == guest_id).first()
    if not guest:
        return False

    db.delete(guest)
    db.commit()
    return True
