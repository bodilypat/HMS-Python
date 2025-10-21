#app/models/amenities/hotel_amenity.py

from sqlalchemy import Column, Integer, String, Text, UniqueConstraint
from db.base_class import Base 

class HotelAmenity(Base):
    __tablename_ = "hotel_amenities"
    __table_args__ = (
        UniqueConstraint("name", name="uq_hotel_amenity_name"),
    )

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True, doc="Name of teh amenity")
    description = Column(Text, nullable=True, doc="Deleted description of the amenity")

    def __repr__(self):
        return f"<HotelAmenity(id={self.id}, name='{self.name})>"