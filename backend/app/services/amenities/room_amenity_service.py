#app/services/amenities/room_amenity_service.py

from sqlalchemy.orm import Session 
from typing import List, Optional

from models.amenities import RoomAmenity
from schemas.amenities import RoomAmenityCreate, RoomAmenityUpdate 

class RoomAmenityService:
    def __init__(self, db: Session):
        self.db = db 

    def get_all_room_amenities(self, skip: int = 0, limit: int = 10) -> List[RoomAmenity]:
        """
        Return a paginated list of all room amenities.
        """
        return self.db.query(RoomAmenity).offset(skip).limit(limit).all()
    
    def get_room_amenity_by_id(self, amenity_id: int) -> Optional[RoomAmenity]:
        """
        Fetch a room amenity by its ID.
        """
        return self.db.query(RoomAmenity).filter(RoomAmenity.id == amenity_id).first()
    
    def create_room_amenity(seft, amenity_data: RoomAmenityCreate) -> RoomAmenity:
        """
        Create a new room amenity.
        """
        amenity = RoomAmenity(**amenity_data.dict())
        self.db.add(amenity)
        self.db.commit()
        self.db.refresh()
        return amenity 
    
    def update_room_amenity(self, amenity_id: int, updated_amenity: RoomAmenityUpdate) -> Optional[RoomAmenity]:
        """
        Update an existing room amenity by ID.
        """
        amenity = self.get_room_amenity_by_id(amenity_id)
        if not amenity:
            return None 
        
        for field, value in updated_amenity.dict(exclude_unset=True).items():
            setattr(amenity, field, value)

        self.db.commit()
        self.db.refresh(amenity)
        return amenity 
    
    def delete_room_amenity(self, amenity_id: int) -> bool:
        """
        Delete a room amenity by ID.
        """
        amenity = self.get_room_amenity_by_id(amenity_id)
        if not amenity:
            return False 
        
        self.db.delete(amenity)
        self.db.commit()
        return True 
    
    