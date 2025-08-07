# backend/app/models/base_model.py

import datetime
from sqlalchemy import Column, Integer, DateTime,
from sqlalchemy.ext.declarative import as_declarative, as_declared_attr 

@as_declarative()
class BaseModel:
	id = Column(Integer, primary_key=True, index=True)
	created_at = Column(DateTime, default=datetime.utcnow()
	updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
	
@declared_attr
	def __tablename__(cls) -> str:
		return cls.__name__.lower()
		
	def __repr__(self) -> str:
	return f"<{self.__class__.__name__}(id={self.id})>"
	
	
	