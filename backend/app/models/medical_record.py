#app/models/medical_record.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base

class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    appointment_id = Column(Integer, ForeignKey('appointments.id'), nullable=False)

    diagnosis = Column(String(255), nullable=False)
    symptoms = Column(Text, nullable=False)
    treatment = Column(Text, nullable=False)
    record_type = Column(
        String(100), 
        default= datetime.utcnow, 
        onupdate=datetime.utcnow
    )

    record_date = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    patient = relationship("Patient", back_populates="medical_records")
    doctor = relationship("Doctor", back_populates="medical_records")
    appointment = relationship("Appointment", back_populates="medical_records", uselist=False)
    
    def __repr__(self):
        return f"<MedicalRecord(id={self.id}, appointment_id={self.appointment_id}, record_date={self.record_date})>"
    