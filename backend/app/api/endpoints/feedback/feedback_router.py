#app/api/feedback/feedback_router.py 

from fastapi import APIRouter, Depends, HTTPException, Query, status, Response 
from sqlalchemy.orm import Session
from typing import List 

from schemas.feedback import FeedbackCreate, FeedbackUpdate, FeedbackRead 
from db.session import get_db 
from services.feedback import feedback_service 

router = APIRouter()

@router.get("/", response_model=List[FeedbackRead], summary="Get a list of Feedback")
def read_feedbacks(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db : Session = Depends(get_db)
    ):
    return feedback_service.get_all_feedbacks(db, skip, limit)

@router.get("/{feedback_id}", response_model=FeedbackRead, summary="Get a single Feedback by ID")
def read_feedback(
        feedback_id: int,
        db: Session = Depends(get_db)
    ):
    feedback = feedback_service.get_feeback_by_id(db, feedback_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback

@router.post("/", response_model=FeedbackRead , status_code=status.HTTP_201_CREATED, summary="Create a new Feedback")
def create_feedback(
        feedback: FeedbackCreate,
        db: Session = Depends(get_db)
    ):
    return feedback_service.create_feedback(db, feedback)

@router.put("/{feedback_id}", response_model=FeedbackRead, summary="Update an existing Feedback")
def update_feedback(
        feedback_id: int,
        updated_feedback: FeedbackUpdate,
        db: Session = Depends(get_db)
    ):
    updated = feedback_service.update_feedback(db, feedback_id, updated_feedback)
    if not updated:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return updated 

@router.delete("/{feedback_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Feedback")
def delete_feedback(
        feedback_id: int,
        db: Session = Depends(get_db)
    ):
    success = feedback_service.delete_feedback(db, feedback_id)
    if not success:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return Response(status_code=status.HTTP_NO_CONTENT)
