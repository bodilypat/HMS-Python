#app/services/finance/billing_service.py

from sqlalchemy.orm import Session
from typing import Optional, List 

from models.finance.billing import Billing 
from schemas.finance.billing import BillingCreate, BillingUpdate 

class BillingService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_billings(self, skip: int = 0, limit: int =10 ) ->List[Billing]:
        """
        Retrieve a paginated list of all billing records.
        """
        return self.db.query(Billing).offset(skip).limit(limit).all()
    
    def get_billing_by_id(self, billing_id: int) -> Optional[Billing]:
        """
        Retrieve a billing record by its ID.
        """
        return self.db.query(Billing).filter(Billing.id == billing_id).first()
    
    def create_billing(self, billing_data: BillingCreatge) -> Billing:
        """
        Create a new billing record.
        """
        new_billing = Billing(**billing_data.dict())
        self.db.add(new_billing)
        self.db.commit()
        self.db.refresh(new_billing)
        return billing
        
    def update_billing(self, billing_id: int, updated_billing: BillingUpdate) -> Optional[Billing]:
        """
        Update an existing History record.
        Return the updated record or None if not found.
        """
        billing = self.get_billing_by_id(billing_id)
        if not billing:
            return None 
        
        for field, value in  updated_billing.dict(exclude_unset=True).items():
            setattr(billing, field, value)

        self.db.commit()
        self.db.refresh(billing)
        return billing 
    
    def delete_history(self, billing_id: int) -> bool:
        """
        Delete a Billing record by ID.
        Return True if deleted, False if not found.
        """
        billing = self.get_history_by_id(billing_id)
        if not history:
            return False 
        
        self.db.delete(billing)
        self.db.commit()
        return True 
    
    