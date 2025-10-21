#app/models/amenities/room_amenity.py

from sqlalchemy import Table, Column, Integer, ForeignKey
from models.base_model import Base
from sqlalchemy.orm import relationship

room_amenity_association = Table (
    "room_amenities",
    Base.metadata,
    Column("room_id", Integer, ForeignKey("room_id"), primary_key=True)
    Column("amenity_id", Integer, ForeignKey("amenities.id"), primary_key=True),
)

