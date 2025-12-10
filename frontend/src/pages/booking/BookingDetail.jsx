//src/pages/booking/BookingDetail.jsx 

import React, { useEffect, useState } from "react";
import { useParams, Link, useNavigate } from "react-router-dom";

import { Card } from "../../components/ui/Card";
import { Button } from "../../components/ui/Button";
import { Badge } from "../../components/ui/Badge";
import { Divider } from "../../components/ui/Divider";
import { Spinner } from "../../components/ui/Spinner";
import { Alert } from "../../components/ui/Alert";

import Breadcrumb from "../../components/common/Breadcrumb";
import ConfirmationDialog from "../../components/common/ConfirmationDialog";
import EmptyState from "../../components/common/EmptyState";

import Table from "../../components/tables/Table";
import TableRow from "../../components/tables/Table/TableRow";
import TableCell from "../../components/tables/Table/TableCell";

import useFetch from "../../hooks/useFetch";
import { formatDate } from "../../utils/formatDate";

const BookingDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const { data, loading, error, fetchData } = useFetch();
  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);

  useEffect(() => {
    fetchData(`/api/bookings/${id}`);
  }, [id]);

  const statusColors = {
    Booked: "primary",
    CheckedIn: "success",
    CheckedOut: "secondary",
    Cancelled: "danger",
    NoShow: "warning",
  };

  const handleDelete = async () => {
    try {
      await fetch(`/api/bookings/${id}`, { method: "DELETE" });
      navigate("/bookings");
    } catch (err) {
      console.error(err);
    }
  };

  if (loading)
    return (
      <div className="center">
        <Spinner size={45} />
      </div>
    );

  if (error) return <Alert type="error" message={error} />;

  if (!data)
    return (
      <EmptyState
        title="Booking not found"
        description="The booking ID does not exist or has been removed."
      />
    );

  return (
    <div className="booking-detail">

      {/* Breadcrumb */}
      <Breadcrumb
        items={[
          { label: "Dashboard", to: "/dashboard" },
          { label: "Bookings", to: "/bookings" },
          { label: `Booking #${data.booking_reference}` },
        ]}
      />

      {/* Header Actions */}
      <div className="page-header">
        <h2>Booking Details</h2>

        <div className="header-actions">
          <Link to={`/bookings/${id}/edit`}>
            <Button>Edit Booking</Button>
          </Link>

          {data.status === "Booked" && (
            <Button variant="success">Check In</Button>
          )}

          {data.status === "CheckedIn" && (
            <Button variant="secondary">Check Out</Button>
          )}

          <Button variant="danger" onClick={() => setShowDeleteConfirm(true)}>
            Delete
          </Button>
        </div>
      </div>

      {/* Booking Summary */}
      <Card>
        <h3>Summary</h3>

        <Divider />

        <Table>
          <tbody>
            <TableRow>
              <TableCell header>Booking Reference</TableCell>
              <TableCell>{data.booking_reference}</TableCell>
            </TableRow>

            <TableRow>
              <TableCell header>Status</TableCell>
              <TableCell>
                <Badge color={statusColors[data.status]}>
                  {data.status}
                </Badge>
              </TableCell>
            </TableRow>

            <TableRow>
              <TableCell header>Booking Source</TableCell>
              <TableCell>{data.booking_source}</TableCell>
            </TableRow>

            <TableRow>
              <TableCell header>Total Amount</TableCell>
              <TableCell>${Number(data.total_amount).toFixed(2)}</TableCell>
            </TableRow>

            {data.notes && (
              <TableRow>
                <TableCell header>Notes</TableCell>
                <TableCell>{data.notes}</TableCell>
              </TableRow>
            )}
          </tbody>
        </Table>
      </Card>

      <br />

      {/* Guest / Room / Staff Info */}
      <div className="grid-3">
        <Card>
          <h3>Customer Information</h3>
          <Divider />

          <p><strong>Name:</strong> {data.customer_name}</p>
          <p><strong>Email:</strong> {data.customer_email}</p>
          <p><strong>Phone:</strong> {data.customer_phone}</p>
        </Card>

        <Card>
          <h3>Room Details</h3>
          <Divider />

          <p><strong>Room:</strong> {data.room_number}</p>
          <p><strong>Type:</strong> {data.room_type}</p>
          <p><strong>Amenities:</strong> {data.room_amenities}</p>
        </Card>

        <Card>
          <h3>Staff In Charge</h3>
          <Divider />

          <p><strong>Name:</strong> {data.staff_name}</p>
          <p><strong>Role:</strong> {data.staff_role}</p>
        </Card>
      </div>

      <br />

      {/* Stay Information */}
      <Card>
        <h3>Stay Information</h3>

        <Divider />

        <Table>
          <tbody>
            <TableRow>
              <TableCell header>Check-In Date</TableCell>
              <TableCell>{formatDate(data.check_in_date)}</TableCell>
            </TableRow>

            <TableRow>
              <TableCell header>Check-Out Date</TableCell>
              <TableCell>{formatDate(data.check_out_date)}</TableCell>
            </TableRow>

            <TableRow>
              <TableCell header>Nights</TableCell>
              <TableCell>{data.stay_nights} nights</TableCell>
            </TableRow>

            <TableRow>
              <TableCell header>Guest Count</TableCell>
              <TableCell>{data.guest_count} guests</TableCell>
            </TableRow>
          </tbody>
        </Table>
      </Card>

      {/* Delete Confirmation Modal */}
      <ConfirmationDialog
        open={showDeleteConfirm}
        title="Delete Booking?"
        message="Are you sure you want to delete this booking? This action cannot be undone."
        onClose={() => setShowDeleteConfirm(false)}
        onConfirm={handleDelete}
      />
    </div>
  );
};

export default BookingDetail;

