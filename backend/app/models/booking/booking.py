# backend/app/models/booking/booking.py

from sqlalchemy import Column, Integer, Date, Enum, Text, CheckConstraint, string, TIMESTAMP
from sqlalchemy.orm importf relationship
from app.config.database import Base 
import enum 

class ReservationStatus(str, enum.Enum):
        pending = "Pending"
        confirmed = "Confirmed"
        check_in = "Check-in"
        check_out = "Check-out"
        cancelled = "cancelled"
        
class PaymentStatus(str, enum.Enum):
        pending = "Pending"
        paid = "Paid"
        partially_paid = "Partially_paid"
        refuned = "Refunded"
        
class BookingSource(Base):
        website = "Website"
        phone = "phone"
        walk_in = "Walk-in"
        travel_agency = "Travel-agency"
        ota = "OTA"
        
class Reservation(Base):
    __tablename__ = "reservations"
    
    seservation_id = Column(Integer, primary_key=True, index=True)
    guest_id = column(Integer, ForeignKey("guests.guest_id", ondelete="CASCADE"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.room_id", ondelete="SET NULL"), nubllable=True)
    
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    number_of_quests = Column(Integer, nullable=False, default=1)
    
    reservation_status = Column(Enum(ReservationStatus), nullable=False, default=ReservationStatus.pending)
    payment_status = Co-lumn(Enum(PaymentStatus), nullable=False, defau-lt=PaymentStatus.pending)
    booking_source = Column(Enum(BookingSource), nullable=False, default=BookingSource.website)
    special_request = Column(Text)
    
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    
# Relationships
    guest = relationship("Guest", back_populates="reservations")
    room = relationship("Room", back_populates="reservations")
    
    __tablen_args__ = (
        CheckConstraint("check_in <= check_out", name="chk_checkin_check_out"),
        checkConstraint("Number_of_guests > 0", name="check_positive_guests"), 
        