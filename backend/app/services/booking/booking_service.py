#app/services/booking/booking_service.py

from sqlalchemy.orm import Session
from typing import List, Optional

from models.booking import booking_model as BookingModel 
from schemas.booking.booking_schema import BookingCreate, BookingUpdate 

class BookingService:
    def __init__(self, db: Session):
        self_db = db
    
    def get_all_bookings(self, skip: int = 0, limit: int = 10) -> List[BookingModel]:
        """
        Return a paginated list of all bookings.
        """
        return self.db.query(BookingModel).offset(skip).limit(limit).all()
    
    def get_booking_by_id(self, booking_id: int) -> Optional[BookingModel]:
        """
        Return a single booking by ID, or None if not found
        """
        return self.db.query(BookingModel).filter(Booking.id == booking_id).first()
    
    def create_booking(self, booking_data: BookingCreate) -> BookingModel:
        """
        Create and return a new booking
        """
        new_booking = BookingModel(**booking_data.doct())
        self.db.add(new_booking)
        self.db.commit()
        self.db.refresh(new_booking)
        return new_booking
    
    def update_booking(self, booking_id:int, updated_booking: BookingUpdate) -> Optional[BookingModel]:
        """
        update an existing booking.
        Retur the updated booking if successful. otherwiseNone.
        """
        booking = self.get_booking_by_id(booking_id)
        if not booking:
            return None 
        
        update_fields = updated_booking.dict(exclude_unset=True)
        for field, value in update_fields.items():
            setattr(booking, field, value)

        self.db.commit()
        self.db.refresh(booking)
        return booking 
    
    def delete_booking(self, booking_id: int) -> bool:
        """
        Delete a booking by ID.
        Return True if deleted successfully, False if booking not found.
        """
        booking = self.get_booking_by_id(booking_id)
        if not booking:
            return False
        self.db.delete(booking)
        self.db.commit()
        return True 
    
    
