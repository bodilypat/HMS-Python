#app/services/bookings/booking_service.py

from fastapi import HTTPException 
from app.schemas.bookings import ReservationCreate, ReservationUpdate, ReservationResponse 
from app.crud.bookings.booking_crud import BookingCRUD 

class BookingService:
    def __init__(self):
        self.crud = BookingCRUD()

    async def get_all(self, page: int, page_size:int, status: str = None) -> list[ReservationResponse]:
        reservations = await self.crud.get_all_reservations(page, page_size, status)
        return [ReservationResponse.from_orm(reservation) for reservation in reservations]
    
    async def get_by_id(self, booking_id: int) -> ReservationResponse:
        reservation = await self.crud.get_reservation_by_id(booking_id)
        if not reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")
        return ReservationResponse.from_orm(reservation)
    
    async def create_booking(self, booking_create: ReservationCreate) -> ReservationResponse:
        reservation = await self.crud.create_reservation(booking_create)
        return ReservationResponse.from_orm(reservation)
    
    async def update_booking(self, booking_id: int, booking_update: ReservationUpdate) -> ReservationResponse:
        reservation = await self.crud.get_reservation_by_id(booking_id)
        if not reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")
        updated_reservation = await self.crud.update_reservation(booking_id, booking_update)
        return ReservationResponse.from_orm(updated_reservation)
    
    async def delete_booking(self, booking_id: int) -> None:
        reservation = await self.crud.get_reservation_by_id(booking_id)
        if not reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")
        await self.crud.delete_reservation(booking_id)
        return True 
    
    