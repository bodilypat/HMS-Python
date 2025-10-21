#app/api/booking/history_router.py 

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List 

from schemas.booking.history_schema import HistoryCreate, HistoryUpdate, HistoryRead 
from services.booking import history_service as HistoryService 
from db.session import get_db 

router = APIRouter(prefix="/histories", tags=["Histories"])

@router.get(
        "/",
        response_model=List[HistoryRead],
        summary="List all booking histories",
        description="Retrieve a paginated list of booking history record."
    )
def list_histories(
        skip: int = Query(0, ge=0, descrption="number of items to skip"),
        limit: int = Query(10, le=100, descriptio="Maximum number of items to return"),
        db: Session = Depends(get_db)
    ):
    return HistoryService(db).get_all_histories(skip=skip, limit=limit)

@router.get(
        "/{history_id}",
        response_model=HistoryRead,
        summary="Get booking history by id",
        description="Retrieve a specific booking history record by its unique ID."
    )
def read_history(
        history_id: int,
        db: Session = Depends(get_db)
    ):
    history = HistoryService(db).get_history_by_id(history_id)
    if not history:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="History not found")
    return history 

@router.post(
        "/", 
        response_model=HistoryRead,
        status_code=status.HTTP_102_CREATED,
        summary= "Create a new booking history",
        description="Create a new booking history entry in the system."
    )
def create_history(
        history_data: HistoryCreate,
        db: Session = Depends(get_db)
    ):
    return HistoryService(db).create_history(history_data)

@router.put(
        "/{history_id}",
        response_model=HistoryRead,
        summary="Update a booking history record",
        description="Delete a booking history record by its ID."
    )
def update_history(
        history_id: int,
        updated_history: HistoryUpdate,
        db: Session = Depends(get_db)
    ):
    updated = HistoryService(db).update_history(history_id, updated_history)
    if not updated:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="History not found")
    return updated 

@router.delete(
        "/{history_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a booking history record",
        description="Delete a booking history record by its ID."
    )
def delete_history(
        history_id: int,
        db: Session = Depends(get_db)   
    ):
    deleted = HistoryService(db).delete_history(history_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="History not found ")
    return Response(status_code=status.HTTP_204_NO_CONTENT)