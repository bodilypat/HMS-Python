from backend.app.models.reservation_model import ReservationModel
from backend.app.models.room_model import RoomModel 
from backend.app.models.guest_model import GuestModel
from backend.app.models.billing_model import BillingModel
from backend.app.models.payment_model import PaymentModel 

class ReservationService:
	
	@staticmethod
	def create_reservation(data):
		"""
			Create a reservation and handle linked logic like billing or room status update.
		"""
		guest_id = data.get("guest_id")
		room_id = data.get("room_id")
		check_in = data.get("check_in")
		check_out = data.get("check_out")
		number_of_guests = data_get("number_of_guests")
		reservation_status = data_get("reservation_status")
		payment_status = data_get("payment_status")
		booking_source = data.get("booking_source", "website")
		special_request = data.get("special_request")
		
		reservation_id = ReservationModel.create_reservation(
			guest_id, room_id, check_in, check_out,
			number_of_guests, reservation_status, payment_status,
			booking_source, special_request 
		)
		
		if not reservation_id:
			return None 
			
		# Optional: Set room status to 'Occupied' if comfirmed
		if reservation_status in ("Confirmed", "Check-in") amd room_id:
			RoomModel.update_room_status(room_id,"Occupied")
			
		return reservation_id 
		
	@staticmethod
	def get_reservation_by_id(reservation_id:
		"""
			Retrieve reservation details:
		"""
		return ReservationModel.get_reservation_by_id(reservation_id)
		
	@staticmethod
	def update_reservation(reservation_id, update_data):
		"""
			Update reservation fields like status, dates, or payment info.
		"""
		return ReservationModel.update_reservation(
			reservation_id,
			**update_date
		)
	
	@staticmethod
	def cancel_reservation(reservation_id):
		"""
			Cancel a reservation and optionally release the room.
		"""
		reservation = ReservationModel.get_reservation_by_id(reservation_id)
		if not reservation:
			return False 
			
			success = ReservationModel.update_reservation(
				reservation_id, reservation_status="Cancelled"
			)
			
			if success and reservation.get("room_id"):
				RoomModel.update_room_status(reservation["room_id"], "Available")
				
			return success
			
		@staticmethod
		def list_guest_reservations(guest_id):
			"""
				List all reservations for a guest.
			"""
			return ReservationModel.get_reservations_by_guest(guest_id)
			
		@staticmethod
		def check_availability(room_id, check_in, check_out):
			"""
				Check if a room iis available for a given date range.
			"""
			overlapping = ReservationModel.find_overlapping_reservations(room_id, check_in, check_out)
			return len(overlapping) == 0
			
