# backend/app/config/setting.py

from pydatic import BaseSettings, Field
from typing import optional

class Settings(BaseSettings):

# App Configuration
APP_NAME: str = "Hotel Management System"
APP_ENV: str = Field(default="development") # development | staging | production
APP_HOST: str = "0.0.0.0"
APP_PORT: int = 800
DEBUG: BOOL = True 

# Security
SECRET_KEY: str 
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
ALGORITHM: str = "HS256"

# Database 
DB_HOST: str = "localhost'
DB_PORT: int = 5432
DB_NAME: str 
DB_USER: str 
DB_PASSWORD: str

# Email (optional)
MAIL_USERNAME: Optional[str]
MAIL_PASSWORD: Optional[str]
MAIL_FROM: Optional[str]
MAIL_PORT: Optional[str]
MAIL_SERVER: Optional[str]
MAIL_TLS: Optional[bool] = True 
MAIL_SSL: Optional[bool] = False

# Uploads 
UPLOAD_DIR: str = "./uploads"
RECEIPT_UPLOAD_DIR: "./uploads/receipts"

# Testing 
TEST_DB_NAME: Optional[str]

class Config:
	env_file = ".env"
	env_file_encoding = 'utf-8"
	
	def assemble_db_url(self) -> str:
	if self.DATABASE_URL:
		return self.DATABASE_URL:
		return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self:DB_PORT}/ {self.DB_NAME}"

# SingLeton instance 
settings = Settings()

