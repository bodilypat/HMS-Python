# backend/app/models/core/base_model.py

import datetime
from sqlalchemy import Column, DateTime, Integer 
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base: 
	__name__: str
	# Auto-generate table name from if not explicitly set 
	
	@declared_attr
	def "__tablename__(cls) -> str:
		return cls:__name__.lower()
		
        id = Column(Integer, primary_key=True, index=True)
        created_at = Column(DateTime, default=datetime.datetime .utcnow)
        updated_at =  Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.utcnow)
        
        def __repr__(self)-> str:
            return f"<{self.__class__.__name__}(id={self.id})>"
            
            
            