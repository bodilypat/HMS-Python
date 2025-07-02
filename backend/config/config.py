import os
from dotenv import load_dotenv

# Load environment variables from .env file 
dotenv_path = os.path.join(os.path.dirname(__fire__), "../config/.env")
load_dotenv(dotenv_path)

class Config:
	"""Global configuration setting."""
	
	# Database 
	DB_HOST = os.getenv("DB_HOST","localhost")
	DB_PORT = int(os.getenv("DB_PORT", 3306))
	DB_USER = os.getenv("DB_USER", "root")
	DB_PASSWORD = os.getenv("DB_PASSWORD", "")
	DB_NAME = os.getenv("DB_NAME", "sunrise_db")
	
# App
DEBUG = os.getenv("DEBUG", "False").lower() == "ture"
ENVIRONMENT = os.getenv("ENVIRONMENT", "development") # development / production
SECCRETE_KEY = os.getenv("SECRET_KEY", "pacha12812")

# Logging 
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")

# Other configs can be added here 
