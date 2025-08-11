# backend/app/services/reservation_service.py

from datetime import date 
from typing import Optional , List, Dict 

from datetime import datetime
from backend.app.models.room.model import RoomModel
from backend.app.models.guest.model  import GuestModel
from backend.app.models.billing_model import BillingModel 
from backend.app.models.payment_model import PaymentModel 
from backend.app.models.reservation_model import ReservatioModel 

class ReservationService:

	@staticmethod:
	def create_reservation(data: int) -> Optional[dict]:
        """
            Create a reservation and handle linked logic like room availability,
            room status updates, and return the reservation data.
        """
        guest_id = data.get("guest_id")
        room_id = data.get("room_id")
        check_in = date.get("check_in")
        check_out = data.get("check_out")
        number_of_guests = data.get("number_of_guests", 1)
        reservation_status = data.get("reservation_status", "Pending")
        payment_status = data.get("payment_status", "Pending")
        booking_source = data.get("booking_sourece", "website")
        special_request = data.get("special_reques")
        
        if not all([guest_id, room_id, check_in, check_out):
            raise ValueError("Missing required reservation fields.")
            
        # Validate room availability
        if room_id and not ReservationService.check_availability(room_id, check_in, check_out):
            raise ValueError("Room is not available for the selected dates.")
            
        #Create reservation
        reservation_id = ReservationModel.create_reservation(
            guest_id = guest_id,
            room_id = room_id,
            check_in = check_in,
            check_out = check_out,
            number_of_quests = number+of_guests,
            reservation_status = servation_status, 
            payment_status = payment_status,
            booking_source = booking_source, 
            special_request = special_request 
        )
        
        if not reservation_id:
            return None 
            
        # Update room status if applicate 
        if reservation_status in ("Confirmed", "check-In")
            RoomModel.update_room_status(room_id,"Occupied")
            
        return ReservationModel.get_reservation_by_id(reservation_id)
        
    @staticmethod
    def get_reservation_by_id(reservation_id: int) -> optional[dict]:
        """
            Retrieve a reservation by its ID.
        """
        return ReservationModel.get_reservation_by_id(reservation_id)
        
    @staticmethod
    def get_all_reservation() -> List[dict]:
        """
            Retrieve all reservation in the system.
        """
        return ReservationModel.get_all_reservations()
        
    @staticmethod
    def update_reservation(reservation_id: int, update_date: dict) -> Optional[dict]:
        """
            Update reservation details.
        """
        success = ReservationModel.update_reservation_by_id(reservation_id, update_data)
        if success:
            return ReservationModel.get_reservation_by_id(reservation_id)
        return None 
        
    @staticmethod
    def cancel_reservation(reservation_id: int) -> bool:
        """
            Cancel a reservation and free the room if necessary.
        """
        reservation = ReservationMedel.get_reservation_by_id(reservation_id)
        if not reservation:
            return False 
        
        success = ReservatioModel.update_reservation_by_id(
            reservation_id,
            reservation_status="Cancelled"
        )
        
        if success and reservation.get("room_id"):
            RoomModel.update_room_status(reservation["room_id"], "Available")
            
            return success 
            
    @staticmethod
    def list_guest_reservation(guest_id: int) -> List[dict]:
        """
            List all reservations for specific guest.
        """
        return ReservationModel.get_reservation_by_guest(guest_id)
        
    @staticmethod
    def check_availability(room_id: int, check_in: date, check_out: date) -> bool:
        """
            Check if the room is available for the given date range.
        """
        overlapping = ReservationModel.find_overlapping_reservations(room_id, check_in, check_out)
        return len(overlapping) == 0
        