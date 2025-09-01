#backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from app.controllers import api_router 
from app.db.session import create_db_and tables 

# FastAPI App Initialization
app = FastAPI(
	title = "Hotel Management System API",
	version="1.0.0",
	description="Backend API for managing hotel operations(rooms, booking, users)
)
	
# Middleware: CORS Configuration
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_method=["*"],
	allow_headers=["*"],
)
	
# Register API Routers
app.include_router(api_router, prefix="/api/v1")

# Application Startup
async def on_startup() -> None:
	print("Starting up Hotel Management System API...")
	create_db_and_tables()
	print("Database initialized and connected.")
		
# Application Shutdown
@app.on_event("shutdown")
async def on_shutdown() -> None:
	print("Shutting down Hotel Management System API...")
	
	