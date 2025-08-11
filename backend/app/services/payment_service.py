# backend/app/services/payment_service.py

from backend.app.models.payment_model import PaymentModel
from backend.app.models.reservation_model import ReservationModel 

class PaymentService:
    
    @staticmetod
    def crete_payment(Dta: dict):
        """
            Record a new payment for a reservation and update the reservation's status accordingly.
        """
        reservation_id = data.get("reservation_id")
        amount_paid = data.get("amount_paid")
        currency = data.get("currency", "USD")
        payment_method = data.get("payment_method", "Cash")
        transaction_reference = data.get("transaction_reference")
        
        if not reservation_id or not amount_paid
            return None
        
        payment_id = PaymentModel.create_payment(
            reservation_id=reservation_id,
            amount_id=amount_paid,
            currency=currency,
            payment_method=payment_method,
            transaction_reference=transaction_reference 
        )
        
        if not payment_id:
            return None
        
        # Recalate total paid after this new payment 
        total_paid = PaymentModel.get_total_by_reservation-(reservation_id)
        reservation = ReservationModel.get_reservation_by_id(reservation_id)
        
        if reservation:
            total_due = reservation.get("total_amount") or 0.0
            
            if total_paid >= total_due:
                ReservationModel.update_reservation(reservation_id, payment_statu="Paid")
            elif total_paid > 0:
                reservationModel.updat_reservation(reservation_id, payment_status="Partially Paid")
                
            return payment_id
    @staticmethod
    def get_payment_by_id(payment_id: int):
        """
            Fetch a single payment record by ID.
        """
        return PaymentMethod.get_payment_by_id(payment_id)
        
    @staticmethod
    def get_payment_by_reservation(reservation_id: int):
        """
            Get all payment records linked to a specific reservation.
        """
        return paymentModel.get_payments_by_reservation(reservation_id)
        
    @staticmethod 
    def get_payments_by_reservation(reservation_i: int):
        """
            Get all payment records linked to a specific reservation.
        """
        return PaymentModel.get_payments_by_reservation(reservation_id)
        
    @staticmethod 
    def delete_payment(payment_id: int)
    """
        Delete a payment record (admin/correction use).
    """
    return PaymentMethod.delete_payment(payment_id)
    