#app/models/booking/booking_model.py

from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from db.base_class import Base 

class Booking(Bass):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    guest_id = Column(Integer, ForeignKey("guests.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    number_of_quests = Column(Integer, nullbale=False)
    special_requests = Column(String, nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), ondelete=func.now())

    guest = relationship("Guest", back_populates="bookings")
    room = relationship("Room", back_populates="booking")

    