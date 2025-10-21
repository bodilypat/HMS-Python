#app/models/finance/payment.py

from sqlalchemy import Column, Integer, Float, String, ForeignKey, Datetime, func
from sqlalchemy.orm import relationship
from models.base_model import Base 

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=False)
    payment_method=  Column(String(50), nullable=False)
    amount_paid = Column(Numeric(10, 2), nullable=False)
    paid_at = Column(Datetime(timezone=True), server_default=func.now(), nullable=False)
    transaction_id = Column(String(100), nullable=True)

    __table_args__ = (
        CheckConstraint(
            "payment_method IN('cash','card','online','wallet')",
            name = 'payment_method_check'
        ),
    )
