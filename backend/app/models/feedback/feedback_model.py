# backend/app/models/feedback/feedback_model.py

from backend.config.db_connect import get_connection

class FeedbackModel:
	@staticmethod
	def create_feedback(guest_id, reservation_id, rating, comment=None):
		"""Insert new feedback from a guest."""
		conn = get_connection()
		if not conn:
			return None 
			
		try:
			with conn.cursor() as cursor:
			sql = """
				INSERT INTO feedback (
					guest_id, reservation_id, rating, comment, feedback_date
					) VALUES(%s, %s, %s, %s, NOW())
                """
				values = (guest_id, reservation_id, rating, comment)
				cursor.execute(sql,values)
				conn.commit()
				return cursor.lastrowid
			except Exception as e:
			print(f"[Error] creating feedback: {e}")
			return None
		finally:
			conn.close()
			
	@staticmethod
	def get_feedback_by_id(feedback_id):
		"""Retrieve feedback by ID."""
		conn = get_connection()
		if not conn:
			return None 
			
		try:
			with conn.cursor(dictionary=True) as cursor:
			cursor.execute("SELECT * FROM feedback WHERE feedback_id = %s", (feedback_id,))
			return cursor.fetchone()
		except Exception as e:
			print(f"Error retrieving feedback: {e}")
			return None 
		finally:
			conn.close()
			
	@staticmethod
	def get_feedback_by_guest(guest_id):
		"""Retrieve all feedback submitted by a guest."""
		conn = get_connection()
		if not conn:
			return []
			
		try:
			with conn.cursor(dictionary=True) as cursor:
			cursor.execute("SELECT * FROM feedback WHERE guest_id = %s", (guest_id,))
			return cursor.fetchall()
		except Exception as e:
			print(f"Error retrieving guest feedback: {e})
			return [[]
		finally:
			conn.close()
			
	@staticmethod
    def get_feedback_by_reservation(reservation_id):
        """Retrieve feedback related to a specific reservation."""
        conn = get_connection()
        if not conn:
            return []
            
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM feedback WHERE reservation_id = %s", (reservation_id,))
                return cursor.fetchall()
        except Exception as e:
            print(f"Error retrieving reservation feedback: {e}")
            return []
        finally:
            conn.close()
            
    @staticmethod 
    def delete_feedback(feedback_id):
        """Delete feedback by ID."""
        conn = get_connection()
        if not conn:
            return False 
            
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM feedback WHERE feedback_id = %s",(feedback,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error deleting feedback: {e}")
            return False 
        finally: 
            conn.close()
