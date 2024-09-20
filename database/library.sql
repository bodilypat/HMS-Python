CREATE DATABASE library;

USE library;

CREATE TABLE authors(
    id INT AUTO_INCREMENT KEY,
    name VARCHAR(255) NOT NULL,
    birthdate date,
    nitionality VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE books(
    id INT AUTO_INCREMENT PRIMARTY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    pulishered_date DATE,
    isbn VARCHAR(20) UNIQUE, 
    available INT DEFAULT 1
);

CREATE TABLE publishers(
    id INT AUTO_INCREMENT KEY,
    name VARCHAR(200) NOT NULL,
    address VARCHAR(255),
    contact_number VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE borrows(
    id INT AUTO_INCREMENT KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCE users(id);
    FOREIGN KEY (book_id) REFERENCE books(id);
);

CREATE TABLE users(
    id INT AUTO_INCREMENT KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(15);
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);

