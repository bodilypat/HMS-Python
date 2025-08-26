# backend/app/constants.py
from enum import Enu

# User Roles
class UserRole(str, Enum):
	ADMIN = "admin"
	STAFF = "staff"
	Guest = "guest"
	
# ROOM Statuses 
class RoomStatus(str, Enum):
	AVAILABLE = "available"
	OCCUPIED = "occupied"
	MAINTENANCE = "maintenance"
	RESERVED = "reserved"
	OUT_OF_SERVICE = "out_of_service"
	
# Reservation Statuses 
class ReservationStatus(str, Enum):
	PENDING = "pending"
	CONFIRMED = "confirmed"
	CHECKED_IN = "checked_in"
	CHECKED_OUT = "checked_out"
	CANCELLED = "cancelled"
	NO_SHOW = "no_show" 
	
# Payment Methods 
class PaymentMethod(str, Enum):
	CASE = "cash" 
	CREDIT_CARD = "credit_card"
	DEBIT_CARD = "debit_card"
	ONLINE = "online"
	BANK_TRANSFER = "bank_transfer" 
	
# Payment Statuses 
class PaymentStatus(Str, Enum):
	PENDING = "pending"
	COMPLETED = "completed"
	FAILED = "failed"
	REFUNDED = "refunded"
	
# Default Configs 
DEFULT_CURRENT = "USD"
DEFAULT_TIMEZONE = "UTC"
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

