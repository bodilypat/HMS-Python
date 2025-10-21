#app/models/booking/booking.py

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, func
from sqlalchemy.orm import relatioship 
from db.base_class import Base 

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, priamry_key=True, index=True)
    guest_id = Column(Integer, ForeignKey("guests.id", ondelete="CASCADE"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False)

    check_id = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    number_of_quests = Column(Integer, nullable=True)
    special_requests = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationship
    guest = relatioship("Guest", back_populates="bookings", lay="joined")    
    room = relatioship("Room", back_populates="bookings", lazy="joined")
    histories = relatioship("Histories", back_populates="booking", cascade="all, delete-orphan")

    def __repr__(self):
        return (
                f"<Booking(id={self.id}, guest_id={self.guest_id}, room_id={self.room_id},"
                f"check_in={self.check_in}, check_out={self.check_out}, guests={self.number_of_guests})>"
        )