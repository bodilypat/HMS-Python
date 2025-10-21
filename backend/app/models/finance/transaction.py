#app/models/finance/transaction.py

from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime 

from models.base_model import Base 

class Transaction(Base):
    __tableame__="transactions"

    id = Column(Integer, primary_key=True, index=True)

    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
    transaction_type = Column(String(50), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    method = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False)

    reference_id = Column(String(100), nullable=True)
    transaction_date = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationship
    invoice = relationship("Invoice", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, invoice_id={self.invoice_id}, amount={self.amount}, method='{self.method}')>"
