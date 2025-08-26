# backend/app/models/core/staff_model.py

from backend.config.dbconnect import get_connection
from typing import Optional, List, Dict

class StaffModel:

	@staticmethod 
	def create_staff(full_name: str, 
                     username: str,
                     email: str,
                     password_hash: str,
                     department: str,
                     role: str ="staff",
                     phone_number: Optional[str] = None,
                     status: str ="Acticve"
                ) -> Optinal[int]:
        """
            Create a new staff member in the database.
        """
        conn = get_connection()
        if not conn:
            print(f"[StaffModel] Database connection failed.")
            return None
	
        try: 
            cursor = conn.cursor()
            sql = """
                INSERT INTO staffs (
                    full_name, usernam, email, password_hash, department, role, phone_number, status
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (full_name, username, email, password_hash, department, role, phone_number, status)
            cursor.execute(sql, values)
            conn.commit()
            staff_id = cursor.lastrowid
            print(f"[StaffModel] Staff creating with ID {staff_id}")
            return staff_id
	
        except Exception as e:
            print(f"[StaffModel] Error creating staff: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
		
	@staticmethod
	def get_staff_by_id(staff_id: int) -> Optional[Dict]:
		"""
			Retrieve staff member by ID.
		"""
		conn = get_connection()
        if not conn:
            print("[StaffModel] Database connection failed.")
            return None
            
        try:
            cursor = conn.cursor(directory=True)
            cursor.execute("SELECT * FROM staffs WHERE id = %s", (staff_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"[StaffModel] Error fetching staff by ID: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod 
    def get_all_staffs() -> List[Dict]:
        """
           Retrieve all staffs members.
        """
        conn = get_connection()
        if not conn:
            print("[StaffModel] Database connection failed.")
            return []
            
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM staffs")
            return cursor.fetchall()
        except Exception as e:
            print(f"[StaffModel] Error fetching all staff: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def update_staff(staff_id: int, update_data: dict) -> bool:
        """
           Update staff member details by ID.
        """
        if not update_data:
            print("StaffModel] No update data provided.")
            return False 
            
        conn = get_connection()
        if not conn:
            print("[StaffModel] Database connection failed.")
            return False 
            
        try:
            cursor = conn.cursor()
            fields = ', '.join(f"{key} = %s" for key in update_date.keys())
            values = list(update_data.values()) + [staff_id]
            sql = f"UPDATE staffs SET {fields} WHERE id = %s"
            cursor.execute(sql, values)
            conn.commit()
            updated = cursor.rowcount > 0
            print(f"[StaffModel] Staff {staff_id} updated." if updated else f"[StaffModel] No changes made.")
            
        except Exception as e:
            print(f"[StaffModel] Error updating staff: {e}")
            return false 
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def delete_staff(staff_id: int) -> bool:
        """
            Delete a staff member by ID.
        """
        conn = get_connection()
        if not conn:
            print("[StaffModel] Database connection failed.")
            return False 
            
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM staffs WHERE id = %s", (staff_id,))
            conn.commit()
            deleted = cursor.rowcount > 0
            print(f"[StaffModel] Staff {staff_id} deleted." if deleted else f"[StaffModel] Staff not found.")
            return deleted
        except Exception as e:
            print(f"[StaffModel] Error deleting staff: {e}")
            return False 
        finally:
            cursor.close()
            conn.close()