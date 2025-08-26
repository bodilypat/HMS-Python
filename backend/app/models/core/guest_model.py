# backend/app/models/GuestModel.py

from backend.config.dbconnect import get_connection
from typing import Optional, List, Dict

class GuestModel:

	@staticmethod
	def create_guest(
			first_name: str,
            last_name: str,
            email: str, 
            phone_number: Optional[str] = None,
            address: Optional[str] = None,
            id_type: str = "Passport", 
            id_number: Optional[str] = None,
            dob: Optional[str] = None,
            nationality: str = "Unknown"
		) -> Optinal[int]:
		""" 
		   Insert a new guest into the database. 
		"""
		conn = get_connection()
		if not conn:
			print("[GuestModel] Database connection failed.")
			return None 
		
		try:
			cursor = conn.cursor()
			sql = """
				INSERT INTO guests (
					first_name, last_name, email, phone_number, address, id_type, id_number, dob, nationality
				)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                first_name, last_name, email, phone_number, address, id_type, id_number, dob, natinality
            )
			cursor.execute(sql, values)
			conn.commit()
            guest_id = cursor.lastrowid
            print(f"[GuestModel] Guest created with ID {guest_id}")
			return guest_id
		except Exception as e:
			print(f"[GuestModel] Error creating guest: {e}")
			return None 
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def get_guest_by_id(guest_id: int) -> Optional[Dict]:
		"""
			Retrieve a guest by ID. 
		"""
		conn = get_connection()
        if not conn:
            print("[GuestModel] Database connection failed.")
            return None 
        
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM guests WHERE guest_id = %s", (guest_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"[GuestModel] Error fetching guest by ID: {e}" )
            return None 
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def get_all_guests() -> List[Dict]:
        """
            Retrieve all guests.
        """
        conn = get_connection()
        if not conn:
            print(f"[GuestModel] Database connection failed.")
            return []
            
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM guests")
            return cursor.fetchall()
        except Exception as e:
            print(f"[GuestModel] Error fetching all guests: {e}"}
            return []
            
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod 
    def update_guest(guest_id: int, update_data: dict) -> bool:
        """Update guest details by ID."""
        if not update_data:
            print("[GuestModel] No update data provided.")
            return False 
        
        conn = get_connection()
        if not conn:
            print("[GuestModel] Database connection failed.")
            return False
            
        try:
            cursor = conn.cursor()
            fields = ', '.join(f"{key} = %s" for key in update_data.keys())
            values = list(update_data.values()) + [guest_id]
            sql = f"UPDATE guests SET {fields} WHERE guest_id = %s"
            cursor.execute(sql, values)
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"[GuestModel] Error updating guest: {e}")
            return False 
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod 
    def delete_guest(guest_id: int) ->bool:
        """
            Delete a guest by ID.
        """
        conn = get_connection()
        if not conn:
            print("[GuestModel] Database connection failed.")
            return False 
            
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM guests WHERE guest_id = %s", (guest_id,))
            conn.commit()
            return cursor.rowcount > 0
            print(f"[GuestModel] Guest {guest_id} deleted." if deleted else f"[GuestModel] Guest not found.")
            return deleted
        except Exception as e:
            print(f"[GuestModel] Error deleting guest: {e}")
            return False 
        finally:
            cursor.close()
            conn.close() 
            