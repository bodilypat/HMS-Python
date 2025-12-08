//src/api/staffApi.js 

import axiosClient from './axiosClient';

/* standard error handler  */
function handleApiError(action: string, error: any) {
    console.error(`Error ${action}:`, error);
    throw error;
}

const staffApi = {
    /* Fetch all staff members */
    async fetchStaff() {
        try {
            const response = await axiosClient.get('/staff');
            return response.data;
        } catch (error) {
            handleApiError('fetching staff', error);
        }
    },

    /* Fetch a single staff member by ID */
    async fetchStaffById(staffId: string) {
        try {
            const response = await axiosClient.get(`/staff/${staffId}`);
            return response.data;
        } catch (error) {
            handleApiError(`fetching staff with ID ${staffId}`, error);
        }
    },

    /* Create a new staff member */
    async createStaff(staffData: any) {
        try {
            const response = await axiosClient.post('/staff', staffData);
            return response.data;
        } catch (error) { 
            handleApiError('creating staff', error);
        }
    },

    /* Update an existing staff member */
    async updateStaff(staffId: string, staffData: any) {
        try {
            const response = await axiosClient.put(`/staff/${staffId}`, staffData);
            return response.data;
        } catch (error) {
            handleApiError(`updating staff with ID ${staffId}`, error);
        }
    },

    /* Delete a staff member */
    async deleteStaff(staffId: string) {
        try {
            const response = await axiosClient.delete(`/staff/${staffId}`);
            return response.data;
        } catch (error) {
            handleApiError(`deleting staff with ID ${staffId}`, error);        
        }
    },
};
export default staffApi;
