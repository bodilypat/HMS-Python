//src/services/staffService.js 

import { staffApi } from '../api/staffApi';

const roomService = {
  getStaffList: async () => {
    try {
        const response = await staffApi.getAll();
        return response.data;
        } catch (error) {
            console.error('Error fetching staff list:', error);
            throw error;
        }
    },
    getStaffById: async (id) => {   
        try {
            const response = await staffApi.getById(id);
            return response.data;
        } catch (error) {
            console.error(`Error fetching staff with ID ${id}:`, error);
            throw error;
        }
    },  
    createStaff: async (staffData) => {
        try {
            const response = await staffApi.add(staffData);
            return response.data;
        } catch (error) {
            console.error('Error creating staff:', error);
            throw error;
        }   
    },
    updateStaff: async (id, staffData) => {
        try {   
            const response = await staffApi.update(id, staffData);
            return response.data;
        }
        catch (error) {
            console.error(`Error updating staff with ID ${id}:`, error);
            throw error;
        }
    },
    deleteStaff: async (id) => {
        try {
            const response = await staffApi.delete(id); 
            return response.data;
        } catch (error) {
            console.error(`Error deleting staff with ID ${id}:`, error);
            throw error;
        }
    }
};