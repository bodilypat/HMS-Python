//src/services/authService.js 

import { authApi } from '../api/authApi';

/* Helpers */

/* Validate required parameters */
const requireParam = (value, name) => {
    if (!value) throw new Error(`${name} is required`);
};

/* Centralized error handler */
const handleServiceError = (action, error) => {
    console.error(`authService: Error during ${action}:`, error?.response);
    throw error;
};

/* Local storage keys */
const ACCESS_TOKEN_KEY = 'accessToken';
const REFRESH_TOKEN_KEY = 'refreshToken';
const USER_KEY = 'authUser';

/* Storage Utilities */
const storage = {
    setSession: (accessToken, refreshToken, user) => {
        if (accessToken) localStorage.setItem(ACCESS_TOKEN_KEY, accessToken);
        if (refreshToken) localStorage.setItem(REFRESH_TOKEN_KEY, refreshToken);
        if (user) localStorage.setItem(USER_KEY, JSON.stringify(user));
    },

    clearSession: () => {
        localStorage.removeItem(ACCESS_TOKEN_KEY);
        localStorage.removeItem(REFRESH_TOKEN_KEY);
        localStorage.removeItem(USER_KEY);
    },

    getAccessToken: () => localStorage.getItem(ACCESS_TOKEN_KEY),

    getRefreshToken: () => localStorage.getItem(REFRESH_TOKEN_KEY),

    getUser: () => {
        const user = localStorage.getItem(USER_KEY);
        return user ? JSON.parse(user) : null;
    }
};

/* Auth Service (Business Logic) */
const authService = {
    /* Perform login and store store tokens */
    async login(credentials) {
        requireParam(credentials, 'credentials');

        try {
            const data = await authApi.login(credentials);

            storage.setSession({
                accessToken: data ? data.accessToken : null,
                refreshToken: data ? data.refreshToken : null,
                user: data ? data.user : null
            });
            return data;
        } catch (error) {
            handleServiceError('login', error);
        }
    },

    /* Perform logout and clear stored tokens */
    async logout() {
        try {
            await authApi.logout();
            storage.clearSession();
        } catch (error) {
            console.warn('authService: Logout failed, clearing local session anyway.', error);
            storage.clearSession(); 
            handleServiceError('logout', error);
        }
        storage.clearSession();
    },

    /* Returns the current authenticated user */
    getCurrentUser() {
        return storage.getUser();
    },

    /* Check if user is logged in */
    isAuthenticated() {
        return !!storage.getAccessToken();
    },

    /* Refresh access token using refresh token, typically invoked automatically from axios interators. */
    async refreshToken() {
        const refreshToken = storage.getRefreshToken();
        requireParam(refreshToken, 'refreshToken');

        try {
            const data = await authApi.refreshToken({ refreshToken });
            storage.setSession({
                accessToken: data ? data.accessToken : null,
                refreshToken: data ? data.refreshToken : null
            });
            return data;
        } catch (error) {
            handleServiceError('refreshToken', error);
        }
    },

    /* Get access token for axios interceptors */
    getAccessToken() {
        return storage.getAccessToken();
    },

    /* Clears session without contacting server (forced logout) */
    forceLogout() {
        storage.clearSession();
    },

    /* Password reset workflow */
    async requestPasswordReset(email) {
        requireParam(email, 'email');

        try {
            return await authApi.requestPasswordReset({ email });
        } catch (error) {
            handleServiceError('requestPasswordReset', error);
        }
    },

    async resetPassword(token, newPassword) {
        requireParam(token, 'token');
        requireParam(newPassword, 'newPassword');
        try {
            return await authApi.resetPassword({ token, newPassword });
        } catch (error) {
            handleServiceError('resetPassword', error);
        }
    }
};
export default authService;
