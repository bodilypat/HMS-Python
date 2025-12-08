//src/api/axiosConfig.js 

import axios from 'axios';

/* ========== Axios Configuration ==========
* - Base URL 
* - JWT Attach on Requests
* - Auto Refresh on 401 
* - Refresh Queue (Prevents multiple parallel refresh calls)
* - Unified Error Normalization
* ==========================================
 */

const API_BASE_URL = 
    import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

    export const axiosInstance = axios.create({
        baseURL: API_BASE_URL,
        withCredentials: true,
        headers: {
            'Content-Type': 'application/json',
        },
    });

    /* TOKEN UTILS */
    const ACCESS_KEY = 'access_token';
    const REFRESH_KEY = 'refresh_token';

    const getAccessToken = () => localStorage.getItem(ACCESS_KEY);
    const getRefreshToken = () => localStorage.getItem(REFRESH_KEY);

    const setAccessToken = (token) => {
        localStorage.setItem(ACCESS_KEY, token);
    };

    const clearTokens = () => {
        localStorage.removeItem(ACCESS_KEY);
        localStorage.removeItem(REFRESH_KEY);
    };

    /* REFRESH LOGIC */
    let isRefreshing = false;
    let retryQueue = [];

    /* Resolves or rejects queued request when refresh finishes */
    const resolveRetryQueue = (error, newToken = null) => {
    retryQueue.forEach(({ resolve, reject }) => 
        error ? reject(error) : resolve(newToken)
    );
    retryQueue = [];
    };

    /* REQUEST INTERCEPTOR (Attaches access token) */
    axiosInstance.interceptors.request.use(
        (config) => {
            const token = getAccessToken();
            if (token) {
                config.headers['Authorization'] = `Bearer ${token}`;
            }
            return config;
        },
        (error) => Promise.reject(error)
    );

    /* RESPONSE INTERCEPTOR (Handles 401 and refresh) */
    axiosInstance.interceptors.response.use(
        (response) => response,
        async (error) => {
            const originalRequest = error.config;
            
            // If request already retried -> prevent infinite loops 
            if (originalRequest?._retry) {
                return Promise.reject(error);
            }

            const status = error?.response?.status;

            // Handle 401 Unauthorized (expired token)
            if (status === 401) {
                const refreshToken = getRefreshToken();

                // No refresh token -> user must log in manually 
                if (!refreshToken) {
                    clearTokens();
                    return Promise.reject(error);
                }

                // If refresh is already in progress -> queue request 
                if (isRefreshing) {
                    return new Promise((resolve, reject) => {
                        retryQueue.push({ resolve, reject });
                    })
                    .then((newToken) => {
                        originalRequest.headers.Authorization = `Bearer ${newToken}`;
                        return axiosInstance(originalRequest);
                    })
                    .catch(Promise.reject);
                }

                // Start refresh sequence 
                isRefreshing = true;

                try {
                    const refreshResponse = await axiosInstance.post(
                        `${API_BASE_URL}/auth/refresh/`,
                        { refresh: refreshToken }
                    );

                    const newAccessToken = refreshResponse.data?.access_token;

                    // If backend didn't return token -> treat as failure 
                    if (!newAccessToken) {
                        throw new Error('Refresh token failed: missing access token');
                    }

                    setAccessToken(newAccessToken);

                    // Update defaults for future requests
                    axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${newAccessToken}`;

                    // Release queued requests 
                    resolveRetryQueue(null, newAccessToken);


                    originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
                    return axiosInstance(originalRequest);
                } catch (refreshError) {
                    clearTokens();
                    resolveRetryQueue(refreshError, null);
                    return Promise.reject(refreshError);
                } finally {
                    isRefreshing = false;
                }
            };
            // Unified error normalization
            const normalizedError = {
                status: status || 500,
                message: error?.response?.data?.message || error.message,
                data: error?.response?.data || null,
                error: error.response?.data?.error || null,
            };

            return Promise.reject(normalizedError);
        }
    );




