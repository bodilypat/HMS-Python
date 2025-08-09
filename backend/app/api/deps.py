# backend/app/api/deps.py

from fastapi import Depends, HTTPException
from backend.auth_headler import varify_token

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
        
    return user 
    