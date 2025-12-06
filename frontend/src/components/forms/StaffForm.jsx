//src/components/forms/StaffForm.jsx

import React, { useState, useEffect } from 'react';
import { Input, Button, Select, DatePicker, inputNumber, message } from '../ui';
import staffService from '../../services/staffService';

const initialFormState = {
    first_name: '',
    last_name: '',
    role: 'Other',
    email: '',
    phone_number: '',
    salary: 0.0,
    hire_date: null,
    status: 'Active',
};

const roleOptions = ['Admin','Manager','Receptionist','Housekeeping','Security','Maintenance','Accountant','Other'];

const statusOptions = [
    { label: 'Active', value: 'Active'},
    { label: 'Inactive', value: 'Inactive'}
];

const requiredFields = ['first_name', 'last_name', 'email', 'phone_number', 'hire_date'];

const StaffForm = ({ staff = null, onSuccess = () => {} }) => {
    const [formData, setFormData] = useState(initialFormState);
    const [loading, setLoading] = useState(false);
    const [errors, setErrors] = useState({});

    useEffect(() => {
        if (staff) {
            setFormData({
                ...staff,
                hire_date: staff.hire_date ? new Date(staff.hire_date) : null,
            });
        }, [staff]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleDateChange = (date) => {
        setFormData({ ...formData, hire_date: date });
    };

    const handleNumberChange = (value) => {
        setFormData({ ...formData, salary: value });
    };

    const validateForm = () => {
        const newErrors = {};
        requiredFields.forEach(field => {
            if (!formData[field]) {
                newErrors[field] = 'This field is required';
            }
        });
        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!validateForm()) return;
        setLoading(true);
        try {
            if (staff) {
                await staffService.updateStaff(staff.id, formData);
                message.success('Staff member updated successfully');
            } else {
                await staffService.createStaff(formData);
                message.success('Staff member created successfully');
            }
            onSuccess();
        } catch (error) {
            message.error('An error occurred. Please try again.');
        }
        setLoading(false);
    };

    return (
        <form onSubmit={handleSubmit}>
            <Input
                label="First Name"
                name="first_name"
                value={formData.first_name}
                onChange={handleChange}
                error={errors.first_name}
            />
            <Input
                label="Last Name"
                name="last_name"
                value={formData.last_name}
                onChange={handleChange}
                error={errors.last_name}
            />
            <Select
                label="Role"
                name="role"
                value={formData.role}
                onChange={handleChange}
                options={roleOptions}
            />
            <Input
                label="Email"
                name="email"    
                value={formData.email}
                onChange={handleChange}
                error={errors.email}    
            />
            <Input
                label="Phone Number"
                name="phone_number" 
                value={formData.phone_number}
                onChange={handleChange}
                error={errors.phone_number}    
            />
            <InputNumber
                label="Salary"
                name="salary"
                value={formData.salary}
                onChange={handleNumberChange}
                min={0}
                step={0.01}
            />
            <DatePicker
                label="Hire Date"
                name="hire_date"
                value={formData.hire_date}
                onChange={handleDateChange}
                error={errors.hire_date}
            />
            <Select
                label="Status"
                name="status"
                value={formData.status}
                onChange={handleChange}
                options={statusOptions}
            />
            <Button type="submit" loading={loading}>
                {staff ? 'Update Staff' : 'Create Staff'}
            </Button>
        </form>
    );
};
