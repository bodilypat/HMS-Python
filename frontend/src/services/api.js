/* src/services/api.js */
import axiosfrom 'axios';

const api = axios.create({
	baseURL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000/api',
	headers: {
		'Content-Type': 'application/json',
	},
	withCredentials: true,
});

api.interceptors.request.use((config) => {
	const token = localStorage.getItem('token');
	if (token) {
		config.headers.Authorization = 'Bearer ${token}';
	}
	return config;
});
expert default api;

