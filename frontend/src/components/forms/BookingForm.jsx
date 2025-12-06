//src/components/forms/BookingForm.jsx 

import React, { useState, useEffect } from 'react';
import { Input, Button, Select, DatePicker, InputNumber, message } from '../../components/ui';
import bookingService from '../../services/bookingService';

const BookingForm = ({ booking = null, onSuccess }) => {
    const [reservationId, setReservationId] = useState(booking ? booking.reservation_id : null);
    const [staffId, setStaffId] = useState(booking ? booking.staff_id : null);
    const [customerId, setCustomerId] = useState(booking ? booking.customer_id : null);
    const [roomId, setRoomId] = useState(booking ? booking.room_id : null);
    const [checkInDate, setCheckInDate] = useState(booking ? booking.check_in_date : '');
    const [checkOutDate, setCheckOutDate] = useState(booking ? booking.check_out_date : '');
    const [guestCount, setGuestCount] = useState(booking ? booking.guest_count : 1);
    const [status, setStatus] = useState(booking ? booking.status : 'Booked');
    const [bookingSource, setBookingSource] = useState(booking ? booking.booking_source : 'Online');
    const [totalAmount, setTotalAmount] = useState(booking ? booking.total_amount : 0.0);
    const [notes, setNotes] = useState(booking ? booking.notes || '' : '');
    const [errors, setErrors] = useState({});
    const validate = () => {
        const e = {};
        if (!staffId) e.staffId = 'Staff ID is required';
        if (!customerId) e.customerId = 'Customer ID is required';
        if (!roomId) e.roomId = 'Room ID is required';
        if (!checkInDate) e.checkInDate = 'Check-in date is required';
        if (!checkOutDate) e.checkOutDate = 'Check-out date is required';
        if (new Date(checkInDate) >= new Date(checkOutDate)) e.dateRange = 'Check-out date must be after check-in date';
        if (!Number.isInteger(Number(guestCount)) || Number(guestCount) <= 0) e.guestCount = 'Guest count must be an integer > 0';
        if (totalAmount === '' || Number(totalAmount) < 0) e.totalAmount = 'Total amount must be 0 or greater';
        setErrors(e);
        return Object.keys(e).length === 0;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!validate()) return;
        const bookingData = {
            reservation_id: reservationId ? Number(reservationId) : null,
            staff_id: Number(staffId),
            customer_id: Number(customerId),
            room_id: Number(roomId),
            check_in_date: checkInDate,
            check_out_date: checkOutDate,
            guest_count: Number(guestCount),
            status,
            booking_source: bookingSource,
            total_amount: Number(totalAmount),
            notes,
        };
        try {
            if (booking && booking.booking_id) {
                await bookingService.updateBooking(booking.booking_id, bookingData);    
            } else {
                await bookingService.createBooking(bookingData);
            }
            message.success('Booking saved successfully');
            onSuccess();
        } catch (error) {
            console.error('Error saving booking:', error);
            message.error('Error saving booking: ' + (error.message || 'Save failed'));
        }
    };  
    return (
        <form onSubmit={handleSubmit}>
            <Input  
                label="Staff ID"
                value={staffId}
                onChange={(e) => setStaffId(e.target.value)}
                error={errors.staffId}
            />
            <Input
                label="Customer ID"
                value={customerId}
                onChange={(e) => setCustomerId(e.target.value)}
                error={errors.customerId}
            />
            <Input
                label="Room ID"
                value={roomId}
                onChange={(e) => setRoomId(e.target.value)}
                error={errors.roomId}
            />
            <DatePicker
                label="Check-In Date"
                value={checkInDate}
                onChange={(date) => setCheckInDate(date)}
                error={errors.checkInDate}
            />
            <DatePicker
                label="Check-Out Date"
                value={checkOutDate}
                onChange={(date) => setCheckOutDate(date)}
                error={errors.checkOutDate || errors.dateRange}
            />
            <InputNumber
                label="Guest Count"
                value={guestCount}
                onChange={(value) => setGuestCount(value)}
                error={errors.guestCount}
            />
            <Select
                label="Status"
                value={status}  
                onChange={(value) => setStatus(value)}
                options={[
                    'Booked','CheckedIn','CheckedOut','Cancelled','NoShow'  
                ].map((s) => ({ label: s, value: s }))}
            />
            <Select
                label="Booking Source"
                value={bookingSource}  
                onChange={(value) => setBookingSource(value)}
                options={[
                    'Online','Phone','WalkIn','TravelAgent','Corporate'  
                ].map((s) => ({ label: s, value: s }))}
            />
            <InputNumber
                label="Total Amount"
                value={totalAmount}
                onChange={(value) => setTotalAmount(value)}
                error={errors.totalAmount}
            />
            <Input
                label="Notes"
                value={notes}
                onChange={(e) => setNotes(e.target.value)}
                error={errors.notes}
            />
            {errors.submit && <div className="error">{errors.submit}</div>}
            <Button type="submit">Save Booking</Button>
        </form>
    );
}
