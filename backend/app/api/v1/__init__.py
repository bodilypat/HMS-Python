# backend/app/controllers/__init__.py

from fastapi import APIRouter

# Import routers from each domain
from app.controllers.core.user import router as user_router
from app.controllers.core.guest import router as guest_router 
from app.controllers.core.staff import router as staff_router

from app.controllers.room.room import router as room_router
from app.controllers.room.category import router as category_router
from app.controllers.room.availability import router as room_availability_router 

from app.controllers.booking.booking import router as booking_router
from app.controllers.booking.reservation import router as reservation_router 

from app.controllers.fanance.billing import router as billing_router 
from app.controllers.finance.payment import router as payment_router

from app.controllers.service.hotel import router as hotel_router
from app.controllers.service.room_service import router as room_service_router

from app.controllers.feedback.feedback import router as feedback_router

# Initialize top-level router 
api_router = APIRouter()

# Core 
api.router.include_router(user_router, prefix="core/users", tags=["Users"])
api.router.include_router(guest_router, prefix="core/guests", tags=["Guests"])
api.router.include_router(staff_router, prefix="/core/staff", tags=["staff"])

# Room Management 
api_router.include_router(room_router, prefix="/rooms", tags=["Rooms"])
api_router.include_router(category_router, prefix="/rooms/categories", tags=["Room categories"])
api_router.include_router(room_availability_router, prefix="/rooms/availability", tags=["Room Availability")

#booking 
api_router.include_router(booking_router, prefix="/bookings", tags=["bookings"])
api_router.include_router(reservation_router,prefix="/reservations", tags=["Reservation0s"])

# finanace
api_router.include_router(billing_router, prefix="/finance/billing", tags=["Billing"])
api.router.include_router(payment_router, prefix="finance/payments", tags=["Payments"])

# Services 
api_router.include_router(hotel_router, prefix="/services/hotel", tags=["Hotel Services"])
api_router.include_router(room_service_router, prefix="/services/room", tags=["Room Service"])

# Feedback
api_router.include_router(feedback_router, prefix="/feedback", tags=["Feedback"])