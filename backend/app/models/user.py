# backend/app/models/user.py 

from backend.config.dbconnect import get_connection

class UserModel:
	
	@staticmethod 
	def create_user(full_name, usermame, email, password_hash, role="Guest", phone_number=None, status="Active"):
        """
            Create a new user record in the database.
        """
		conn = get_connection()
		
		if not conn: 
			printf("Datebase connection failed.")
			return False
			
		try:
			cursor = conn.cursor()
			sql = """
					INSERT INTO users(full_name, email, password_hash, role, phone_number, status)
					VALUES (%s, %s, %s, %s, %s, %s)
				"""
				
				values = (full_name, usermame, email, password_hash, role, phone_number, status)
				cursor.excute(sql, values)
				conn.commit()
				return cursor.lastrowind
        except Exception as e:
            print(f"[UserModel] Error creating usr: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def get_usr_by_email(email):
        """
            Retrieve a user by email.
        """
        conn = get_connection()
        if not conn:
            print("Database connection failed.")
            return None
        
        try:
            cursor = conn.cursor(dictionary=True) 
            cursor.execute("SELECT * FROM users WHERE email = %s", (email))
            return cursor.fetchone()
            
        except exception as e:
            print(f"[UserModel] Error fetching user: {e}")
            return None 
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def get_user_by_id(user_id):
        """
           retrieve a user by their ID.
        """
        conn = get_connection()
        if not conn:
            print("[UserMode] database connection failed.")
            return None
        
        try: 
            cursor = conn.cursor(dictional=True)
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            return cursor.fetchone()
        except Exception as :
            print(f"[UserModel] Error fetching user by ID: {e}")
            return None 
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def update_user(user_id, update_date: dict):
        """
           Update user fields by ID.
        """
        conn = get_connection()
        if not conn:
            print("[UserModel] Database connection failed.")
            return False
        try:
            cursor = conn.cursor()
            fields = ', '.join("f{key} %s" for key in update_data.keys())
            values = list(update_data.values()) + [user_id]
            sql = f"UPDATE users SET {fields} WHERE id = %s"
            cursor.execute(sql, values)
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"[UserMode] Error updating user: {e}")
            return False 
            
        finally:
            cursor.close()
            conn.close()
            
    @staticmehod
    def delete_user(user_id):
        """
           Delete a user by ID.
        """
        conn = get_connection()
        if not conn:
            print("[UserMode] Database connection failed.")
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            return cursor.rowcount > 0
            
        except Exception as e:
            print(f"[UserMode] Error deleting user: {e}")
            return False 
        finally:
            cursor.close()
            conn.close()