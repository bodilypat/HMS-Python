//src/components/forms/GuestForm.jsx 

import React, { useState, useEffect } from 'react';
import guestService from '../../services/guestService';

const GuestForm = ({ guest = null, onSuccess = () => {} }) => {
    const [firstName, setFirstName] = useState(guest ? guest.first_name : '');
    const [middleName, setMiddleName] = useState(guest ? guest.middle_name : '');   
    const [lastName, setLastName] = useState(guest ? guest.last_name : '');
    const [email, setEmail] = useState(guest ? guest.email : '');
    const [phoneNumber, setPhoneNumber] = useState(guest ? guest.phone_number : '');
    const [alternatePhone, setAlternatePhone] = useState(guest ? guest.alternate_phone : '');
    const [emergencyContact, setEmergencyContact] = useState(guest ? guest.emergency_contact : '');
    const [address, setAddress] = useState(guest ? guest.address : '');
    const [idType, setIdType] = useState(guest ? guest.id_type : 'Passport');
    const [idNumber, setIdNumber] = useState(guest ? guest.id_number : '');
    const [dob, setDob] = useState(guest ? guest.dob : '');
    const [gender, setGender] = useState(guest ? guest.gender : 'Other');
    const [nationality, setNationality] = useState(guest ? guest.nationality : 'Unknown');
    const [isActive, setIsActive] = useState(guest ? !!guest.is_active : true);
    const [errors, setErrors] = useState({});   
    const validate = () => {
        const e = {};
        if (!firstName || firstName.trim() === '') e.firstName = 'First name is required';
        if (!lastName || lastName.trim() === '') e.lastName = 'Last name is required';
        if (!dob) e.dob = 'Date of birth is required';
        setErrors(e);
        return Object.keys(e).length === 0;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!validate()) return;

        const guestData = {
            first_name: firstName.trim(),
            middle_name: middleName.trim(),
            last_name: lastName.trim(),
            email: email.trim(),
            phone_number: phoneNumber.trim(),
            alternate_phone: alternatePhone.trim(),
            emergency_contact: emergencyContact.trim(),
            address: address.trim(),
            id_type: idType,
            id_number: idNumber.trim(),
            dob,
            gender,
            nationality,
            is_active: isActive,
        };
        try {
            if (guest && guest.guest_id) {
                await guestService.updateGuest(guest.guest_id, guestData);
            } else {
                await guestService.createGuest(guestData);
            }
            onSuccess();
        } catch (error) {
            console.error('Error saving guest:', error);
        }
    };
    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>First Name:</label>
                <input type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)} />
                {errors.firstName && <span className="error">{errors.firstName}</span>}
            </div>
            <div>
                <label>Middle Name:</label>
                <input type="text" value={middleName} onChange={(e) => setMiddleName(e.target.value)} />
            </div>
            <div>
                <label>Last Name:</label>
                <input type="text" value={lastName} onChange={(e) => setLastName(e.target.value)} />
                {errors.lastName && <span className="error">{errors.lastName}</span>}
            </div>
            <div>
                <label>Email:</label>
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
            </div>
            <div>
                <label>Phone Number:</label>
                <input type="text" value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} />
            </div>
            <div>
                <label>Alternate Phone:</label>
                <input type="text" value={alternatePhone} onChange={(e) => setAlternatePhone(e.target.value)} />
            </div>
            <div>
                <label>Emergency Contact:</label>
                <input type="text" value={emergencyContact} onChange={(e) => setEmergencyContact(e.target.value)} />
            </div>
            <div>
                <label>Address:</label>
                <input type="text" value={address} onChange={(e) => setAddress(e.target.value)} />
            </div>
            <div>
                <label>ID Type:</label>
                <select value={idType} onChange={(e) => setIdType(e.target.value)}>
                    {['Passport', 'Driver License', 'National ID', 'Other'].map((type) => (
                        <option key={type} value={type}>{type}</option>
                    ))}
                </select>
            </div>
            <div>
                <label>ID Number:</label>
                <input type="text" value={idNumber} onChange={(e) => setIdNumber(e.target.value)} />
            </div>
            <div>
                <label>Date of Birth:</label>
                <input type="date" value={dob} onChange={(e) => setDob(e.target.value)} />
                {errors.dob && <span className="error">{errors.dob}</span>}
            </div>
            <div>
                <label>Gender:</label>
                <select value={gender} onChange={(e) => setGender(e.target.value)}>
                    {['Male', 'Female', 'Other'].map((option) => (  
                        <option key={option} value={option}>{option}</option>
                    ))}
                </select>
            </div>
            <div>   
                <label>Nationality:</label>
                <input type="text" value={nationality} onChange={(e) => setNationality(e.target.value)} />
            </div>
            <div>   
                <label>
                    <input type="checkbox" checked={isActive} onChange={(e) => setIsActive(e.target.checked)} />
                    Active  
                </label>
            </div>
            <button type="submit">Save Guest</button>
        </form>
    );
}
