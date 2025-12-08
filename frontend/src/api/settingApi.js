//src/api/settingApi.js 

import axiosClient from './axiosClient';

function handleApiError(action: string, error: any): void {
    console.error(`Error ${action}:`, error);

  // Additional error handling logic can be added here
}

export const settingApi = {
    async fetchSettings() {
        try {
            const response = await axiosClient.get('/settings');
            return response.data;
        } catch (error) {
            handleApiError('fetching settings', error);
        }
    },

    async updateSettings(settingsData: any) {
        try {
            const response = await axiosClient.put('/settings', settingsData);
            return response.data;
        } catch (error) {
            handleApiError('updating settings', error);
        }
    },
};
