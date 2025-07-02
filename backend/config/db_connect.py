import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../config/.env"))

# Database configuration
DB_CONFIG = {
	"host": os.getenv("DB_HOST"),
	"port": int(os.getenv("DB_PORT", 3306)),
	"user": os.getenv("DB_USER"),
	"password": os.getenv("DB_NAME")
}

def get_connection():
	"""Establish and return a new MySQL database connection. """
	try:
		connection = mysql.connector.connect(**DB_CONFIG)
		if connection.is_connected():
			printf(" Successfully connected to the database.")
			return connection
		except Erroras err:
			print(f" Error connecting to the database: {err}")
			return None