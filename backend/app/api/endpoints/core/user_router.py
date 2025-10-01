#app/controllers/core/user_router.py

from fastapi import APIRouter, Depends, HTTPException, query, status, Response 
from sqlalchemy.orm import Session
from dependancies import get_db

from schemas.core.user import UserCreate, UserRead, UserUpdate
from services.core.user import UserService

router = APIRouter(prefix="/users", tags=["User Management"])

@router.get("/", response_model=List[UserRead], summary="Get a list of User")
def read_users(
        skip: int = query(0, ge=0),
        limit: int = query(10, le=100),
        db: Session = Depends(get_db)
    ):
    return UserService(db).get_all_users(skip, limit)

@router.get("/{user_id}", response_model=UserRead, summary="Get a single User by ID")
def read_user(
        user_id: int,
        db: Session = Depends(get_db)
    ):
    user = UserService(db).get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user 

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED, summary="Create a new User")
def create_user(
        user_in: UserCreate,
        db: Session = Depends(get_db)
    ):
    service = UserService(db)
    if service.get_user_by_email(user_in.email):
        raise HTTPException(status_code=404, detail="Email already registed")
    return service.create_user(user_in)

@router.put("/{user_id}", response_model=UserUpdate, summary="Update an existing User")
def update_user(
        user_id: int,
        updated_user: UserUpdate,
        db: Session = Depends(get_db)
    ):
    updated = UserService(db).update_user(user_id, updated_user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete User")
def delete_user(
        user_id: int,
        db: Session = Depends(get_db)
    ):
    user = UserService(db).delete_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return None 


