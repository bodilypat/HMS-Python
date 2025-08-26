# backend/app/models/base.py 

import datetime 
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class BaseModel:
	"""Base class for all SQLAlchemy models with default id and timestamps."""
	
	id = Column(Integer, primary_key=True, index=True)
	created_at = Column(DateTime, default=datetime.utcnow)
	updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
	
@declared_attr
	def__tablename__(cls) -> str: 
	return cls.__name__.lower()
	
	def __repr__(self) -> str:
	return f"{self.__class__.__name__}{id={self.id})>"