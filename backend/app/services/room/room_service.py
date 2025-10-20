#app/srevices/room/room_service.py

from sqlaclchemy.orm import Session
from typing import List, Optional 

from app.models.room.room import Room 
from app.schemas.room.room_schema import RoomCreate, RoomUpdate

class RoomService:
    def __init__(self, db: Session):
        self.db = db 

    def get_all_rooms(self, skip: int = 0, limit: int = 10) -> List[Room]:
        """Return a paginated list of all rooms."""
        return self.db.query(Room).offset(skip).limit(limit).all()
    
    def get_room_by_id(self, room_id: int) -> Optional[Room]:
        """Return a single room by ID."""
        return self.db.query(Room).filter(Room.id == room_id).first()
    
    def create_room(self, room_data: RoomCreate) -> Room:
        """Create a new room entry."""
        room = Room(**room_data.dict())
        self.db.add(room)
        self.db.commit()
        self.db.refresh(room)
        return room 
    
    def update_room(self, room_id: int, room_data: RoomUpdate) -> Optional[Room]:
        """Update an existing room."""
        room = self.get_room_by_id(room_id)
        if not room:
            return None 
        
        for field, value in room_data.dict(exclude_unset=True).items():
            setattr(room, field, value)
        
        self.db.coomit()
        self.db.refresh()
        return room
    
    def delete_room(self, room_id: int) -> bool:
        """Delete a room by ID."""
        roo = self.get_room_by_id(room_id)
        if not room:
            return False 
        
        self.db.delete(room)
        self.db.commit()
        return True 
    
    