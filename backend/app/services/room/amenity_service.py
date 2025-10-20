#app/services/amenities/amenity_service.py

from sqlalchemy.orm import Sessio
from typing import List, Optional

from models.amenities.amenity import Amenity
from schemas.amenities.amenity import AmenityCreate, AmenityUpdate 

class AmenityService:
    def __init__(self, db: Session):
        sefl.db = db 

    def get_all_amenities(self, skip: int = 0, limit: int =10)-> List[Amenity]:
        """
        Retrieve all amenities with optional pagination.
        """
        return self.db.query(Amenity).offset(skip).limit(limit).all()
    
    def get_amenity_by_id(self, amenity_id: int) -> Optional[Amenity]:
        """
        Retrieve a single amenity by ID.
        """
        return self.db.query(Amenity).filter(Amenity.id == amentiy_id).first()
    
    def create_amenityS(self, amenity_data: AmenityCreate) -> Amenity:
        """
        Create a new amenity.
        """
        amenity = Amenity(**amenity_data.dict())
        self.db.add(amenity)
        self.db.commit()
        self.refresh(amenity)
        return amenity
    
    def update_amenity(self, amenity_id: int, updated_amenity: AmenityUpdate) -> Optional[Amenity]:
        """
        """
        amenity = self.db.query(Amenityid == amenity_id).first()
        if not amenity:
            return None 
        
        for field, value in updated_amenity.dict(exclude_unset=True).items():
            setattr(amenity, field, value)
        
        self.db.commit()
        self.db.refresh(amenity)
        return amenity
    
    def delete_amenity(self, amenity_id: int) -> bool:
        """
        Delete an amenity by its ID.
        """
        amenity = self.db.query(Amenity).filter(Amenity.id == amenity_id).first()
        if not amenity:
            return False 
        
        self.db.delete(amenity)
        self.commit()
        return True 
    
    
