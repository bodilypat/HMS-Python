# backend/app/models/BillingModel.py

from backend.config.db_connect import get_connection
from typing import Optional, Dict, Any

class BillingModel:

	@staticmethod
	def create_billing( 
            reservation_id, 
            service_charge=0.00, 
            discount=0.00, 
            total_amount=0.00, 
            payment_status='Unpaid')
        ) -> Optional[int]:
                    
		"""
            Insert a new billing record.
        """
		conn = get_connection()
		if not conn:
			return None
			
		try:
			cursor = conn.cursor()
			sql = """
				    INSERT INTO billings ( reservation_id, service_charge, discount, total_amount, payment_status )
				    VALUES (%s, %s, %s, %s, %s)
			     """
			values = (reservation_id, service_charge, discount, total_amount, payment_status )
			cursor.execute(sql, values)
			conn.commit()
			return cursor.lastrowid
		except Exception as e:
			print(f "[Error] Creating billing: {e}")
			return None
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def get_billing_by_reservation(reservation_id: int) -> Optional[Dict[str, Any]]:
		"""
            Fetch billing info for a reservation.
        """
		conn = get_connection()
		if not conn:
			return None
			
		try:
			cursor = conn.cursor(dictionary=True)
			cursor.execute("SELECT * FROM billings WHERE reservation_id = %s", (reservation_id,))
			return cursor.fetchone()
		except Exception as e:
			print(f"[Error] Fetching billing: {e}")
			return None
		finally:
			cursor.close()
			conn.close()
			
	@staticmethod
	def update_billing(
            billing_id: int, 
            service_charge: Optional[float] =None,
            discount: Optional[float] = None,
            total_amount: Optional[float] = None, 
            payment_status: Optional[str] = None
        ) -> bool:
                
		"""
            Update billing information selectively.
        """
		conn = get_connection()
		if not conn:
			return False
			
		try:
			cursor = conn.cursor()
			fields = []
			values = []
			
			if service_charge is not None:
				fields.append("service_charge = %s")
				values.append(service_charge)
			if discount is not None:
				fields.append("discount = %s")
				values.append(discount)
			if total_amount is not None:
				fields.append("total_amount = %s")
				values.append(total_amount)
			if payment.status is not None:
				fields.append("payment_status = %s")
				values.append(payment_status)
				
			if not fields:
				return False # Noting to update_ 
				
				sql = f"UPDATE billings SET{', '.join(fields)} WHERE billing_id = %s"
				values.append(billing_id)
				
				cursor.execute(sql, tuple(values))
				conn.commit()
				return cursor.rowcount > 0
			except exception as e:
				print(f"[Error] updating billing: {e}")
				return False
			finally:
				cursor.close()
				conn.close()
				
	@staticmethod
	def delete_billing(billing_id: int) -> bool:
		"""Delete a billing record"""
		conn = get_connection()
		if not conn:
			return False
		try:
			cursor = conn.cursor()
			cursor.execute("DELETE FROM billings WHERE billings = %s", (billing_id,))
			conn.commit()
			return cursor.rowcount > 0
		except Exception as e:
			print(f"Error deleting billing: {e}")
			return False
		finally:
			cursor.close()
			conn.close()
			
	