# backend/app/models/RoomTypeModel.py

from typing import Optional, List, Dict, Any
from backend.config.db_connect import get_connection

class RoomTypeModel:
	@staticmethod
	def create_room_type(
        type_name: str,
        description: Optional[str],
        base_price: float,
        default_capacity: int,
        bed_count: int,
        amenities: Optional[str]
    ) -> Optional[int]:
        """
           Insert a new room type into the database.
        """
        conn = get_connection()
        if not conn:
            print(f"[RoomTypeModel] Database connection failed.")
            return None
        
        try:
            cursor = conn.cursor()
            sql = """
                    INSERT INTO room_types (
                        type_name, description, base_price, default_capacity, bed_count, amenities
                    )
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                values = (type_name, description, base_price, default_capacity, bed_count, amenites)
                cursor.execute(sql, values)
                conn.commit()
                return cursor.lastrowid
            except Exception as e:
                print(f"[Error] Creating room type: {e}")
                return None 
            finally:
                cursor.close()
                conn.close()
                
    @staticmethod
    def get_room_type_id(room_type_id: int) -> Optional[Dict[str, Any]]:
        """
            Fetch a room type by ID. 
        """
        conn = get_connection()
        if not conn:
            print("[RoomTypeModel] Database connection failed.")
            return None
        
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM room_types WHERE room_type_id = %s", (room_type_id,))
            return cursor.fetchone()
        except Exception  as e:
            print(f"[RoomTypeModel] Error Fetching room type by ID: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def get_all_room_type() -> List[Dict[str, Any]]:
        """
            Fetch all room types.
        """
        conn = get_connection()
        if not conn:
            print("[RoomTypeModel] Database connection failed.")
            return []
            
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM room_types ORDER BY created_at DESC")
            return cursor.fetchall()
        except Exception as e:
            print(f"[Error] Fetching all room types: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod 
    def update_room_type(
            room_type_id: int,
            type_name: Optional[str] = None 
            description: Optional[str] = None 
            base_price: Optional[float] = None 
            default_capacity: Optional[int] = None 
            bed_count: Optional[int] = None 
            amenites: Optional[str] = None
        ) -> bool:
            """
                Update a room type record. 
            """
            conn = get_connection()
            if not conn:
                print("[RoomTypeModel] Database connection failed.")
                return False 
                
            try:
                cursor = conn.cursor()
                fields = []
                value = []
                
                if type_name is not None:
                    fields.append("type_name = %s")
                    values.append(type_name)
                if description is not None:
                    fields.append("description = %s")
                    values.append(description)
                if base_price is not None:
                    fields.append("base_price = %s")
                    values.append(base_price)
                if default_capacity is not None:
                    fields.append("default_capacity = %s")
                    values.append(default_capacity)
                if bed_count is not None:
                    fields.append("bed_count = %s")
                    values.append(bed_count)
                if amenities is not None:
                    fields.append("amenities = %s")
                    values.append(amenites)
                    
            if not fields:
                print("[RoomTypeModel] No fields to update.")
                return False
                
                sql = f"UPDATE room_types SET {', '.join(fields)} WHERE room_type_id = %s"
                values.append(room_type_id)
                
                cursor.execute(sql, tuple(values))
                conn.commit()
                updated = cursor.rowcount >
                if updated:
                    print(f"[RoomTypeModel] Room type {room_type_id} updated.")
                else:
                    print(f"[RoomTypeModel] No update performed for room type {room_type_id}.")
                        
                return updated
            except Exception as e:
                print(f" [Error] Updating room type: {e}")
                return False
            finally:
                cursor.close()
                conn.close()
                
    @staticmethod
    def delete_room_type(room_type_id: int) ->bool:
        """
            Delete a room type by ID.
        """
        conn = get_connection()
        if not conn:
            print("[RoomTypeModel] Database connection failed.")
            return False 
            
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM room_types WHERE room_type_id = %s", (room_type_id,))
            conn.commit()
            deleted = cursor.rowcount > 0
            if deleted:
                print(f"[RoomTypeModel] Room Type {room_type_id} deleted.")
            else:
                print(f"[RoomTypeModel] Room type {room_type_id} not found.")
            return deleted            
        except Exception as e:
            print(f"[RoomTypeModel] Error deleting room type: {e}")
            return False 
        finally:
            cursor.close()
            conn.close()