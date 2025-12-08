//src/services/guestService.js 

const API_URL = '../api/guestApi';

/* Helper */

/* Normalize quest object fields  */
const formatGuests = (guests) => {
    ...guest
const guestService = {
    /* Fetch all guests with optional formatting/deduping */
    async getAllGuests() {
        try {
            const { data } = await guestApi.getAllGuests();
            return formatGuests(data);
        } catch (error) {
            console.error('Error in service fetching guests:', error);
            throw error;
        }
    },

    /* Fetch a guest by ID */
    async getGuestById(guestId) {
        try {
            const { data } = await guestApi.getGuestById(guestId);
            return data;
        } catch (error) {
            console.error(`Error in service fetching guest with ID ${guestId}:`, error);
            throw error;
        }
    },

    /* Create a new guest */
    async createGuest(guestData) {
        try {
            const { data } = await guestApi.createGuest(guestData);
            return data;
        } catch (error) {
            console.error('Error in service creating guest:', error);
            throw error;
        }
    },

    /* Update an existing guest */
    async updateGuest(guestId, guestData) {
        try {
            const { data } = await guestApi.updateGuest(guestId, guestData);
            return data;
        } catch (error) {
            console.error(`Error in service updating guest with ID ${guestId}:`, error);
            throw error;
        }
    },

    /* Delete a guest */
    async deleteGuest(guestId) {
        try {
            const { data } = await guestApi.deleteGuest(guestId);
            return data;
        } catch (error) {
            console.error(`Error in service deleting guest with ID ${guestId}:`, error);
            throw error;
        }
    },
};
export default guestService;

