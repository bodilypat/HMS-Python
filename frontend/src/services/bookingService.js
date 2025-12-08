/* src/services/bookingService.js */
import api from './api';

/**
 * Helper to normalize and rethrow API errors.
 * Attaches response.status and response.data when available.
 */
function formatError(err) {
	if (err && err.response) {
		const { status, data } = err.response;
		const message = (data && data.message) || err.message || 'API Error';
		const error = new Error(message);
		error.status = status;
		error.data = data;
		throw error;
	}
	throw err;
}

const bookingService = {
	/** Get all bookings -> returns response.data */
	getAllBookings: async () => {
		try {
			const res = await api.get('/bookings');
			return res.data;
		} catch (err) {
			formatError(err);
		}
	},

	/** Get a single booking by id */
	getBookingById: async (id) => {
		try {
			const res = await api.get(`/bookings/${id}`);
			return res.data;
		} catch (err) {
			formatError(err);
		}
	},

	/** Create a new booking */
	createBooking: async (data) => {
		try {
			const res = await api.post('/bookings', data);
			return res.data;
		} catch (err) {
			formatError(err);
		}
	},

	/** Update an existing booking by id */
	updateBooking: async (id, data) => {
		try {
			const res = await api.put(`/bookings/${id}`, data);
			return res.data;
		} catch (err) {
			formatError(err);
		}
	},

	/** Delete a booking by id */
	deleteBooking: async (id) => {
		try {
			const res = await api.delete(`/bookings/${id}`);
			return res.data;
		} catch (err) {
			formatError(err);
		}
	},
};

export default bookingService;
