-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th6 11, 2025 lúc 02:37 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `bookstore_db`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` int(11) NOT NULL,
  `description` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `books`
--

INSERT INTO `books` (`id`, `title`, `author`, `price`, `stock`, `description`, `created_at`) VALUES
(1, 'Lập trình PHP & MySQL Toàn tập', 'Nguyễn Văn A', 250000.00, 50, 'Cuốn sách hướng dẫn chi tiết từ cơ bản đến nâng cao về lập trình web với PHP và MySQL.', '2025-06-11 12:30:58'),
(2, 'Clean Code: A Handbook of Agile Software Craftsmanship', 'Robert C. Martin', 350000.00, 40, 'Mã sạch - Cẩm nang về sự khéo léo của phần mềm linh hoạt. Phải có cho mọi lập trình viên.', '2025-06-11 12:30:58'),
(3, 'JavaScript: The Good Parts', 'Douglas Crockford', 280000.00, 60, 'Khám phá những phần tinh túy và hiệu quả nhất của ngôn ngữ lập trình JavaScript.', '2025-06-11 12:30:58'),
(4, 'Lập trình Hướng đối tượng với C++', 'Phạm Văn Ất', 195000.00, 70, 'Giáo trình kinh điển về lập trình hướng đối tượng sử dụng ngôn ngữ C++ tại Việt Nam.', '2025-06-11 12:30:58'),
(5, 'Python Crash Course', 'Eric Matthes', 450000.00, 55, 'Khóa học cấp tốc về Python, một trong những cuốn sách bán chạy nhất thế giới cho người mới bắt đầu.', '2025-06-11 12:30:58'),
(6, 'Đắc Nhân Tâm', 'Dale Carnegie', 120000.00, 100, 'Nghệ thuật thu phục lòng người, cuốn sách gối đầu giường về kỹ năng giao tiếp.', '2025-06-11 12:30:58'),
(7, 'Tư Duy Nhanh và Chậm', 'Daniel Kahneman', 225000.00, 45, 'Phân tích hai hệ thống tư duy định hình cách chúng ta đưa ra quyết định và phán xét.', '2025-06-11 12:30:58'),
(8, '7 Thói Quen Của Người Thành Đạt', 'Stephen R. Covey', 150000.00, 120, 'Thay đổi cuộc sống của bạn bằng cách xây dựng những thói quen hiệu quả và bền vững.', '2025-06-11 12:30:58'),
(9, 'Sức Mạnh Của Thói Quen', 'Charles Duhigg', 135000.00, 85, 'Khám phá khoa học đằng sau việc hình thành và thay đổi thói quen trong cuộc sống và công việc.', '2025-06-11 12:30:58'),
(10, 'Dế Mèn Phiêu Lưu Ký', 'Tô Hoài', 75000.00, 150, 'Tác phẩm văn học thiếu nhi kinh điển của Việt Nam, kể về cuộc phiêu lưu của chú dế mèn.', '2025-06-11 12:30:58'),
(11, 'Số Đỏ', 'Vũ Trọng Phụng', 88000.00, 65, 'Một tác phẩm trào phúng bậc thầy, phơi bày những lố lăng của xã hội thành thị Việt Nam thời Pháp thuộc.', '2025-06-11 12:30:58'),
(12, 'Tôi Thấy Hoa Vàng Trên Cỏ Xanh', 'Nguyễn Nhật Ánh', 105000.00, 200, 'Câu chuyện tuổi thơ trong sáng, mộc mạc và đầy cảm xúc tại một làng quê Việt Nam.', '2025-06-11 12:30:58'),
(13, 'Nhà Giả Kim', 'Paulo Coelho', 95000.00, 110, 'Một câu chuyện đầy cảm hứng về việc theo đuổi ước mơ và khám phá vận mệnh của bản thân.', '2025-06-11 12:30:58'),
(14, 'Trăm Năm Cô Đơn', 'Gabriel Garcia Marquez', 180000.00, 50, 'Một trong những tiểu thuyết vĩ đại nhất của thế kỷ 20, thuộc dòng chủ nghĩa hiện thực huyền ảo.', '2025-06-11 12:30:58'),
(15, 'Giết Con Chim Nhại', 'Harper Lee', 125000.00, 90, 'Một câu chuyện cảm động về sự bất công và lòng dũng cảm ở miền Nam nước Mỹ.', '2025-06-11 12:30:58'),
(16, 'Kiêu Hãnh và Định Kiến', 'Jane Austen', 115000.00, 80, 'Tiểu thuyết lãng mạn kinh điển về tình yêu, giai cấp và những định kiến xã hội.', '2025-06-11 12:30:58'),
(17, 'Lược Sử Thời Gian', 'Stephen Hawking', 180000.00, 30, 'Khám phá những bí ẩn của vũ trụ, từ Vụ Nổ Lớn cho đến các lỗ đen.', '2025-06-11 12:30:58'),
(18, 'Sapiens: Lược Sử Loài Người', 'Yuval Noah Harari', 299000.00, 60, 'Một cái nhìn tổng quan đầy hấp dẫn về lịch sử của loài người từ thời tiền sử đến nay.', '2025-06-11 12:30:58'),
(19, 'Xứ Cát (Dune)', 'Frank Herbert', 249000.00, 40, 'Tiểu thuyết khoa học viễn tưởng kinh điển, đặt nền móng cho rất nhiều tác phẩm sau này.', '2025-06-11 12:30:58'),
(20, 'Chúa Tể Của Những Chiếc Nhẫn', 'J.R.R. Tolkien', 399000.00, 35, 'Bộ tiểu thuyết giả tưởng hoành tráng, một cuộc phiêu lưu giữa thiện và ác tại vùng Trung Địa.', '2025-06-11 12:30:58'),
(21, 'Vũ trụ phiêu lưu kí', 'Duong Anh', 6000000.00, 23, 'Siêu đặc biệt', '2025-06-11 12:33:54');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `orders`
--

CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL,
  `customer_name` varchar(255) NOT NULL,
  `customer_email` varchar(255) NOT NULL,
  `customer_phone` varchar(20) NOT NULL,
  `customer_address` text NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `order_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `orders`
--

INSERT INTO `orders` (`order_id`, `customer_name`, `customer_email`, `customer_phone`, `customer_address`, `total_amount`, `order_date`) VALUES
(1, 'Duong', 'duonganhdn2000@gmail.com', '0968524357', 'Hà Nội', 803000.00, '2025-06-11 12:34:17');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `order_details`
--

CREATE TABLE `order_details` (
  `order_detail_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `order_details`
--

INSERT INTO `order_details` (`order_detail_id`, `order_id`, `book_id`, `quantity`, `price`) VALUES
(1, 1, 3, 1, 280000.00),
(2, 1, 10, 1, 75000.00),
(3, 1, 14, 1, 180000.00),
(4, 1, 17, 1, 180000.00),
(5, 1, 11, 1, 88000.00);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`);

--
-- Chỉ mục cho bảng `order_details`
--
ALTER TABLE `order_details`
  ADD PRIMARY KEY (`order_detail_id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `book_id` (`book_id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `books`
--
ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT cho bảng `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `order_details`
--
ALTER TABLE `order_details`
  MODIFY `order_detail_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `order_details`
--
ALTER TABLE `order_details`
  ADD CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`),
  ADD CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
