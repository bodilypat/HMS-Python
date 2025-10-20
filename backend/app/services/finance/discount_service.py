#app/services/finance/discount_service.py (Business logic layer )

from sqlalchemay.orm import Session
from typing import List, Optional
from models.finance.discount import Discount 
from schemas.finance.discount import DiscountCreate, DiscountUpdate 

class DiscountService:
    def __init__(self, db: Session):
        self.db = db

    def get_list_discount(self, skip: int = 0, limit: int = 10) -> List[Discount]:
        """
        Retrieve a paginated list of all Discounts.
        """
        return self.db.query(Discount).offset(skip).limit(limit).all()
    
    def get_discount_by_id(self, discount_id: int) -> Optional[Discount]:
        """
        Retrive a singe Discount by its ID.
        """
        return self.db.query(Discount).filter(Discount.id == discount_id).first()
    
    def create_discount(self, discount_data: DiscountCreate) -> Discount:
        """
        Create a new Discount record.
        """
        try:
            discount = Discount(**discount_data.dict())
            self.db.add(discount)
            self.db.commit()
            self.db.refresh(discount)
            return discount 
        except Exception as e:
            print(f"[Error] Failed to created discount: {e}")
            self.db.rollback()
            return None 
        
    def update_discount(self, discount_id: int, updated_discount: DiscountUpdate) -> Optional[Discount]:
        """
        Update an existing Discount.
        """
        discount = self.get_discount_by_id(discount_id)
        if not discount:
            return None 
        
        for field, value in updated_discount.dict(exclude_unset=True).items():
            setattr(discount, field, value)

        try:
            self.db.commit()
            self.db.refresh(discount)
            return discount
        except Exception as e:
            print(f"[Error] Failed to update payment: {e}")
            self.db.rollback()
            return None
        
    def delete_discount(self, discount_id: int) -> bool:
        """
        Delete a discount record by ID.
        """
        discount = self.get_discount_by_id(discount_id)
        if not discount:
            return false 
        try:
            self.db.delete(discount)
            self.db.commit()
            return True 
        except Exception as e:
            print(f"[Error] Failed to delete discount: {e}")
            self.db.rollback()
            return False 
        
        

