#app/models/prescription.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base

class Prescription(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False)

    medication = Column(String(100), nullable=False)
    instructions = Column(Text, nullable=False)
    dosage = Column(String(50), nullable=False)
    frequency = Column(String(50), nullable=False)
    duration = Column(String(50), nullable=False)
    notes = Column(Text, nullable=True)

    prescribed_date = Column(DateTime, default=datetime.utcnow)
    valid_until = Column(DateTime, nullable=True)
    status = Column(String(50), default="active")  #  active, completed, cancelled

    # Relationships
    patient_id = relationship("Patient", back_populates="prescriptions")
    doctor = relationship("Doctor", back_populates="prescriptions")
    appointment = relationship("Appointment", back_populates="prescriptions", uselist=False)
    
    def __repr__(self):
        return f"<Prescription(id={self.id}, appointment_id={self.appointment_id}, medication_name={self.medication_name})>"    
    
