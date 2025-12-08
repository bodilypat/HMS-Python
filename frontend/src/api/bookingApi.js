//src/api/bookingApi.js 

import axiosClient from './axiosClient';

/* standard error handler */
function handleApiError(action: string, error: any) {
    console.error(`Error ${action}:`, error);
    throw error;
}
const bookingApi = {
    /* Fetch all bookings */
    async fetchBookings() {
        try {
            const response = await axiosClient.get('/bookings');
            return response.data;
        } catch (error) {
            handleApiError('fetching bookings', error);
        }   
    },

    /* Fetch booking by ID */
    async fetchBookingById(bookingId: string) {
        try {
            const response = await axiosClient.get(`/bookings/${bookingId}`);
            return response.data;
        } catch (error) {
            handleApiError(`fetching booking with ID ${bookingId}`, error);
        }   
    },

    /* Create a new booking */
    async createBooking(bookingData: any) {
        try {
            const response = await axiosClient.post('/bookings', bookingData);
            return response.data;
        } catch (error) {
            handleApiError('creating booking', error);
        }
    },

    /* Update an existing booking */
    async updateBooking(bookingId: string, bookingData: any) {
        try {
            const response = await axiosClient.put(`/bookings/${bookingId}`, bookingData);
            return response.data;
        } catch (error) {
            handleApiError(`updating booking with ID ${bookingId}`, error);
        }   
    },

    /* Delete a booking */
    async deleteBooking(bookingId: string) {
        try {   
            const response = await axiosClient.delete(`/bookings/${bookingId}`);
            return response.data;
        } catch (error) {
            handleApiError(`deleting booking with ID ${bookingId}`, error);
        }   
    },

};
export default bookingApi;
