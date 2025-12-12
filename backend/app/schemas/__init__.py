#app/schemas/__init__.py

from app.schemas.core.user_schema import UserCreate, UserUpdate
from app.schemas.core.guest_schema import GuestCreate, GuestUpdate
from app.schemas.core.staff_schema import StaffCreate, StaffUpdate

from app.schemas.room.room_schema import RoomCreate, RoomUpdate,
from app.schemas.room.category_schema import CategoryCreate, CategoryUpdate,
from app.schemas.room.availability_schema import AvailabilityCreate, AvailabilityUpdate
from app.schemas.room.amenity_schema import AmenityCreate, AmenityUpdate
from app.schemas.room.room_price_schema import RoomPriceCreate, RoomPriceUpdate

from app.schemas.booking.booking_schema import BookingCreate, BookingUpdate
from app.schemas.booking.reservation_schema import ReservationCreate, ReservationUpdate
from app.schemas.booking.availability_check_schema import AvailabilityCheckCreate, AvailabilityCheckUpdate
from app.schemas.booking.history_schema import HistoryCreate, HistoryUpdate 

from app.schemas.finance.billing_schema import BillingCreate, BillingUpdate
from app.schemas.finance.payment_schema import PaymentCreate, PaymentUpdate 
from app.schemas.finance.invoice_schema import InvoiceCreate, InvoiceUpdate
from app.schemas.finance.transaction_schema import TransactionCreate, TransactionUpdate 
from app.schemas.finance.discount_schema import DiscountCreate, DiscountUpdate 

from app.schemas.amenities.hotel_amenity_schema import HotelAmenityCreate, HotelAmenityUpdate,
from app.schemas.amenities.room_amenity_schema import RoomAmenityCreate, RoomAmentityUpdate 

from app.schemas.feedback.feedback_schema import FeedbackCreate, FeedbackUpdate 

