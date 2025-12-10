// src/pages/booking/CheckIn.jsx

import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';

import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';
import { Badge } from '../../components/ui/Badge';
import { Spinner } from '../../components/ui/Spinner';
import { Alert } from '../../components/ui/Alert';

import Breadrumb from '../../components/common/Breadrumb';
import FormGroup from '../../components/common/FormGroup';
import TextArea from '../../components/common/TextArea';

import useFetch from '../../hooks/useFetch';
import { formatDate } from '../../utils/formatDate';

const CheckIn = () => {
    const { id } = useParams();
    const navigate = useNavigate();

    const { data: booking, loading, error } = useFetch(`/bookings/${id}`);

    const [checkInNotes, setCheckInNotes] = useState('');
    const [submitError, setSubmitError] = useState('');
    const [successMessage, setSuccessMessage] = useState('');
    const [submitting, setSubmitting] = useState(false);

    const statusColors = {
        Booked: 'primary',
        CheckIn: 'success',
        CheckOut: 'secondary',
        Cancelled: 'danger',
        NoShow: 'warning',
    };

    useEffect(() => {
        if (booking?.checkInNotes) {
            setCheckInNotes(booking.checkInNotes);
        } else {
            setCheckInNotes('');
        }
        setSubmitError('');
        setSuccessMessage('');
    }, [booking]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!booking) return;
        if (booking.status !== 'Booked') {
            setSubmitError('Booking is not eligible for check-in.');
            return;
        }

        setSubmitError('');
        setSuccessMessage('');
        setSubmitting(true);

        try {
            const response = await fetch(`/bookings/${id}/checkin`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ checkInNotes }),
            });

            if (!response.ok) {
                let msg = 'Failed to check in';
                try {
                    const data = await response.json();
                    if (data?.message) msg = data.message;
                } catch (_) {}
                throw new Error(msg);
            }

            setSuccessMessage('Check-in successful!');
            // short delay to show success then navigate back to bookings
            setTimeout(() => navigate('/bookings'), 1400);
        } catch (err) {
            setSubmitError(err.message || 'An unexpected error occurred');
        } finally {
            setSubmitting(false);
        }
    };

    if (loading) {
        return (
            <div className="center">
                <Spinner />
            </div>
        );
    }

    if (error) {
        return (
            <div className="center">
                <Alert type="danger">{error}</Alert>
            </div>
        );
    }

    if (!booking) {
        return (
            <Alert
                type="warning"
                message="Booking not found. It may have been cancelled or does not exist."
            />
        );
    }

    const isEligible = booking.status === 'Booked';

    return (
        <div className="check-in-page">
            {/* Breadcrumb */}
            <Breadrumb
                items={[
                    { label: 'Bookings', path: '/bookings' },
                    { label: `Booking #${booking.id}`, path: `/bookings/${booking.id}` },
                    { label: 'Check-In' },
                ]}
            />

            <div className="page-header">
                <h1>Check-In for Booking #{booking.id}</h1>
                <Badge color={statusColors[booking.status] || 'secondary'}>
                    {booking.status}
                </Badge>
            </div>

            {!isEligible && (
                <Alert type="warning" message="This booking is not eligible for check-in." />
            )}

            <Card>
                <form onSubmit={handleSubmit}>
                    <FormGroup label="Guest Name">
                        <div>{booking.guestName || booking.guest?.name || '—'}</div>
                    </FormGroup>

                    <FormGroup label="Room">
                        <div>{booking.room?.number || booking.roomNumber || '—'}</div>
                    </FormGroup>

                    <FormGroup label="Dates">
                        <div>
                            {formatDate(booking.startDate)} — {formatDate(booking.endDate)}
                        </div>
                    </FormGroup>

                    <FormGroup label="Check-In Notes">
                        <TextArea
                            value={checkInNotes}
                            onChange={(e) => setCheckInNotes(e.target.value)}
                            placeholder="Add any notes for the guest or housekeeping..."
                            rows={5}
                            maxLength={1000}
                            aria-label="Check-in notes"
                            autoFocus
                        />
                    </FormGroup>

                    {submitError && <Alert type="danger">{submitError}</Alert>}
                    {successMessage && <Alert type="success">{successMessage}</Alert>}

                    <div className="form-actions">
                        <Button type="button" variant="secondary" onClick={() => navigate(-1)} disabled={submitting}>
                            Cancel
                        </Button>
                        <Button
                            type="submit"
                            variant="primary"
                            disabled={submitting || !isEligible}
                        >
                            {submitting ? 'Checking in...' : 'Confirm Check-In'}
                        </Button>
                    </div>
                </form>
            </Card>
        </div>
    );
};

export default CheckIn;