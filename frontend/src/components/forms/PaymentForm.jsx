//src/components/forms/PaymentForm.jsx 

import React, { useState, useEffect } from 'react';
import paymentService from '../../services/paymentService';
import { Input, Button, Select, DatePicker, InputNumber, message } from '../../components/ui';

const PaymentForm = ({ payment = null, onSuccess }) => {
    const [reservationId, setReservationId] = useState(payment ? payment.reservation_id : null);
    const [amountPaid, setAmountPaid] = useState(payment ? payment.amount_paid : 0.0);
    const [currency, setCurrency] = useState(payment ? payment.currency : 'USD');
    const [exchangeRate, setExchangeRate] = useState(payment ? payment.exchange_rate : 1.0);
    const [paymentMethod, setPaymentMethod] = useState(payment ? payment.payment_method : 'Cash');
    const [paymentStatus, setPaymentStatus] = useState(payment ? payment.payment_status : 'Pending');
    const [transactionReference, setTransactionReference] = useState(payment ? payment.transaction_reference || '' : '');
    const [paymentDate, setPaymentDate] = useState(payment ? payment.payment_date : '');
    const [notes, setNotes] = useState(payment ? payment.notes || '' : '');
    const [errors, setErrors] = useState({});
    const validate = () => {
        const e = {};
        if (!reservationId) e.reservationId = 'Reservation ID is required';
        if (amountPaid === '' || Number(amountPaid) < 0) e.amountPaid = 'Amount paid must be 0 or greater';
        if (exchangeRate === '' || Number(exchangeRate) <= 0) e.exchangeRate = 'Exchange rate must be greater than 0';
        if (!paymentDate) e.paymentDate = 'Payment date is required';
        setErrors(e);
        return Object.keys(e).length === 0;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!validate()) return;
        const paymentData = {
            reservation_id: Number(reservationId),
            amount_paid: Number(amountPaid),
            currency,
            exchange_rate: Number(exchangeRate),
            payment_method: paymentMethod,
            payment_status: paymentStatus,
            transaction_reference: transactionReference.trim(),
            payment_date: paymentDate,
            notes,
        };
        try {
            if (payment && payment.payment_id) {
                await paymentService.updatePayment(payment.payment_id, paymentData);
            } else {
                await paymentService.createPayment(paymentData);
            }
            message.success('Payment saved successfully');
            if (onSuccess) onSuccess();
        } catch (error) {
            message.error('Failed to save payment');
        }
    };
    return (
        <form onSubmit={handleSubmit}>
            <Input
                label="Reservation ID"
                value={reservationId || ''}
                onChange={(e) => setReservationId(e.target.value)}
                error={errors.reservationId}
            />
            <InputNumber
                label="Amount Paid"
                value={amountPaid}
                onChange={(value) => setAmountPaid(value)}
                error={errors.amountPaid}
            />
            <Input
                label="Currency"
                value={currency}
                onChange={(e) => setCurrency(e.target.value)}
                error={errors.currency}
            />
            <InputNumber
                label="Exchange Rate"
                value={exchangeRate}
                onChange={(value) => setExchangeRate(value)}
                error={errors.exchangeRate}
            />
            <Select
                label="Payment Method"
                value={paymentMethod}
                onChange={(value) => setPaymentMethod(value)}
                error={errors.paymentMethod}
                options={[
                    'Credit Card','Cash','Online Transfer','Other'
                ].map((method) => ({ label: method, value: method }))}
            />
            <Select
                label="Payment Status"
                value={paymentStatus}
                onChange={(value) => setPaymentStatus(value)}
                error={errors.paymentStatus}
                options={[
                    'Completed','Pending','Failed','Refunded'   
                ].map((status) => ({ label: status, value: status }))}
            />
            <Input
                label="Transaction Reference"
                value={transactionReference}
                onChange={(e) => setTransactionReference(e.target.value)}
                error={errors.transactionReference}
            />
            <DatePicker
                label="Payment Date"
                value={paymentDate}
                onChange={(date) => setPaymentDate(date)}
                error={errors.paymentDate}
            />
            <Input
                label="Notes"
                value={notes}
                onChange={(e) => setNotes(e.target.value)}
                error={errors.notes}
            />
            <Button type="submit">Save Payment</Button>
        </form>
    );
};
