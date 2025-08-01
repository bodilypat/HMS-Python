from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine
from app.config.settings import get_settings

engine = create_engine(get_settings().DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

def int_db():
	from app.models.base_model import Base 
	Base.metadata.create_all(bind=engine)
	
	