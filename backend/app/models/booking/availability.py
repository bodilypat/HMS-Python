#app/models/booking/availability.py

from sqlalchemy import Column, Integer, Date, Boolean, ForeignKey 
from sqlalchemy.orm import relationship
from db.base import Base 

class Availability(Base):
    __tablename__ = "availabilities"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False)

    available_from = Column(Date, nullable=False)
    available_to = Column(Date, nullable=False)
    is_available = Column(Boolean, default=True)

    room = relationship(
            "Room",
            book_populates="availabilities",
            lazy='joined'
    )

    def __repr__(self):
        return (
            f"<Availability(id={self.id}, room_id={self.room_id},"
            f"from={self.available_from}, to={self.available_to},"
            f"available={self.is_available})>"
            )
        