//src/components/tables/GuestTable.jsx

import React, { useState, useEffect } from 'react';
import guestService from '../../services/guestService';
import GuestForm from '../forms/GuestForm';
import { Button, Table, Modal, message } from '../ui';

const GuestTable = () => {
  const [guests, setGuests] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingGuest, setEditingGuest] = useState(null);

  const fetchGuests = async () => {
    setLoading(true);

    try {
        const data = await guestService.getAllGuests();
        setGuests(data);
    } catch (error) {
        console.error('Error fetching guests:', error);
        message.error('Failed to fetch guests');
    } finally {
        setLoading(false);
    }
};

useEffect(() => {
    fetchGuests();
}, []);

    const handleSearch = (e) => {
        setSearchTerm(e.target.value);
    };
    const filteredGuests = guests.filter(guest =>
        guest.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        guest.email.toLowerCase().includes(searchTerm.toLowerCase())
    );
    const openModal = (guest = null) => {
        setEditingGuest(guest);
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
        setEditingGuest(null);
    };

    const handleEdit = (guest) => {
        openModal(guest);
    };

    const handleDelete = async (guestId) => {
        try {
            await guestService.deleteGuest(guestId);
            message.success('Guest deleted successfully');
            fetchGuests();
        } catch (error) {
            console.error('Error deleting guest:', error);
            message.error('Failed to delete guest');
        }
    };

    const handleFormSubmit = async (guestData) => {
        try {
            if (editingGuest) {
                await guestService.updateGuest(editingGuest.id, guestData);
                message.success('Guest updated successfully');
            } else {
                await guestService.createGuest(guestData);
                message.success('Guest created successfully');
            }
            fetchGuests();
            closeModal();
        } catch (error) {
            console.error('Error saving guest:', error);
            message.error('Failed to save guest');
        }
    };

    if (loading) return <div>Loading...</div>;
    
    return (
        <div>
            <Button onClick={() => openModal()}>Add Guest</Button>
            <Table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Address</th>
                        <th>Gender</th>
                        <th>Nationality</th>
                        <th>Active</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {filteredGuests.map(guest => (
                        <tr key={guest.id}>
                            <td>{guest.id}</td>
                            <td>{guest.firstName}</td>
                            <td>{guest.lastName}</td>
                            <td>{guest.email}</td>
                            <td>{guest.phone}</td>
                            <td>{guest.address}</td>
                            <td>{guest.gender}</td>
                            <td>{guest.nationality}</td>
                            <td>{guest.isActive ? 'Yes' : 'No'}</td>
                            <td>
                                <Button onClick={() => handleEdit(guest)}>Edit</Button>
                                <Button onClick={() => handleDelete(guest.id)}>Delete</Button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </Table>
            <Modal isOpen={isModalOpen} onClose={closeModal}>
                <GuestForm
                    guest={editingGuest}
                    onSubmit={handleFormSubmit}
                    onCancel={closeModal}
                />
            </Modal>
        </div>
    );
};
