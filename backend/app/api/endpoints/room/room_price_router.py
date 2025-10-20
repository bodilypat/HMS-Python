#app/api/room/room_price_router.py

from fastapi import APIRouter, Depends, HTTPException, Query, status, Response 
from sqlachemy.orm import Session
from typing import List 

from schemas.room.room_price_schema import RoomPriceCreate, roommPriceUpdate, RoomPriceRead
from services.room import room_price_service as RoomPriceService
from db.session import get_db

router = APIRouter(prefix="/pricing", tags=["pricing"])
# Optionally: dependencies = [Depends(verify_token)]

@router.get(
        "/",
        response_model=List[RoomPriceRead],
        summary="List all room pricing entries",
        description="Retrieve a paginated list of all room pricing entries."
    )
def list_pricing(
        skip: int = Query(0, ge=0, description="Number of items to skip"),
        limit: int = Query(10, le=100, description="Max number of items to return"),
        db: Session = Depends(get_db)
    ):
    return RoomPriceService(db).get_all_room_prices(skip, limit)

@router.get(
        "/{room_price_id}",
        response_model=RoomPriceRead,
        summary="Get a price entry by ID",
        description="Retrieve a specific room pricing entry by its Id."
    )
def get_price_by_id(
        room_price_id: int,
        db: Session = Depends(get_db)
    ):
    price = RoomPriceService(db).get_price_by_id(room_price_id)
    if not price:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Price not found")
    return price 

@router.post(
        "/",
        response_model=status.HTTP_201_CREATED,
        summary="Create a new price entry",
        description="Create a new pricing record for a room."                    
    )
def create_room_price(
        price_data: RoomPriceCreate,
        db: Session = Depends(get_db)
    ):
    try:
        return RoomPriceService(db).create_price(price_data)
    except Exception as e:
        raise HTTPException(status=status.HTTP_500, detail=str(e))
    
@router.put(
        "/{room_price_id}",
        response_model=RoomPriceRead,
        summary="Update an existing price entry",
        description="Update the price inforamtion for a room"
    )
def update_price(
        room_price_id: int ,
        updated_price: RoomPriceUpdate,
        db: Session = Depends(get_db)
    ):
    updated = RoomPriceService(db).update_price(room_price_id, updated_price)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Price not foundd")
    return updated

@router.delete(
        "/{room_price_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a pricing entry"
        description="Delete a specific room price entry by ID."
    )
def delete_price(
        room_price_id: int,
        db: Session = Depends(get_db)
    ):
    success = RoomPriceService(db).delete_price(room_price_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Price not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

