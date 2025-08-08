# backend/app/api/v1/endpoints/user.py

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from typing import List 

from app.schemas import user as user_schemas 
from app.services import user_service
from app.api.deps import get_db 
from app.middleware.auth_required import get_current_active_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[user_schemas.UserOut])
def get_all_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
        Get a list of all users (paginated).
    """
    return user_service.get_users(db, skip=skip, limit=limit)
    
@router.get('/me", response_model=user_schemas.UserOut)
def get_current_user(current_user: user_schemas.UserOut = Depends(get_current_actice_user)):
    """
        Get the currently authenticated user's details.
    """
    return current_user
    
@router.get("/{user_id}", response_model=user_schemas.UserOut)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
        Get a user by ID.
    """
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user 
    
@router.put("/{user_id}", response=user_schemas.UserOut)
def update_user(user_id: int, user_in: user_schemas.UserUpdate, db: Session = Depends(get_db)):
    """
        Update an existing user.
    """
    updated_user = user_service.update_user(db, user_id, user_in)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found or update failed")
    return updated_user
    
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
        Delete a user by ID.
    """
    success = user_service.delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found or already deleted")
    return
    
    