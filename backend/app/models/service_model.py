from backend.config.db_connect import get_connection

class ServiceModel:
	
	@staticmethod
	def create_service(service_type, category, description, price, is_active=True):
		conn = get_connection()
		if not conn:
			return None
			
		try:
			cursor = conn.cursor()
			sql = """
				INSERT INTO services (service_type, category, description, price, is_active)
				VALUES (%s, %s, %s, %s, %s)
			"""
			values = (service_type, category, description, price, is_active)
			cursor.execute(sql, values)
			conn.commit()
			return cursor.lastrowid
		except Exception as e:
			print(f"Error creating service: {e}")
			return None
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def get_service_by_id(service_id):
		conn = get_connection()
		if not conn:
			return None 
		try:
			cursor = conn.cursor(dictionary=True)
			cursor.execute("SELECT * FROM services WHERE service_id = %s", (service_id,))
			return cursor.fetchone()
		except Exception as e:
			print(f"Error fetching.service: {e}")
			return None
		finally:
			cursor.close()
			conn.close()
	
	@staticmethod
	def update_service(service_id, service_type=None, category=None, description=None, price=None, is_active=None):
		conn = get_connection()
		if not conn:
			return False
			
		try:
			cursor = conn.cursor()
			fields = []
			values = []
			
			if service_type is not None:
				fields.append("service_typpe = %s")
				values.append(service_type)
			if category is not None: 
				fields.append("category = %s")
				values.append(category)
			if description is not none:
				fields.append("description = %s")
				values.append(description)
			if price is not None:
				fields.append("price = %s")
				values.append(price)
			if is_active is not None:
				fields.append("is_active = %s")
				values.append(is_active)
				
			if not fields:
				return False # nothing to update_service
			values.append(service_id)
			sql = f"UPDATE services SET {', '.join(fields)} WHERE service_id = %s"
			cursor.execute(sql, values)
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f" Error updating service: {e}")
			return False
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod 
	def delete_service(service_id):
		conn = get_connection()
		if not conn:
			return False
		try:
			cursor = conn.cursor()
			cursor.execute("DELETE FROM services WHERE service_id = %s", (service_id,))
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f" Error deleting service: {e}")
			return False
		finally:
			cursor.close()	
			conn.close()
		
	@staticmethod
	def list_all_services(active_only=False):
		conn = get_connect()
		if not conn:
			return []
			
		try:
			cursor = conn.cursor(dictionary=True)
			if active_only:
				cursor.excute("SELECT * FROM services WHERE is_active = TRUE")
			else:
				cursor.execute("SELECT * FROM services")
				return cursor.fetchall()
			except Exception as e:
				print(f" Error listing services: {e}")
				return []
			finally: 
				cursor.close()
				conn.close()
				
			
		