from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine
from app.config.settings import get_settings

# Create the SQLAlchemy engine
engine = create_engine(get_settings().DATABASE_URL, echo=False)

# Create a configurated "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush= bind=engine)

def int_db():
    """
        Initializes the database by creating all tables defined in the models.
    """
	from app.models.base_model import Base 
	Base.metadata.create_all(bind=engine)
	
	