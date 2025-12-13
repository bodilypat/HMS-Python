#app/services/auth/auth_service.py

from app.schemas.auth import UserRegister, UserLogin, UserResponse, TokenResponse 
from app.crud.auth.user_crud import UserCRUD 
from app.core.security import verify_password, hash_password 
from .token_service import TokenService 
from fastapi import HTTPException, status 

class AuthService:
    def __init__(self):
        self.user_crud = UserCRUD()
        self.token_service = TokenService()

#-------------------------------
# REGISTER
#-------------------------------
async def register(self, data: UserRegister) -> UserResponse:
    existing = await self.user_crud.get_by_email(data.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )
    
    hashed_password = hash_password(data.password)

    user = await self.user_crud.create(
        email=data.email,
        full_name=data.full_name,
        hashed_password=hashed_password
    )
    return UserResponse.from_orm(user)

#-------------------------------
# LOGIN
#-------------------------------
async def login(self, data: UserLogin) -> TokenResponse:
    user = await self.user_crud.get_by_email(data.email)
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    access_token, refresh_token = self.token_service.create_tokens(user.id)
    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer"
    )

#-------------------------------
# LOGOUT
#-------------------------------
async def logout(self, user_id: int) -> None:
   await self.token_service.invalidate_tokens(user_id)
   return {'message': 'Successfully logged out'}
