#app/models/booking/availability.py

from sqlalchemy import Column, Integer, Date, Boolean, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship

Base = declarative_base()

class Availability(Base):
    __tablename__="avaiabilities"
    
    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False)

    available_from = Column(Date, nullable=False)
    available_to = Column(Date, nullable=False)
    is_availale = Column(Boolean, default=True)

    room = relationship("Room", back_populates="availabilitities", lazy="joined")

    def __repr__(self):
        return f"<Availability(room_id={self.room_id}, from={self.available_from}, to={self.available_to}, available={self.is_availale})"