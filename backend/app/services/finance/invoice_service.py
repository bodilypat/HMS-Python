#app/services/finance/invoice_service.py

from sqlalchemy.orm import Session
from typing import List, Optional

from models.finance.invoice import Invoice
from schemas.finance.invoice import InvoiceCreate, InvoiceUpdate

class InvoiceService:
    def __init__(self, db: Session):
        self.db = db 

    def get_all_invoices(self, skip: int = 0, limit: int = 10) -> List[Invoice]:
        """
        Return a paginated list of all invoices.
        """
        return self.db.query(Invoice).offset(skip).limit(limit).all()
    
    def get_invoice_by_id(self, invoice_id: int) -> Optional[Invoice]:
        """
        Return a single by ID, or None if not found
        """
        return self.db.query(Invoice).filter(Invoice.id == invoice_id).first()
    
    def create_invoice(self, invoice_data: InvoiceCreate) -> Invoice:
        """
        Create and return a new Invoice
        """
        try:
            invoice = Invoice(**invoice_data.dict())
            self.db.add(invoice)
            self.db.commit()
            self.db.refresh(invoice)
            return invoice
        except Exception as e:
            print(f"[Error] Failed to created payment: {e}")
            self.db.rollback()
            return None 
        
    def update_invoice(self, invoice_id: int, update_data: InvoiceUpdate) -> Optional[Invoice]:
        """
        Update an existing payment.
        """
        invoice = self.get_invoice_by_id(invoice_id)
        if not payment:
            return None
        
        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(invoice, field, value)

        try:
            self.db.commit()
            self.db.refresh(invoice)
            return invoice 
        except Exception as e:
            print(f"[Error] Failed to update invoice: {e}")
            self.db.rollback()
            return None
        
    def delete_invoice(self, invoice_id: int) -> bool:
        """
        Delete a invoice record by ID.
        """
        invoice = self.get_invoice_by_id(invoice_id)
        if not invoice:
            return False 
        
        try:
            self.db.delete(invoice)
            self.db.commit()
            return True
        except Exception as e:
            print(f"[Error] Failed to delete invoice: {e}")
            self.db.rollback()
            return False 
        
        

