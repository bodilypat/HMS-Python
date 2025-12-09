// src/pages/guests/GuestsList.tsx

import React, { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";

import Table from "../../components/Table";
import Button from "../../components/Button";
import SearchBar from "../../components/SearchBar";
import Pagination from "../../components/Pagination";

import guestService from "../../services/guestService";
import { formatDate } from "../../utils/dateUtils";
import { formatCurrency } from "../../utils/currencyUtils";

type Guest = {
    id: string | number;
    first_name?: string;
    last_name?: string;
    email?: string;
    phone?: string;
    registration_date?: string | null;
    total_spent?: number;
};

const ITEMS_PER_PAGE = 10;
const DEBOUNCE_MS = 350;

const GuestsList: React.FC = () => {
    const navigate = useNavigate();

    const [guests, setGuests] = useState<Guest[]>([]);
    const [searchQuery, setSearchQuery] = useState("");
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    // to avoid race conditions when multiple fetches are in-flight
    const fetchIdRef = useRef(0);
    const debounceRef = useRef<number | undefined>(undefined);

    const columns = useMemo(
        () => [
            {
                key: "full_name",
                label: "Full Name",
                width: "25%",
                render: (g: Guest) => `${g.first_name ?? ""} ${g.last_name ?? ""}`.trim() || "—",
            },
            {
                key: "email",
                label: "Email",
                width: "25%",
                render: (g: Guest) => g.email ?? "—",
            },
            {
                key: "phone",
                label: "Phone",
                width: "20%",
                render: (g: Guest) => g.phone ?? "—",
            },
            {
                key: "registration_date",
                label: "Registration Date",
                width: "20%",
            },
            {
                key: "total_spent",
                label: "Total Spent",
                render: (g: Guest) => formatCurrency(g.total_spent ?? 0),
            },
        ],
        []
    );

    const formatCell = useCallback((key: string, value: any) => {
        if (key === "registration_date") return formatDate(value);
        return value ?? "—";
    }, []);

    const fetchGuests = useCallback(
        async (query: string, page: number) => {
            const currentFetchId = ++fetchIdRef.current;
            setIsLoading(true);
            setError(null);
            try {
                // guestService.getGuests is expected to return { data: { guests: Guest[], total_pages: number } }
                const response = await guestService.getGuests({
                    search: query,
                    page,
                    limit: ITEMS_PER_PAGE,
                });
                // ignore out-of-order responses
                if (currentFetchId !== fetchIdRef.current) return;
                const data = response?.data;
                setGuests(Array.isArray(data?.guests) ? data.guests : []);
                setTotalPages(Number(data?.total_pages) || 1);
            } catch (err) {
                if (currentFetchId !== fetchIdRef.current) return;
                console.error("Error fetching guests:", err);
                setError("Failed to load guests.");
            } finally {
                if (currentFetchId === fetchIdRef.current) setIsLoading(false);
            }
        },
        []
    );

    // debounced effect for search + page changes
    useEffect(() => {
        window.clearTimeout(debounceRef.current);
        debounceRef.current = window.setTimeout(() => {
            fetchGuests(searchQuery.trim(), currentPage);
        }, DEBOUNCE_MS);

        return () => {
            window.clearTimeout(debounceRef.current);
        };
    }, [searchQuery, currentPage, fetchGuests]);

    const handleSearch = (query: string) => {
        setSearchQuery(query);
        setCurrentPage(1);
    };

    const handleRowClick = (guest: Guest) => {
        navigate(`/guests/${guest.id}`);
    };

    const handlePageChange = (page: number) => {
        if (page < 1) return;
        setCurrentPage(page);
    };

    return (
        <div>
            <h1>Guests</h1>

            <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 20 }}>
                <SearchBar onSearch={handleSearch} placeholder="Search guests..." />
                <Button onClick={() => navigate("/guests/new")}>Add New Guest</Button>
            </div>

            <Table
                columns={columns}
                data={guests}
                isLoading={isLoading}
                onRowClick={handleRowClick}
                rowKey="id"
                formatCell={formatCell}
                emptyMessage={isLoading ? "Loading..." : error ?? "No guests found."}
            />

            <Pagination currentPage={currentPage} totalPages={totalPages} onPageChange={handlePageChange} />
        </div>
    );
};

export default GuestsList;
