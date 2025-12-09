//src/pages/guests/GuestEdit.jsx 

import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

import Button from '../../components/common/Button';
import Card from '../../components/common/Card';
import Input from '../../components/common/Input';
import Select from '../../components/common/Select';
import TextArea from '../../components/common/TextArea';
import spinner from '../../assets/spinner.gif';
import ErrorMessage from '../../components/common/ErrorMessage';


import guestService from '../../services/guestService';
import formatDate from '../../utils/formatDate';

const idTypes = [
  { value: 'passport', label: 'Passport' },
  { value: 'driver_license', label: 'Driver License' },
  { value: 'national_id', label: 'National ID' },
];

const genders = [
    { value: 'male', label: 'Male' },
    { value: 'female', label: 'Female' },
    { value: 'other', label: 'Other' },
    { value: 'prefer_not_to_say', label: 'Prefer not to say' },
];

const GuestEdit = () => {
    const { guestId } = useParams();
    const navigate = useNavigate();

    const [loading, setLoading] = useState(true);
    const [guest, setGuest] = useState(null);
    const [error, setError] = useState('');

    /* REACT HOOK FORM */
    const {
        register,
        handleSubmit,
        setValue,
        formState: { errors },
    } = useForm();

    /* LOAD GUEST */
    const loadGuest = async () => {
        try {
            setLoading(true);
            const data = await guestService.getGuestById(guestId);
            setGuest(data);

            // prefill form fields 
            Object.keys(data).forEach((key) => {
                if (key === 'date_of_birth') {
                    setValue(key, formatDate(data[key]));
                } else {
                    setValue(key, data[key]);
                }
            });
        } catch (err) {
            setError('Failed to fetch guest details.');
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        loadGuest();
    }, [guestId]);

    /* ON SAVE */
    const onSubmit = async (data) => {
        try {
            setLoading(true);
            await guestService.updateGuest(guestId, data);
            navigate('/guests');
        } catch (err) {
            setError('Failed to update guest details.');
        } finally {
            setLoading(false);
        }
    };

    /* STATE: LOADING & ERROR */
    if (loading) {
        return (
            <div className="loading-container">
                <img src={spinner} alt="Loading..." />
            </div>
        );
    }
    if (error) {
        return <ErrorMessage message={error} />;
    }
    /* RENDER FORM */
    return (
        <div className="guest-edit-page">
            <h2>Edit Guest Details</h2>
            <Card>
                <form onSubmit={handleSubmit(onSubmit)} className="guest-edit-form">
                    <Input
                        label="Full Name"
                        {...register('full_name', { required: 'Full Name is required' })}
                        error={errors.full_name?.message}
                        defaultValue={guest.full_name}
                    />
                    <Input
                        label="Email"
                        type="email"
                        {...register('email', {
                            required: 'Email is required',
                            pattern: {
                                value: /^\S+@\S+$/i,
                                message: 'Invalid email address',
                            },
                        })}
                        error={errors.email?.message}
                        defaultValue={guest.email}
                    />
                    <Input
                        label="Phone Number"
                        {...register('phone_number', { required: 'Phone Number is required' })}
                        error={errors.phone_number?.message}
                        defaultValue={guest.phone_number}
                    />
                    <Select
                        label="Gender"
                        options={genders}
                        {...register('gender', { required: 'Gender is required' })}
                        error={errors.gender?.message}
                        defaultValue={guest.gender}
                    />
                    <Input
                        label="Date of Birth"
                        type="date"
                        {...register('date_of_birth', { required: 'Date of Birth is required' })}
                        error={errors.date_of_birth?.message}
                        defaultValue={guest.date_of_birth}
                    />
                    <Select
                        label="ID Type"
                        options={idTypes}
                        {...register('id_type', { required: 'ID Type is required' })}
                        error={errors.id_type?.message}
                        defaultValue={guest.id_type}
                    />
                    <Input
                        label="ID Number"
                        {...register('id_number', { required: 'ID Number is required' })}
                        error={errors.id_number?.message}
                        defaultValue={guest.id_number}
                    />
                    <TextArea
                        label="Address"
                        {...register('address', { required: 'Address is required' })}
                        error={errors.address?.message}
                        defaultValue={guest.address}
                    />
                    <div className="form-actions">
                        <Button type="submit" variant="primary">
                            Save Changes
                        </Button>
                        <Button type="button" variant="secondary" onClick={() => navigate('/guests')}
>                            Cancel
                        </Button>
                    </div>
                </form>
            </Card>
        </div>
    );
};
export default GuestEdit;
