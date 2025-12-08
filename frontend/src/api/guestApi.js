//src/api/guestApi.js

import axiosClient from '../axiosClient';
/* Helpers */

/* Standardized error handler */
const handleApiError = (action, error) => {
  console.error(`guestApi: Error during ${action}:`, error?.response );
  throw error;
}

/* Ensure required parameter is provided */
const requireParam = (value, name) => {
  if (!value) throw new Error(`${name} is required`);
};

/* Guest API */
const guestApi = {
  /* Fetch all guests */
  getAllGuests: async () => {
    try {
      const response = await axiosClient.get('/guests');
      return response.data;
    } catch (error) {
      handleApiError('fetching guests', error);
    }
  },

  /* Fetch a guest by ID */
  getGuestById: async (guestId) => {
    if (!guestId) throw new Error('Guest ID is required');

    try {
      const response = await axiosClient.get(`/guests/${guestId}`);
      return response.data;
    } catch (error) {
      handleApiError(`fetching guest with ID ${guestId}`, error);
    }
  },

  /* Create a new guest */
  createGuest: async (guestData) => {
    if (!guestData) throw new Error('Guest data is required');

    try { 
      const response = await axiosClient.post('/guests', guestData);
      return response.data;
    } catch (error) {
      console.error('Error creating guest:', error);
      throw error;
    }
  },

  /* Update an existing guest */
  updateGuest: async (guestId, guestData) => {
    if (!guestId) throw new Error('Guest ID is required');
    if (!guestData) throw new Error('Guest data is required');

    try {
      const response = await axiosClient.put(`/guests/${guestId}`, guestData);
      return response.data;
    } catch (error) {
      console.error(`Error updating guest with ID ${guestId}:`, error);
      throw error;
    }
  },

  /* Delete a guest */
  deleteGuest: async (guestId) => {
    if (!guestId) throw new Error('Guest ID is required');

    try {
      const response = await axiosClient.delete(`/guests/${guestId}`);
      return response.data;
    } catch (error) {
      console.error(`Error deleting guest with ID ${guestId}:`, error);
      throw error;
    }
  },
};
export default guestApi;
