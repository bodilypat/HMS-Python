# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

from app.routes import api
from app.database import init_db

def create_app() -> FastAPI:
	# Initialize FastAPI app
	app = FastAPI(
		title ="Hotel Management System API",
		version="1.0.0",
        description="Backend API for managing hotel operations",
    }
    
    # Middleware setup 
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_method=["*"],
        allow_headers=["*"],
    )
    
    # Register API routes
    app.include_router(api.router)
    
    return app

app = create_app()

# Initialize the database (create tables)
init_db()

    