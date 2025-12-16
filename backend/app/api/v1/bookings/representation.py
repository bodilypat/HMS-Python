#app/api/v1/rooms/representation.py 

from typing import List 

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.bookings.representation import RepresentationCreate, RepresentationRead, RepresentationUpdate
from app.services.bookings import representation_service as RepresentationService 

router = APIRouter(prefix="/representations", tags=["representations"])

#--------------------------------------
# Create Representation
#--------------------------------------
@router.post(
    "/", 
    response_model=RepresentationRead, 
    status_code=status.HTTP_201_CREATED
)
def create_representation(
    representation_in: RepresentationCreate, 
    db: Session = Depends(get_db)
) -> RepresentationRead:
    representation = RepresentationService.create_representation(db, representation_in)
    return representation

#--------------------------------------
# List Representations
#--------------------------------------
@router.get(
    "/", 
    response_model=List[RepresentationRead]
)
def list_representations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> List[RepresentationRead]:
    representations = RepresentationService.list_representations(db, skip=skip, limit=limit)
    return representations
#--------------------------------------
# Get Representation by ID
#--------------------------------------
@router.get(
    "/{representation_id}", 
    response_model=RepresentationRead
)
def get_representation(
    representation_id: int, 
    db: Session = Depends(get_db)
) -> RepresentationRead:
    representation = RepresentationService.get_representation(db, representation_id)
    if not representation:
        raise HTTPException(status_code=404, detail="Representation not found")
    return representation

#--------------------------------------
# Update Representation
#--------------------------------------
@router.put(
    "/{representation_id}", 
    response_model=RepresentationRead
)
def update_representation(
    representation_id: int, 
    representation_in: RepresentationUpdate, 
    db: Session = Depends(get_db)
) -> RepresentationRead:
    representation = RepresentationService.update_representation(db, representation_id, representation_in)
    if not representation:
        raise HTTPException(status_code=404, detail="Representation not found")
    return representation

#--------------------------------------
# Delete Representation
#--------------------------------------
@router.delete(
    "/{representation_id}", 
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_representation(
    representation_id: int, 
    db: Session = Depends(get_db)
) -> None:
    success = RepresentationService.delete_representation(db, representation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Representation not found")
    return None

