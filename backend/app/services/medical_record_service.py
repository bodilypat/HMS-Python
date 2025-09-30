#app/services/medical_record_service.py

from sqlalchemy.orm import Session 
from app.schemas.medical_record import MedicalRecordCreate, MedicalRecordUpdated 
from app.models.medical_record import  MedicalRecord
from typing import List, Optional

class MedicalRecordService:
    def __init__(self, db: Session):
        self.db = db 

    def get_medical_records(self, skip: int = 0, limit: int = 10) ->List[MedicalRecord]:
        return self.db.query(MedicalRecord).offset(skip).limit(limit).all()
    
    def get_medical_record_by_id(self, medical_record_id: int) -> Optional[MedicalRecord]:
        return self.db.query(MedicalRecord).filter(MedicalRecord.id == medical_record_id).first()
    
    def create_medical_record(self, medical_record_info: MedicalRecordCreate) -> Optional[MedicalRecord]:
        new_medical_record = MedicalRecord(**medical_record_info.dict())

        self.db.add(new_medical_record)
        self.db.commit()
        self.db.refresh(new_medical_record)
        return new_medical_record
    
    def update_medical_record(self, medical_record_id: int, updated_medical_record: MedicalRecordCreate) -> Optional[MedicalRecord]:
        medical_record = self.db.query(MedicalRecord).filter(MedicalRecord.id == medical_record_id).first()

        if not medical_record:
            return None
        
        for field, value in updated_medical_record.dict(exclude_unset=True).items():
            setattr(medical_record, field, value)

        self.db.commit()
        self.db.refresh(medical_record)
        return medical_record 
    
    def delete_medical_record(self, medical_record_id: int) -> Optional[MedicalRecord]:
        medical_record = self.db.query(MedicalRecord).filter(MedicalRecord.id == medical_record_id).first()

        if not medical_record:
            return False 
        
        self.db.delete(medical_record)
        self.db.commit()
        return True
    
    
