#app/schemas/room/room_price.py

from pydantic import BaseModel, Field, condecimal
from typing import Optional
from datetime import date 

# Shared base class 
class RoomPriceBase(BaseModel):
    room_id: int = Field(..., description="ID of the room")
    season: Optiona[str] = Field(None, description="Season name or label")

    base_price: condecimal(max_digits=10, decimal_places=2) = Field(..., ge=0, description="Base price before discount/tax")
    discount: Optional[condecimal(max_digits=10, decimal_places=2)] = Field(default=0.0, ge=0, description="Discount applied")
    tax: Optional[condecimal(max_digits=10, decimal_places=2)] = Field(default=0.0, get=0, description="Tax amount")
    final_price: condecimal(max_digits=10, decimal_places=2) = Field(..., get=0, description="Final calculated price")

    start_date: date = Field(..., description="Start dte of price validity")
    end_date: date = Field(..., description="End date of price validaty")

    # For creating a room price
class RoomPriceCreate(RoomPriceBase):
    pass

# For updating an existing room price (partial updates)
class RoomPriceUpdate(BaseModel):
    season: Optional[str]
    base_price: Optional[condecimal(max_digits=10, decimal_places=2)]
    discount: Optional[condecimal(max_digits=10, decimal_places=2)]
    tax: Optional[condecimal(max_digits=10, decimal_places=2)]
    final_price: Optional[condecimal(max_digits=10, decimal_places=2)]
    start_date: Optional[date]
    end_date: Optional[date]

# For reading from the database
class RoomPriceRead(RoomPriceBase):
    id: int

    class Config:
        orm_mode = True 

        
