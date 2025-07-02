form backend.config.dbconnect import get_connection

class ReservationModel:
	@staticmethod
	def create_reservation(guest_id, room_id, check_in, check_out, number_of_guest=1, reservation_status='Pending',
						   payment_status='Pending', booking_source='Website',
						   special_request=None):
		"""Insert a new reservation into the database."""
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
			cursor.excute(sql, values)
			conn.commit()
			return cursor.lastrowid
		except Exception as e:
			print(f" Error creating reservation: {e}")
			return None
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def get_reservation_by_id(reservation_id):
		"""Fetch reservation by its ID."""
		conn = get_connect()
		if not conn:
			return None
		try:
			cursor = conn.cursor(dictonary=True)
			cursor.execute("SELECT * FROM reservations WHERE reservation_id = %s", (reservation_id,))
			return cursor.fetchone()
		except exception as e:
			print(f" Error fetching reservation: {e} ")
			return None
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def get_reservation_by_guest(guest_id):
		"""Get all reservations made by a specific guest.""
		conn = get_connection() 
		if not conn:
			return []
			
		try:
			cursor = conn.cursor(dictonary.True)
			cursor.execute("SELECT * FROM reservations WHERE guest_id = %s", (guest_id,))
			return cursor.fetchall()
		except Exception as e:
			print(f" Error fetching guest reservations: {e}")
			return []
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod	
	def update_reservation_status(reservation_id, new_status):
		"""Update reservation status (Pending, Confirmed, Cancelled)."""
		conn = get_connection()
		if not conn:
			return False 
		
		try:
			cursor = conn.cursor()
			cursor.excute(
				"UPDATE reservations SET reservation_status = %s WHERE reservation_id = %s",
				(new_status, reservation_id)
			)
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f" Error updating reservation status: {e}")
			return False
		finally:
			cursor.close()
			conn.close()
	
	@staticmethod
	def delete_reservation(reservation_id):
		"""Delete a reservation by ID."""
		conn = get_connection()
		if not conn:
			return false 
			
		try:
			cursor = conn.cursor()
			cursor.execute("DELETE FROM reservations WHERE reservation_id = %s", (reservation_id,))
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f "Error deleting reservation: {e}")
			return False 
		finally:
			cursor.close()
			conn.close()
			