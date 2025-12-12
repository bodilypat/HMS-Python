#app/schemas/rooms.py

from pydantic import BaseModel 
from typeing import Optional
from datetime import date 

# Room 
class RoomCreate(BaseModel):
    room_number: str
    room_type_id: int 
    floor: Optional[int]
    status: str = 'available'

class RoomResponse(BaseModel):
    id: int
    room_number: str
    room_type_id: Optional[int]
    floor: Optional[int]
    status: str

    class Config:
        orm_mode = True

# Room Type
class RoomTypeCreate(BaseModel):
    name: str
    description: Optional[str] = None
    capacity: int
    price: float

class RoomTypeUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    capacity: Optional[int] 
    price: Optional[float]

class RoomTypeResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    capacity: int
    price: float

    class Config:
        orm_mode = True

# Amenity

class AmenityCreate(BaseModel):
    name: str 
    description: Optional[str] = None
    active: bool = Ture 

class AmenityUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    active: Optional[bool]

class AmenityResponse(BaseModel):
    id: int 
    name: str 
    description: Optional[str]
    active: bool 

    class Config:
        orm_mode = True

# Room Availability 

class RoomAvailabilityResponse(BaseModel):
    room_id: int
    room_number: str
    room_type_id: int 
    floor: Optional[int]
    status: str 
    available_from: date
    available_to: date
    
    class Config:
        orm_mode = True

        