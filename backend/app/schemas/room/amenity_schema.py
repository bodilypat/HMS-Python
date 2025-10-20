#app/schemas/room/amenity_schema.py

from pydantic import BaseModel, Field 
from typing import Optional

class AmenityBase(BaseModel):
    name: str = Field(..., max_length=100, description="Name of the amenity")
    description: Optional[str] = Field(None, description="Detailed description of the amenity")

class AmenityCreate(AmenityBase):
    """Schema for creating a new amenity."""
    pass 

class AmenityUpdate(BaseModel):
    """Schema for updating an existing amenity."""
    name: Optional[str] = Field(None, description="Updated name of the amenity")
    description: Optional[str] = Field(None, description="Updated description")

class AmenityRead(AmenityRead):
    """Schema for readig an amenity fro the database."""
    id: int 

    class Config:
        orm_mode = True
        