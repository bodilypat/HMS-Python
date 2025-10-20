#app/services/core/guest_service.py

from sqlalchemy.orm import Session
from typing import List, Optional 

from app.models.core.guest_model import GuestModel 
from app.schema.core.guest_schema import GuestCreate, GuestUpdate 
from passlib.context import CryptContext 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class GuestService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_guests(sef, skip: int = 0, limit: int = 10) -> List[GuestModel]:
        """
        Retrieve a paginated list of guests.
        """
        return self.db.query(GuestModel).offset(skip).limit(limit).all()
    
    def get_guest_by_id(self, guest_id: int) -> Optional[GuestModel]:
        """
        REtrieve a guest by their unique ID.
        """
        return self.db.query(GuestModel).filter(GuestModel.email == email).first()
    
    def create_guest(self, guest_info: GuestCreate) -> GuestModel:
        """
        Create a new guest with a hashed password.
        """
        hashed_password = self.hash_password(guest_info.password)

        new_guest = GuestModel(
            name=guest_info.name,
            email=guest_info.email,
            hashed_password=hashed_password,
            role=guest_info.role,
            is_active=guest_info.is_active
        )
        self.db.add(new_guest)
        self.db.commit()
        self.db.refresh(new_guest)
        return new_guest
    
    def update_guest(self, guest_id: int, guest_data: GuestUpdate) -> Optional[GuestModel]:
        """
        Update an existing guest's data.
        """
        guest = self.get_guest_by_id(guest_id)
        if not guest:
            return None 
        
        update_data = guest_data.dict(exclude_unset=True)
        # Handle password update securely
        if "password" in update_data:
            update_data["hashed_password"] = self.hash_password(update_data.pop("password"))

        for field, value in update_data.items():
            setattr(guest, field, value)

        self.db.commit()
        self.db.refresh(guest)
        return guest 
    
    def delete_guest(self, guest_id: int) -> bool:
        """
        Delete a guest by ID.
        """
        guest = self.get_guest_by_id(guest_id)
        if not guest:
            return False 
        
        self.db.delete(guest)
        self.db.commit()
        return True
    
    def hash_password(self, password: str) -> str:
        """
        Hash a plaintext password using bcrypt.
        """
        return pwd_context.hash(password)
