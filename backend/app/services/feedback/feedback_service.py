#app/services/feedback/feedback_service.py (Business layer)

from sqlalchemy.orm import Session 
from typing import List, Optional

from models.feedback.feedback import Feedback
from schemas.feedback.feedback import FeedbackCreate, FeedbackUpdate

class FeedbackService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_feedbacks(self, skip: int = 0, limit: int = 10) -> List[Feedback]:
        """
        Retrieve a list of feedback entries with pagination.
        """
        return (
            self.db.query(Feedback)
            .order_by(Feedback.created_at.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_feedback_by_id(self, feedback_id: int) -> Optional[Feedback]:
        """
        Retrieve a single feedback entry by ID.
        """
        return self.db.query(Feedback).filter(Feedback.id == feedback_id).first()
    
    def create_feedback(self, feedback_data: FeedbackCreate) -> Feedback:
        """
        Create a new feedback entry.
        """
        new_feedback = Feedback(**feedback_data.dict())
        self.db.add(new_feedback)
        self.db.commit()
        self.db.refresh(new_feedback)
        return new_feedback
    
    def update_feedback(self, feedback_update: FeedbackUpdate) -> Optional[Feedback]:
        """
        Update an existing feedback entry.
        """
        feedback = self.get_feedback_by_id(feedback_id)
        if not feedback:
            return None 
        
        for feild, value in feedbavk_update.dict(exclude_unset=True).items():
            setattr(feedback, feild, value)

        self.db.commit()
        self.db.refresh(feedback)
        return feedback
    
    def delete_feedback(self, feedback_id: int) -> bool:
        """
        Delete a feedback entry by ID.
        """
        feedback = self.get_feedback_by_id(feedback_id)
        if not feedback:
            return False 
        
        self.db.delete(feedback)
        self.db.commit()
        return True 
    