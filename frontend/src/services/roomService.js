//src/srevices/roomService.js 

import { roomApi } from '../api/roomApi';

/* Helpers */
const requireParam = (value, name) => {
    if (!value) throw new Error(`${name} is required`);
};

/* Standardized service error wrapper */
const handleServiceError = (action, error) => {
    console.error(`roomService: Error during ${action}:`, error?.response);
    throw error;
};

/* Format room object (normalize room data) */
const formatRoom = (room) => {
    return {
        id: room.id,
        number: room.number,
        type: room.type,
        status: room.status,
        price: room.price,
        amenities: room.amenities || [],
        description: room.description || ''
    };
};
/* Format List */
const formatRooms = (rooms) => {
    return rooms.map(formatRoom);
};

/* Format availability response */
const formatAvailability = (availability) => {
    return {
        roomId: availability.roomId,
        availableDates: availability.availableDates || []
    };
};

/* Room Service (business logic) */
const roomService = {
    /* Get all rooms */
    async getAllRooms() {
        try {
            const { data } = await roomApi.getAllRooms();
            return formatRooms(data);
        } catch (error) {
            handleServiceError('fetching all rooms', error);
        }
    },

    /* Get room by ID */
    async getRoomById(roomId) {
        requireParam(roomId, 'Room ID');    
        try {
            const { data } = await roomApi.getRoomById(roomId);
            return formatRoom(data);
        } catch (error) {
            handleServiceError(`fetching room with ID ${roomId}`, error);
        }
    },

    /* Check room availability */
    async checkRoomAvailability(roomId, startDate, endDate) {
        requireParam(roomId, 'Room ID');
        requireParam(startDate, 'Start date');
        requireParam(endDate, 'End date');
        try {
            const { data } = await roomApi.checkRoomAvailability(roomId, startDate, endDate);
            return formatAvailability(data);
        } catch (error) {
            handleServiceError(`checking availability for room ID ${roomId}`, error);
        }
    }

    /* create room */
    async createRoom(roomData) {
        requireParam(roomData, 'Room data');
        try {
            const { data } = await roomApi.createRoom(roomData);
            return formatRoom(data);
        } catch (error) {
            handleServiceError('creating room', error);
        }
    },

    /* update room */
    async updateRoom(roomId, roomData) {
        requireParam(roomId, 'Room ID');
        requireParam(roomData, 'Room data');
        try {
            const { data } = await roomApi.updateRoom(roomId, roomData);
            return formatRoom(data);
        } catch (error) {
            handleServiceError(`updating room with ID ${roomId}`, error);
        }
    },

    /* delete room */
    async deleteRoom(roomId) {
        requireParam(roomId, 'Room ID');
        try {
            const { data } = await roomApi.deleteRoom(roomId);
            return data;
        } catch (error) {
            handleServiceError(`deleting room with ID ${roomId}`, error);
        }
    },

    /* Room Type */
    async getAllRoomTypes() {
        try {
            const { data } = await roomApi.getAllRoomTypes();
            return data;
        } catch (error) {
            handleServiceError('fetching all room types', error);
        }
    },

    async getRoomTypeById(typeId) {
        requireParam(typeId, 'Type ID');
        try {
            const { data } = await roomApi.getRoomTypeById(typeId);
            return data;
        } catch (error) {
            handleServiceError(`fetching room type with ID ${typeId}`, error);
        }
    },

    async createRoomType(typeData) {
        requireParam(typeData, 'Type data');
        try {
            const { data } = await roomApi.createRoomType(typeData);
            return data;
        } catch (error) {
            handleServiceError('creating room type', error);
        }
    },

    async updateRoomType(typeId, typeData) {
        requireParam(typeId, 'Type ID');
        requireParam(typeData, 'Type data');
        try {
            const { data } = await roomApi.updateRoomType(typeId, typeData);
            return data;
        } catch (error) {
            handleServiceError(`updating room type with ID ${typeId}`, error);
        }
    },

    async deleteRoomType(typeId) {
        requireParam(typeId, 'Type ID');
        try {
            const { data } = await roomApi.deleteRoomType(typeId);
            return data;
        } catch (error) {
            handleServiceError(`deleting room type with ID ${typeId}`, error);
        }
    },
};
