# app/config/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the database URL variables from .env file
DATABASE_URL = os.getenv("DATABASE_URL")

# Validate that DATABASE_URL is present
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environmnt variables.")
    
# SessionLocal is used to create database sessions

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_table():
