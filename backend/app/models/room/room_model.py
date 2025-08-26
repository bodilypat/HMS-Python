# backend/app/models/room/room_model.py

from backend.config.dbconnect import get_connection
from typing import Optional, List, Dict 

class RoomModel:
    @staticmethod
    def create_room(room_number: str,
                    room_type_id: int,
                    floor_number: int, 
                    price_per_night: float,
                    room_status: str = 'Available', 
                    room_description: Optional[str] = None,
                    beds_count: int = 1, 
                    capacity: int = 1
                ) -> Optional[int]:                        
            """
                Insert a new room into the database.
            """
            conn = get_connection()
            if not conn:
                print("[RoomModel] Database connection failed.")
                return None 
            
            try:
                cursor = conn.cursor()
                sql = """
                        INSERT   INTO rooms(
                            room_number, room_type_id, floor_number, price_per_night,
                            room_status, room_description, beds_count, capacity
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
                values = (
                    room_number, room_type_id, floor_number, price_per_night,
                    room_status, room_description, beds_count, capacity
                )
                cursor.execute(sql, values)
                conn.commit()
                return cursor.lastrowid
            except Exception as e:
                print(f"[RoomModel] Error creating room: {e}")
                return None
            finally:
                cursor.close()
                conn.close()
            
    @staticmethod
    def get_room_by_id(room_id: int) -> Optional[Dict]:
        """
            Retrieve room details by room ID.
        """
        conn = get_connection()
        if not conn:
            print("[RoomModel] Database connection failed.")
            return None
        
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM rooms room_id = %s", (room_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"[RoomModel] Error Fetching room by ID: {e}")
            return None 
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def get_all_rooms() -> List[Dict]:
        """
            Retrieve all rooms.
        """
        conn = get_connection()
        if not conn:
            print("[RoomModel] Database connection failed.")
            return []
            
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM rooms")
            return cursor.fetchall()
        except Exception as e:
            print(f"[RoomModel] Error Fetching all rooms: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod 
    def update_room_status(room_id: int, new_status: str) -> bool:
        """
            Update the status of a room (Available, Occupied, Maintenance). 
        """
        conn = get_connection()
        if not conn:
            print("[RoomModel] Database connection failed.")
            return False
            
        try:
            cursor = conn.cursor()
            sql = "UPDATE rooms SET room_status = %s WHERE room_id = %s"
            cursor.execute(sql, (new_status, room_id))
            conn.commit()
            updated = cursor.rowcount > 0
            print(f"[RoomModel] Room {room_id} status updated to {new_status}." if updated else print(f"[RoomModel] No update performed.")
            return updated
        except Exception as e:
            print(f"[RoomModel] Error updating room status: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def delete_room(room_id: int) ->bool:
        """
            Delete a room by its ID.
        """
        conn = get_connection()
        if not conn:
            print("[RoomModel] Database connection failed.")
            return False 
            
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM rooms WHERE room_id = %s", (room_id,))
            conn.commit()
            deleted = cursor.rowcount > 0
            print(f"{RoomModel] Room {room_id} deleted.") if deleted else print(f"[RoomModel] Room not found.")
            return deleted
        except Exception as e:
            print(f"[RoomModel] Error deleting room: {e}")
            return False 
        finally:
            cursor.close()
            conn.close()