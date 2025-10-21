#app/models/room/amenity.py

from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship
from app.db.base_class import Base 

class Amenity(Base):
    __tablename__ = "amenities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Many-to-Many with room 
    rooms = relationship(
        "Room",
        secondary="room_amenities",
        back_populates= "amenities"
    )

    def __repr__(self):
        return f"<Amenity(id={self.id}, name={self.name})>"