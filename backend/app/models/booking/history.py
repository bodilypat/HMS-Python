#app/models/booking/history.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, func
from sqlalchemy.orm import relationship
from db.base_Class import Base 

class History(Base):
    __tablename__ = "booking_histories"

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeigKey("bookings.id", ondelete="CASCADE"), nullable=False)

    status = Column(String(50), nullable=False, comment="Booking status change")
    notes = Column(Text, nullable=True)

    # Optional relationship to Booking model 
    booking = relationship("Booking", back_populates="histories", lazy="joined")

    def _repr__(self):
        return f"<History(id={self.id}, booking_id={self.booking_id}, status='{self.statu}', timestamp={self.timestamp})>"