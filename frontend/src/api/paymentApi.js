//src/api/paymentApi.js 

import axiosClient from './axiosClient';

/* standard error handler */
function handleApiError(action: string, error: any) {
    console.error(`Error ${action}:`, error);
    throw error;
}

const paymentApi = {
    /* Fetch all payments */
    async fetchPayments() {
        try {
            const response = await axiosClient.get('/payments');
            return response.data;
        } catch (error) {
            handleApiError('fetching payments', error);
        }
    },

    /* Fetch payment by ID */
    async fetchPaymentById(paymentId: string) {
        try {
            const response = await axiosClient.get(`/payments/${paymentId}`);
            return response.data;
        } catch (error) {
            handleApiError(`fetching payment with ID ${paymentId}`, error);
        }
    },

    /* Create a new payment */
    async createPayment(paymentData: any) {
        try {
            const response = await axiosClient.post('/payments', paymentData);
            return response.data;
        } catch (error) {
            handleApiError('creating payment', error);
        }
    },

    /* Update an existing payment */
    async updatePayment(paymentId: string, paymentData: any) {
        try {
            const response = await axiosClient.put(`/payments/${paymentId}`, paymentData);
            return response.data;
        } catch (error) {
            handleApiError(`updating payment with ID ${paymentId}`, error);
        }
    },

    /* Delete a payment */
    async deletePayment(paymentId: string) {
        try {
            const response = await axiosClient.delete(`/payments/${paymentId}`);
            return response.data;
        } catch (error) {
            handleApiError(`deleting payment with ID ${paymentId}`, error);
        }
    },
};

