CREATE DATABASE NHANVIEN

USE NHANVIEN

CREATE TABLE NHANVIEN(
	MA_NHANVIEN VARCHAR(5) NOT NULL,
	HO_NHANVIEN NVARCHAR(20) NOT NULL,
	TEN_NHANVIEN NVARCHAR(20) NOT NULL,
	MAPHONG VARCHAR(5) NOT NULL,
	GIOITINH NVARCHAR(3) NOT NULL,
	TUOI INT NOT NULL,
	DIACHI NVARCHAR(50) NOT NULL,
	TONGSO_DA INT NOT NULL
)

ALTER TABLE NHANVIEN
ADD LUONG DECIMAL(18,0);

CREATE TABLE PHONG(
	MAPHONG VARCHAR(5) NOT NULL,
	TENPHONG NVARCHAR(50) NOT NULL,
	DIADIEM NVARCHAR(50) NOT NULL,
	TRUONGPHONG NVARCHAR(50) NOT NULL,
	NGAY_THANHLAP DATE NOT NULL,
	SOLUONG_NV INT NOT NULL
)

ALTER TABLE NHANVIEN
ADD CONSTRAINT PK_NHANVIEN
PRIMARY KEY (MA_NHANVIEN)

ALTER TABLE PHONG
ADD CONSTRAINT PK_PHONG
PRIMARY KEY (MAPHONG)

ALTER TABLE NHANVIEN
ADD CONSTRAINT FK_MAPHONG
FOREIGN KEY (MAPHONG) REFERENCES PHONG (MAPHONG) 

INSERT INTO PHONG (MAPHONG, TENPHONG, DIADIEM, TRUONGPHONG, NGAY_THANHLAP, SOLUONG_NV)
VALUES 
('P001', N'Phòng Kinh doanh', N'Tầng 1', N'Nguyễn Văn A', '2018-01-01', 5),
('P002', N'Phòng Nhân sự', N'Tầng 2', N'Trần Thị B', '2019-03-15', 5),
('P003', N'Phòng Kế toán', N'Tầng 3', N'Lê Văn C', '2020-05-10', 5),
('P004', N'Phòng IT', N'Tầng 4', N'Phạm Thị D', '2021-07-20', 5),
('P005', N'Phòng Marketing', N'Tầng 5', N'Hồ Văn E', '2022-09-05', 5);

INSERT INTO NHANVIEN (MA_NHANVIEN, HO_NHANVIEN, TEN_NHANVIEN, MAPHONG, GIOITINH, TUOI, DIACHI, TONGSO_DA, LUONG)
VALUES 
-- Nhân viên phòng P001
('NV001', N'Nguyễn', N'An', 'P001', N'Nam', 30, N'Hà Nội', 10, 9000),
('NV002', N'Trần', N'Bình', 'P001', N'Nữ', 28, N'Hồ Chí Minh', 6, 8000),
('NV003', N'Lê', N'Chi', 'P001', N'Nữ', 32, N'Đà Nẵng', 8, 10000),
('NV004', N'Phạm', N'Dũng', 'P001', N'Nam', 35, N'Cần Thơ', 11, 9500),
('NV005', N'Hoàng', N'Giang', 'P001', N'Nữ', 27, N'Hải Phòng', 9, 8700),

-- Nhân viên phòng P002
('NV006', N'Nguyễn', N'Hạnh', 'P002', N'Nữ', 29, N'Hà Nội', 7, 9200),
('NV007', N'Trần', N'Hưng', 'P002', N'Nam', 33, N'Đà Nẵng', 10, 8600),
('NV008', N'Lê', N'Khoa', 'P002', N'Nam', 31, N'Cần Thơ', 6, 9100),
('NV009', N'Phạm', N'Linh', 'P002', N'Nữ', 26, N'Hồ Chí Minh', 5, 9400),
('NV010', N'Hoàng', N'Mai', 'P002', N'Nữ', 30, N'Hải Phòng', 9, 8900),

-- Nhân viên phòng P003
('NV011', N'Nguyễn', N'Nam', 'P003', N'Nam', 34, N'Đà Nẵng', 13, 10500),
('NV012', N'Trần', N'Oanh', 'P003', N'Nữ', 28, N'Hà Nội', 7, 9700),
('NV013', N'Lê', N'Phúc', 'P003', N'Nam', 36, N'Hải Phòng', 10, 9300),
('NV014', N'Phạm', N'Quang', 'P003', N'Nam', 32, N'Cần Thơ', 12, 9800),
('NV015', N'Hoàng', N'Rin', 'P003', N'Nữ', 29, N'Hồ Chí Minh', 9, 9500),

-- Nhân viên phòng P004
('NV016', N'Nguyễn', N'Sơn', 'P004', N'Nam', 30, N'Đà Nẵng', 8, 10200),
('NV017', N'Trần', N'Thư', 'P004', N'Nữ', 27, N'Cần Thơ', 6, 9700),
('NV018', N'Lê', N'Tiến', 'P004', N'Nam', 33, N'Hà Nội', 10, 9200),
('NV019', N'Phạm', N'Uyên', 'P004', N'Nữ', 29, N'Hồ Chí Minh', 7, 9300),
('NV020', N'Hoàng', N'Vinh', 'P004', N'Nam', 35, N'Hải Phòng', 11, 9900),

-- Nhân viên phòng P005
('NV021', N'Nguyễn', N'Yến', 'P005', N'Nữ', 26, N'Cần Thơ', 9, 9100),
('NV022', N'Trần', N'Zin', 'P005', N'Nam', 32, N'Hà Nội', 8, 9400),
('NV023', N'Lê', N'Anh', 'P005', N'Nữ', 28, N'Đà Nẵng', 7, 8800),
('NV024', N'Phạm', N'Bảo', 'P005', N'Nam', 34, N'Hồ Chí Minh', 10, 9900),
('NV025', N'Hoàng', N'Cường', 'P005', N'Nam', 30, N'Hải Phòng', 9, 9600);

SELECT 
	NV.HO_NHANVIEN + ' '+ NV.TEN_NHANVIEN AS HOTEN_NV,
	CASE
		WHEN NV.LUONG <(SELECT AVG(NV2.LUONG)
						FROM NHANVIEN NV2 
						WHERE NV2.MAPHONG =NV.MAPHONG)
		THEN 'TANG LUONG'
		ELSE 'KHONG TANG LUONG'
	END AS KETQUA
FROM NHANVIEN NV
JOIN PHONG P ON P.MAPHONG = NV.MAPHONG;


SELECT 
	NV.MA_NHANVIEN,
    NV.HO_NHANVIEN + ' ' + NV.TEN_NHANVIEN AS HOTEN_NV,
    NV.LUONG,
    P.TENPHONG,
	CASE
		WHEN NV.LUONG = (
			SELECT MAX(NV2.LUONG)
			FROM NHANVIEN NV2
			WHERE NV2.MAPHONG = NV.MAPHONG
		)
	THEN  'truongphong'
    ELSE 'nhanvien'

END AS XEPLOAI
FROM NHANVIEN NV
JOIN PHONG P ON P.MAPHONG = NV.MAPHONG

SELECT 
    NV.MA_NHANVIEN,
    NV.HO_NHANVIEN + ' ' + NV.TEN_NHANVIEN AS HOTEN_NV,
    NV.LUONG,
    CASE 
        WHEN NV.LUONG > 0 AND NV.LUONG < 8500 THEN NV.LUONG * 0.1
        WHEN NV.LUONG >= 8500 AND NV.LUONG < 9000 THEN NV.LUONG * 0.12
        WHEN NV.LUONG >= 9000 AND NV.LUONG < 10000 THEN NV.LUONG * 0.2
        WHEN NV.LUONG >= 10000 THEN NV.LUONG * 0.25
        ELSE 0
    END AS DONG_THUE
FROM NHANVIEN NV
JOIN PHONG P ON P.MAPHONG = NV.MAPHONG;

CREATE PROC CK_THEMPHONG
    @MaPhong VARCHAR(5),
    @TenPhong NVARCHAR(50),
    @DiaDiem NVARCHAR(50),
    @TruongPhong NVARCHAR(50),
    @NgayThanhLap DATE,
    @SoLuong_NV INT
AS
BEGIN
	BEGIN TRY
		INSERT INTO PHONG VALUES
		(@MaPhong,@TenPhong,@DiaDiem,@TruongPhong,@NgayThanhLap,@SoLuong_NV);
		PRINT N'Thêm dữ liệu thành công';
	END TRY

	BEGIN CATCH
		PRINT N'Thêm dữ liệu thất bại';
		PRINT N'Mã lỗi: ' + CAST(ERROR_NUMBER() AS NVARCHAR);
		PRINT N'Chi tiết lỗi: ' + ERROR_MESSAGE();
	END CATCH
END;

EXEC CK_THEMPHONG
    @MaPhong = 'P006',
    @TenPhong = N'Phòng Kiểm thử',
    @DiaDiem = N'Tầng 6',
    @TruongPhong = N'Đặng Văn Kiểm',
    @NgayThanhLap = '2024-05-01',
    @SoLuong_NV = 3;

