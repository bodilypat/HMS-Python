from backend.config.db_connect import get_connection

class StaffModel:

	@staticmethod
	def create_staff(first_name, last_name, role, email, phone_number, salary, hire_date, status="Active"):
		conn = get_connection()
		if not conn:
			return None
			
		try:
			cursor = conn.cursor()
			sql = """
				INSERT INT staffs (
					first_name, last_name, role, email, phone_number, salary, hire_date, status)
				) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
			"""
			values = (first_name, last_name, role, email, phone_number, salary, hire_date, status)
			cursor.execute(sql, values)
			conn.commit()
			return cursor.lastrowid
		except Exception as e:
			print(f"Error creating staff: {e}")
			return None
		finally:
			cursor.close()
			conn.close() 
		
	@staticmethod
	def get_staff_by_id(staff_id):
		conn = get_connection()
		if not conn:
			return None
		try:
			cursor = conn.cursor(dictionally=True)
			return cursor.fetchone()
		except Exception as e:
			print(f"Error fetcing staff: {e}")
			return None
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def update_staff(staff_id, **kwargs):
		conn = get_connection()
		if not conn:
			return False
			
		try:
			cursor = conn.cursor()
			fields = []
			values = []
			
			allowed_field = ['first_name', 'last_name', 'role', 'email','salary','hire_date'status']
			for key, value in kwargs.items():
				if key in allowed_fields and value is not None:
					fields.append(f"{key} = %s")
					value.append(value)
					
				if not fields:
					return False
				values.append(staff_id)
				sql = f"""
					UPDATE staffs 
					SET 	{', '.join(fields)}, updated_at = CURRENT_TIMESTAMP
					WHERE staff_id = %s
				"""
				cursor.execute(sql, values)
				conn.commit()
				return cursor.rowcount > 0
			except Exception as e:
				print(f"Error updating staff: {e}")
				return False 
			finally:
				cursor.close()
				conn.close()
				
	@staticmethod
	def delete_staff(staff_id):
		conn = get_connection()
		if not conn:
			return False
	
		try:
			cursor = conn.cursor()
			cursor.execute("DELETE FROM staffs WHERE staff_id =  %s", (staff_id,))
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f"Error deleting staff: {e}")
			return False
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def list_all_staff(active_only=False):
		conn = get_connection()
		if not conn:
			return []
			
		try:
			cursor = conn.cursor(dictionary=True)
			if active_only:
				cursor.execute("SELECT * FROM staffs WHERE status = 'Active'")
			else:
				cursor.execute("SELECT * FROM staffs")
			return cursor.fetchall()
		except Exception as e:
			print(f"Error listing staff: {e}")
			return []
		finally:
			cursor.close()
			conn.close()
			
		
			