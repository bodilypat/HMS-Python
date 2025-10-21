#app/models/finance/discount.py

from sqlalchemy import Column, Integer, String, Float 
from db.base import Base 

class Discount(Base):
    __table__ = "discounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    percentage = Column(Float, nullable=False)
    is_active = Column(Integer, default=1)