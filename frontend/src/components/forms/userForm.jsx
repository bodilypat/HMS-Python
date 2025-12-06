//src/components/UserForm.jsx 

import React, { useState, useEffect } from 'react';
import { Input, Button, Select, InputNumber, DatePicker, message } from '../ui';
import userService from '../services/userService';

const initialFormState = {
    username: '',
    email: '',
    password: '',
    role: 'user',
    status: 'active',
};

const roles = ['Admin', 'Manager','User', 'Guest'];
const statuses = ['Active', 'Inactive', 'Pending'];

const UserForm = ({ user = null, onSuccess = () => {} }) => {
    const [formData, setFormData] = useState(initialFormState);
    const [loading, setLoading] = useState(false);  
    const [errors, setErrors] = useState({});

    useEffect(() => {
        if (user) setFormData({ ...initialFormState, ...user, password: '' }); // reset password
    }, [user]);

    const validate = () => {
        const newErrors = {};
        if (!formData.username) newErrors.username = 'Username is required';
        if (!formData.email) newErrors.email = 'Email is required';
        if (!formData.password && !user) newErrors.password = 'Password is required';
        if (!roles.includes(formData.role)) newErrors.role = 'Invalid role selected';
        if (!statuses.includes(formData.status)) newErrors.status = 'Invalid status selected';
        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!validate()) return;
        
        const userData = {
            username: formData.username,
            email: formData.email,
            password: formData.password || undefined,
            role: formData.role,
            status: formData.status,
        };

        try {
            if (user && user.id) {
                await userService.updateUser(user.id, userData);
                message.success('User updated successfully');
            } else {
                await userService.createUser(userData);
                message.success('User created successfully');
            }
            onSuccess();
        } catch (error) {
            console.error('Error saving user:', error);
            message.error('Failed to save user: ' + (error.message || 'Save failed'));
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <Input
                label="Username"
                name="username"     
                value={formData.username}
                onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                error={errors.username}
            />
            <Input
                label="Email"
                name="email"
                type="email"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                error={errors.email}
            />
            <Input
                label="Password"
                name="password"
                type="password"
                value={formData.password}
                onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                error={errors.password}
                placeholder={user ? 'Leave blank to keep current password' : ''}
            />
            <Select
                label="Role"
                name="role"
                value={formData.role}
                onChange={(value) => setFormData({ ...formData, role: value })}
                options={roles.map((role) => ({ label: role, value: role.toLowerCase() }))}
                error={errors.role}
            />
            <Select
                label="Status"
                name="status"
                value={formData.status} 
                onChange={(value) => setFormData({ ...formData, status: value })}
                options={statuses.map((status) => ({ label: status, value: status.toLowerCase() }))}
                error={errors.status}
            />
            <Button type="submit" disabled={loading}>{user ? 'Update User' : 'Create User'}</Button>
        </form>
    );
};
