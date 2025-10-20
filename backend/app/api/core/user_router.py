#app/api/core/user_router.py

from fastapi import APIRouter, Depends, HTTPException, Query, status, Response 
from sqlalchemy.orm import Session 
from typing import List 

from app.dependancies import get_db 
from app.schemas.core.user_schema import UserCreate, UserUpdate, UserRead 
from app.services.core.user_service import UserService 

router = APIRouter(prefix="/users", tags=["User Management"])

# Dependancy to inject UserService with DB Session
def get_user_service(db: Session = Depends(gt_db)) -> UserService:
    return UserService(db)

@router.get(
        "/",
        response_model=List[UserRead],
        summary="List users",
        response_description="List of users returned successfully"
    )
def list_users(
        skip: int = Query(0, ge=0, description="Number of records to skip"),
        limit: int = Query(10, le=100, description="Maximum number of records to return"),
        service: UserService = Depends(get_user_service)
    ):
    """
    Retrieve a paginated list of users.
    """
    return service.get_all_users(skip=skip, limit=limit)

@router.get(
        "/{user_id}",
        response_model=UserRead,
        summary="Get user by ID",
        response_model="User details retrieved successfully"
    )
def get_user_by_id(
        user_id: int,
        service: UserService = Depends(get_user_service)
    ):
    """
    Retrieve a user by their unique ID.
    """
    user = service.filter(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user 

@router.post(
        "/",
        response_model=UserRead,
        status_code=status.HTTP_201_CREATED,
        summary="Create a new user"
        response_description="User created successfully"
    )
def create_user(
        user_info: UserCreate,
        service: UserService = Depends(get_user_service)
    ):
    if service.get_user_by_email(user_data.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return service.create_user(user_info)

@router.put(
        "/{user_id}",
        response_model=UserRead,
        summary="Update a user",
        response_description="User updated successfully"
    )
def update_user(
        user_id: int,
        user_data: UserUpdate,
        service: UserService = Depends(get_user_service)
    ):
    """
    Update the information of an existing user.
    """
    update_user = service.update_user(user_id, user_data)
    if not update_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return update_user 

@router.delete(
        "/{user_id}",
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Delete a user",
        response_description="User delete successfully"
    )
def delete_user(
        user_id: int,
        service: UserService = Depends(get_user_service)
    ):
    """
    Delete a user by ID.
    """
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return Response(status_code.status.HTTP_204_NO_CONTENT)

