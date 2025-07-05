# backend/app/models/guest_model.py

from backend.config.dbconnect import get_connection 

class GuestModel:

	@staticmethod 
	def create_guest(first_name, last_name, email, phone_number=None, 
	                 address=None, id_type="Passport", id_number=None,
					 dob=None, nationality="unknown"):
		"""
            Insert a new guest into the database.
        """
		conn = get_connection()
		if not conn:
			return None
			
		try:
			cursor = conn.cursor() 
			sql = """
				INSERT INTO guests (
					first_name, last_name, email, phone_number, address,
					id_type, id_number, dob, nationality
				)
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
			"""
			
			values = (
					first_name, last_name, email, phone_number, address,
					id_type, id_number, dob, natinality
				)
			cursor.execute(sql, values)
			conn.commit()
			return cursor.lastrowid
        except Exception as e:
			print(f "[GuestModel] Error creating guest: {e}")
			return None
		finally:
				cursor.close()
				conn.close() 
				
	@staticmethod
    def get_guest_by_id(guest_id):
		"""
           Retrieve a guest by ID.
        """
                
        conn = get_connection()
        if not conn:
			return None 
		try: 
			cursor = conn.cursor(dictionary=True) 
			cursor.execute("SELECT * FROM guests WHERE guest_id = %s", (guest_id,))
			return cursor.fetchone() 
		except Exception as e:
			print(f"[GuestModel] Error fetching guest by ID: {e}")
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
				return []
			try:
				cursor = conn.cursor(dictionary=True)
				cursor.execute("SELECT * FROM guests")
				return cursor.fetchall()
			except Exception as e:
				print(f"[GuestModel] Error fetching all guests: {e}")
				return []
			finally:
				cursor.close()
				conn.close()
       
      @staticmethod 
      def update_guest(guest_id, update_data: dict):
          """
             Update guest details by ID.
          """
           
          conn = get_connection()
          if not conn:
                return False
          try:
                fields = ', '.join(f"{key} = %s" for key in update_data.key())
                values = list(update_data.value()) + [guest_id]
            
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
        def delete_guest(guest_id):
			"""
               Delete a guest by ID.
            """
			conn = get_connection()
			if not conn:
				return False
						
            try:
				cursor = conn.cursor()
				cursor.execute("DELETE FROM guests WHERE guest_id = %s", (guest_id,))
				conn.commit()
				return cursor.rowcount > 0 
			except Exception as e:
				print(f" Error deleting guest: {e}")
                return False
			finally:
				cursor.close()
                conn.close() 
						
						