//src/pages/guests/GuestDetail.jsx

import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

import Button from '../../components/ui/Button.jsx';
import Card from '../../components/ui/Card.jsx';
import Spinner from '../../components/ui/Spinner.jsx';
import ConfirmDialog from '../../components/common/ConfirmDialog.jsx';

import guestService from '../../services/guestService.js';
import formatDate from '../../utils/formatDate.js';
import formatCurrency from '../../utils/formatCurrency.js';

const GuestDetail = () => {
  const { guestId } = useParams();
  const navigate = useNavigate();

  // ================================
  // STATE
  // ================================
  const [guest, setGuest] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isConfirmOpen, setIsConfirmOpen] = useState(false);

  // ================================
  // LOAD GUEST DATA
  // ================================
  const loadGuest = async () => {
    try {
      setIsLoading(true);
      const data = await guestService.getGuestById(guestId);
      setGuest(data);
    } catch (err) {
      console.error(err);
      setError('Failed to load guest data.');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadGuest();
  }, [guestId]);

  // ================================
  // ACTION HANDLERS
  // ================================
  const handleEdit = () => {
    navigate(`/guests/${guestId}/edit`);
  };

  const handleBack = () => {
    navigate('/guests');
  };

  const handleDelete = async () => {
    try {
      await guestService.deleteGuest(guestId);
      navigate('/guests');
    } catch (err) {
      console.error(err);
      setError('Failed to delete guest.');
    }
  };

  // ================================
  // RENDER
  // ================================
  if (isLoading) {
    return (
      <div className="flex justify-center items-center h-full py-40">
        <Spinner />
      </div>
    );
  }

  if (!guest) {
    return (
      <div className="p-4 text-center">
        <Button onClick={handleBack}>Back to Guests</Button>
        {error ? (
          <div className="text-red-500 mt-4">{error}</div>
        ) : (
          <div className="mt-4">No guest data available.</div>
        )}
      </div>
    );
  }

  return (
    <div className="page-container">
      {/* HEADER */}
      <div className="page-header">
        <h2 className="page-title">Guest Details</h2>
        <div className="page-actions">
          <Button onClick={handleBack}>Back</Button>
          <Button onClick={handleEdit} variant="primary">
            Edit Guest
          </Button>
          <Button onClick={() => setIsConfirmOpen(true)} variant="danger">
            Delete Guest
          </Button>
        </div>
      </div>

      {/* PERSONAL INFO */}
      <Card title="Personal Information">
        <div className="detail-grid">
          <DetailItem label="Full Name" value={guest.full_name} />
          <DetailItem label="Email" value={guest.email} />
          <DetailItem label="Phone" value={guest.phone_number} />
          <DetailItem label="Date of Birth" value={formatDate(guest.dob)} />
          <DetailItem label="Gender" value={guest.gender} />
          <DetailItem label="Nationality" value={guest.nationality} />
        </div>
      </Card>

      {/* IDENTIFICATION */}
      <Card title="Identification">
        <div className="detail-grid">
          <DetailItem label="ID Type" value={guest.id_type} />
          <DetailItem label="ID Number" value={guest.id_number} />
        </div>
      </Card>

      {/* ADDRESS */}
      <Card title="Address">
        <div className="detail-grid">
          <DetailItem label="Street" value={guest.address?.street || '--'} />
          <DetailItem label="City" value={guest.address?.city || '--'} />
          <DetailItem label="State" value={guest.address?.state || '--'} />
          <DetailItem label="Postal Code" value={guest.address?.postal_code || '--'} />
          <DetailItem label="Country" value={guest.address?.country || '--'} />
        </div>
      </Card>

      {/* STATUS */}
      <Card title="Status">
        <div className="detail-grid">
          <DetailItem label="Member Since" value={formatDate(guest.created_at)} />
          <DetailItem label="Total Bookings" value={guest.total_bookings || 0} />
          <DetailItem label="Total Spent" value={formatCurrency(guest.total_spent || 0)} />
          <DetailItem label="Last Active" value={formatDate(guest.updated_at)} />
        </div>
      </Card>

      {/* CONFIRM DELETE DIALOG */}
      <ConfirmDialog
        isOpen={isConfirmOpen}
        title="Delete Guest"
        message="Are you sure you want to delete this guest? This action cannot be undone."
        onConfirm={handleDelete}
        onCancel={() => setIsConfirmOpen(false)}
      />
    </div>
  );
};

export default GuestDetail;
