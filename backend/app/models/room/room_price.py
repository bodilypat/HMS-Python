#app/room/room_price.py

from sqlalchemy import Column, Integer, ForeignKey, Numeric, Date 
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class RoomPrice(Base):
    __tablename__ = "room_prices"

    id = Column(Integer, Primary_key=True, index=True)
    room_id = Column(Date, ForeignKey("room.id", ondelete="CASCADE"), nullable=False)

    season = Column(String(50), nullable=True)
    base_price = Column(Numeric(10, 2), nullable=False)
    discount = Column(Numeric(10, 2), nullable=True, default=0.0)
    tax = Column(Numeric(10, 2), nullable=True, default=0.0)
    final_price = Column(Numeric(10,2), nullable=False)

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    # Relationship
    room = eletionship("Room", back_populates="prices")

    def _repr__(self):
        return f"<RoomPrice(id={self.id}, room_id={self.room_id}, price={self.price})>"