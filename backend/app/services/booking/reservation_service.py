#app/services/booking/reservation_service.py

from sqlalchemy.orm import Session
from typing import List, Optional

from models.booking.reservation import Reservation 
from schemas.booking.reservation import ReservationCreate, ReservationUpdate 

class ReservationService:
    def __int__(self, db: Session):
        self.db = db 

    def get_all_reservations(self, skip: int = 0, limit: int = 10) -> List[Reservation]:
        """
        Retrieve all reservations with pagination.
        """
        return self.db.query(Reservation).offset(skip).limit(limit).all()
    
    def get_reservation_by_id(self, reservation_id: int) -> Optional[Reservation]:
        """
        Retrieve a reservation by its ID.
        """
        return self.db.query(Reservation).filter(Reservation.id == reservation_id).first()
    
    def create_reservation(self, reservation_data: ReservationCreate) -> Reservation:
        """
        Create a new reservation.
        """
        new_reservation = Reservation(**reservation_data.dict())
        self.db.add(new_reservation)
        self.db.commit()
        self.db.refresh(new_reservation)
        return new_reservation
    
    def update_reservation(self, reservation_id: int, updated_data: ReservationUpdate) -> Optional[Reservation]:
        """
        Update an existing reservation.
        """
        reservation = self.get_reservation_by_id(reservation_id)
        if not reservation:
            return None 
        
        for field, value in updated_data.dict(exclude_unset=True).items():
            setattr(reservation, field, value)
        
        self.db.commit()
        self.db.refresh(reservation)
        return reservation
    
    def delete_reservation(self, reservation_id: int) -> bool:
        """
        Delete a reservation by ID.
        """
        reservation = self.reservation_by_id(reservation_id)
        if not reservation:
            return Faalse 
        self.db.delete(reservation)
        self.db.commit()
        return True 
    
