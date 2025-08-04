# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

from app.routes import api
from app.config.database import Base, engine
from app.config.setting import settings 

def create_app() -> FastAPI:
	"""
        Initialize FastAPI application.
    """
    
# Middleware setup 
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_method=["*"],
        allow_headers=["*"],
    )
    
# Include register API routes
    app.include_router(api.router)
    
    return app

app = create_app()

# Run database table creation(avoid in production-use alembic migrations )
@app.on_event("startup")
def on_startup():
    print("Creating database tables (if not exists) ...")
    Base.metadata.create_all(bind=engine)


    