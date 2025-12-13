#app/services/reservation_service.py

from fastapi import HTTPException 
from app.schemas.bookings import ReservationCreate, ReservationUpdate, ReservationResponse 
from app.crud.bookings.reservation_crud import ReservationCRUD 
from datetime import date 

class ReservationService:
    def __init__(self):
        self.crud = ReservationCRUD()

    async def get_all(self, page: int, page_size: int, guest_id: int = None) -> list[ReservationResponse]:
        reservations = await self.crud.get_all_reservations(page, page_size, guest_id)
        return [ReservationResponse.from_orm(reservation) for reservation in reservations]
    
    async def get_by_id(self, reservation_id: int) -> ReservationResponse:
        reservation = await self.crud.get_reservation_by_id(reservation_id)
        if not reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")
        return ReservationResponse.from_orm(reservation)
    
    async def create_reservation(self, reservation_create: ReservationCreate) -> ReservationResponse:
        reservation = await self.crud.create_reservation(reservation_create)
        return ReservationResponse.from_orm(reservation)
    
    async def update_reservation(self, reservation_id: int, reservation_update: ReservationUpdate) -> ReservationResponse:
        reservation = await self.crud.update_reservation(reservation_id, reservation_update)
        if not reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")
        return ReservationResponse.from_orm(reservation)

    async def delete_reservation(self, reservation_id: int) -> None:
        reservation = await self.crud.delete_reservation(reservation_id)
        if not reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")
        return None

    async def check_in(self, reservation_id: int) -> ReservationResponse:
        reservation = await self.crud.get_reservation_by_id(reservation_id)
        if not reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")
        reservation = await self.crud.check_in_reservation(reservation_id)
        return ReservationResponse.from_orm(reservation)
        
    async def check_out(self, reservation_id: int) -> ReservationResponse:
        reservation = await self.crud.get_reservation_by_id(reservation_id)
        if not reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")
        reservation = await self.crud.check_out_reservation(reservation_id)
        return ReservationResponse.from_orm(reservation)
