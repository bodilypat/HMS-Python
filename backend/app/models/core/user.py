from backend.config.dbconnect import get_connection

class UserModel:
	
	@staticmethod 
	def create_user(full_name, usermame, email, password_hash. role="Guest", phone_number=None, status="Guest"):
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
            
            
            