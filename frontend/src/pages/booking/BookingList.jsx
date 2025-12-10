//src/pages/booking/BookingList.jsx 

import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { Card } from "../../components/ui/Card";
import { Button } from "../../components/ui/Button";
import { Badge } from "../../components/ui/Badge";
import { Spinner } from "../../components/ui/Spinner";
import { Alert } from "../../components/ui/Alert";

import SearchBar from "../../components/common/SearchBar";
import FilterPanel from "../../components/common/FilterPanel";
import Breadcrumb from "../../components/common/Breadcrumb";
import EmptyState from "../../components/common/EmptyState";

import Table from "../../components/tables/Table";
import TableHeader from "../../components/tables/Table/TableHeader";
import TableBody from "../../components/tables/Table/TableBody";
import TableRow from "../../components/tables/Table/TableRow";
import TableCell from "../../components/tables/Table/TableCell";
import TableEmpty from "../../components/tables/Table/TableEmpty";

import PaginationTable from "../../components/tables/Pagination/PaginationTable";

import useFetch from "../../hooks/useFetch";
import { formatDate } from "../../utils/formatDate";

const BookingList = () => {
  const { data, loading, error, fetchData } = useFetch();

  const [search, setSearch] = useState("");
  const [filters, setFilters] = useState({
    status: "",
    source: "",
  });

  const [page, setPage] = useState(1);
  const perPage = 10;

  useEffect(() => {
    fetchData("/api/bookings");
  }, []);

  const statusColors = {
    Booked: "primary",
    CheckedIn: "success",
    CheckedOut: "secondary",
    Cancelled: "danger",
    NoShow: "warning",
  };

  const filteredBookings = data
    ?.filter((b) =>
      search.length === 0
        ? true
        : (
            b.booking_reference +
            b.customer_name +
            b.room_number
          )
            .toLowerCase()
            .includes(search.toLowerCase())
    )
    ?.filter((b) => (filters.status ? b.status === filters.status : true))
    ?.filter((b) =>
      filters.source ? b.booking_source === filters.source : true
    );

  const paginated = filteredBookings?.slice(
    (page - 1) * perPage,
    page * perPage
  );

  return (
    <div className="booking-list">

      {/* Breadcrumb */}
      <Breadcrumb
        items={[{ label: "Dashboard", to: "/dashboard" }, { label: "Bookings" }]}
      />

      <div className="list-header">
        <h2>Booking Management</h2>

        <Link to="/bookings/new">
          <Button variant="primary">+ New Booking</Button>
        </Link>
      </div>

      <Card>
        {/* Search & Filters */}
        <div className="actions-row">
          <SearchBar
            placeholder="Search by reference, customer, room..."
            value={search}
            onChange={(value) => setSearch(value)}
          />

          <FilterPanel
            filters={[
              {
                label: "Status",
                name: "status",
                options: [
                  "Booked",
                  "CheckedIn",
                  "CheckedOut",
                  "Cancelled",
                  "NoShow",
                ],
              },
              {
                label: "Source",
                name: "source",
                options: ["Online", "Phone", "WalkIn", "TravelAgent", "Corporate"],
              },
            ]}
            onFilterChange={(updated) => setFilters(updated)}
          />
        </div>

        {loading && (
          <div className="center">
            <Spinner size={40} />
          </div>
        )}

        {error && <Alert type="error" message={error} />}

        {!loading && filteredBookings?.length === 0 && (
          <EmptyState
            title="No bookings found"
            description="Try adjusting your search or filters"
          />
        )}

        {!loading && filteredBookings?.length > 0 && (
          <>
            <Table>
              <TableHeader
                columns={[
                  "Reference",
                  "Customer",
                  "Room",
                  "Check-in",
                  "Check-out",
                  "Nights",
                  "Status",
                  "Amount",
                  "Source",
                  "Actions",
                ]}
              />

              <TableBody>
                {paginated?.map((b) => (
                  <TableRow key={b.booking_id}>
                    <TableCell>{b.booking_reference}</TableCell>
                    <TableCell>{b.customer_name}</TableCell>
                    <TableCell>{b.room_number}</TableCell>

                    <TableCell>{formatDate(b.check_in_date)}</TableCell>
                    <TableCell>{formatDate(b.check_out_date)}</TableCell>

                    <TableCell>{b.stay_nights}</TableCell>

                    <TableCell>
                      <Badge color={statusColors[b.status]}>
                        {b.status}
                      </Badge>
                    </TableCell>

                    <TableCell>${Number(b.total_amount).toFixed(2)}</TableCell>

                    <TableCell>{b.booking_source}</TableCell>

                    <TableCell>
                      <div className="row-actions">
                        <Link to={`/bookings/${b.booking_id}`}>
                          <Button size="sm" variant="ghost">
                            View
                          </Button>
                        </Link>

                        <Link to={`/bookings/${b.booking_id}/edit`}>
                          <Button size="sm" variant="secondary">
                            Edit
                          </Button>
                        </Link>
                      </div>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>

              <TableEmpty visible={paginated?.length === 0} />
            </Table>

            <PaginationTable
              page={page}
              perPage={perPage}
              total={filteredBookings.length}
              onPageChange={setPage}
            />
          </>
        )}
      </Card>
    </div>
  );
};

export default BookingList;
