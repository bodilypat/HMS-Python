#app/api/v1/bookings/router.py

from fastapi import APIRouter

from .bookings import router as management_router 
from .representation import router as representation_router
from .payments import router as payments_router

router = APIRouter(
    prefix="/bookings",
    tags=["bookings"],
    responses={404: {"description": "Not found"}},
)

# Booking management routes
router.include_router(management_router, prefix="/manage", tags=["booking management"])

# Read-only / presentation routes 
router.include_router(representation_router, prefix="/view", tags=["booking representation"])

# Payment & financial routes
router.include_router(payments_router, prefix="/payments", tags=["booking payments"])

