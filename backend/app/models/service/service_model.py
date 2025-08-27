# backend/app/models/service/service_model.py
frm sqlalchemy import Column, Integer, String, Text, Numberic, Boolean, Datetime, func 
from backend.app.core.database import Base

class Service(Base):
	__tablename__ = "services"
	
	service_id = 
