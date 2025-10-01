#app/controllers/booking/history_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List 

from schemas.booking.history import HistoryCreate, HistoryUpdate, HistoryRead 
from db.session import get_db 
from services.booking import history_service as HistoryService 

router = APIRouter(prefix="histories", tags=["Histories"])

@router.get("/", response_model=List[HistoryRead], summary="Get a list of histories")
def read_histories(
        skip: int = Query(0, ge=0, description="Number of items to skip"),
        limit: int = Query(10, le=100, description="Maximum number of times to return"),
        db: Session = Depends(get_db)
    ):
    """Retrieve a paginated list of history record."""
    return HistoryService(db).get_all_histories(skip, limit)

@router.get("/{history_id}", response_model=HistoryRead, summary="Get a single history by ID")
def read_history(
        history_id: int,
        db: Session = Depends(get_db)
    ):
    """Retrievee a specific history record by ID."""
    history = HistoryService(db).get_history_by_id(history_id)
    if not history:
        raise HTTPException(status_code=404, detail="History not found")
    return history

@router.post("/", response_model=HistoryRead, status_code=status.HTTP_201_CREATED, summary="Create a new history")
def create_history(
        history_data: HistoryCreate,
        db: Session = Depends(get_db)
    ):
    """Create a new history record."""
    return HistoryService(db).create_history(history_data)

@router.put("/{history_id}", response_model=HistoryRead, summary="Update an existing history")
def update_history(
        history_id: int,
        updated_data: HistoryUpdate,
        db: Session = Depends(get_db)
    ):
    updated = HistoryService(db).update_history(history_id, updated_data)
    if not updated:
        raise HTTPException(status_code=404, detail="History not found")
    return updated 

@router.delete("/history_id", status_code=status.HTTP_NO_CONTENT, summary="Delete a history")
def delete_history(
        history_id: int,
        db: Session = Depends(get_db)
    ):
    """Delete a history record by ID."""
    deleted = HistoryService(db).delete_history(history_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="History not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
