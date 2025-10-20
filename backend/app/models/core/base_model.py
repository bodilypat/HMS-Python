# backend/app/models/core/base_model.py

from datetime import datetime
from sqlalchemy.orm import declared_attr, as_declarative 
from sqlalchemy import Column, DateTime 

@as_declarative()
class Base:
	id: int 
	__name__: str 
	# Automatically generate table names 
	@declared_attr
	def __tablename__(cls) -> str:
		return cls.__name__.lower()
		
	class TimestampMixin:
		created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
		updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utc.now)