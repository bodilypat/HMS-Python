#app/models/availability.py

from sqlalchemy import Column, Integer, Date, Boolean, ForeignKey, UniqueConstraint
from sqlAlchemy.orm import relationship 
from app.db.base_class import Base 

class RoomAvailablity(Base):
    __tablename__ = "room_availability"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False, index=True)

    date = Column(Date, nullable=False, index=True) # Specific date of availability 
    is_available = Column(Boolean, default=True, nullable=False) # True if room is available on this date 

    # Ensures one availability record per room per date 
    __tablename__ = (
            UniqueConstraint("room_id", "date", name="uix_room_date"),
    )

    # Optional: Relationship to Room model
    room = relationship("Room", back_populates="availabilities")

    def __repr__(self):
        return( f"<RoomAmenity(id={self.id}), room_id={self.room_id}, "
                f"date={self.date}, available={self.is_available})>"
            )