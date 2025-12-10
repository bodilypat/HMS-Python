/*  src/pages/booking/bookingList.js */

import React, { useEffect, useState } from 'react';
import bookingService from '../../services/bookingService';
import './BookingList.css'; /* Optional CSS for styling */

const BookingList = () => {
	const [bookings, setBookings] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);
	
	useEffect(() => {
		const fetchBookings = async () => {
			try {
				const response = await bookingService.getAllBooking();
				setBookings(response.data);
			} catch (err) {
				setError('Failed to fetch bookings.');
				console.error(err);
			} finally {
				setLoading(false);
			}
		};
		fetchBookings();
	}, []);
	
	if (loading) return <p>Loading bookings...</p>;
	if (error) return <p className="error">{error}</p>;
	
	return (
		<div className="booking-list-container">
			<h2>Reservations</h2>
				{bookings.length === 0 ? (
					<p>No bookings found.</p>
				) : (
					<table className="booking-table">
						<thead>
							<tr>
								<th>Guest Name</th>
								<th>Room</th>
								<th>Check-In</th>
								<th>Check-Out</th>
								<th>Status</th>
								<th>Payment</th>
							</tr>
						</thead>
						<tbody>
							{bookings.map((booking) => (
								<tr key={booking.reservation_id}>
									<td>{booking.guest_name || 'N/A'}</td>
									<td>{booking.room_number || 'N/A'}</td>
									<td>{booking.check_in}</td>
									<td>{booking.check_out}</td>
									<td>{booking.reservation_status}</td>
									<td>{booking.payment_status}</td>
								</tr>
							))}
						</tbody>
					</table>
				)}
		</div>
	);
};
export default BookingList;
