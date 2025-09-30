#app/services/billing_service.py

from sqlalchemy.orm import Session
from app.schemas.billing import BillingCreate, BillingUpdate 
from app.models.billing import Billing
from typing import List, Optional

class BillingService:

    def __init__(self, db: Session):
        self.db = db

    def get_all_billing(self, skip: int = 0, limit: int = 10) -> List[Billing]:
        return self.db.query(Billing).offset(skip).limit(limit).all()
    
    def get_billing_by_id(self, billing_id: int) -> Optional[Billing]:
        return self.db.query(Billing).filter(Billing.id == billing_id).first()
    
    def create_billing(self, billind_data: BillingCreate) -> Billing:
        new_billing = Billing(**billind_data.dict())

        self.db.add(new_billing)
        self.db.commit()
        self.db.refresh(new_billing)
        return new_billing
    
    def update_billing(self, billing_id: int, updated_billing: BillingUpdate) -> Optional[Billing]:
        billing = self.db.query(Billing).filter(Billing.id == billing_id).first()

        if not billing:
            return None 
        
        for field, value in updated_billing.dict(exclude_unset=True).items()
            setattr(billing,field, value)
        
        self.db.commit()
        self.db.refresh(billing)
        return billing 
    
    def delete_billing(self, billing_id: int) -> Optional(Billing):
        billing = self.db.query(Billing).filter(Billing.id == billing_id).first()

        if not billing:
            return False 
        
        self.db.delete(billig)
        self.db.commit()
        return True 
    
    