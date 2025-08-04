# backend/app/config/__init__.py

"""
	App Configuration Initialization
	This package centralizes configuration settings,
	includeing environment variables, database setup,
	and other shared config utilities
"""
from .setting import settings
from .database import engine, SessionLocal, Base 

__all__= [
	"settings",
	"engine",
	"SessionLocal",
	"Base",
]
