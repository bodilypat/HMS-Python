# backend/app/models/HousekeepingModel.py 

from backend.config.db_connect import get_connection

class HousekeepingModel:
	@staticmethod
	def create_task(room_id, staff_id, cleaning_date, cleaing_status="Pending"):
		conn = get_connection()
		if not conn:
			return None
		
		try:
			with conn.cursor() as cursor:
            sql = """
				INSERT INTO housekeeping (
					room_id, staff_id, cleaning_date, cleaning_status
				) VALUES (%s, %s, %s, %s)
			"""
			values = (room_id, staff_id, cleaning_datge, cleaning_status)
			cursor.execute(sql, values)
			conn.commit()
			return cursor.lastrowid
		except Exception as e:
			print(f"Error creating housekeeping task: {e}")
			return None
		finally:
			
			conn.close()
            
	@staticmethod
	def get_task_by_id(housekeeping_id):
		conn = get_connection()
		if not conn:
			return None
            
		try:
			with conn.cursor(dictionally=True) as cursor:
			cursor.execute(
				"SELECT * FROM housekeeping_id = %s",(housekeeping,)
			)
			return cursor.fetchone()
		except Exception as e:
			print(f"Error fetching housekeeping task: {e}")
			return None
		finally:
			
			conn.close()
			
	@staticmethod
	def update_task(housekeeping_pid, cleaning_status=None, cleaning_date=None):
		conn = get_connection()
		if not conn:
			return False
		try:
			cursor = conn.cursor()
			fields = []
			values = []
			
			if cleaning_status is not None:
				fields.append("cleaning_status = %s")
				values.append(cleaning_status)
			if cleaning_date is not None:
				fields.append("cleaning_date = %s")
				values.append(cleaning_date)
				
			if not fields:
				return False 
			
            fields.append("update_at = CURRENT_TIMESTAMP")
			values.append(housekeeping_id)
			sql = """
				UPDATE housekeepings
				SET {', '.join(fields)}, updated_at = CURRENT_TIMESTAMP
				WHERE housekeeping_id = %s
			"""
			cursor.execute(sql, values)
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f"Error updating husekeeping task: {e}")
			return False 
		finally: 
			conn.close()
			
	@staticmethod
	def delete_task(housekeeping_id):
		conn = get_connection()
		if not conn:
			return False
		
		try:
			with conn.cursor() as cursor:
			cursor.execute("DELETE FROM housekeepings WHERE housekeeping_id = %s", (housekeepig_id,))
			conn.commit()
			return cursor.rowcount > 0 
		except Exception as e:
			print(f"Error deleting housekeeping task: {e}")
			return False
		finally:
			conn.close()
			
	@staticmethod
	def list_tasks_by_room(room_id):
		conn = get_connection()
		if not conn:
			return []
			
		try:
			cursor = conn.cursor(dictionary=True)
			cursor.execute("SELECT * FROM housekeepings WHERE room_id = %s", (room_id,))
			return cursor.fetchall()
		except Exception as e:
			print(f"Error listing housekeeping tasks: {e}")
			return []
		finally:
			conn.close()
	
	@staticmethod
	def list_task_by_staff(staff_id):
		conn = get_connection()
		if not conn:
			return []
			
		try:
			with conn.cursor(dictionary=True) as cursor:
			cursor.execute("SELECT * FROM housekeepigs WHERE staff_id = %s", (staff_id,))
			return cursor.fetchall()
		except Exception as e:
			print(f"Error listing housekeeings WHERE staff_id = %s", (staff_id,))
			return []
		finally:
			
			conn.close()
			
			
				