#app/models/booking/history.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, func 
from sqlalchemy.orm import relationship
from db.base_class import Base 

class History(Base):
    __tablename__= "booking_histories"

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("booking.id"), nullable=False)
    status = Column(String(50), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    notes = Column(Text, nullable=True)