#users/services/auth_service.py 

from django.core.exceptions import ObjectDoesNotExist
from app.users.models import User

class UserService:
    """Service layer for User model.
       Handles CRUD operations and business logic for users.
       """

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        """Retrieve a user by their ID.
           Raises ObjectDoesNotExist if user does not exist.
        """
        try:
            return User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(f"User with id {user_id} does not exist.")
        
    @staticmethod
    def get_user_by_email(email: str) -> User:
        """Retrieve a user by their email.
           Returns None if user does not exist.
        """     
        try:        
            return User.objects.get(email=email)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(f"User with email {email} does not exist.")
    
    @staticmethod
    def create_user(**user_data) -> User:
        """Create a new user.
           Accept email, first_name, last_name, password, and role.
           Password will be hashed automatically.
        """
        password = user_data.pop("password", None)
        user = User(**user_data)
        if password:
            user.set_password(password)
            
        user.save()
        return user
    
    @staticmethod
    def update_user(user_id: int, **update_data) -> User:
        """Update an existing user.
           Accepts fields to update as keyword arguments.
        """
        user = UserService.get_user_by_id(user_id)
        
        password = update_data.pop("password", None)
        for key, value in update_data.items():
            setattr(user, key, value)
        
        if password:
            user.set_password(password)
        
        user.save()
        return user
    
    @staticmethod
    def delete_user(user_id: int) -> None:
        """Delete a user by their ID."""
        user = UserService.get_user_by_id(user_id)
        user.delete()
    
    @staticmethod
    def list_users() -> list[User]:
        """Retrieve all users."""
        return list(User.objects.all())    
    
    @staticmethod
    def authenticate_user(email: str, password: str) -> User | None:
        """Authenticate a user by email and password.
           Returns the user if authentication is successful, else None.
        """
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except ObjectDoesNotExist:
            return None
        return None
    @staticmethod
    def is_admin(user_id: int) -> bool:
        """Check if a user has admin role."""
        user = UserService.get_user_by_id(user_id)
        return user.role == 'admin'
    
    @staticmethod
    def is_staff(user_id: int) -> bool:
        """Check if a user has staff role."""
        user = UserService.get_user_by_id(user_id)
        return user.role == 'staff'
    
    @staticmethod
    def set_user_role(user_id: int, role: str) -> User:
        """Set the role of a user."""
        user = UserService.get_user_by_id(user_id)
        user.role = role
        user.save()
        return user
    
    
