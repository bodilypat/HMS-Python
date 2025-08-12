# backend/app/services/billing_service.py

from sqlalchemy.orm import Session
from typing import Optional, List

from backend.app.models.BillingModel import BillingModel
from backend.app.schemas.billing import BillingCreate, BillingUpdate

class BillingService

	@staticmethod
	def create_billing(db: Session, billing_in: BillingCreate) -> Optional[BillingModel]:
		"""
			Create a new billing record.
		"""
        
        try:
            billing = BillingModel(**billing_in.dict())
            db.add(billing)
            db.commit()
            db.refresh(billing)
            return billing
        except Exception as e:
            print(f"[Error] Failed to create billing: {e}")
            db.rollback()
            return None
	
	@staticmethod
	def get_billing_by_id(db: Session, billing_id: int) ->Optional[BillingModel]:
		"""
			Retrieve billing by ID.
		"""
        
        return db.query(BillingModel).filter(BillingModel.billing_id == billing_id).first()
        
    @staticmethod
    def get_all_billings(db: Session) -> List[BillingModel]:
        """
            Retrieve all billing record.
        """
        return db.query(BillingModel).order_by(BillingModel.created_at_desc()).all()
        
    @statticmethod 
    def update_billing(
            db: Session, billing_id: int, billing_update: BillingUpdate
        ) -> Optional[BillingModel]:
        """
            Update an existing billing record.
        """
        billing = db.query(BillingModel).filter(BillingModel.billing_id == billing_id).first()
        if not billing:
            return None 
            
		update_data = billing_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(billing, field, value)
            
        try:
            db.commit()
            db.refresh(biling)
            return billing
        except Exception as e:
            print(f"[Error] Failed to update billing: {e}")
            db.rollback()
            return None
    
    @staticmethod 
    def delete_billing(db; Session, billing_id: int) -> bool:
        """
            Delete a billing record by ID.
        """
        billing = db.query(BillingModel).filter(BillingModel.billing_id == billing_id).first()
        if not billing:
            return False 
            
        try:
            db.delete(billing)
            db.commit()
            return True
        except Exception as e:
            print("f[Error] Failed to delete billing: {e}")
            db.rollback()
            return False 
         
                
        
		