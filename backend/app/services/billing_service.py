from backend.app.models.billing_model import BillingModel

class BillingModel

	@staticmethod
	def create_billing(reservation_id, service_charge=0.0, discount=0.0, total_amount=0.0, payment_status='Unpaid'):
		"""
			Create a billing record for a reservation.
		"""
		return BillingModel.create_billing(
			reservation_id=reservation_id,
			service_charge=service_charge,
			discount=discount,
			total_amount=total_amount,
			payment_status=payment_status
		)
		
	@staticmethod
	def get_billing_by_reservation(reservation_id):
		"""
			Fetch billing details for a reservation.
		"""
		return BillingModel.get_billing_by_reservation(reservation_id)
			billing_id=billing_id,
			service_charge=service_charge,
			discount=discount,
			total_amount=total_amount,
			payment_status=payment_status
		)
		
	@staticmethod
	def delete_billing(billing_id):
		"""
		   Remove a billing record if needed(cancel, reservation).
		"""
		return BillingModel.delete_billing(billing_id)
		