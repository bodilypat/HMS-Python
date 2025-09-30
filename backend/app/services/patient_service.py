#app/services/patient_service.py

from sqlalchemy.orm import Session
from app.schemas.patient import PatientCreate, PatientUpdate 
from app.models.patient import Patient 
from typing import List, Optional 

class PatientService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_patients(self, skip: int = 0, limit: int = 10) -> List[Patient]:
        return self.db.query(Patient).offset(skip).limit(limit).all()
    
    def get_patient_by_id(self, patient_id: int) -> Optional[Patient]:
        return self.db.query(Patient).filter(Patient.id == patient_id).first()
    
    def create_patient(self, patient_info: PatientCreate) -> Optional[Patient]:
        new_patient = Patient(**patient_info.dict())

        self.db.add(new_patient)
        self.db.commit()
        self.db.refresh(new_patient)
        return new_patient
    
    def update_patient(self, patient_id: int, updated_patient: PatientUpdate) -> Optional[Patient]:
        patient = self.db.query(Patient).filter(Patient.id == patient_id).first()

        if not patient:
            return None 
        
        for field, value in updated_patient.dict(exclude_unset=True).items():
            setattr(patient, field, value)

        self.db.commit()
        self.db.refresh(patient)
        return patient
    
    def delete_patient(self, patient_id: int) -> Optional[Patient]:
        patient = self.db.query(Patient).filter(Patient.id == patient_id).first()

        if not patient:
            return False 
        
        self.db.delete(patient)
        self.db.commit()
        return True 
    
