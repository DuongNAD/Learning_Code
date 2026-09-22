-- ==========================================================
-- SCRIPT TẠO CƠ SỞ DỮ LIỆU BÁN MÁY ẢNH (PRJ301 - FPT UNIVERSITY)
-- Thiết kế: Tách riêng bảng Admin và User (Khách hàng)
-- ==========================================================

USE master;
GO

IF EXISTS (SELECT name FROM sys.databases WHERE name = N'CameraShopDB')
BEGIN
    ALTER DATABASE CameraShopDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE CameraShopDB;
END
GO

CREATE DATABASE CameraShopDB;
GO

USE CameraShopDB;
GO

-- 1. BẢNG ADMIN (Quản trị viên)
CREATE TABLE [Admin] (
    admin_id INT IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    full_name NVARCHAR(100),
    email VARCHAR(100),
    status INT DEFAULT 1 -- 1: Active, 0: Locked
);
GO

-- 2. BẢNG USER (Khách hàng)
CREATE TABLE [User] (
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    full_name NVARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    address NVARCHAR(255),
    status INT DEFAULT 1 -- 1: Active, 0: Blocked
);
GO

-- 3. BẢNG CATEGORY (Danh mục sản phẩm: DSLR, Mirrorless, Lens, Phụ kiện)
CREATE TABLE Category (
    category_id INT IDENTITY(1,1) PRIMARY KEY,
    category_name NVARCHAR(100) NOT NULL,
    status INT DEFAULT 1 -- 1: Active, 0: Hidden
);
GO

-- 4. BẢNG BRAND (Thương hiệu máy ảnh: Sony, Canon, Nikon, Fujifilm)
CREATE TABLE Brand (
    brand_id INT IDENTITY(1,1) PRIMARY KEY,
    brand_name NVARCHAR(100) NOT NULL,
    status INT DEFAULT 1 -- 1: Active, 0: Hidden
);
GO

-- 5. BẢNG PRODUCT (Sản phẩm máy ảnh)
CREATE TABLE Product (
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    product_name NVARCHAR(200) NOT NULL,
    price DECIMAL(12, 2) NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    thumbnail VARCHAR(255),
    description NVARCHAR(MAX),
    category_id INT FOREIGN KEY REFERENCES Category(category_id),
    brand_id INT FOREIGN KEY REFERENCES Brand(brand_id),
    admin_id INT FOREIGN KEY REFERENCES [Admin](admin_id), -- Admin tạo/quản lý
    status INT DEFAULT 1 -- 1: Active, 0: Inactive/Deleted
);
GO

-- 6. BẢNG CARTS (Giỏ hàng người dùng)
CREATE TABLE Carts (
    cart_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT UNIQUE FOREIGN KEY REFERENCES [User](user_id),
    created_at DATETIME DEFAULT GETDATE()
);
GO

-- 7. BẢNG CART_DETAILS (Chi tiết giỏ hàng)
CREATE TABLE Cart_Details (
    cart_id INT FOREIGN KEY REFERENCES Carts(cart_id) ON DELETE CASCADE,
    product_id INT FOREIGN KEY REFERENCES Product(product_id),
    quantity INT NOT NULL DEFAULT 1,
    PRIMARY KEY (cart_id, product_id)
);
GO

-- 8. BẢNG ORDER (Đơn đặt hàng)
CREATE TABLE [Order] (
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT FOREIGN KEY REFERENCES [User](user_id),
    order_date DATETIME DEFAULT GETDATE(),
    total_money DECIMAL(14, 2) NOT NULL,
    receiver_name NVARCHAR(100) NOT NULL,
    shipping_address NVARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    note NVARCHAR(500),
    status INT DEFAULT 1 -- 1: Chờ xử lý, 2: Đang giao, 3: Hoàn thành, 4: Đã hủy
);
GO

-- 9. BẢNG ORDER_DETAILS (Chi tiết đơn hàng - Bắt buộc có price lưu vết)
CREATE TABLE Order_Details (
    order_id INT FOREIGN KEY REFERENCES [Order](order_id) ON DELETE CASCADE,
    product_id INT FOREIGN KEY REFERENCES Product(product_id),
    price DECIMAL(12, 2) NOT NULL, -- Giá snapshot tại thời điểm mua
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, product_id)
);
GO

-- 10. BẢNG REVIEW (Đánh giá / Bình luận sản phẩm)
CREATE TABLE Review (
    review_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT FOREIGN KEY REFERENCES [User](user_id),
    product_id INT FOREIGN KEY REFERENCES Product(product_id),
    rating INT CHECK (rating >= 1 AND rating <= 5),
    comment NVARCHAR(500),
    created_at DATETIME DEFAULT GETDATE()
);
GO

-- ==========================================================
-- DỮ LIỆU MẪU BAN ĐẦU (SEED DATA)
-- ==========================================================
INSERT INTO [Admin] (username, password, full_name, email)
VALUES ('admin', '123', N'Quản Trị Viên', 'admin@camerashop.com');

INSERT INTO [User] (username, password, full_name, email, phone, address)
VALUES ('khachhang1', '123', N'Nguyễn Văn A', 'khach1@gmail.com', '0912345678', N'Hà Nội');

INSERT INTO Category (category_name) 
VALUES (N'Mirrorless'), (N'DSLR'), (N'Ống kính (Lens)'), (N'Phụ kiện máy ảnh');

INSERT INTO Brand (brand_name) 
VALUES ('Sony'), ('Canon'), ('Nikon'), ('Fujifilm');

INSERT INTO Product (product_name, price, quantity, thumbnail, description, category_id, brand_id, admin_id)
VALUES 
(N'Sony Alpha A7 Mark IV', 52990000, 10, 'sony-a7iv.jpg', N'Máy ảnh mirrorless full-frame cảm biến 33MP', 1, 1, 1),
(N'Canon EOS R6 Mark II', 56500000, 5, 'canon-r6ii.jpg', N'Cảm biến 24.2MP, chụp liên tiếp 40fps', 1, 2, 1),
(N'Fujifilm X-T5', 41990000, 8, 'fuji-xt5.jpg', N'Thiết kế hoài cổ, cảm biến X-Trans CMOS 5 HR 40MP', 1, 4, 1);
GO
