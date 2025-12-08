//src/api/authApi.js 

import axiosClent from '../api/axiosClent';

/* Helpers */
const requireParam = (value, name) => {
    if (value === undefined || value === null) {
        throw new Error(`Parameter "${name}" is required.`);
    };

    const handleApiError = (action, error) => {
        console.error(`Error during ${action}:`, error);
        throw error;
    };

    /* Auth API */
export const authService = {
    /* Check if user is logged in */
    isAuthenticated() {
        return !!storage.getAccessToken();
    },

    /* Get access token for axios interceptors */
    getAccessToken() {
        return storage.getAccessToken();
    },

    /* Clears session without contacting server (forced logout) */
    forceLogout() {
        storage.clearSession();
    },

    /* Refresh access token using refresh token, typically invoked automatically from axios interators. */
    async refreshToken() {
        try {
            const refreshToken = storage.getRefreshToken();
            if (!refreshToken) {
                throw new Error('No refresh token available.');
            }
            const response = await axiosClent.post('/auth/refresh-token', {
                refreshToken: refreshToken,
            });
            const { accessToken, refreshToken: newRefreshToken } = response.data;
            storage.setSession(accessToken, newRefreshToken);
            return accessToken;
        } catch (error) {
            handleApiError('token refresh', error);
        }
    },

    /* Login with email and password */
    async login(email = requireParam(email, 'email'), password = requireParam(password, 'password')) {
        try {
            const response = await axiosClent.post('/auth/login', {
                email: email,
                password: password,
            });
            const { accessToken, refreshToken } = response.data;
            storage.setSession(accessToken, refreshToken);
            return response.data;
        } catch (error) {
            handleApiError('login', error);
        }
    },

    /* Logout user */
    async logout() {
        try {
            await axiosClent.post('/auth/logout');
        } catch (error) {
            handleApiError('logout', error);
        } finally {
            this.forceLogout();
        }
    },

    /* Password reset workflow */
    async requestPasswordReset(email = requireParam(email, 'email')) {
        try {
            await axiosClent.post('/auth/request-password-reset', {
                email: email,
            });
        } catch (error) {
            handleApiError('password reset request', error);
        }
    },

    async resetPassword(token = requireParam(token, 'token'), newPassword = requireParam(newPassword, 'newPassword')) {
        try {
            await axiosClent.post('/auth/reset-password', {
                token: token,
                newPassword: newPassword,
            });
        } catch (error) {
            handleApiError('password reset', error);
        }
    },  
};

/* Helpers for session storage */
const storage = {
    setSession(accessToken, refreshToken) {
        localStorage.setItem('accessToken', accessToken);
        localStorage.setItem('refreshToken', refreshToken);
    },

    getAccessToken() {
        return localStorage.getItem('accessToken');
    },

    getRefreshToken() {
        return localStorage.getItem('refreshToken');
    },

    clearSession() {
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');
    }
};

