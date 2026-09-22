CREATE DATABASE TABLE_BAIVIET

USE TABLE_BAIVIET

CREATE TABLE BAIVIET (
	ID VARCHAR(5) NOT NULL,
	TIEUDE NVARCHAR(50) NOT NULL,
	NOIDUNG NVARCHAR(100)
)

ALTER TABLE BAIVIET
ALTER COLUMN NOIDUNG NVARCHAR(225);

ALTER TABLE BAIVIET
ADD CONSTRAINT PK_BAIVIET
PRIMARY KEY (ID)

INSERT INTO BAIVIET (ID, TIEUDE, NOIDUNG) 
VALUES
('BV001', 'ISO 22000 là gì?', 'ISO 22000 là tiêu chuẩn quốc tế về hệ thống quản lý an toàn thực phẩm, giúp doanh nghiệp đảm bảo chất lượng sản phẩm và bảo vệ sức khỏe người tiêu dùng.'),
('BV002', 'Lợi ích của việc chứng nhận ISO 9001', 'Chứng nhận ISO 9001 giúp doanh nghiệp cải thiện hiệu quả quản lý chất lượng, nâng cao sự hài lòng của khách hàng và tăng cường khả năng cạnh tranh trên thị trường.'),
('BV003', 'ISO 14001 và bảo vệ môi trường', 'ISO 14001 là tiêu chuẩn về hệ thống quản lý môi trường, giúp doanh nghiệp giảm thiểu tác động tiêu cực đến môi trường và tuân thủ các quy định về bảo vệ môi trường.'),
('BV004', 'HACCP trong sản xuất thực phẩm', 'HACCP là phương pháp quản lý an toàn thực phẩm, giúp phát hiện và phòng ngừa các nguy cơ có thể xảy ra trong quá trình sản xuất thực phẩm.'),
('BV005', 'ISO 45001 và sự an toàn lao động', 'ISO 45001 là tiêu chuẩn về hệ thống quản lý an toàn và sức khỏe nghề nghiệp, giúp doanh nghiệp đảm bảo môi trường làm việc an toàn và bảo vệ sức khỏe của người lao động.');

CREATE FULLTEXT CATALOG MYFULLTEXTCATALOG AS DEFAULT;

CREATE FULLTEXT INDEX ON BAIVIET (NOIDUNG)
KEY INDEX PK_BAIVIET
ON MYFULLTEXTCATALOG;



