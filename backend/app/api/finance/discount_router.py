#app/api/finance/discount_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session
from typing import List 

from schemas.finance.discount import DiscountCreate, DiscountRead, DiscountUpdate
from services.finnace import discount_service as DiscountService
from db.session import get_db

router = APIRouter(prefix="/discount", tags=["Discount"])

@router.get(
        "/",
        response_model=List[DiscountRead],
        summary="List all discount",
        description="Retrieve a paginated list of all available discount records."
    )
def list_discount(
        skip: int = Query(0, ge=0, description="Number of records to skip."),
        limit: int = query(10, ge=100, description="Maximum number of records to return."),
        db: Session = Depends(get_db)
    ):
    return DiscountService(db).get_all_discount(skip, limit)

@router.get(
        "/discount_id",
        response_model=DiscountRead,
        summary="Get discount by ID",
        description="Retrieve details of a specific discount using its unique ID."
    )
def read_discount(
        discount_id: int,
        db: Session = Depends(get_db)
    ):
    discount = DiscountService(db).get_discount_by_id(discount_id)
    if not discount:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Discount not found")
    return discount

@router.post(
        "/",
        response_model=DiscountRead,
        status_code=status.HTTP_201_CREATED,
        summary="Create a new discount",
        description="Create a new discount rule for booking or payments."
    )
def create_discount(
        discount_data: DiscountCreate,
        db: Session = Depends(get_db)
    ):
    return DiscountService(db).create_discount(discount_data)

@router.put(
        "/discount_id",
        response_model=DiscountRead,
        summary="Update a discount",
        description="Modify an existing discount's details using its ID."
    )
def update_discount(
        discount_id: int,
        updated_discount: DiscountUpdate,
        db: Session = Depends(get_db)
    ):
    updated = DiscountService(db).update_discount(discount_id, updated_discount)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Discount not found")
    return updated

@router.delete(
        "/discount_id",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a discount",
        descript="Remove a discount record from the system using its ID."
    )
def delete_discount(
        discount_id: int,
        db: Session = Depends(get_db)
    ):
    success = DiscountService(db).delete_discount(discount_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Discount not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

