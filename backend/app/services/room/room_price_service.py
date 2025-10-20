#app/room/room_price_service.py

from sqlalchemy.orm import Session
from typing import List, Optional

from models.room.room_price import RoomPrice 
from schemas.room.room_price import RoomPriceCreate, RoomPriceUpdate 

class RoomPriceService:
    def __init__(self, db: Session):
        self.db = db 

    def get_all_room_prices(self, skip: int = 0, limit: int = 10) -> List[RoomPrice]:
        """
        Return all room prices (paginated).
        """
        return self.db.query(RoomPrice).offset(skip).limit(limit).all()
    
    def get_price_by_id(self, price_id: int) -> Optional[RoomPrice]:
        """
        Return a single room price by ID.
        """
        return self.db.query(RoomPrice).filter(RoomPrice.id == price_id).first()
    
    def create_price(self, price_data: RoomPriceCreate) -> RoomPrice:
        """
        Create a new room price.
        """
        price = RoomPrice(**price_data.dict())
        self.db.add(price)
        self.db.commit()
        self.db.refresh(price)
        return price
    
    def update_price(self, price_id: int, price_data: RoomPriceUpdate) -> Optional[RoomPrice]:
        """
        Update an existing room price.
        """
        price = self.db.query(RoomPrice).filter(RoomPrice.id == price_id).first()
        if not price:
            return None 
        
        for key, value in price_data.dict(exclude_unset=True).items():
            setattr(price, key, value)

        self.db.commit()
        self.db.refresh(price)
        return price
    
    def delete_price(self, price_id: int) -> bool:
        """
        Delete a  room price.
        """
        price = self.db.query(RoomPrice).filter(RoomPrice.id == price_id).first()
        if not price:
            return False 
        
        self.db.delete(price)
        self.db.commit()
        return True 
    
    