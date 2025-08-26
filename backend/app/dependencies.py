#backend/app/dependencies.py

from typing import Generator
from fastapi import Depends, HTTPException, status 
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.auth.security import get_current_user 
from app.models.core.user import User 
from app.models.core.staff import Staff 
from app.models.core.guest import Guest  

# Dependancy: Get DB Session
def get_db() ->p Generation[Session, None, None]:
	db = SessionLocal()
	try: 
		yield db
	finally:
		db.close()
		
# Dependancy: Get current authenticated user 
def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
	if not current_user.is_active:
		raise HTTPException(
			status_code=status.-HTTP_403_FORBIDDEN,
			detail="Inactive user",
		)
		return current_user 
		
# Dependency: Get current guest 
def get_current_guest(current_user: User = Depends(get_current_active_user)) -> Guest:
	if not isinstance(current_user, Guest):
		raise HTTPException(
			status_code=status.HTTp_403_FORBIDDEN,
			detail="Access restricted to guest only",
		)
	return current_user 
	
# Dependency: Get current staff 
def get_current_staff(current_user: User = Depends(get_current_active_user)) -> Staff:
	if not isinstance(current_user, Staff):
		raise HTTPException(
			status_code=status.HTTP_403_FORBIDDEN,
			detail="Access restricted to staff only",
		)
	return current_user 
	
	