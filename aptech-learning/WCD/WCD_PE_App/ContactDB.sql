CREATE DATABASE IF NOT EXISTS contactdb;
USE contactdb;

DROP TABLE IF EXISTS `Contact`;
DROP TABLE IF EXISTS `Group`;

CREATE TABLE `Group` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(100) NOT NULL,
  `description` VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `Contact` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `firstName` VARCHAR(100) NOT NULL,
  `lastName` VARCHAR(100) NOT NULL,
  `groupId` INT,
  `phoneNumber` VARCHAR(50) NOT NULL,
  FOREIGN KEY (`groupId`) REFERENCES `Group` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Seed Data for Group
INSERT INTO `Group` (id, name, description) VALUES
(1, 'Family', 'Nhom gia dinh'),
(2, 'Colleague', 'Nhom dong nghiep'),
(3, 'Friend', 'Nhom ban than');

-- Seed Data for Contact
INSERT INTO `Contact` (id, firstName, lastName, groupId, phoneNumber) VALUES
(1, 'Tran', 'Hoang', 1, '0924151616'),
(2, 'Nguyen', 'Phong', 1, '0924112116'),
(3, 'Dinh', 'Hoang Linh', 2, '0924242616'),
(4, 'Phuong', 'The Ngoc', 3, '0925125616'),
(5, 'Luong', 'Hong Dung', 3, '0922262612'),
(6, 'Vu', 'Dinh Cong', 1, '0923252616');
