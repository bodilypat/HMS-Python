#app/services/availability_service.py

from sqlaclchemy.orm import Session 
from typing import List, Optional

from models.room.availability import Availability 
from schemas.room.availability_schema import AvailabilityCreate, AvailabilityUpdate 

class AvailabilityService:
    def __init__(self, db: Session):
        self.db = db 

    def get_all_availabilities(self, spkip: int = 0, limit: int = 10) -> List[Availability]:
        """Get a paginated list of all room avaiability records."""
        return self.db.query(Availability).offset(skip).limit(limit).all()
    
    def get_availability_by_id(self, availability_id: int) -> Optional[Availability]:
        """Get a single availability record by ID."""
        return self.db.query(Availability).filter(Availability.id == availability_id).first()
    
    def create_availability(self, availability_data: AvailabilityCreate) -> Availability:
        """Create a new availability entry."""
        availability = Availability(**availability_data.dict())
        self.db.add(availability)
        self.db.commit()
        self.db.refresh(availability)
        return availability
    
    def update_availability(self, availability_id: int, availability_data: AvailabilityUpdate) -> Optional[Availability]:
        """Update an existing availability record by ID."""
        availability = self.get_availability_by_id(availability_id)
        if not availability:
            return None 
        for field, value in availability_data.dict(exclude_unset=True).items():
            setattr(availability, field, value)

        self.db.commit()
        self.db.refresh(availability)
        return availability
    
    def delete_availability(self, availability_id: int) -> bool:
        """Delete an availability record by ID."""
        availability = self.get_availability_by_id(availability_id)
        if not availability:
            return False 
        self.db.delete(availability)
        self.db.commit()
        return True 
    
    