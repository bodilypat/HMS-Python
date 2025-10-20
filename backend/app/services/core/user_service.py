#app/services/core/user_service.py

from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.core.user_model import UserModel
from app.schemas.core.user_schema import UserCreate, UserUpdated
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db: Session):
        self.db = db 

    def _hash_password(self, password: str) -> str:
        """
        Securely hash the user's password using bcrypt.
        """
        return pwd_context.hash(password)
    
    def get_all_users(self, skip: int = 0, limit: int = 10) -> List[UserModel]:
        """
        Retrieve a paginated list of users.
        """
        return self.db.query(UserModel).offset(skip).limit(limit).all()
    
    def get_user_by_id(self, user_id: int) -> Optional[UserModel]:
        """
        Retrieve a user by their unique ID.
        """
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()
    
    def create_user(self, user_info: UserCreate) -> UserModel:
        """
        Create a new user with a hashed password.
        Raises ValueError if the email is already taken.
        """
        if self.get_user_by_email(user_info_email):
            raise ValueError("Email already exists")
        
        new_user = UserModel(
            full_name=user_info.full_name,
            email=user_info.email,
            hashed_password=self._hash_password(user_info.password),
            role=user_info or "user",
            is_active=user_info.is_active if hasattr(user_info, "is_active") else True
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[UserModel]:
        """
        Update an existing user's information.
        """
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        update_data = user_data.dict(exclude_unset=True)

        # Handle password update securely
        if "password" in update_data:
            update_data["hashed_pasword"] = self._hash_password(update_data.pop("password"))

        for field, value in update_data.items():
            setattr(user, field, value)

        self.db.commit()
        self.db.refresh(user)
        return user
    
    def delete_user(self, user_id: int) -> bool:
        """
        Delete a user by ID. Return True if deleted, False if not found.
        """
        user = self.get_user_by_id(user_id)
        if not user:
            return False 
        
        self.db.delete(user)
        self.db.commit()
        return True
    
    

