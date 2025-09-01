/* src/routes/RoleBaseRoute.js */

import React from 'react';
import { Navigate } from 'react-router-dom';
import { userAuth } from '../hooks/useAuth';

const RoleBaseRoute = ({ children, allowedRoles }) => {
	const { user, isAuthenticated } = useAuth();
	
	if (!isAuthenticated) {
		return <Navigate to ="/login" replace />;
	}
	
	if (!allowedRoles.includes(user.role)) {
		return <Navigate to = "/unauthorized" replace />;
	}
	return children;
};
export default RoleBaseRoute;
