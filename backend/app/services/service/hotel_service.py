#backend/app/services/service/hotel_service.py

from sqlalchem.orm import Session
from typing import List, Optional

from backend.app.models.service.service_model import ServiceModel
from backend.app.schemas.service.service_schema import ServiceCreate, ServiceUpdate 

class HotelService:

	@staticmethod
	def get_services(
			db: Session,
			skip: int = 0,
			limit: int = 0
		) -> List[ServiceModel]:
		return db.query(ServiceModel).offset(skip).limit(limit).all()
		
	@staticmethod
	def create_service(
			db: Session,
			service_in: ServiceCreate
		) -> Optional[ServiceModel]:
		try:
			service = ServiceModel(**service_in.dict())
			db.add(service)
			db.commit()
			db.refresh(service)
			return service
		except Exception as e:
			print(f"[Error] Failed to create service: {e}")
			db.rollback()
			return None 
	@staticmethod
	def get_services_by_id(db: Session, service_id: int) -> Optional[ServiceModel]:
        return db.query(ServiceModel).filter(ServiceModel.id == service_id).first()
        
    @staticmethod
    def update_service(db: Session, service_id: int, service_in: ServiceUpdate) -> Optional[ServiceModel]:
        service = db.query(ServiceModel).filter(ServiceModel.id == service_id).first()
        if not service:
            return None 
            
        for key, value in service_in.dict(exclude_unset=True).items():
            setattr(service, key, value)
            
        try:
            db.commit()
            db.refresh(service)
            return service 
        except Exception as e:
            print(f"[Error] Failed to update service: {e}")
            db.rolback()
            return False 
            
    @staticmethod 
    def delete_service(db: Session, service_id: int) -> bool:
        service = db.query(ServiceModel).filter(ServiceModel.id == service_id).first()
        if not service:
            return False 
        
        try:
            db.delete(service)
            db.commit()
            return True 
        except Exception as e:
            print(f"[Error] Failed to delete service: {e}")
            db.rollback()
            return False
