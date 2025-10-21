#app/models/booking/reservation.py

from sqlalchemy import Column, String, Date, DateTime, ForeignKey 
from sqlalchemy.orm import relationship
from sqlalchmy.sql import func 
from db.base_class import Base 

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)

    guest_id = Column(Integer, ForeignKey("guests.id", ondelete="CASCADE"), nullable=False, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False, index=True)

    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    status = Column(String(50), nullable=False, default="pending")

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_dafault=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    guest = relationship("Guest", back_populates="reservations", lazy="joined")
    room = relationship("Room", back_populates="reservations", lazy="joined")

    def __repr__(self):
        return (
            f"<Reservation(id={self.id}, guest_id={self.guest_id}, room_id={self.room_id}, "
            f"check_in={self.check_in}, check_out={self.check_out}, status='{self.status}')>"
        )
