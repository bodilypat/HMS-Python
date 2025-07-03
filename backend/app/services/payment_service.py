from backend.app.models.payment_model import PaymentModel
from backend.app.models.reservation_model import ReservationModel 

class PaymentModel
	
	@staticmethod
	def record_payment(reservation_id, amount_paid, current='USD', payment_method='Cash', transaction_reference=None):
		"""
			Record a new payment for a reservation and update the reservation payment status if needed.
		"""
		payment_id = PaymentModel.create_payment(
			reservation_id=reservation_id,
			amount_paid=amoun_paid,
			currency=currency,
			payment_method=payment_method,
			transaction_reference=transaction_reference
		)
		
		if not payment_id:
			return None
			
		total_paid = PaymentModel.get_total_by_reservation(reservation_id)
		reservation = ReservationModel.get_reservation_by_id(reservation_id)
		
		if reservation:
			total_due = reservation.get("toal_amount") or 0.0
			if total_paid >= total_due:
				ReservationModel.update_reservation(reservation_id, payment_status="Paid")
			elif total_paid > 0:
				ReservationModel.update_reservation(reservation_id, payment_status="Partially Paid")
				
		return payment_id
	
	@staticmethod
	def get_payments_by_reservation(reservation_id):
		"""
			Fetch a single payment record.
		"""
		return PaymentModel.get_payment_by_id(payment_id)
	
	@staticmethod
	def delete_payment(payment_id):
		"""
			Delete a payment record (admin, correction).
		"""
		return PaymentModel.delete_payment(payment_id)
		
		