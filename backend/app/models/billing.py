#app/models/billing.py

from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from .base import Base

class Billing(Base):
    __tablename__ = 'billings'

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    appointment_id = Column(Integer, ForeignKey('appointments.id'), nullable=False)
    prescription_id = Column(Integer, ForeignKey('prescriptions.id'), nullable=True)

    total_amount = Column(Float, nullable=False)
    paid_amount = Column(Float, nullable=False, default=0.0)
    due_amount = Column(Float, nullable=False)

    payment_status = Column(String(50), nullable=False)  # 'pending' 'paid', 'partially_paid', 'cancelled'
    payment_method = Column(String(50), nullable=True)  # 'credit_card', 'cash', 'insurance'
    insurance_provider = Column(String(100), nullable=True)
    insurance_claim_number = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)

    notes = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    patient = relationship("Patient", back_populates="billings")
    prescripton = relationship("Prescription", back_populates="billings")
    appointment = relationship("Appointment", back_populates="billing")

    def __repr__(self):
        return f"<Billing(id={self.id}, appointment_id={self.appointment_id}, amount={self.amount}, status={self.status})>"
    