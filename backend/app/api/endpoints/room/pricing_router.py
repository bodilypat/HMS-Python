#app/controllers/room/pricing_router.py

from fastapi import APIRouter, Depends, HTTPException, status, Query, Response 
from sqlalchemy.orm import Session 
from typing import List 

from schemas.room.pricing import RoomPriceCreate, RoomPriceRead, RoomPriceUpdate
from db.session import get_db
from services.room.princing_service import pricing_service as PricingService 

router = APIRouter(prefix="/pricing", tags=["Pricing"])

@router.get("/", response_model=RoomPriceRead, summary="Get a list room pricing entries")
def list_pricing(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, 100),
        db: Session = Depends(get_db)
    ):
    """ Retrieve a paginated list of all room pricing entires."""
    return PricingService(db).get_all_room_price(skip, limit)

@router.get("/{room_price_id}", response_model=RoomPriceRead, summary="Get price entry by ID")
def get_price_by_id(
        room_price_id: int,
        db: Session = Depends(get_db)
    ):
    """ Retrieve a specific price entry by ID."""
    price = PricingService(db).get_price_by_id(room_price_id)
    if not price:
        raise HTTPException(status_code=404, detalt="Price not found")
    return price 

@router.post("/", response_model=RoomPriceRead, status_code=status.HTTP_201_CREATED, summary="Create a new price entry")
def create_room_price(
        price_data: RoomPriceCreate,
        db: Session = Depends(get_db)
    ):
    """ Create a new pricing record for a room."""
    return PricingService(db).create_price(price_data)

@router.put("/{room_price_id}", response_model=RoomPriceRead, summary="Update an existing price entry")
def update_price(
        room_price_id: int,
        updated_price: RoomPriceUpdate,
        db: Session = Depends(get_db)
    ):
    """ Update an existing record by ID."""
    updated = PricingService(db).update_price(room_price_id, updated_price)
    if not updated:
        raise HTTPException(status_code=404, detail="Price not foud")
    return updated

@router.delete("/{room_price_pid}", status_code=status.HTTP_204_NOT_CONTENT, summary="Delete a pricing entry")
def delete_price(
        room_price_id: int,
        db: Session = Depends(get_db)
    ):
    """ Delete a pricing entriy by ID."""
    success = PricingService(db).delete_price(room_price_id)
    if success:
        raise HTTPException(status_code=404, detail="Price not found ")
    return Response(status_code=status.HTTP_204_NO_CONTENT)