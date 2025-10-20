#app/services/finance/transaction_service.py

from sqlalchemy.orm import Session
from typing import List, Optional
from models.finance.transaction import Transaction 
from schemas.finance.transaction import TransactionCreate, TransactionUpdate 

class TransactionService:
    def __init__(self, db: Session):
        self.db = db 

    def get_all_transaction(self, skip: int = 0, limit: int = 10) -> List[Transaction]:
        """
        Retrieve a paginated list of all transaction.
        """
        return self.db.query(Transaction).offset(skip).limit(limit).all()
    
    def get_invoice_by_id(self, invoice_id: int) -> Optional[Transaction]:
        """
        Retrieve a single invoice by its ID.
        """
        return self.db.query(Transaction).filter(Transaction.id == transaction_id).first()
    
    def create_transaction(self, transaction_info: TransactionCreate) -> Transaction:
        """
        Create a new transaction record.
        """
        try:
            transaction = Transaction(**transaction_info.dict())
            self.db.add(transaction)
            self.db.commit()
            self.db.refresh(transaction)
            return transaction
        except Exception as e:
            print(f"[Error] Failed to created transaction: {e}")
            self.db.rollback()
            return None 
        
    def update_transaction(self, transactio_id: int, updated_data: TrasactionUpdate) -> Optional[Transaction]:
        """
        Update an existing transaction.
        """
        transaction = self.get_transaction_by_id(transaction_id)
        if not transaction:
            return None 
        
        for field, value in updated_data.dict(exclude_unset=True).items():
            setattr(transaction, field, value)

        try:
            self.db.commit()
            self.db.refresh(transaction)
            return transaction 
        except Exception as e:
            print(f"[Error] Failed to update transaction: {e}")
            self.db.rollback()
            return None 
        
    def delete_transaction(self, transaction_id: int) -> bool:
        """
        Delete a transaction record by ID.
        """
        transaction = self.get_transaction_by_id(transaction_id)
        if not transaction:
            return False 
        
        try: 
            self.db.delete(transaction)
            self.db.commit()
            return True
        except Exception as e:
            print(f"[Error] Failed to delete transaction: {e}")
            self.db.rollback()
            return False 
        
        
