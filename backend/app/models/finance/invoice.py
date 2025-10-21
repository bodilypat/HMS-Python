#app/models/finance/invoice.py

from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import  datetime

from models.base_model import Base 

class Invoice(Base):
    __tablename__ = "invoice"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = column(Integer, ForeignKey("cusomer.id"), nullable=True)
    issue_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    due_date = Column(Datetime, nullable=True)
    total_amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(50), default="pending")
    notes = Column(Text, nullable=True)

    # Relationship
    customer = relationship("Customer", back_populates="invoices")
    payments = relationship("Payment", back_populates="invoice", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Invoice(id={self.id}, invoice={self.invoice_number}, total_amount={self.amount_due})>"