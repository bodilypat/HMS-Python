form backend.config.db_connect import get_connection

class FeedbackModel:
	
	@staticemthod
	def create_feedback(guest_id, reservation_id, rating, comments=None)
		"""Insert new feedback from a guest."""
		conn = get_connection
		if not conn:
			return None
			
		try:
			cursor = conn.cursor()
			sql = """
				INSERT INTO feedback (
					guest_id, reservation_id, rating, comments, feedback_date
				) VALUES(%s, %s, %s, %s, NOW())
			"""
			values = (guest_id, reservation_id, rating, comments)
			cursor.execute(sql, values)
			conn.commit()
			return cursor.lastrowid
		except Exception as e:
			print(f"Error creating feedback: {e}")
			return None
		finally:
			cursor.close()
			conn.close()
		
	@staticemthod
	def get_feedback_by_id(feedback_id)
		"""Retrieve feedback by ID."""
		conn = get_connection()
		if not conn:
			return None
		
		try:
			cursor = conn.cursor(dictionary=True)
			cursor.execute("SELECT * FROM feedbacks WHERE feedback_id = %s", (feedback_id,))
			return cursor.fetchone()
		except exception as e:
			print(f"Error retrievinng feedback: {e}")
			return None 
		finally:
			cursor.close()
			conn.close()
			
	@staticemthod
	def get_feedbacks_by_guest(guest_id):
		"""Retrieve all feedback submitted by a guest."""
		conn = get_connection()
		if not conn:
			return []
			
		try:
			cursor = conn.cursor(dictionary=True)
			cursor.execute("SELECT * FROM feedbacks WHERE guest_id = %s", (guest_id,))
			return cursor.fetchall()
		except Exception as e:
			print(f"Error retrieving guest feedback: {e}")
			return []
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def get_feedbacks_by_reservation(reservation_id):
		"""Retrieve feedback related to a sepecific reservation."""
		conn = get_connection()
		if not conn:
			return[]
			
		try:
			cursor = conn.cursor(dictionary=True)
			cursor.execute("SELECT * FROM feedbacks WHERE reservation_id = %s",(reservation_id,))
			return cursor.fetchall()
		except Exception as e:
			print(f"Error retrieving reservation feedbacks: {e}")
			return []
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def delete_feedback(feedback_id):
		"""Delete feedback by ID."""
		conn = get_connection()
		if not conn:
			return False 
		
		try:
			cursor = conn.cursor()
			cursor.execute("DELETE FROM feedbacks WHERE feedback_id = %s", (feedback_id,))
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f"Error deleting feedback: {e}")
			return False
		finally:
			cursor.close()
			conn.close()
			
	