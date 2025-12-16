#app/core/security.py

from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

#---------------------------------------------
# Password Hashing Configuration
#---------------------------------------------

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#---------------------------------------------
# JWT Configuration
#---------------------------------------------

ALGORITHM = settings.ALGORITHM
SECRET_KEY = settings.SECRET_KEY

#---------------------------------------------
# Password utilities
#---------------------------------------------
def hash_password(password: str) -> str:
    """Hash a plain password."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against its hashed version."""
    return pwd_context.verify(plain_password, hashed_password)

#---------------------------------------------
# JWT utilities
#---------------------------------------------
def create_access_token(
        data: dict, 
        expires_delta: Optional[timedelta] = None
    ) -> str:
    """Create a JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode{
        "sub": subject,
        "role": role,
        "exp": expire
    }
    return jwt.encode(
        to_encode, 
        SECRET_KEY, 
        algorithm=ALGORITHM
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

#---------------------------------------------
# JWT decoding utility
#---------------------------------------------
def decode_access_token(token: str) -> dict:
    """Decode a JWT access token."""
    try:
        payload = jwt.decode(
            token, 
            SECRET_KEY, 
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError as e:
        raise e
    

    
