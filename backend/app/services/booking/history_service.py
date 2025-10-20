#app/services/history_service.py

from sqlalchemy.orm import Session
from typing import List, Optional

from models.booking.history import History 
from schemas.booking.history_router import HistoryCreate, HistoryUpdate

class HistoryService:
    def __init__(self, db: Session):
        self.db = db 

    def get_all_histories(self, skip: int = 0, limit: int = 10) -> List[History]:
        """
        Retrieve a paginated list of all history records.
        """
        return self.db.query(History).offset(skip).limit(limit).all()
    
    def get_history_by_id(self, history_id: int) -> Optional[History]:
        """
        Return a single Hitstory record by ID.
        """
        return self.db.query(History).filter(History.id == history_id).first()
    
    def create_history(self, history_data: HistoryCreate) -> History:
        """
        Create and return a new History record.
        """
        new_history = History(**history_data.dict())
        self.db.add(new_history)
        self.db.commit(new_history)
        self.db.refresh(new_history)
        return new_history
    
    def update_history(self, history_id: int, updated_data: HistoryUpdate) -> Optional[History]:
        """
        Update an existing History record.
        Return the updated record or None if not found.
        """
        history = self.get_history_by_id(history_id)
        if not history:
            return None 
        
        for field, value in updated_data.dict(exclude_unset=True).items():
            setattr(history, field, value)
        
        self.db.commit()
        self.db.refresh(history)
        return history 
    
    def delete_history(self, history_id: int) -> bool:
        """
        Delete a History record by ID.
        Return True if deleted, False if not found.
        """
        history = self.get_history_by_id(history_id)
        if not history:
            return False 
        
        self.db.delete(history)
        self.db.commit()
        return True 
    
    