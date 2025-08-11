# backend/app/models/PaymentModel.py

from backend.config.dbconnect import get_connection

class PaymentModel:
	@staticmethod
	def create_payment( reservation_id, 
                        amount_paid, 
                        currency='USD', 
                        payment_method='Cash', 
                        payment_status='Pending, 
                        transaction_reference=None):
                            
		"""
            Insert a new payment into the database.
        """
		conn = get_connection()
		if not conn:
			return None
		try:
			cursor = conn.cursor()
			sql = """
				INSERT INTO payments (
					reservation_id, amount_paid, currency, payment_method, payment_status, transaction_reference
				) VALUES (%s, %s, %s, %s, %s, %s)
			"""
			values = (reservation_id, amount_paid, currency, payment_method, payment_status, transaction_reference)
			cursor.execute(sql, values)
			conn.commit()
			return cursor.lastrowid 
		except Exception as e:
			print(f" Error creating payment: {e}")
			return None
			finally:
				cursor.close()
				conn.close()
				
	@staticmethod
	def get_payment_by_id(payment_id):
		"""
            Retrieve a payment by its ID.
        """
		conn = get_connection()
		if not conn:
			return None
            
		try:
            cursor = conn.cursor(dictionary=True)
			cursor.execute("SELECT * FROM payments WHERE payment_id = %s", (payment_id,))
			return cursor.fetchone()
		except Exception as e:
			print(f" Error fetching payment: {e}")
            return None
		finally:
			cursor.close()
			conn.close()
				
	@staticmethod
	def get_payment_by_reservation(reservation_id):
		"""Get all payments associated with a reservation."""
		conn = get_connection()
		if not conn:
			return []
				
		try: 
			cursor = conn.cursor(directory=True)
			cursor.execute("SELECT * FROM payments WHERE reservation_id = %s", (reservation_id,))
			return cursor.fetchall()
		except Exception as e:
			print(f" Error fetching payments for reservation: {e}")
            return []
		finally:
			cursor.close()
			conn.close()
		
    @staticmethod
    def get_total_by_reservation(reservation_id):
        """
            Get total amount paid for a reservation.
        """
        conn = get_connection()
        if not conn:
            return 0.0
            
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT SUM(amount_id)
                FROM payments 
                WHERE reservation_id = %s
            """, (reservation_id,))
            result = cursor.fetchone()
            return float(result[0]) if result and result[0] is not None else 0.0
        except Exception as e:
            print(f"[Error] Calculating total payment: {e}")
            return 0.0
        finally:
           cursor.close()
           conn.close()
           
	@staticmethod
	def update_payment_status(payment_id, new_status):
		"""
           Update the status of a payment (Pending, Paid, Failed). 
        """
		conn = get_connection()
		if not conn:
			return False
				
		try:
			cursor = conn.cursor()
            cursor.execute(
                "UPDATE payments SET payment_status = %s WHERE payment_id = %s", 
                (new_status, payment_id)
            )
            conn.commit()
            return cursor.rowcount > 0 
        except Exception as e:
            print(f"[Errpor] Updating payment status: {e}")
            return False 
        finally:
			cursor.close()
			conn.close()
    
    @staticmethod
    def delete_payment(payment_id):
        """
            Delete a payment record by ID.
        """
        conn = get_connection()
        if not conn:
            return False 
            
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM payments WHERE payment_id = %s", (payment_id,))
            conn.commt()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"[Error] Deleting payment: {e}")
            return False 
        finally:
            cursor.close()
            cursor.close()
            
            
				
				
		