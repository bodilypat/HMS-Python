# backend/app/models/user.py

from backend.config.dbconnect import get_connection

class UserModel:
	
	@staticmethod
	def create_user(full_name, username,email, password_hash, role="Guest", phone_number=None, status="Active"):
		"""
			Create a new user record in the database.
		"""
		conn = get_connection()
		if not conn:
			print("[UserModel] Database connection failed.")
			return None 
		
		try:
			cursor = conn.cursor()
			sql = """
				INSERT INTO users (full_name, username, email, password_hash, role, phone_number, status)
				VALUES (%s, %s, %s, %s, %s, %s, %s)
			"""
			values = (full_name, username, email, password_hash, phone_number, status)
			cursor.execute(sql, values)
			conn.commit()
			return cursor.lastrowid
		except Exception as e:
			print(f"[UserModel] Error Creating user: {e}")
			return None 
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def get_user_by_email(email):
	"""
		Retrieve a user by email.
	"""
	conn = get_connection()
	if not conn:
		print("[UserModel] Database connection failed.")
		return None 
		
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return cursor.fetchone()
    except Exception as e:
        print(f"[UserModel] Error fetchng user by ID: {e}")
        return None 
    finally:
        cursor.close()
        conn.close()
        
    @staticmethod
    def update_user(user_id, update_data: dict):
        """
            Update user fields by ID.
        """
        if not update_data:
            print("[UserModel] No data provided to update.")
            return False 
        
        conn = get_connection()
        if not conn:
            print("[UserModel] Database connection failed.")
            return False 
            
        try:
            cursor = conn.cursor()
            fields = ', '.join(f"{key} = %s"  for key in update_data_keys())
            values = list(update_data.values()) + [user_id]
            sql = f"UPDATE users SET {fields} WHERE id = %s"
            cursor.execute(sql, values)
            conn.commit()
            return cursor.rowcount > 0 
        except Exception as e:
            print(f"[UserModel] Error updating user: {e}")
            return False 
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def delete_user(user_id):
        """
            Delete a user by ID.
        """
        conn = get_connection()
        if not conn:
            print("[UserModel] Database connection failed.")
            return False 
        
        try: 
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            return cursor.rowcount > 0 
        except Exception as e:
            print(f"[UserModel] Error deleting user: {e}")
            return False 
        finally:
            cursor.close()
            conn.close()
            
			