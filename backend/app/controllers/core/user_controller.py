# backend/app/controllers/core/user_controller.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.core import security
from app.schemas import user as user_schemas
from app.services import user_service
from app.api.deps import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_moe=user_schemas.UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: user_schemas.UserCreate, db: Session = Depends(get_db)):
    """
        Register a new user.
    """
     existing_user = user_service.get_user_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(status code=400, detail="Email already registered")
        
        created_user = user.service.create_user(db, user_in)
        return created_user
    
@router.post("/login", response_model=user_schemas.Token)
def login(from_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
        Authenticate user and return access & refresh tokens.
    """
    user = user_service.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
            
        access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = security.create_access_token(
            data={"sub": str(user_id)}, expire_delta=access_token_expires
        )
        refresh_token = security.create_refresh_token(data={"sub": srt(user.id)})
        
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
        
@router.post("/refresh", response_model=user_schemas.Token)
def refresh_token(refresh_token: str):
    """
        Refresh the access token using a valid refresh token.
    """
    Payload = security.verify_refresh_token(refresh_token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
        
        user_id = payload["sub"]
        access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
        new_access_token = security.create_access_token (
            data={"sub": str(user_id)}, expire_delta=access_token_expires
        )
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
 