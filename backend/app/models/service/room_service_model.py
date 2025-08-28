# backend/app/models/service/room_service_model.py

from typing import Optional, List, Dict, Any
from backend.config.db_connect import get_connection

class RoomServiceModel:

	@staticmethod
	def create_room_service(reservation_id: int, service_id: int, service_status="Requested", note=None)-> Optional[int]:
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
			print(f"[Error] Creating room service: {e} ")
			return None 
		finally:
			cursor.close()
			conn.close()
			
		@staticmethod	
		def get_room_service_by_id(room_service_id: int) -> Optional[Dict[str, Any]]:
            """Fetch a room service request by its ID."""
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
				print(f"[Error] Fetching room service: {e}")
				return None
			finally:
				cursor.close()
				conn.close() 
			
		@staticmethod
		def update_room_service(
                room_service_id: int, 
                service_status: Optional[str] = None, 
                note: Optional[str] = None
            ) -> bool:
                
            """Update service status or note of a room service request."""
            
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
				fields.append("notes = %s")
				values.appen(note)
				
			if not fields:
				return False # Nothing to update 
				
			fields.append("updated_at = CURRENT_TIMESTAMP")
			sql = f"""
				UPDATE room_services
				SET {', '.join(fields)}
				WHERE room_service_id = %s 
			"""
            values.append(room_service_id)
			cursor.execute(sql, tuple(values))
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f"Error updating room service: {e}")
			return False
		finally:
			cursor.close()
			conn.close() 
			
	@staticmethod
	def delete_room_service(room_service_id: int) -> bool:
        """Delete a room service request."""
		conn = get_connection() 
		if not conn	
			return False 
			
		try:
			cursor = conn.cursor()
			cursor.execute("
                DELETE FROM room_services WHERE room_service_id = %s", 
                (room_service_id,)
            )
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f"[Error] Deleting room service: {e}")
			return False
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def list_service_by_reservation(reservation_id: int) -> List[Dict[str, Any]]:
        """List all room service requests for a given reservation."""
		conn = get_connection()
		if not conn:
			return []
			
		try:
			cursor = conn.cursor(dictionary=True)
			cursor.execute(
                "SELECT * FROM room_services WHERE reservation_id = %d = %s",
                (reservation_id,)
            )
			return cursor.fetchall()
		except Exception as e:
			print(f" Error listing room services: {e} ")
			return []
		finally:
			cursor.close()
			conn.close()