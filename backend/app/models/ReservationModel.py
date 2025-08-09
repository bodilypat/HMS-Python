# backend/app/models/ReservationModel.py

from backend.app.core.database import get_connection
from typing import Optional, List, Dict, Any
from datetime import date 

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
				guest_id, room_id, check_in, check_out, 
                number_of_guests, reservation_status,
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
    def get_all_reservation() -> List[Dict[str, Any]]:
        """
           Retrieve all reservations.
        """
        conn = get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM reservations ORDER BY created_at DESC")
            return cursor.fetchall()
        except Exception as e:
            print(f"[Error] Failed to fetch all reservation: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
         
	@staticmethod	
	def update_reservation(reservation_id: int, **fields) -> bool:
		"""Update reservation with provided fields."""
		if not fields:
			return False 
		
		try:
            columns = ", ".join([F"{key} = %s", for key in fields.keys()])
            values = list(fields.values()) + [reservation_id]
            
			cursor = conn.cursor()
			query = f"UPDATE reservations SET {columns} WHERE reservation_id = %s"
            cursor.execute(query, values)
            conn.commit()
            return cursor.rowcount > 0
		except Exception as e:
			print(f"[Error] Failed to update reservation status: {e}")
			return False
		finally:
			cursor.close()
			conn.close()
            
    @staticmethod
    def update_reservation_stataus(reservation_id: int, new_status: str) -> bool:
        """
           Update reservation status.
        """
        return ReservationModel.update_reservation(reservation_id, reservation_status=new_status)
        
	@staticmethod
	def delete_reservation(reservation_id: int) -> bool:
        
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
			