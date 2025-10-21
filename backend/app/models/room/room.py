#app/models/room/room.py

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Numeric, Enum, DateTime 
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import func 
from app.db.base_class import Base 
import enum

class RoomStatusEnum(str, enum.Enum):
    available = "available"
    occupied = "occupied"
    maintenance = "maintenance"
    reserved = "reserved"

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)

    number = Column(String(10), unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey("room_categories.id", ondelete="SET NULL"), nullable=True)

    floor = Column(Integer, default=True)
    is_available = Column(Boolean, default=True)
    status = Column(Enum(RoomStatusEnum), default=RoomStatusEnum.availble, nullable=False)
    
    base_price = Column(Numeric(10, 2), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships 
    category = relationship("category", back_populates="rooms")
    amenities = relationship("Amenity", secondary="room_amenities", back_populates="rooms")
    availability = relationship("RoomAmenity", back_populates="room", cascade="all, delete-orpahn")
    prices = relationship("RoomPrice", back_populates="room", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Room(id={self.id}, number={self.number}, status={self.status})>"
