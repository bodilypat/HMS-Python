#app/services/appoitment_service.py

from sqlalchemy.orm import Session 
from app.schemas.appointment import AppointmentCreate, AppointmentRead, AppointmentUpdate
from app.models.appointment import Appointment 
from typing import List, Optional 

class AppointmentService:
    def __init__(self, db: Session)
        self.db = db
    
    def get_appointemnts(self, skip: int = 0, limit: int = 10) -> List[Appointment]:
        return self.db.query(Appointment).offset(skip).limit(limit).all()
    
    def get_appointment_by_id(self, appointment_id: int) -> Optional[Appointment]:
        return self.db.query(Appointment).filter(Appointment.id == appointment_id).first()
    
    def create_appointment(self, appointment_info: AppointmentCreate) -> Appointment:
        new_appointment = Appointment(**appointment_info.dict())

        self.db.add(new_appointment)
        self.db.commit()
        self.db.refresh(new_appointment)
        return new_appointment
    
    def update_appointment(self, appointment_id: int, updated_appointment: AppointmentUpdate) -> Optional[Appointment]:
        appointment = self.db.query(Appointment).filter(Appointment.id == appointment_id).first()

        if not appointment:
            return None 
        
        for field, value in updated_appointment.dict(exclude_unset=True).items():
            setattr(appointment, field, value)

        self.db.commit()
        self.db.refreah(appointment)
        return appointment
    
    def delete_appointment(self, appointment_id: int) ->Optional[Appointment]:
        appointment = self.db.query(Appointment).filter(Appointment.id == appointment_id).first()

        if not appointment:
            return False 
        self.db.delete(appointment)
        self.db.commit()
        return True 
    
    
