# backend/app/models/room_type_model.py

from backend.core.database import Base, get_session
from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound 

class RoomType(Base):
	__tablename__= "room_types"
	
	room_type_id = Column(Integer, primary_key=True, index=True)
	type_name = Column(String(50), unique=True, nullable=False)
	description = Column(Text, nullable=True)
	base_price = Column(Float, nullable=False)
	default_capacity = Column(Integer, nullable=False, default=1)
	bed_count = Column(Integer, nullable=False, default=1)
	amenities = Column(Text, nullable=True)
	
	def as_dict(self):
        return {
            "room_type_id": self.room_type_id,
            "type_name": self.type_name,
            "description": self.base_price,            
            "default_capacity": self.default_capacity,
            "amenities": self.amenities
        }
class RoomTypeModel:
    
    @staticmethod
    def get_all():
        with get_session() as db:
            room_types = db.query(RoomType).all()
            return [r.as_dict() for r in room_types]
            
    @staticmethod
    def get_by_id(room_type_id: int):
        with get_session() as db:
            return db.query(RoomType).filter_by(room_type_id=room_type_id).first().as_dict()
            
    @staticmethod
    def get_by_type_name(type_name: str):
        with get_session() db:
            room_type = db.query(RoomType).filter_by(type_name=type_name).first()
            return room_type.as_dict() if room_type else None 
            
    @staticmethod
    def create(data: dict):
        with get_session() as db:
            room_type = roomType(**data)
            db.add(room_type)
            db.commit()
            db.refresh(room_type)
            return room_type.as_dict()
            
    @staticmethod
       def update(room_type_id: int,  update_data: dict):
          with get_session() as db:
              room_type = db.query(RoomType).filter_by(room_type_id=room_type_id).first()
              if not room_type:
                return None
               for key, value in update_data.items():
                   setattr(room_type, key, value)
               db.commit()
               db.referesh(room_type)
               return room_type.as_dict()
               
    @staticmethod
    def deleted(room_type_id: int):
        with get_session() as db:
            room_type = db.query(RoomType).filter_by(room_type_id=room_type_id).first()
            if not room_type:
                return False
            db.delete(room_type)
            db.commit() 
            return True 
            
                
        