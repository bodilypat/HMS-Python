import bcrypt
import jwt
import datetime
from backend.app.models.user_model import UserModel
from backend.config import config  # For secret key, expiration

class AuthService:
    SECRET_KEY = config.SECRET_KEY
    JWT_ALGORITHM = "HS256"
    TOKEN_EXPIRE_MINUTES = 60

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))

    @staticmethod
    def generate_token(user_id, role):
        """
        Generate JWT token for authenticated user.
        """
        payload = {
            "user_id": user_id,
            "role": role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=AuthService.TOKEN_EXPIRE_MINUTES)
        }
        return jwt.encode(payload, AuthService.SECRET_KEY, algorithm=AuthService.JWT_ALGORITHM)

    @staticmethod
    def decode_token(token: str):
        try:
            decoded = jwt.decode(token, AuthService.SECRET_KEY, algorithms=[AuthService.JWT_ALGORITHM])
            return decoded
        except jwt.ExpiredSignatureError:
            return {"error": "Token expired"}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}

    @staticmethod
    def register_user(full_name, username, email, password, phone_number=None, role="Guest"):
        """
        Register a new user and store them in the DB.
        """
        password_hash = AuthService.hash_password(password)
        return UserModel.create_user(
            full_name=full_name,
            username=username,
            email=email,
            password_hash=password_hash,
            role=role,
            phone_number=phone_number
        )

    @staticmethod
    def login_user(email, password):
        """
        Authenticate user by email and password.
        """
        user = UserModel.get_user_by_email(email)
        if not user:
            return {"error": "User not found"}

        if not AuthService.verify_password(password, user["password_hash"]):
            return {"error": "Invalid password"}

        token = AuthService.generate_token(user_id=user["user_id"], role=user["role"])
        return {
            "token": token,
            "user": {
                "user_id": user["user_id"],
                "email": user["email"],
                "full_name": user["full_name"],
                "role": user["role"]
            }
        }
