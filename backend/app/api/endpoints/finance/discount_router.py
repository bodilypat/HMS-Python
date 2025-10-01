#app/controller/finance/discount_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response
from sqlalchemy import Session
from typing import List 

from schemas.finance.discount import DiscountCreate, DiscountUpdate, DiscountRead 
from db.session import get_db 
from services.finance import discount_service

router = APIRouter(prefix="/discount", tags=["Discount"])

@router.get("/", response_model=List[DiscountRead], summary="Get a list of Discount")
def read_discount(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return discount_service.get_all_discount(db, skip, limit)

@router.get("{/discount_id}", response_model=DiscountRead, summary="Get a single Discount by ID")
def read_discount(
        discount_id: int,
        db: Session = Depends(get_db)
    ):
    discount = discount_service.get_discount_by_id(db, discount_id)
    if not discount:
        raise HTTPException(status_code=404, detail="Discount not found")
    return discount 

@router.post("/", response_model=DiscountRead, status_code=status.HTTP_201_CREATED, summary="Create a new Discount")
def create_discount(
        discount: DiscountCreate,
        db: Session = Depends(get_db)
    ):
    return discount_service.create_discount(db, discount)

@router.put("/{discount_id}", response_model=DiscountRead, detail="Update an existing Discount")
def update_discount(
        discount_id: int,
        updated_discount: DiscountUpdate,
        db: Session = Depends(get_db)
    ):
    updated = discount_service.update_discount(db, discount_id, updated_discount)
    if not updated:
        raise HTTPException(status_code=404, detail="Discount not found")
    return updated 

@router.delete("/discount_id", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Discount")
def delete_discount(
        discount_id: int,
        db: Session = Depends(get_db)
    ):
    success = discount_service.delete_discount(db, discount_id)
    if not success:
        raise HTTPException(status_code=404, detail="Discount not found")
    return Response(status_code=status.HTTP_NO_CONTENT)
