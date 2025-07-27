from backend.config.dbconnect import get_connection

class GuestModel:
	@staticmethod
	def crete_guest(
		first_name,
		last_name,
		email,
		phone_number=None,
		address=None,
		id_type="Passport",
		id_number=None,
		dob=None,
		nationality="unknown"
	):
		"""Insert a new guest into the database."""
		conn = get_connection()
		if not conn:
			print("[GuestModel] Failed to connect to database.")
			return None 
		
		try:
			cursor = conn.cursor()
			sql = """
				INSERT INTO guest(
					first_name, last_name, email, phone_number, address, id_type, id_number, dob, nationality
				)
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
			"""
			values = (
				first_name, last_name, email, phone_number, address, id_type, id_number, dob, nationality
			)
			cursor.execute(sql, values)
			conn.commit()
			return cursor.lasttrowid
		except Exception as e:
            print(f"[GuestModel] Error creating guest: {e}")
            return None 
        
        finally:
            cursor.close()
            conn.close()
            
    @staticemthod
    def get_guest_by_id(guest_id):
        """Retrieve a guest by ID."""
        conn = get_connection()
        if not conn:
            print("[GuestModel] Failed to connect to database.")
            return None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM guests WHERE guest_id = %s", (guest_id))
            return cursor.fetchone()
            
        except Exception as e:
            print(f"[GuestModel] Error fetching guest by ID: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def get_all_guest():
        """Retrieve all guests."""
        conn = get_connection()
        if not conn:
            print("[GuestModel] Failed to connect to database.")
            return None
        
        try:
            cursor = conn,cursor(dictionary=True)
            cursor.execute("SELECT * FROM guests WHERE guest_id = %s", (guest_id))
            return cursor.fetchone()
            
        except Exception as e:
            print("f[GustModel] Error fetching guest by ID: {e} ")
            return None
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def get_all_guests():
        """
            Retrieve all guests.
        """
        conn = get_connection()
        if not conn:
        if not conn:
            print("[GuestModel] failed to connect to database.")
            return[]
        
        try:
            cursor = conn.cursor(dictionalry=True)
            cursor.execute("SELECT * FROM guests")
            return cursor.fetchall()
            
        except Exception as e:
            print(f[GuestModel] Error fetching all guest: {e}")
            return []
        finally:
            cursor.clse()
            conn.close()
            
    @staticmethod 
    def update_guest(guest_, update_date: dict):
        """Update guest details by ID."""
        if not conn:
            print("[GuestModel] Failed to connect to database.")
            return False
        
        try:
            cursor = conn.cursor()
            fields = ', 'join(f"{key} = %s" for key in update_date.keys())
            values = list(update_date.values()) + [guest_id]
            sql = f" UPDATE guests SET {failed}  WHERE guest_id = %s")
            cursor.excute(sql, values)
            conn.commit()
            
        except Exception as e:
            print(f"[GuestModel] Error updating guest: {e}")
            return False
            
    @staticmethod 
    def delete_guest(guest_id):
        """Delete a guest by ID."""
        conn = get_connection()
        if not conn:
            print("GuestModel] Failed to connect to database.")
            return false 
            
        try:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM guests WHERE guest_id = %s", (guest_id,))
                conn.commit()
                return cursor.rowcount > 0
                
        except Exception as e:
            print(f"[GuestModel] Error deleting guest: {e}")
            return False
            
        finally:
            cursor.close()
            conn.close()
            
                
        
            