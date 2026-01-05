#app/models/patient.py

from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.models.base import Base

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)

    # Optional link to user account (patient portal)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True, unique=True)
    
    # Patient Personal Information
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)

    # Contact Information
    phone_number = Column(String, nullable=True)
    email = Column(String, nullable=True, unique=True)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    zip_code = Column(String, nullable=True)
    country = Column(String, nullable=True)

    # Medical Information
    medical_conditions = Column(String, nullable=True)
    blood_group = Column(String, nullable=True)
    allergies_info = Column(String, nullable=True)
    emergency_contacts_info = Column(String, nullable=True)
    assigned_doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=True)

    # appointment information
    next_appointment = Column(DateTime, nullable=True)

    # insurance Information
    insurance_provider = Column(String, nullable=True)
    insurance_policy_number = Column(String, nullable=True)

    # System  flags 
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="patient", uselist=False, foreign_keys=[user_id])
    assigned_doctor = relationship("Doctor", back_populates="patients", foreign_keys=[assigned_doctor_id])
    appointments = relationship("Appointment", back_populates="patient", cascade="all, delete-orphan")

    medical_records = relationship("MedicalRecord", back_populates="patient", cascade="all, delete-orphan")
    prescriptions = relationship("Prescription", back_populates="patient", cascade="all, delete-orphan")
    bills = relationship("Bill", back_populates="patient", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Patient(id={self.id}, name={self.first_name} {self.last_name}, dob={self.date_of_birth})>"
    
    