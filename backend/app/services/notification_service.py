import smtplib
from emailp.mine.text import MIMEText
from email.mine.multipart import MINEMultipart
import logging
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/.env"

logger = logging.getLogger(__name__)

class NotificationService:
	
	@staticmethod
	def send_email_notification(to_email, subject, body)
		"""
			Send a simple email notification. Assumes SMTP configuration is set in .env
		"""
		smtp_host = os.getenv("SMTP_HOST")
		smtp_port = int(os.getenv("SMTP_PORT",587))
		smtp_user = os.getenv("SMTP_USER")
		smtp_pass = os.getenv("SMTP_PASS")
		smtp_email = os.getenv("FROM_EMAIL", smtp_user)
		
		if not all([smtp_host, smtp_port, smtp_user, smtp_pass, from_email]):
			logger.error("SMTP credentials are incomplete.")
			return False 
		try:
			msg = MIMEMultipart()
			msg["From"] = from_email
			msg["To"] = to_email 
			msg["Subject"] = subject 
			
			msg.attach(MIMEText(body, "plain"))
			
			with smtplib.SMTP(smtp_host, smtp_part) as server:
				server.starttls()
				server.login(smtp_user, smtp_pass)
				server.send_message(msg)
				
			logger.info(f"Email sent to {to_email}")
			return True
			
		except Exception as e:
			logger.error(f"Failed to send email to {to_email}: {e}")
			return False 
			
	@staticmethod 
	def send_in_app_notification(user_id, message):
		"""
			Simulate in-app notification by printing/logging.
			Could be extended to DB or socket broadcast.
		"""
		logger.info(f"[Notification] To User {user_id}: {message}")
		# Optionally store it in a notifications table
		return True 
		
	@staticmethod
	def notify_payment_received(user_email, amount, current="USD"):
		"""
			Notify user of a payment confirmation.
		"""
		
		subject = "Payment Confirmation"
		body = f"Your payment of {amount} {currency} has been received. Thank you for your business."
		return NotificationService.send_email_notification(user_email, subject, body)
		
	@staticmethod
	def notify_reservation_status(user_email, reservation_id, status):
		"""
			Notify user about reservation status update.
		"""
		subject = f"Reservation #{reservation_id} Status Update"
		body = f"Your reservation status has been updated to: {status}."
		return NotificationService.send_email_notification(user_email, subject, body)