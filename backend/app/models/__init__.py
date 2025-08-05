# backend/app/models/__init__.py

from app.models.core.user import User
from app.models.core.guest import Guest
from app.models.core.staff import Staff

from app.models.room.room import Room
from app.models.room.roomtype import RoomType

from app.models.booking.booking import Booking
from app.models.booking.reservation import Reservation

from app.models.finance.payment import Payment
from app.models.finance.billing import Billing

from app.models.service.service import Service 
from app.models.service.room_service import RoomService

from app.models.feedback.feedback import Feedback

# Optional: import the base class if defined separately
from app.models.core.base_model import Base

# Optional: List of all models fro bulk metadata operations
__all__ = [
        "User",
        "Guest",
        "Staff",
        "Room",
        "RoomType",
        "Booking",
        "Reservation",
        "Payment",
        "Billing",
        "Service",
        "Roomservice",
        "Feedback",
        "Base"
	]
	