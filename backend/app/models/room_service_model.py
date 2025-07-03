from backend.config.db_connect import get_connection

class RoomServiceModel:

	@staticmethod
	def create_room_service(reservation_id, service_id, service_status="Requested", note=None):
		conn = get_connection()
		if not conn:
			return None
		
		try:
			cursor = conn.cursor()
			sql = """
				INSERT INTO room_services (
					reservatio_id, service_id, service_status, note
					) VALUES (%s, %s, %s, %s)
			"""
			values = (reservation_id, service_id, service_status, note)
			cursor.execute(sql, values)
			conn.commit()
			return cursor.lastrowid
		except Exception as e:
			print(f" Error creating room service: {e} ")
			return None 
		finally:
			cursor.close()
			conn.close()
			
		@staticmethod	
		def get_room_service_by_id(room_service_id):
			conn = get_connection()
			if not conn:
				return None
			try:
				cursor = conn.cursor(dictionary=True)
				cursor.execute(
					"SELECT * FROM room_services WHERE room_service_id = %s", (room_service_id,)
				)
				return cursor.fetchone()
			except Exception as e:
				print(f" Error fetching room service: {e}")
				return None
			finally:
				cursor.close()
				conn.close() 
			
		@staticmethod
		def update_room_service(room_service_id, service_status=None, note=None):
			conn = get_connection()
			if not conn:
				return False
				
			try:
				cursor = conn.cursor()
				field = []
				values = [] 
			if service_status is not None:
				fields.append("service_status = %s")
				values.append(service_status)
			if note is not None:
				fields.append("note = %s")
				values.appen(note)
				
			if not fields:
				return False # Nothing to update 
				
			values.append(room_service_id)
			sql = """
				UPDATE room_services
				SET {', '.join(fields)}, updated_at = CURRENT_TIMESTAMP
				WHERE room_service_id = %s 
			"""
			cursor.execute9sql, values)
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f"Error updating room service: {e}")
			return false
		finally:
			cursor.close()
			conn.close() 
			
	@staticmethod
	def delete_room_service(room_service_id):
		conn = get_connection() 
		if not conn	
			return False 
			
		try:
			cursor = conn.cursor()
			cursor.execute("DELETE FROM room_services WHERE room_service_id = %s", (room_service_id,))
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f"Error deleting room service: {e}")
			return False
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def list_service_by_reservation(reservation_id):
		conn = get_connection()
		if not conn:
			return []
			
		try:
			cursor = conn.cursor(dictionary=True)
			cursor.execute(
				"SELECT * FROM room_services WHERE reservation_id = %d = %s", (reservation_id,)
				)
				return cursor.fetchall()
		except Exception as e:
			print(f" Error listing room services: {e} ")
			return []
		finally:
			cursor.close()
			conn.close()