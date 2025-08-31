/* src/services/bookingService.js */
import api from './api';

const bookingService = {
	getAllBooking: () => api.get('/bookings'),
	getBookingById: (id) => api.get('/bookings/${id}'),
	createBooking: (data) => api.post('/bookings', data),
	updateBooking: (id, data) => api.put('/bookings/${id}', data),
	deleteBooking: (id) => api.delete('/bookings/${id}'),
};
export default bookingService;
