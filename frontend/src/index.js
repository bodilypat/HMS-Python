import React, { Suspense, lazy } from 'react';
import { Routes, Route, Nevigate } from 'react-router-dom';
import ProtectedRoute from '.ProtectedRoute';

// Lazy-loaded pages
const Home = lazy(() => import('../pages/Home'));
const Login = lazy(() => import('../pages/Login'));
const Register = lazy(() => import('../pages/Register'));
const Dashboard = lazy(() => import('../pages/Dashboard'));
const Booking = lazy(() => import('../pages/Booking'));
const Rooms = lazy(() => import('../pages/Rooms'));
const Feedback = lazy(() => import('../pages/Feedback'));
const Profile = lazy(() => import('../pages/Profile'));
const NotFound = () => <h2<404 - Page Not Found</h2>;

const AppRoutes = () => {
	return (
		<Suspense fallback={<div>Loading...</div>} />
			<Routes>
				{/* Public routes */}
				<Route path="/" element={Home />} />
				<Route path="/login" element={<Login />} />
				<Route path="/register" element={<Register />} />
				
				{/* Protected routes */}
				<Route path="/dashboard" element={<Dashboard />} />
					<Route element={<ProtectedRoute />} />
					<Route path="/booking" element={<Booking />} />
					<Route path="/rooms" element={<Rooms />} />
					<Route path="/feedback" element={<Feedback />} />
					<Route path="/profile" element={<Profile />} />
				</Route>
				{/* Catch-all for 404 */}
				<Route path="*" element={<NotFound />} />
			</Routes>
		</Suspense>
	);
};
export default AppRoutes;
			
