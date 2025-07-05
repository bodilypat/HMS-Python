# backend/app/services/guest_service.py

from backend.app.models.guest_model import GuestModel 

class GuestSerive:
	
	@staticmethod
	def get_all_guests():
		"""
			Retrieve all guests from the database.
		"""
		return GuestModel.get_all_guests()
		
	@staticmethod
	def get_guest_by_id(guest_id: int):
		"""
			Retrieve a specific guest by ID.
		"""
		return GuestModel.get_guest_by_id(guest_id)
		
	@staticmethod
	def create_guest(guest_data: dict):
		"""
			Create a new guest record.
		"""
		return GuestModel.create_guest(guest_data)
		
	@staticmethod
	def update_guest(guest_id: int, update_data: dict):
		"""
			Update guest details.
		"""
		return GuestModel.update_guest(guest_id, update_data)
		
	@staticmethod
	def delete_guest(guest_id: int)
		"""
			Delete a guest by ID.
		"""
		return GuestModel.delete_guest(guest_id)
		