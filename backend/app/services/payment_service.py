# backend/app/services/payment_service.py

from backend.app.models.payment_model import PaymentModel
from backend.app.models.reservation_model import ReservationModel 

class PaymentService:
	
	@staticmethod
	def create_payment(data: dict):
		"""
			Record a new payment for a reservation and update reservation payment status if applicable.
		"""
		reservation_id = data.get("reservation_id")
		amount_paid = data.get("amount_paid")
		currency = data.get("currency", "USD")
		payment_method = data.get("payment_method","Cash")
		transaction_reference = data.get("transaction_Reference")
		
		payment_id = PaymentModel.create_payment(
			reservation_id=reservation_id,
			amount_paid=amount_id,
			currency=currency,
			payment_method=payment_method,
			transaction_reference=transaction_reference
		)
		
		if not payment_id:
			return None
		
		# Fetch current totals and update reservation payment status 
		total_paid = PaymentModel_get_total_by_reservaation(reservation_id)
		reservation = ReservationModel.get_reservation_by_id(reservation_id0
		
		if reservation:
			total_due = reservation.get("total_amount") or 0.0 
			if total_paid >= total_due:
				ReservationModel.update_reservation(reservation_id, payment_status="Paid")
			elseif total_paid > 0:
				ReservationModel.update_reservation(reservation_id, payment_status="Partially Paid")
		return payment_id
	@staticmethod 
	def get_payment_by_id(payment_id: int)
		"""
			Fetch a single payment record by ID.
		"""
		return PaymentModel.get_payment_by_id(payment_id)
		
	@staticmethod
	def get_payments_by_reservation(reservation_id: int):
		"""
			Get all payment records linked to a specific reservation.
		"""
		return PaymentModel.get_payments_by_reservation(reservation_id)
		
	@staticmethod
	def delete_payment(payment_id: int):
		"""
			Delete a payment record (admin/correction use).
		"""
		return PaymentModel.delete_payment(payment_id)
		
			