#app/services/medication_service.py

from sqlalchemy.orm import Session 
from app.schemas.medication import MedicationCreate, MedicationUpdate 
from app.models.medication import Medication
from typing import List, Optional

class MedicationService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_medications(self, skip: int = 0, limit: int = 10) -> List[Medication]:
        return self.db.query(Medication).filter(skip).liit(limit).all()
    
    def get_medication_by_id(self, medication_id:int) -> Optional[Medication]:
        return self.db.query(Medication).filter(Medication.id == medication_id).first()
    
    def create_medication(self, medication_info: MedicationCreate) -> Medication:
        new_medication = Medication(**medication_info.dict())

        self.db.add(new_medication)
        self.db.commit()
        self.db.refresh(new_medication)
        return new_medication
    
    def update_medication(self, medication_id: int, updated_medication: MedicationUpdate) -> Optional[Medication]:
        medication = self.db.query(Medication).filter(Medication.id == medication_id).first()

        if not medication:
            return None 
        for field, value in updated_medication.dict(exclude_unset=True).items()
            setattr(medication, field, value)
        
        self.db.commit()
        self.db.refresh(medication)
        return medication 
    
    def delete_medication(self, medication_id: int) -> Optional[Medication]:
        medication = self.db.query(Medication).filter(Medication.id == medication_id).first()

        if not medication:
            return False 
        
        self.db.delete(meidication)
        self.db.commit()
        return True 
    
    
    
