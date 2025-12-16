#app/api/api_router.py

from fastapi import APIRouter

from app.api.v1.auth.router import router as auth_router
from app.api.v1.rooms.router import router as rooms_router
from app.api.v1.booking.router import router as booking_router
from app.api.v1.guests.router import router as quests_router
from app.api.v1.staff.router import router as staff_router 
from app.api.v1.services.router import router as services_router
from app.api.v1.billing.router import router as billing_router
from app.api.v1.reports.router import router as reports_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(rooms_router, prefix="/rooms", tags=["Rooms"])
api_router.include_router(booking_router, prefix="/booking", tags=["Booking"])
api_router.include_router(quests_router, prefix="/guests", tags=["Guests"])
api_router.include_router(staff_router, prefix="/staff", tags=["Staff"])
api_router.include_router(services_router, prefix="/services", tags=["Services"])
api_router.include_router(billing_router, prefix="/billing", tags=["Billing"])
api_router.include_router(reports_router, prefix="/reports", tags=["Reports"])
