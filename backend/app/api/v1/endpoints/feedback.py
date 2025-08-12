# backend/app/api/v1/endpoints/feedback.py

from fastapi import APIRouter, HTTPException, Depends, status
from typing import List 

from backend.app.schemas.feedback import FeedbackCreate, FeedbackUpdate, FeedbackOut
from backend.app.services.feedback_service import FeedbackService
from backend.app.pi.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter(
        prefix="/feedback",
        tags=["Feedback"
    )
    
    @router.post("/", response_model=FeedbackOut, status_code=status.HTTP_201_CREATED)
    def create_feedback(feedback_in: FeedbackCreate, db: Session = Depends(get_db)):
        """
            Create new feedback.
        """
        feedback = FeedbackService.create_feedback(db, feedback_in)
        if not feedback:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create feedback."
            )
            return feedback
    @router.get("/{feedback_id}", response_model=FeedbackOut)
    def get_feedback_by_id(feedback_id: int, db: Session = Depends(get_db)):
        """
            Retrieve feedback by ID.
        """
        feedback = FeedbackService.get_feedback_by_id(db, feedback_id)
        if not feedback:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Feedback not found."
            )
            return feedback
    @router.get("/", response_model=List[FeedbackOut])
    def list_all_feedback(db: Session = Depends(get_db)):
        """
            List all feedback entries.
        """
        return FeedbackService.get_all_feedback(db)
        
    @router.patch("/{feedback_id}", response_model=FeedbackOut)
    def update_feedback(feedback_id: feedback_in: FeedbackUpdate, db: Session = Depends(get_db)):
        """
            Update feedback by ID.
        """
        updated= FeedbackService.update(db, feedback_id, feedback_in)
        if not updated:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detailp=f"Feedback with ID {feedback_id} not found or not updated."
            )
            return updated
            
    @router_delete("/{feedback_id}", status_code=status.HTTP_201_CONTENT)
    def delete_feedback(remark_id, db: Session = Depends(get_db)):
        """
            delete a feedbac entry
        """
        deleted = FeedbackService.delete_feedbackdb, feedback_id)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Feedback with ID {feedback_id} not found or could not be deleted."
                
           
           
   