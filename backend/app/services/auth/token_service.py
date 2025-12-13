#pp/services/auth/token_service.py

from datetime import datetime, timedelta
from jose import jwt 
from fastapi import HTTPException, status 
from app.core.config import settings 
from app.crud.auth.token_crud import TokenCRUD 

class TokenService:
    def __init__(self):
        self.token_crud = TokenCRUD()

#-----------------------
# GENERATE TOKEN 
#-----------------------
def generate_tokens(self, user_id: int):
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

    access_token = jwt.encode(
        {"sub": str(user_id), "exp": datetime.utcnow() + access_token_expires, "type": "access"},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    
    refresh_token = jwt.encode(
        {"sub": str(user_id), "exp": datetime.utcnow() + refresh_token_expires, "type": "refresh"},
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


    return access_token, refresh_token

#-----------------------------------
# REFRESH TOKEN 
#-----------------------------------
def refresh_tokens(self, refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")
        user_id = int(payload.get("sub"))
        return self.generate_tokens(user_id)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token expired")
    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    
    access_token, refresh_token = self.generate_tokens(user_id)

    return access_token, refresh_token 

#----------------------------
# INVALID TOKEN 
#----------------------------
async def invalidate_token(self, user_id: int):
    await self.token_crud.invalidate_token(user_id)
    return True 

