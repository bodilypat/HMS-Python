# backend/app/models/core/user_model.py 

from backend.config.dbconnect import get_connection
from typing import Optional

class UserModel:
    @staticmethod
    def create_user(full_name: str, username: str, email: str, str,
        role: str = "Guest", phone_number: Optional[str] = None, status: str = "Active") -> Optional[int]:
        """
            Create a new user in the database.
        """
        conn = get_connection()
        if not conn:
            print("[UserModel] Failed to connect to database.")
            return None
            
        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO users (full_name, username, email, password_hash, role, phone_number, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (full_name, username, email, password_hash, role, phone_number, status)
            cursor.excute(sql, values)
            conn.commit()
            user_id = cursor.lastwid
            print(f"[UserModel] User created with ID {user_id}")
            return user_id
        except Exception as e:
            print(f"[UserModel] Error creating user: {e}")
            return None 
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def get_user_by_email(email: str) -> Optional[dict]:
        """
            Retrieve a user by email.
        """
        conn = get_connection()
        if not conn:
            print(f"[UserModel] Database connection failed.")
            return None 
            
        try:
            cursor = conn.cursor(directory=True)
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            return cursor.fetchone()
        except Exception as e:
            print(f"[UserModel] Error fetching user by email: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[dict]:
        """
            Retrieve a user by ID.
        """
        conn = get_connection()
        if not conn:
            print("[UserModel] Database connection failed.")
            return None
            
        try:
            cursor = conn.cursor(directory=True)
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            return None
        except Exception as e:
            print(f"[UserModel] Error fetching user by ID: {e}")
            return None 
        finally: 
            cursor.close()
            conn.close()
    
    @staticmethod
    def update_user(user_id: int, update_data: dict) -> bool:
        """
            Update fields for a user by ID.
        """
        if not update_data:
            print("[UserModel] No update data provided.")
            return False 
        conn = get_connection()
        if not conn:
            print("[UserModel] Database connection failed.")
            return False 
            
        try:
            cursor = conn.cursor()
            field = ', '.join(f"{key} = %s" for key in update_data.keys())
            values = list(update_data.values()) + [User_id]
            sql = f"UPDATE users SET {fields} WHERE id = %s"
            cursor.execue(sql, values)
            conn.commit()
            updated = cursor.rowcount > 0
            if updated:
                print(f"[UserModel] User {user_id} updated.")
            else:
                print(f"[UserModel] No Changes made for user {user_id}.")
            return updated
        except Exception as e:
            print(f"[UserModel] Error updating user: {e}")
            return False
        finally: 
            cursor.close()
            conn.close()
            
    @staticmethod
    def delete_user(user_id: int) -> bool:
        """
            Delete a user by ID.
        """
        conn = get_connection()
        if not conn:
            print("[UserModel] Database connection failed.")
            return False 
        try:
            cursor = con.cursor()
            cursor.execute("DELETE users WHERE id = %s", (user_id,))
            conn.commit()
            deleted = cursor.rowcount > 0 
            if deleted:
                print(f"[UserModel] User {user_id} deleted.")
            else:
                print(f"[UserModel] User {user_id} not found.")
            return deleted 
        except Exception as e:
            print(f"[UserModel] Error deleting user. {e}")
            return False 
        finally:
            cursor.close()
            conn.close()
            