# backend/app/models/service/service_model.py
frm sqlalchemy import Column, Integer, String, Text, Numberic, Boolean, Datetime, func 
from backend.app.core.database import Base

class Service(Base):
	__tablename__ = "services"
	
	service_id = Column(Integer, priamry_key=True, index=True, autoincrement=True)
    service_type = Column(String(100), nullable=False)
    category = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)
    price = Column(Numberic(10, 2), nullable=False)
    is_active = Column(Boolean, default=True
    created_at = Column(Datetime, server_default=func.mow())
    updated_at = Column(Datetime, service_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return (
            f"<Service(id={self.service_id}, type='{self.service_type}', "
            f" price={self.price}, active={self.is_active})>"
        )
        