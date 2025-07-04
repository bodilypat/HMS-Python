# backend/routers/api_router.py

from fastapi import APIRouter
from app.controllers import guest_controller

# Import all controllers 
from app.controllers import(
	guest_controller,
	room_controller,
	room_type_controller,
	reservation_controller,
	payment_controller,
	billing_controller,
	service_controller,
	room_service_controller,
	staff_controller,
	housekeeping_controller
	feedback_controller,
	)
	
	# Main API router
	api_router = APIRouter()
	
	# Register all sub-routers here
	api_router.include_router(guest_controller.router, prefix="/guests", tags=["Guests"])
	api_router.include_router(room_controller.router, prefix="/rooms", tags["Rooms"])
	api_router.include_router(room_type_controller.router, prefix="/room-types", tags=["Room types"])
	api_router.include_router(reservation_controller.router, prefix="/reservations", tags=["Reservations"])
    api_router.include_router(payment_controller.router, prefix="/payments", tags=["payments"])
    api_router.include_router(billing_controller.router, prefix="/billings", tags=["billings"])
    api_router.include_router(service_controller.rouetr, prefix="/services", tags=["Services"])
    api_router.include_router(room_service_controller.router, prefix="/room-services", tags=["Room Services"])
    api_router.include_router(staff_controller.router, prefix="/staffs", tags=["staff"])
    api_router.include_router(housekeeping.router, prefix="/housekeeping", tags=["Housekeeping"])
    api_router.include_router(feedback_controller.router, prefix="/feedbacks", tags=["Feedback"])
