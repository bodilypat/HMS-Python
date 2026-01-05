#app/models/doctor.py

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer, primary_key=True, index=True)
    # Link to users table (authentication)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    specialty = Column(String, nullable=False)
    license_number = Column(String, unique=True, nullable=False)

    phone_number = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    experince_years = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship with Patient model   
    patients = relationship("Patient", back_populates="doctor")
    user = relationship("User", back_populates="doctor_profile")
    appointments = relationship("Appointment", back_populates="doctor", )
    prescriptions = relationship("Prescription", back_populates="doctor")

    def __repr__(self):
        return f"<Doctor(id={self.id}, name={self.first_name} {self.last_name}, specialty={self.specialty})>"
    
