//src/api/roomApi.js 

import axiosCleint from '../axiosClient';

/* Standardized error handler */
const handleApiError = (action, error) => {
  console.error(`roomApi: Error during ${action}:`, error?.response );
  throw error;
}

/* Ensure required parameter is provided */
const requireParam = (value, name) => {
  if (!value) throw new Error(`${name} is required`);
};

/* Room API */
const roomApi = {
/* Fetch all rooms */
    getAllRooms: async () => {
        try {
        const response = await axiosCleint.get('/rooms');
        return response.data;
        } catch (error) {
        handleApiError('fetching rooms', error);
        }   
    },

/* Fetch a room by ID */
    getRoomById: async (roomId) => {
        requireParam(roomId, 'Room ID');
        try {
            const response = await axiosCleint.get(`/rooms/${roomId}`);
            return response.data;
        } catch (error) {
            handleApiError('fetching room by ID', error);
        }
    },

/* Create a new room */
    createRoom: async (roomData) => {
        requireParam(roomData, 'Room data');
        try {
            const response = await axiosCleint.post('/rooms', roomData);
            return response.data;
        } catch (error) {
            handleApiError('creating room', error);
        }
    },
/* Update an existing room */
    updateRoom: async (roomId, roomData) => {
        requireParam(roomId, 'Room ID');
        requireParam(roomData, 'Room data');
        try {
            const response = await axiosCleint.put(`/rooms/${roomId}`, roomData);
            return response.data;
        } catch (error) {
            handleApiError('updating room', error);
        }
    },  
/* Delete a room */
    deleteRoom: async (roomId) => {
        requireParam(roomId, 'Room ID');
        try {
            const response = await axiosCleint.delete(`/rooms/${roomId}`);
            return response.data;
        } catch (error) {
            handleApiError('deleting room', error);
        }
        },
    };
export default roomApi;
