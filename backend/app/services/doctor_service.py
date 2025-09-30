#app/services/doctor_service.py

from sqlalchemy.orm import Session
from app.schemas.doctor import DoctorCreate, DoctorUpdate, DoctorRead 
from app.models.doctor import Doctor 
from typing import List, Optional
from passlib.context import CryptContext

pwd_context = CryptContext(schemas=["bcrypt"], depredecated="auto")

class DoctorService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_doctors(self, skip: int = 0, limit: int = 10) -> Optional[Doctor]:
        return self.db.query(Doctor).offset(skip).limit(limit).all()
    
    def get_doctor_by_id(self, doctor_id: int) -> Optional[Doctor]:
        return self.db.query(Doctor).filter(Doctor.id == doctor_id).first()
    
    def get_doctor_by_email(self, doctor_email: str) ->Optional[Doctor]:
        return self.db.query(Doctor).filter(Doctor.id == doctor_email).first()
    
    def create_doctor(self, doctor_info: DoctorCreate) -> Doctor:
        hashed_password = pwd_context.hash(doctor_info.password)
        db_doctor = Doctor(
            email = doctor_info.email,
            hashed_password = doctor_info.password,
            full_name = doctor_info.full_name,
            is_active = doctor_info.is_active,
        )
        self.db.add(Doctor)
        self.db.commit()
        self.db.refresh(Doctor)
        return db_doctor
    
    def update_doctor(self, doctor_id: int, updated_doctor: DoctorUpdate) ->Optional[Doctor]:
        doctor = self.db.query(Doctor).filter(Doctor.id == doctor_id).first()
        if not doctor:
            return None
        
        for field, value in updated_doctor.dict(exclude_unset=True).items():
            setattr(guest, field, value)

        self.db.commit(doctor)
        self.db.refresh(doctor)
        return doctor
    
    def delete_doctor(self, doctor_id: int) -> Optional[Doctor]:
        doctor = self.db.query(Doctor).filter(Doctor.id == doctor_id).first()

        if not doctor:
            return False 
        
        self.db.delete(doctor)
        self.db.commit()
        return True
