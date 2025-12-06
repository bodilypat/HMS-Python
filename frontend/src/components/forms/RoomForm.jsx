//frontend/src/components/forms/RoomForm.jsx 

import React, { useState } from 'react';
import { Input, Button, Select, TextArea, Checkbox, message } from '../ui';
import roomService from '../../services/roomService';

const RoomForm = ({ room = null, onSuccess = () => {} }) => {
    const [roomNumber, setRoomNumber] = useState(room ? room.room_number : '');
    const [roomTypeId, setRoomTypeId] = useState(room ? room.room_type_id : '');
    const [floorNumber, setFloorNumber] = useState(room ? room.floor_number : 0);
    const [pricePerNight, setPricePerNight] = useState(room ? room.price_per_night : 0.0);
    const [bedsCount, setBedsCount] = useState(room ? room.beds_count : 1);
    const [capacity, setCapacity] = useState(room ? room.capacity : 1);
    const [status, setStatus] = useState(room ? room.room_status : 'Available');
    const [description, setDescription] = useState(room ? room.room_description || '' : '');
    const [isActive, setIsActive] = useState(room ? !!room.is_active : true);
    const [errors, setErrors] = useState({});

    const validate = () => {
        const e = {};
        if (!roomNumber || roomNumber.toString().trim() === '') e.roomNumber = 'Room number is required';
        if (!roomTypeId) e.roomTypeId = 'Room type is required';
        if (floorNumber === '' || floorNumber === null || Number(floorNumber) < 0) e.floorNumber = 'Floor number must be 0 or greater';
        if (pricePerNight === '' || Number(pricePerNight) < 0) e.pricePerNight = 'Price per night must be 0 or greater';
        if (!Number.isInteger(Number(bedsCount)) || Number(bedsCount) <= 0) e.bedsCount = 'Beds count must be an integer > 0';
        if (!Number.isInteger(Number(capacity)) || Number(capacity) < Number(bedsCount)) e.capacity = 'Capacity must be an integer >= beds count';
        setErrors(e);
        return Object.keys(e).length === 0;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!validate()) return;

        const roomData = {
            room_number: String(roomNumber).trim(),
            room_type_id: Number(roomTypeId),
            floor_number: Number(floorNumber),
            price_per_night: Number(pricePerNight),
            beds_count: Number(bedsCount),
            capacity: Number(capacity),
            room_status: status,
            room_description: description,
            is_active: Boolean(isActive),
        };

        try {
            if (room && room.room_id) {
                await roomService.updateRoom(room.room_id, roomData);
            } else {
                await roomService.createRoom(roomData);
            }
            onSuccess();
        } catch (err) {
            console.error('Error saving room:', err);
            setErrors((prev) => ({ ...prev, submit: err.message || 'Save failed' }));
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Room Number:</label>
                <input type="text" value={roomNumber} onChange={(e) => setRoomNumber(e.target.value)} />
                {errors.roomNumber && <span className="error">{errors.roomNumber}</span>}
            </div>

            <div>
                <label>Room Type ID:</label>
                <input type="number" value={roomTypeId} onChange={(e) => setRoomTypeId(e.target.value)} />
                {errors.roomTypeId && <span className="error">{errors.roomTypeId}</span>}
            </div>

            <div>
                <label>Floor Number:</label>
                <input type="number" min="0" value={floorNumber} onChange={(e) => setFloorNumber(e.target.value)} />
                {errors.floorNumber && <span className="error">{errors.floorNumber}</span>}
            </div>

            <div>
                <label>Price Per Night:</label>
                <input type="number" min="0" step="0.01" value={pricePerNight} onChange={(e) => setPricePerNight(e.target.value)} />
                {errors.pricePerNight && <span className="error">{errors.pricePerNight}</span>}
            </div>

            <div>
                <label>Beds Count:</label>
                <input type="number" min="1" value={bedsCount} onChange={(e) => setBedsCount(e.target.value)} />
                {errors.bedsCount && <span className="error">{errors.bedsCount}</span>}
            </div>

            <div>
                <label>Capacity:</label>
                <input type="number" min={bedsCount || 1} value={capacity} onChange={(e) => setCapacity(e.target.value)} />
                {errors.capacity && <span className="error">{errors.capacity}</span>}
            </div>

            <div>
                <label>Status:</label>
                <select value={status} onChange={(e) => setStatus(e.target.value)}>
                    <option value="Available">Available</option>
                    <option value="Occupied">Occupied</option>
                    <option value="Cleaning">Cleaning</option>
                    <option value="Maintenance">Maintenance</option>
                    <option value="OutOfService">OutOfService</option>
                </select>
            </div>

            <div>
                <label>Description:</label>
                <textarea value={description} onChange={(e) => setDescription(e.target.value)} />
            </div>

            <div>
                <label>
                    <input type="checkbox" checked={isActive} onChange={(e) => setIsActive(e.target.checked)} />
                    Active
                </label>
            </div>

            {errors.submit && <div className="error">{errors.submit}</div>}

            <button type="submit">{room ? 'Update Room' : 'Create Room'}</button>
        </form>
    );
};

export default RoomForm;
