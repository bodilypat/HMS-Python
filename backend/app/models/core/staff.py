#app/models/staff_model.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime, func 
from app.db.base import Base 

class StaffModel(Base):
    __tablename__ = "staff"

    id: int = Column(Integer, primary_key=True, index=True)
    full_name: str = Column(String(100), nullable=False)
    email: str = Column(String(120), unique=True, nullable=False, index=True)
    hashed_password: str = Column(String(255), nullable=False)
    phone: str = Column(String(20), nullable=True)
    role: str = Column(String(50), nullable=False, default="staff")
    is_active: bool = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(Datetime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

def __repr__(self):
    return f"<StaffModel(id={self.id}, name='{self.full_name}', email='{self.email}', role='{self.role}')>"