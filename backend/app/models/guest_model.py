from backend.config.dbconnect import get_connection 
	@staticmethod 
	def create_guest(first_name, last_name, email, phone_number=None, 
	                 address=None, id_type="Passport", id_number=None,
					 dob=None, nationality="unknown"):
		"""Insert a new guest into the database."""
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
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
			"""
			
			values = (
					first_name, last_name, email, phone_number, address,
					id_type, id_number, dob, natinality
				)
				cursor.execute(sql, values)
				conn.commit()
				return cursor.lastrowid
			except Exception as e:
				print(f " Error creating guest: {e}")
				return None
			finally:
				cursor.close()
				conn.close() 
				
			@staticmethod
			def get_guest_by_id(guest_id):
				"""Retrieve a guest by ID."""
				conn = get_connection()
				if not conn:
					return None 
				try: 
					cursor = conn.cursor(dictory=True) 
					cursor.execute("SELECT * FROM guests WHERE guest_id = %s", (guest_id,))
					return cursor.fetchone() 
				except Exception as e:
					print(f" Error fetching guest: {e}")
					return None 
				finally:
					cursor.close() 
					conn.close()
					
			@staticmethod
			def get_all_guests():
				"""Retrieve all guests."""
				conn = get_connection()
				if not conn:
					return []
				try:
					cursor = conn.cursor(dictionary=True)
					cursor.execute("SELECT * FROM guests")
					return cursor.fetchall()
				except Exception as e:
					print(f" Error fetching all guests: {e}")
					return []
				finally:
					cursor.close()
					conn.close()
					
				@staticmethod
				def delete_guest(guest_id):
					"""Delete a guest by ID"""
					conn = get_connection()
					if not conn:
						return
						
					try:
						cursor = conn.cursor()
						cursor.execute("DELETE FROM guests WHERE guest_id = %s", (guest_id,))
						conn.commit()
						return cursor.rowcount > 0 
					exeception as e:
						print(f" Error deleting guest: {e}")
						return False
					finally:
						cursor.close()
						conn.close() 
						
						