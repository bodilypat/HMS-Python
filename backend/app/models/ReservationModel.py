# backend/app/models/ReservationModel.py

form backend.config.dbconnect import get_connection
from typing import Optional, List, Dict, Any

class ReservationModel:
	@staticmethod
	def create_reservation( 
                            guest_id: int,
                            room_id: int,
                            check_in: str,
                            check_out: str,
                            number_of_guests: int= 1,
                            reservation_status: str = 'Pending',
                            payment_status: str = 'Pending',
                            booking_source: str = 'Website', 
                            special_request: Optional[str] = None
                        ) -> Optional[int]:
        """ Insert a new reservation into the database."""
        
		conn = get_connection()
		if not conn:
			return None 
			
		try:
			cursor = conn.cursor()
			sql = """
				INSERT INTO reservations (
					guest_id, room_id, check_in, check_out, number_of_guests, reservation_status,
					payment_status, booking_source, special_request
				) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
			"""
			values = (
				guest_id, room_id, check_in, check_out, number_of_guests, reservation_status,
				payment_status, booking_source, special_request
			)
			cursor.execute(sql, values)
			conn.commit()
			return cursor.lastrowid
		except Exception as e:
			print(f"[Error] Failed to  creating reservation: {e}")
			return None
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def get_reservation_by_id(reservation_id: int) -> Optional[Dict[str, Any]]:
		"""Fetch reservation by its ID."""
        
		conn = get_connection()
		if not conn:
			return None
		try:
			cursor = conn.cursor(dictionary=True)
			cursor.execute("SELECT * FROM reservations WHERE reservation_id = %s", (reservation_id,))
			return cursor.fetchone()
		except Exception as e:
			print(f"[Error] Failed to fetch reservation by ID: {e} ")
			return None
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def get_reservation_by_guest(guest_id: int) -> List[Dict[str, Any]]:
        
		"""Get all reservations made by a specific guest."""
        
		conn = get_connection() 
		if not conn:
			return []
			
		try:
			cursor = conn.cursor(dictionary=True)
			cursor.execute("SELECT * FROM reservations WHERE guest_id = %s", (guest_id,))
			return cursor.fetchall()
		except Exception as e:
			print(f"[Error] Failed to fetch reservation reservations by guest:{e}") 
			return []
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod	
	def update_reservation_status(reservation_id: int, new_status: str) -> bool:
		"""Update reservation status (Pending, Confirmed, Cancelled)."""
		conn = get_connection()
		if not conn:
			return False 
		
		try:
			cursor = conn.cursor()
			cursor.execute(
				"UPDATE reservations SET reservation_status = %s WHERE reservation_id = %s",
				(new_status, reservation_id)
			)
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f"[Error] Failed to update reservation status: {e}")
			return False
		finally:
			cursor.close()
			conn.close()
	
	@staticmethod
	def delete_reservation(reservation_id: str) -> bool:
        
		"""Delete a reservation by ID."""
		conn = get_connection()
		if not conn:
			return False 
			
		try:
			cursor = conn.cursor()
			cursor.execute("DELETE FROM reservations WHERE reservation_id = %s", (reservation_id,))
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f "[Error] Failed to delete reservation: {e}")
			return False 
		finally:
			cursor.close()
			conn.close()
			