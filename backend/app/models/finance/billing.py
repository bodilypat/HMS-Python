#app/models/finance/billing.py

from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Session
from db.base_class import Base 

class BillingModel(Base):
    __tablename__= "billings"

    id = Column(Integer, primary_key=True, index=True)
    reservation_id = Column(Integer, ForeignKey("reservation.id"), nullable=False, index=True)
    service_charge = Column(Float, default=0.00, nullable=False)
    discount = Column(Float, default=0.00, nullable=False)
    total_amount = Column(Float, default=0.00, nullable=False)
    payment_status = Column(String(20), default="Unpaid", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    