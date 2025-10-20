#app/models/core/user_model.py

from sqlalchemy import Column, Integer, String, num, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declaration_base
import enum

Base = declaration_base()

class UserRole(enum.Enum):
    admin = "admin"
    staff = "staff"
    guest = "guest"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.guest)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}', role='{self.role.value}')>"