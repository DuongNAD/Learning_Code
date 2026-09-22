CREATE DATABASE IF NOT EXISTS user_management_db;
USE user_management_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO users (username, password, email) VALUES ('admin', 'admin123', 'admin@example.com');
INSERT INTO users (username, password, email) VALUES ('user1', '123456', 'user1@example.com');
