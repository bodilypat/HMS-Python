# backend/app/api/v1/api_router.py

from fastapi import APIRouter 
from .endpoints import ( auth, user, guest, staff, room, reservation, payment, billing, feedback, service )
    router = APIRouter()
    
    router.include_router(auth.router, prefix="/auth", tags=["Auth"])
    router.include_router(user.router, prefix="/users", tags=["users"])
    router.include_router(guest.router, prefix="/guests", tags=["Guests"])
    router.include_router(staff.router, prefix="/staff", tags=["Staff"])
    router.include_router(room.router, prefix="/rooms", tags=["Rooms"])
    router.include_router(reservation.router, prefix="/reservation", tags=["Reservations"])
    router.include_router(payment.router, prefix="/payments", tags=["Payment"])
    router.include_router(billing.router, prefix="/billings", tags=["Billing"])
    router.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])
    router.include_router(service.router, prefix="/services", tags=["Services"])