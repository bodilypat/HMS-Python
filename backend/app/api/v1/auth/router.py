#app/api/v1/auth/router.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db 
from app.schemas.auth.user import UserCreate, UserLogin, UserResponse
from app.schemas.auth.token import TokenResponse
from app.services.auth.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post(
    "/register", 
    response_model=UserResponse, 
    status_code=status.HTTP_201_CREATED
    )
def register_user(
    user: UserCreate, 
    db: Session = Depends(get_db)
    ):
    """
    Register a new user.
    """
    auth_service = AuthService(db)
    existing_user = auth_service.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered."
        )
    new_user = auth_service.create_user(user)
    return new_user

@router.post(
    "/login",
    response_model=TokenResponse
    )
def login_user(
    user: UserLogin, 
    db: Session = Depends(get_db)
    ):
    """
    Authenticate a user and return a JWT token.
    """
    auth_service = AuthService(db)
    authenticated_user = auth_service.authenticate_user(user.email, user.password)
    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
        )
    token = auth_service.create_access_token(authenticated_user.id)
    return TokenResponse(access_token=token, token_type="bearer")

