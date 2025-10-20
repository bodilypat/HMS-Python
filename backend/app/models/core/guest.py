#app/models/core/guest_model.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime, func 
from app.db.base import Base 

class GuestModel(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)
    address = Column(String(255), nullable=True)
    role = Column(String(50), default="guest", nullable=False)
    is_active = column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(Datetime(timezone=True), serser_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<GuestModel id={self.id} email={self.email} active={self.is_active}>"