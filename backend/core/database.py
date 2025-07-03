import mysql.connector
from mysql.connector import errorcode 
from dotenv import load_dotenv
import os

# Load environment variables 
load_dotenv(dotenv_path="config/.env")

DB_CONFIG = {
    'host': os.getenv("DB_HOST"),
    'port': int(os.geteenv("DB_PORT")),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'database': os.getenv("DB_NAME")
   }
   
   TABLES = {}
   
   # USERS
   TABLES['users'] = """
   CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        full_name VARCHAR(100) NOT NULL,
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        password_hash VARCHAR(255) NOT NULL,
        role ENUM('Admin','Manager','Receptionist','Staff','Guest')NOT NULL DEFAULT 'Guest',
        phone_number VARCHAR(20),
        status ENUM('Active','Inactive','Reception','Staff','Guest') NOT NULL DEFAULT'Guest',
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
    """
    # GUESTS
    TABLES['guests'] = """
    CREATE TABLE IF NOT EXISTS guests (
        guest_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        phone_number VARCHAR(20),
        address TEXT,
        id_type ENUM('Passsport','National ID','Driver Lincence') NOT NULL,
        id_number VARCHAR(50) NOT NULL,
        dob DATE NOT NULL,
        nationality VARCHAR(50) DEFAULT 'Unknown',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
    """
    # ROOM TYPES
    TABLES['room_types'] = """
    CREATE TABLE IF NOT EXISTS room_types (
        room_type_id INT AUTO_INCREMENT PRIMARY KEY,
        type_name VARCHAR(50) UNIQUE NOT NULL,
        description TEXT,
        base_price DECIMAL(10, 2) NOT NULL CHECK (base_price >= 0),
        default_capacity INT NOT NULL DEFAULT 1 CHECK (default_capacity > 0),
        bed_count INT NOT DEFAULT 1 CHECK (bed_count > 0)
        amenities TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
    """
    # ROOMS
    TABLES['rooms'] === """
    CREATE TABLE IF NOT EXISTS rooms (
        room_id INT AUTO_INCREMENT PRIMARY KEY,
        room_number VARCHAR(10) NOT NULL,
        room_type_id INT NOT NULL,
        floor_number INT NOT NULL CHECK (floor_nunber > = 0),
        price_per_night DECIMAL(10,2) NOT NULL CHECK (price_per_night >= 0)
        room_status ENUM('Available','Occupied','Maintenance') NOT NULL DEFAULT 'Available',
        room_description TEXT,
        beds_count INT NOT NULL CHECK (beds_count > 0),
        capacity INT NOT NULL CHECK(capacity >= beds_count),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
    """
    # RESERVATIONS
    TABLES['reservations'] = """
    CREATE TABLE IF NOT EXISTS reservations (
        reservation_id INT AUTO_INCREMENT PRIMARY KEY,
        guest_id INT NOT NULL,
        room_id INT,
        check_in DATE NOT NULL,
        check_out DATE NOT NULL,
        number_of_guests INT NOT NULL DEFAULT 1 CHECK (number_of_guests > 0),
        reservation_status ENUM('Pending','confirmed','Checked-in','Checked-out','Cancelled') NOT NULL DEFAULT 'Pending', 
        payment_status ENUM('Pending','Paid','Partially Paid','Refunded') NOT NULL DEFAULT 'Pending',
        booking_source ENUM('Website','Phone','Walk-in','Traval Agency','OTA') NOT NULL,
        special_request TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        CONSTRAINT chk_date CHECK (check_in <= check_out),
        FOREIGN KEY (guest_id) REFERENCES guests(guest_id) ON DELETE CASCADE,
        FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE SET NULL
    );
    """
    # PAYMENTS
    TABLES['payment'] = """
    CREATE TABLE IF NOT EXISTS payments (
        payment_id INT AUTO_INCREMENT PRIMARY KEY,
        reservation_id INT NOT NULL,
        amount_paid DECIMAL NOT NULL CHECK(amount_paid >= 0),
        currency VARCHAR(3) NOT NULL DEFAULT 'USD',
        payment_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        payment_method ENUM('Credit card','Cash','Online Transfer','Other') NOT NULL,
        payment_status ENUM('Completed','Peding','Failed') NOT NULL DEFAULT 'Pending',
        transaction_reference VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id) ON DELETE CASCADE
    );
    """
    # BILLINGS
    TABLES['billings'] = """
    CREATE TABLE IF NOT EXISTS billings (
        billing_id INT AUTO_INCREMENT PRIMARY KEY,
        reservation_id INT NOT NULL,
        service_charge DECIMAL(10, 2) DEFAULT 0.00 CHECK (service_charge >= 0),
        discount DECIMAL(10, 2) DEFAULT 0.00 CHECK (discount >= 0),
        total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0),
        payment_status ENUM('Paid','Unpaid') NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id) ON DELETE CASCADE 
    );
    """
    # SERVICES
    TABLES['services'] = """
    CREATE TABLE IF NOT EXISTS services (
        service_id INT AUTO_INCREMENT PRIMARY KEY,
        service_type VARCHAR(100) NOT NULL,
        category VARCHAR(50),
        description TEXT,
        price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
        is_active BOOLEAN NOT NULL DEFAULT TRUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
    """
    # ROOM SERVICES
    TABLES['room_services'] = """
    CREATE TABLE IF NOT EXISTS room_services (
        room_serive_id INT AUTO_INCREMENT PRIMARY KEY,
        reservation_id INT NOT NULL,
        service_id INT,
        service_request_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        service_status ENUM('Requested','In Process','Delivered','Cancelled') NOT NOT DEFAULT 'Requested',
        note TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        CHECK (service_request_time <= NOW())
        FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id) ON DELETE CASCADE,
        FOREIGN KEY (service_id) REFERENCES services(service_id) NO DELETE SET NULL
    );
    """
    # STAFFS
    TABLES['staffs'] = """
    CREATE TABLE IF NOT EXISTS staffs (
        staff_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100) NOT NUPLL,
        last_name VARCHAR(100) NOT NULL,
        role ENUM('Receptionist','Housekeeper','Manager','Other') NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        phone_number VARCHAR(15),
        salary DECIMAL(10, 2) NOT NULL CHECK(salary >= 0),
        hire_date DATE NOT NULL,
        status ENUM('Active','Inactive') NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
    """
    # HOUSEKEEPING
    TABLES['housekeepings'] = """
    CREATE TABLE IF NOT EXISTS housekeepings (
        housekeeping_id INT AUTO_INCREMENT PRIMARY KEY,
        room_id INT NOT NULL,
        staff_id INT NOT NULL,
        cleaning_date DATETIME NOT NULL,
        cleaning_status ENUM('Pending','In Process','Completed') NOT NULL,
        CHECK (cleaning_date <= NOW()),
        FOREIGN KEY(room_id) REFERENCES rooms(room_id) ON DELETE CASCADE,
        FOREIGN KEY(staff_id) REFERENCES staffs(staff_id) ON DELETE CASCADE
    );
    """
    # FEEDBACKS
    TABLES['feedbacks'] = """
    CREATE TABLE IF NOT EXISTS feedbacks (
        feedback_id INT AUTO_INCREATE PRIMARY KEY,
        guest_id INT NOT NULL,
        reservation_id INT NOT NULL,
        rating INT NOT NULL CHECK(rating BETWEEN 1 AND 5),
        coments TEXT,
        feedback_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (guest_id) REFERENCES guests(guest_id) ON DELETE CASCADE,
        FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id) ON DELETE CASCADE
    );
    """
    
    # Create tables
    def create_tables():
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            print("Connected to database.")
        
            for name, ddl in TABLES.items():
                print(f"Creating table '{name}'...")
                cursor.execute(ddl)
                print(f" Table '{name}' created (or already exists).")
            
            conn.commit()
            cursor.close()
            conn.close()
            print("All tables created successfully.")
        
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print(" Access denied. check your DB credentials.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print(" Database does not exist.")
            else:
                print(f" Error: {err}")
        except Exception as e:
            print(f " Unexpected error: {e}")
    
    # optional run
    if __name__ == "__main__":
        create_tables()
        