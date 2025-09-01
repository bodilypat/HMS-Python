/* src/routes/ProtectedRoute.js */
import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';

const ProtectedRoute = ({ children }) => {
	const { user, isAuthenticated } = useAuth();
	
	if (!isAuthenticated) {
		return <Navigate to="/login" replace />;
	}
	return children;
};
export default ProtectedRoute;


