#app/models/booking/reservation.py

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from database import Base 

class Reservation(Base):
    __tablename__= "reservations"

    id = Column(Integer, primary_key=True, index=True)
    guest_id = Column(Integer, ForeignKey("guest_id"), nullable=False, index=True)
    room_id = Column(Integer, ForeignKey("room_id"), nullable=False, index=True)
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    status = Column(String(50), nullable=False, default="pending")

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    guest = relationship("Guest", back_populates="reservations")
    room = relationship("Room", back_populates="reservations")