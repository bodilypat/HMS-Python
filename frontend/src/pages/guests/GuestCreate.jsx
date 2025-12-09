//src/pages/guests/GuestCreate.jsx

import React from 'react';
import  { useNavigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';

import Button from '../../components/common/Button';
import Card from '../../components/common/Card';
import Input from '../../components/common/Input';
import Select from '../../components/common/Select';
import TextArea from '../../components/common/TextArea';

import guestService from '../../services/guestService';

const idTypes = [
    { value: 'passport', label: 'Passport' },
    { value: 'driver_license', label: 'Driver License' },
    { value: 'national_id', label: 'National ID' },
];

const genders = [
    { value: 'male', label: 'Male' },
    { value: 'female', label: 'Female' },
    { value: 'other', label: 'Other' },
    { label: 'Prefer not to say', value: 'prefer_not_to_say' },
];

const GuestCreate = () => {
    const useNavigate = useNavigate();

    /* REACT HOOK FORM */
    const { 
        register, 
        handleSubmit, 
        formState: { errors, isSubmitting },
    } = useForm();

    /* SUBMIT HANDLER */
    const onSubmit = async (formData) => {
        try {
            await guestService.createGuest(formData);
            navigate('/guests');
        } catch (error) {
            console.error('Error creating guest:', error);
            alert('Failed to create guest. Please try again.');
        }
    };

    return (
        <div className="page-container">
            <div className="page-header">
                <h1 className="page-title">Create New Guest</h1>

                <div className="page-actions">
                    <Button
                        variant="secondary"
                        onClick={() => navigate('/guests')}
                        disabled={isSubmitting} 
                    >
                        Cancel
                    </Button>
                    <Button
                        variant="primary"
                        onClick={handleSubmit(onSubmit)}    
                        disabled={isSubmitting}
                    >
                        {isSubmitting ? 'Creating...' : 'Create Guest'}
                    </Button>
                </div>
            </div>
            <form id="guest-create-form" onSubmit={handleSubmit(onSubmit)}>
                {/* PERSONAL INFORMATION */}
                <Card title="Personal Information">
                    <div className="form-grid">
                        <Input
                            label="First Name"
                            {...register('first_name', { required: 'First name is required' })}
                            error={errors.first_name?.message}
                        />
                        <Input
                            label="Last Name"
                            {...register('last_name', { required: 'Last name is required' })}
                            error={errors.last_name?.message}
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
                        />
                        <Input
                            label="Phone Number"
                            {...register('phone_number', { required: 'Phone number is required' })}
                            error={errors.phone_number?.message}
                        />
                        <Input
                            label="Alternate Phone Number"
                            {...register('alternate_phone_number')}
                            error={errors.alternate_phone_number?.message}
                        />
                        <Select
                            label="Gender"
                            options={genders}
                            {...register('gender')}
                            error={errors.gender?.message}
                        />
                        <Input
                            label="Nationality"
                            {...register('nationality', { required: '  Nationality is required' })}
                            error={errors.nationality?.message}
                        />
                    </div>
                </Card>
                {/* IDENTIFICATION */}
                <Card title="Identification">
                    <div className="form-grid"> 
                        <Select
                            label="ID Type"
                            options={idTypes}
                            {...register('id_type', { required: 'ID type is required' })}
                            error={errors.id_type?.message}
                        />
                        <Input
                            label="ID Number"
                            {...register('id_number', { required: 'ID number is required' })}
                            error={errors.id_number?.message}
                        />
                        <Input  
                            label="ID Issued Date"
                            type="date"
                            {...register('id_issued_date', { required: 'Issued date is required' })}
                            error={errors.id_issued_date?.message}
                        />
                        <Input
                            label="ID Expiry Date"
                            type="date"
                            {...register('id_expiry_date', { required: 'Expiry date is required' })}
                            error={errors.id_expiry_date?.message}
                        />
                    </div>
                </Card>
                {/* ADDRESS */}
                <Card title="Address">
                    <div className="form-grid">
                        <TextArea
                            label="Street Address"
                            {...register('street_address', { required: 'Street address is required' })}
                            error={errors.street_address?.message}
                        />
                        <Input
                            label="City"
                            {...register('city', { required: 'City is required' })}
                            error={errors.city?.message}
                        />
                        <Input
                            label="State/Province"
                            {...register('state_province', { required: 'State/Province is required' })}
                            error={errors.state_province?.message}
                        />
                        <Input
                            label="Postal Code"
                            {...register('postal_code', { required: 'Postal code is required' })}
                            error={errors.postal_code?.message}
                        />
                        <Input
                            label="Country"
                            {...register('country', { required: 'Country is required' })}
                            error={errors.country?.message}
                        />
                    </div>
                </Card>
                {/* STATUS  */}
                <Card title="Status">
                    <div className="form-grid">
                        <Select
                            label="Status"
                            options={[
                                { value: 'active', label: 'Active' },
                                { value: 'inactive', label: 'Inactive' },
                            ]}
                            {...register('status', { required: 'Status is required' })}
                            error={errors.status?.message}
                        />
                    </div>
                </Card>
                {/* SAVE BUTTON  */}
                <div className="form-actions">
                    <Button
                        type="submit"
                        variant="primary"
                        disabled={isSubmitting}
                    >
                        {isSubmitting ? 'Creating...' : 'Create Guest'}
                    </Button>
                </div>      
            </form> 
        </div>  
    );  
};
export default GuestCreate;

                            
