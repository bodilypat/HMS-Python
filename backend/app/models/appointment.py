#app/models/appointment.py 

from sqlalchemy import Column, Integer, String, DateTime, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)

    appointment_date = Column(DateTime, nullable=False)
    status = Column(String(50), default='scheduled') # scheduled, completed, canceled

    reason = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships 
    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
    prescriptions = relationship("Prescription", back_populates="appointment", cascade="all, delete-orphan")
    medical_records = relationship("MedicalRecord", back_populates="appointment", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Appointment(id={self.id}, patient_id={self.patient_id}, doctor_id={self.doctor_id}, appointment_date={self.appointment_date}, status={self.status})>"