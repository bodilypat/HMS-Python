#app/services/prescription_service.py

from sqlalchemy.orm import Session
from app.schemas.prescription import PrescriptionCreate, PrescriptionUpdate 
from app.models import prescript as Prescription 
from typing import List, Optional

class PrescriptionService: 
    def __init__(self, db: Session):
        self.db = db

    def get_all_prescription(self, skip: int = 0, limit: int = 10) -> List[Optional]:
        return self.db.query(Prescription).offset(skip).limit(limit).all()
    
    def get_prescription_by_id(self, prescription_id: int) -> Optional[Prescription]:
        return self.db.query(Prescription).filter(Prescription.id == Prescriptin_id).first()
    
    def create_prescription(self, precription_info: PrescriptionCreate) -> Prescription:
        new_prescription = Prescription(**prescription_info.dict())

        self.db.add(new_prescription)
        self.db.commit()
        self.db.refresh(new_prescription)
        return new_prescription
    
    def update_prescription(self, prescription_id: int, updated_prescriptionUpdate ) -> Optional[Prescription]:
        prescription = self.db.query(Prescription).filter(Prescription.id == prescription_id).first()

        if not prescription:
            return None 
        
        for key, value in updated_prescription.dict(exclude_unset=True).items():
            setattr(prescription, key, value)

        self.db.commit()
        self.db.refresh(setattr)
        return prescription 

    def delete_prescription(self, prescription_id: int) -> Optional[Prescription]:
        prescription = self.db.query(Prescription).filter(Prescription.id == prescription_id).first()

        if not prescription:
            raise False 
        self.db.delete(prescription)
        self.db.commit()
        return True 
    
    