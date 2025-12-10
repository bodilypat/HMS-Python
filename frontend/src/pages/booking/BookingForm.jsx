//src/pages/booking/BookingForm.jsx 

import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { Alert } from '../../components/Alert';

import Breadcrumbs from '../../components/Breadcrumbs';
import FormGroup from '../../components/FormGroup';
import Input from '../../components/Input';
import Select from '../../components/Select';
import DateInput from '../../components/DateInput';
import Textarea from '../../components/Textarea';
import ErrorMessage from '../../components/ErrorMessage';

import useFetch from '../../hooks/useFetch';
import useForm from '../../hooks/useForm';
import useAlert from '../../hooks/useAlert';

import { BookingService } from '../../services/BookingService';
import { RoomService } from '../../services/RoomService';
import { CustomerService } from '../../services/CustomerService';
import { formatDateForInput } from '../../utils/dateUtils';


const BookingForm = () => {
    const { id } = useParams();
    const navigate = useNavigate();

    const isEditMode = Boolean(id);

    /* FETCH BOOKING IF EDIT MODE */
    const { data: booking, error: bookingError, loading: bookingLoading } = useFetch(
        isEditMode ? () => BookingService.getBookingById(id) : null
    );
    /* FETCH DROPDOWNS DATA */
    const { data: rooms, error: roomsError, loading: roomsLoading } = useFetch(
        () => RoomService.getAllRooms()
    );
    const { data: guests, error: guestsError, loading: guestsLoading } = useFetch(
        () => CustomerService.getAllCustomers()
    );
    const { data: staff, error: staffError, loading: staffLoading } = useFetch(
        () => CustomerService.getAllStaff()
    );

    const [error, setError] = useState(null);

    const { form, setForm, handleChange } = useForm({
        reservationId: '',
        roomId: '',
        guestId: '',
        staffId: '',

        checkInDate: '',
        checkOutDate: '',
        guest_count: 1,

        total_amount: '',
        booking_source: '',
        notes: ''
    });

    useEffect(() => {
        if (booking) {
            setForm({   
                reservationId: booking.reservationId || '',
                roomId: booking.roomId || '',
                guestId: booking.guestId || '',
                staffId: booking.staffId || '',
                checkInDate: formatDateForInput(booking.checkInDate) || '',
                checkOutDate: formatDateForInput(booking.checkOutDate) || '',
                guest_count: booking.guest_count || 1,
                total_amount: booking.total_amount || '',
                booking_source: booking.booking_source || '',
                notes: booking.notes || ''
            });
        }
    }, [booking, setForm]);

    const { alert, showAlert } = useAlert();
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        try {
            if (isEditMode) {
                await BookingService.updateBooking(id, form);
                showAlert('Booking updated successfully', 'success');
            } else {
                await BookingService.createBooking(form);
                showAlert('Booking created successfully', 'success');
            }
            navigate('/bookings');
        } catch (err) {
            setError(err.message || 'An error occurred');
        }
    };

    if (bookingLoading || roomsLoading || guestsLoading || staffLoading) {
        return <div>Loading...</div>;
    }
    if (bookingError || roomsError || guestsError || staffError) {
        return <ErrorMessage message="Failed to load data." />;
    }

    return (
        <div className="booking-form-page">
            <Breadcrumbs
                items={[
                    { label: 'Dashboard', path: '/dashboard' },
                    { label: 'Bookings', path: '/bookings' },
                    { label: isEditMode ? 'Edit Booking' : 'New Booking' }  
                ]}
            />
            <div className="card-header">
                <h3>{isEditMode ? 'Edit Booking' : 'New Booking'}</h3>
            </div>
                <Card>
                    {error && <Alert type="error" message={error} />}
                    <form onSubmit={handleSubmit}>
                        /* Guest */
                        <FormGroup label="Guest" htmlFor="guestId" required>
                            <Select
                                id="guestId"
                                name="guestId"
                                value={form.guestId}
                                onChange={handleChange}
                                options={guests.map(guest => ({
                                    value: guest.id,
                                    label: `${guest.firstName} ${guest.lastName}`
                                }))}
                                placeholder="Select a guest"
                                required
                            />
                    </FormGroup>
                    /* Staff */
                    <FormGroup label="Staff" htmlFor="staffId" required>
                        <Select
                            id="staffId"
                            name="staffId"
                            value={form.staffId}
                            onChange={handleChange}
                            options={staff.map(staffMember => ({
                                value: staffMember.id,
                                label: `${staffMember.firstName} ${staffMember.lastName}`
                            }))}
                            placeholder="Select a staff member"
                            required
                        />
                    </FormGroup>
                    /* Room */
                    <FormGroup label="Room" htmlFor="roomId" required>
                        <Select
                            id="roomId"
                            name="roomId"
                            value={form.roomId}
                            onChange={handleChange}
                            options={rooms.map(room => ({
                                value: room.id,
                                label: `Room ${room.number} - ${room.type}`
                            }))}
                            placeholder="Select a room"
                            required
                        />
                    </FormGroup>
                    {/* Check-In Date */}
                    <FormGroup label="Check-In Date" htmlFor="checkInDate" required>
                        <div className="date-input-wrapper">
                            <FormGroup label="Check-In Date" htmlFor="checkInDate" required>
                                <DateInput
                                    id="checkInDate"
                                    name="checkInDate"
                                    value={form.checkInDate}
                                    onChange={handleChange}
                                    required
                                />
                                <ErrorMessage message={form.checkInDateError} />
                            </FormGroup>
                            <FormGroup label="Check-Out Date" htmlFor="checkOutDate" required>
                                <DateInput
                                    id="checkOutDate"
                                    name="checkOutDate"
                                    value={form.checkOutDate}
                                    onChange={handleChange}
                                    required
                                />
                                <ErrorMessage message={form.checkOutDateError} />
                            </FormGroup>
                        </div>
                        {/* Guest Count */}
                        <FormGroup label="Guest Count" htmlFor="guest_count" required>
                            <Input
                                type="number"
                                id="guest_count"
                                name="guest_count"
                                value={form.guest_count}
                                onChange={handleChange}
                                min="1"
                                required
                            />
                            <ErrorMessage name="guest_count" />
                        </FormGroup>
                        {/* Booking Source */}
                        <FormGroup label="Booking Source" htmlFor="booking_source" required>
                            <Select 
                                id="booking_source"
                                name="booking_source"
                                value={form.booking_source}
                                onChange={handleChange}
                                options={[
                                    "Online",
                                    "Phone",
                                    "WalkIn",
                                    "TravelAgent",
                                    "Corporate",
                                ].map(source => ({ value: source, label: source }))}
                            />
                            <ErrorMessage name="booking_source" />
                        </FormGroup>
                        {/* Total Price */}
                        <FormGroup label="Total Price" htmlFor="total_amount" required>
                            <Input
                                type="number"
                                id="total_amount"
                                name="total_amount"
                                value={form.total_amount}
                                onChange={handleChange}
                                min="0"
                                step="0.01"
                                required
                            />
                            <ErrorMessage name="total_amount" />
                        </FormGroup>
                        /* Notes */
                        <FormGroup label="Notes" htmlFor="notes">
                            <Textarea
                                id="notes"
                                name="notes"
                                value={form.notes}
                                onChange={handleChange}
                                rows="4"
                            />
                            <ErrorMessage name="notes" />
                        </FormGroup>
                        /* Actions */
                        <div className="form-actions">
                            <Button type="submit" variant="primary">
                                {isEditMode ? 'Update Booking' : 'Create Booking'}
                            </Button>
                            <Button type="button" variant="secondary" onClick={() => navigate('/bookings')}>
                                Cancel
                            </Button>
                        </div>
                    </form>
                </Card>
        </div>
    );
};



                

        