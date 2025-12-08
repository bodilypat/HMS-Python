//src/services/paymentService.js 

import { paymentApi } from '../api/paymentApi';

/* Helpers */

/* Validate required parameters */
const requireParam = (value, name) => {
    if (!value) throw new Error(`${name} is required`);
};

/* Standardized service error wrapper */
const handleServiceError = (action, error) => {
    console.error(`paymentService: Error during ${action}:`, error?.response);
    throw error;
};

/* Normalize payment transaction payload */
const formatPaymentTransaction = (transaction) => {
    return {
        id: transaction.id,
        amount: transaction.amount,
        currency: transaction.currency,
        status: transaction.status,
        timestamp: transaction.timestamp
    };
};

/* Format List */
const formatPaymentTransactions = (transactions) => {
    return transactions.map(formatPaymentTransaction);
};

/* Payment Service (business logic) */
const paymentService = {
    /* Initiate a payment (with retry logic hook) */
    async initiatePayment(paymentData) {
        requireParam(paymentData, 'Payment data');
        try {
            const { data } = await paymentApi.initiatePayment(paymentData);
            return formatPaymentTransaction(data);
        } catch (error) {
            handleServiceError('initiating payment', error);
        }
    },

    /* Verify a payment status */
    async verifyPayment(paymentId) {
        requireParam(paymentId, 'Payment ID');
        try {
            const { data } = await paymentApi.verifyPayment(paymentId);
            return formatPaymentTransaction(data);
        } catch (error) {
            handleServiceError('verifying payment', error);
        }
    },

    /* Process refund */
    async refundPayment(paymentId, amount) {
        requireParam(paymentId, 'Payment ID');
        requireParam(amount, 'Refund amount');

        try {
            const { data } = await paymentApi.refundPayment(paymentId, amount);
            return formatPaymentTransaction(data);
        } catch (error) {
            handleServiceError('refunding payment', error);
        }
    },

    /* Get full payment transaction history for a booking */
    async getPaymentHistory(bookingId) {
        requireParam(bookingId, 'Booking ID');

        try {
            const { data } = await paymentApi.getPaymentHistory(bookingId);
            return formatPaymentTransactions(data);
        } catch (error) {
            handleServiceError('fetching payment history', error);
        }
    },
};
