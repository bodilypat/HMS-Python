//src/components/forms/RoomTypeForm.jsx 

import React, { useState, useEffect } from 'react';
import { Input, TextArea, InputNumber, Checkbox, Button, message } from '../ui';
import roomTypeService from '../../services/roomTypeService';

const initialState = {
    type_name: '',
    description: '',
    base_price: 0.0,
    default_occupancy: 1,
    bedC_ount: 1,
    amenities: [],
    is_active: true,
};

const requiredFields = ['type_name'];

const RoomTypeForm = ({ roomType = null,  onSuccess = () => {}  }) => {
    const [formData, setFormData] = useState(initialState);
    const [loading, setLoading] = useState(false);
    const [errors, setErrors] = useState({});

    useEffect(() => {
        if (roomType) {
            setFormData({...initialState, ...roomType});
        }, [roomType]);

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData({ ...formData, [name]: type === 'checkbox' ? checked : value });
    };

    const handleNumberChange = (name, value) => {
        setFormData({ ...formData, [name]: value });
    };

    const validate = () => {
        const newErrors = {};
        requiredFields.forEach(field => {
            if (!formData[field] || formData[field].toString().trim() === '') {
                newErrors[field] = `${field.replace('_', ' ')} is required`;
            }
        });

        if (formData.base_price < 0) newErrors.base_price = 'Base price cannot be negative';
        if (!Number.isInteger(formData.default_occupancy) || formData.default_occupancy <= 0) {
            newErrors.default_occupancy = 'Default occupancy must be a positive integer';
        }

        if (!Number.isInteger(formData.bed_count) || formData.bed_count <= 0) {
            newErrors.bed_count = 'Bed count must be a positive integer';
        }

        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!validate()) return;

        try {
            if (roomType && roomType.room_type_id) {
                await roomTypeService.updateRoomType(roomType.room_type_id, formData);
                message.success('Room type updated successfully');
            } else {
                await roomTypeService.createRoomType(formData);
                message.success('Room type created successfully');
            }
            message.success('Room type saved successfully');
            onSuccess();
        } catch (error) {
            console.error('Error saving room type:', error);
            message.error('Failed to save room type. Please try again.');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <Input
                label="Type Name"
                name="type_name"
                value={formData.type_name}
                onChange={handleChange}
                error={errors.type_name}
                required
            />
            <TextArea
                label="Description"
                name="description"
                value={formData.description}
                onChange={handleChange}
                error={errors.description}
            />
            <InputNumber
                label="Base Price"
                name="base_price"
                value={formData.base_price}
                onChange={(value) => handleNumberChange('base_price', value)}
                error={errors.base_price}
                min={0}
                step={0.01}
                required
            />
            <InputNumber
                label="Default Occupancy"
                name="default_occupancy"
                value={formData.default_occupancy}
                onChange={(value) => handleNumberChange('default_occupancy', value)}
                error={errors.default_occupancy}
                min={1}
                step={1}
                required
            />
            <InputNumber
                label="Bed Count"
                name="bed_count"
                value={formData.bed_count}
                onChange={(value) => handleNumberChange('bed_count', value)}
                error={errors.bed_count}
                min={1}
                step={1}
                required
            />
            <Checkbox
                label="Active"
                name="is_active"
                checked={formData.is_active}
                onChange={handleChange}
            />
            <Button type="submit" loading={loading}>
                {roomType ? 'Update Room Type' : 'Create Room Type'}
            </Button>
        </form>
    );
}
export default RoomTypeForm;