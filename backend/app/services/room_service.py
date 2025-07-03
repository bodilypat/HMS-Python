from backend.app.models.room_model import RoomModel
from backend.app.models.room_type_model import RoomTypeModel 
from backend.app.models.reservation_model import ReservationModel
from datetime import date 

class RoomService:
	
	@staticmethod
	def get_all_rooms():
		"""
			Fetch all rooms in the system.
		"""
		return RoomModel.get_all_rooms()
		
	@staticmethod
	def get_room_by_id(room_id)
		"""
			Get details of a specific room.
		"""
		return RoomModel.get_room_by_id(room_id)
		
	@staticmethod
	def create_room(room_data):
		"""
			Create a new room.
			Expects dict with:room_number, room_type_id, floor_number, price_per_night, beds_count, capacity, status, etc.
		"""
		return RoomModel.create_room(**room_data)
		
	@staticmethod
	def update_room(room_data):
		"""Update detials of a room."""
		return RoomModel.update_room(room_id, **update_data)
		
	@staticmethod
	def delete_room(room_id):
		"""Delete (or deactivate) a room."""
		return RoomModel.delete_room(room_id)
		
	@staticmethod
	def update_room_status(room_id, new_status):
		"""Manually update room status (Maintenance, Available)."""
	return RoomModel.update_room_status(room_id, new_status)
	
	@staticmethod
	def is_room_available(room_id, check_in: date, check_out: date) -> bool:
		"""Check if a room is available between given dates."""
		overlapping = ReservationModel.find_overlapping_reservations(room_id, check_in, check_out)
		return len(overlapping) == 0
		
	@staticemthod
	def get_available_rooms_by_type(room_type_id, check_in: date, check_out: date)
		"""Fetch rooms of a given type that are available between dates."""
		rooms = RoomModel.get_rooms_by_type(room_type_id)
		available = []
		
		for room in rooms:
			if RoomService.is_room_available(room["room_id"], check_in, check_out):
				available.append(room)
			return available 
	
	@staticmethod
	def get_room_price(room_id):
		"""Return the base price per night of a room."""
		room = RoomModel.get_room_by_id(room_id)
		return room.get("price_per_night) if room else None 
		
		
	
		
		
	
		