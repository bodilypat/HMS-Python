#app/services/booking/availability_service.py

from sqlalchemy.orm import Session
from typing import List, Optional

from models.booking.availability import Availability 
from schemas.booking.availability_schema import AvailabilityCreate, AvailabilityUpdate 

class AvailabilityService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_availabilities(self, skip: int = 0, limit: int = 10) ->List[Availability]:
        """
        Retrieve a paginated list of all room availabilities.
        """
        return (
                self.db.query(Availability)
                .offset(skip)
                .limit(limit)
                .all()
        )
    
    def get_availability_by_id(self, room_id: int) -> Optional[Availability]:
        """
        Get the availability record of a specific room by ID.
        """
        return (
            self.db.query(Availability)
            .filter(Availability.room_id == room_id)
            .first()
        )

    def create_availability(self, availability_data: AvailabilityCreate) -> Availability:
        """
        Create a new availability entry for a room.
        """
        new_availability = Availability(**availability_data.dict())
        self.db.add(new_availability)
        self.db.commit()
        self.db.refresh(new_availability)
        return new_availability
    
    def update_availability(self, room_id: int, updated_data: AvailabilityUpdate) -> Optional[Availability]:
        """
        Update an existing room's availability.
        """
        availability = self.get_all_availability_by_id(room_id)
        if not availability:
            return None 
        
        for field, value in updated_data.dict(exclude_unset=True).items():
            setattr(Availability, field, value)

        self.db.commit()
        self.db.refresh(availability)
        return availability
        
    def delete_availability(self, room_id: int) -> bool:
        """
        Delete a room's availability entry.
        """
        availability = self.get_availability_by_id(room_id)
        if not availability:
            return False 
        
        self.db.delete(availability)
        self.db.commit()
        return True 
    
    