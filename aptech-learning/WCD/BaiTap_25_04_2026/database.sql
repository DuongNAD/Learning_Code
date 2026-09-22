CREATE DATABASE IF NOT EXISTS MobileDB;
USE MobileDB;

CREATE TABLE Mobile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DOUBLE NOT NULL,
    warranty VARCHAR(255),
    accessories VARCHAR(255),
    inOutStock BOOLEAN,
    image VARCHAR(500)
);

-- Dữ liệu mẫu ban đầu
INSERT INTO Mobile (name, price, warranty, accessories, inOutStock, image) VALUES 
('iPhone 15 Pro', 999.0, '12 Months', 'Cable, Box', true, 'https://via.placeholder.com/100x150?text=iPhone15'),
('Samsung Galaxy S24', 899.0, '12 Months', 'Cable, Box', true, 'https://via.placeholder.com/100x150?text=S24'),
('Xiaomi 14', 750.0, '18 Months', 'Charger, Cable, Case', false, 'https://via.placeholder.com/100x150?text=Xiaomi14');
