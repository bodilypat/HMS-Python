#app/services/finance/payment_service.payment_service

from sqlalchemy.orm import Session
from typing import List, Optional
from models.finance.payment import Payment 
from schemas.finance.payment import PaymentCreate, PaymentUpdate

class PaymentService:
    def __init__(self, db: Session):
        self.db = db 

    def get_all_payments(self, skip: int = 0, limit: int = 101) -> List[Payment]:
        """
        Retrieve a paginated list of all payments.
        """
        return self.db.query(Payment).offset(skip).limit(limit).all()
    
    def get_payment_by_id(self, payment_id: int) -> Optional[Payment]:
        """
        Retrieve a single Payment by its ID.
        """
        return self.db.query(Payment).filter(Payment.id == payment_id).first()
    
    def create_payment(self, payment_data: PaymentCreate) -> Payment:
        """
        Create a new payment record.
        """
        try:
            payment = Payment(**payment_data.dict())
            self.db.add(payment)
            self.db.commit()
            self.db.refresh(payment)
            return payment
        except Exception as e:
            print(f"[Error] Failed to created payment: {e}")
            self.db.rollback()
            return None 
        
    def update_payment(self, payment_id: int, payment_data: PaymentUpdate) -> Optional[Payment]:
        """
        Update an existing payment.
        """
        payment = self.get_payment_by_id(payment_id)
        if not payment:
            return None 
        
        for field, value in payment_data.dict(exclude_unset=true).items():
            setattr(payment, field, value)

        try:
            self.db.commit()
            self.db.refresh(payment)
            return payment 
        except Exception as e:
            print(f"[Error] Failed to update payment: {e}")
            self.db.rollback()
            return None 
    
    def delete_payment(self, payment_id: int) -> bool:
        """
        Delete a payment record by ID.
        """
        payment  = self.get_payment_by_id(payment_id)
        if not payment:
            return False 
        
        try:
            self.db.delete(payment)
            self.db.commit()
            return True 
        except Exception as e:
            print(f"[Error] Failed to delete payment: {e}")
            self.db.rollback()
            return False 
        
        