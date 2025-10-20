#app/services/amenities/hotel_amenity_router.py

from sqlalchemy.orm import Session 
from typing import List, Optional

from models.amenities import HotelAmenity 
from schemas.amenities import HotelAmenityCreate, HotelAmenityUpdate

class HotelAmenityService:
    def __init__(self, db: Session):
        self.db = db 

    def get_all_hotel_amenities(self, skip: int = 0, limit: int = 10) -> List[HotelAmenity]:
        """
        Fetch a paginated list of hotel amenities.
        """
        return self.db.query(HotelAmenity).offset(skip).limit(limit).all()
    
    def get_hotel_amenity(self, amenity_id: int) -> Optional[HotelAmenity]:
        """
        Fetch a single hotel amenity by its ID.
        """
        return self.db.query(HotelAmenity).filter(HotelAmenity.id == amenity_id).first()
    
    def create_hotel_amenity(self, amenity_data: HotelAmenityCreate) -> HotelAmenity:
        """
        Create a new hotel amenity.
        """
        new_amenity = HotelAmenity(**amenity_data.dict())
        self.db.add(new_amenity)
        self.db.commit()
        self.refresh(new_amenity)
        return new_amenity
    
    def update_hotel_amenity(self, amenity_id: int, updated_amenity: HotelAmenityUpdate) -> Optional[HotelAmenity]:
        """
        Update an existing hotel amenity by ID.
        """
        amenity = self.get_hotel_amenity(amenity_id)
        if not amenity:
            return None 
        
        for field, value in updated_amenity.dict(exclude_unset=True).items():
            setattr(amenity, field, value)

        self.db.commit()
        self.db.refresh(amenity)
        return amenity 
    
    def delete_hotel_amenity(self, amenity_id: int) -> bool:
        """
        Delete a hotel amenity by ID.
        """
        amenity = self.get_hotel_amenity(amenity_id)
        if not amenity:
            return False 
        self.db.delete(amenity)
        self.db.commit()
        return True 
    
    

