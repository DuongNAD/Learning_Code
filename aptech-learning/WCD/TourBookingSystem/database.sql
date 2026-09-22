CREATE DATABASE IF NOT EXISTS tour_booking_db;
USE tour_booking_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    destination VARCHAR(100) NOT NULL,
    departure_date DATE NOT NULL,
    price DOUBLE NOT NULL,
    status ENUM('Confirmed', 'Pending', 'Cancelled') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE destinations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    description TEXT,
    price DOUBLE NOT NULL,
    available_spots INT NOT NULL
);
