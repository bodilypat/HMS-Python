#app/schemas/services.py

from pydantic import BaseModel 
from typing import Optional

class ServiceCreate(BaseModel):
    name: str 
    description: Optional[str] = None 
    price: float 

class ServiceUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str] 
    price: Optional[float]

class ServiceResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float

    class Config:
        orm_mode = True 

# Room Services
class RoomServiceCreate(BaseModel):
    room_id: int 
    service_id: int 
    quantity: int = 1 
    status: str = "pending" 

class RoomServiceResponse(BaseModel):
    id: int 
    room_id: int 
    service_id: int 
    quantity: int
    status: str

    class Config:
        orm_mode = True 

        