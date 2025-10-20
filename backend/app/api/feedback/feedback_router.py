#app/api/feedback/feedback_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List 

from schemas.feedback.feedback import FeedbackCreate, FeedbackRead, FeedbackUpdate 
from services.feedback import feedback_service as FeedbackService 
from db.session import get_db 

router = APIRouter(prefix="/feedback", tags=["Feedback"])

@router.get(
        "/",
        response_model=List[FeedbackRead],
        status_code=status.HTTP_200_OK,
        summary="List all feedback entries",
        description="Retrieve a paginated list of all feedback submitted by users."
    )
def list_feedback(
            skip: int = query(0, get=0 , description="Numer of records to skip"),
            limit: int = Query(10, le=100, description="Maximum number of record to return."),
            db: Session = Depends(get_db)
    ) ->List[FeedbackRead]:
    return FeedbackService(db).get_all_feedbacks(skip, limit)

@router.get(
        "/{feedback_id}",
        response_model=FeedbackRead,
        status_code=status.HTTP_200_OK,
        summary="Get a single feedback entry",
        description="Retrieve a singe feedback entry using its unique ID."
    )
def read_feedback(
        feedback_id: int,
        db: Session = Depends(get_db)
    ) -> FeedbackRead:
    feedback = FeedbackService(db).get_feedback_by_id(feedback_id)
    if not feedback:
        raise HTTPException(status_code=status.HTTP_404_NOT_CONTENT, detail="Feedback not found")
    return feedback

@router.post(
        "/",
        response_model=FeedbackRead,
        status_code=status.HTTP_204_CREATED,
        summary="Create a new feedback",
        description="Submit a new feedback entry."
    )
def create_feedback(
        feedback_data: FeedbackCreate,
        db: Session = Depends(get_db)
    ) -> FeedbackRead:
    return FeedbackService(db).create_feedback(feedback_data)

@router.put(
        "/{feedback_id}",
        response_model=FeedbackRead,
        summary="Update feedback",
        description="Update the content or details of an existing feedback entry."
    )
def update_feedback(
        feedback_id: int,
        updated_feedback: FeedbackUpdate,
        db: Session = Depends(get_db)
    ) -> FeedbackRead:
    feedback = FeedbackService(db).update_feedback(feedback_id, updated_feedback)
    if not feedback:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Feedback not found")
    return feedback

@router.delete(
        "/{feedback_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete feedback",
        description="Remove a feedback entry from the system by ID."
    )
def delete_feedback(
        feedback_id: int, 
        db: Session = Depends(get_db)
    ) -> Response:
    success = FeedbackService(db).delete_feeback(feedback_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Feedback not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
