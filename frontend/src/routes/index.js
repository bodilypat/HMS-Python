/* src/routes/index.js */
import React from 'react';
import { Routes, Route } from 'react-router-dom';

import Login from '../pages/auth/login';
import Register from '../pages/auth/register';
import Dashboard from '../pages/Dashboard';
import BookingList from '../pages/Booking/BookingList';

import ProtectRoute from './ProtectedRoute';
import RoleBaseRoute from './RoleBaseRoute';

const AppRoutes = () => {
	return (
		<Routes>
			</* Public Routes */}
			<Route path="login" element={<Login />} />
			<Route path="/register" element={<Register />} />
			
			{/* Protected Routes */}
			<Route 
				path="/dashboard"
				element={
					<ProtectedRoute>
						<Dashboard />
					</ProtectedRoute>
				}
			/>
		</Routes>
	);
};
export default AppRoutes;
