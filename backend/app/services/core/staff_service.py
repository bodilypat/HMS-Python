#app/services/core/staff_service.py

from sqlalchemy.orm import Session
from app.models.core.staff_model import StaffModel 
from app.schemas.core.staff_schema import StaffCreate, StaffUpdate 
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class StaffService:
    def __init__(self, db: Session):
        self.db = db 

    def get_all_staff(self, skip: int = 0, limit: int =10):
        return self.db.query(StaffModel).offset(skip).limit(limit).all()
    
    def get_staff_by_id(self, staff_id: int):
        return self.db.query(StaffModel).filter(StaffModel.id == staff_id).first()
    
    def get_staff_by_email(self, email: str):
        return self.db.query(StaffModel).filter(StaffModel == email).first()
    
    def create_staff(self, staff_in: StaffCreate):
        hashed_password = pwd_context.hash(staff_in.password)
        db_staff = StaffModel(
            email=staff_in.email,
            hashed_password=hashed_password,
            full_name=staff_in.full_name,
            is_active=staff_in.is_active
        )
        self.db.add(db_staff)
        self.db.commit()
        self.db.refresh(db_staff)
        return db_staff 
    
    def update_staff(self, staff_id: int, updated_staff: StaffUpdate):
        staff = self.get_staff_by_id(staff_id)
        if not staff:
            return None 
        
        update_data = updated_staff.dict(exclude_unset=True)

        if "password" in update_data:
            update_data["hashed_password"] = pwd_context.hash(update_data.pop("password"))

        for key, value in update_data.items():
            setattr(staff, key, value)

        self.db.commit()
        self.db.refresh(staff)
        return staff
    
    def delete_staff(self, staff_id: int):
        staff = self.get_staff_by_id(staff_id)
        if not staff:
            return None 
        
        self.db.delete(staff)
        self.db.commit()
        return staff