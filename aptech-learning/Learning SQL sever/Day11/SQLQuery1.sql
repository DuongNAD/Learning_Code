CREATE DATABASE EcoSystemManagement

USE EcoSystemManagement

CREATE TABLE Animals (
	AnimalID int IDENTITY not null,
	AnimalName varchar(225) not null,
	Species varchar(100) not null,
	Age int not null,
	ArrivalDate date not null,
	ZoneID int not null
)

CREATE TABLE Zones (
	ZoneID int identity not null,
	ZoneName varchar(100) not null,
	AreaSize decimal(8,2) not null,
	NumOfAnimals int default 0
)

alter table Animals
add constraint pk_Animals
primary key (AnimalID)

alter table Zones
add constraint pk_Zones
primary key (ZoneID)

alter table Animals
add constraint fk_ZoneID
foreign key (ZoneID) references Zones (ZoneID)

alter table Animals
add constraint ck_Age
check (Age >=0)

alter table Animals 
add constraint unique_AnimalName
unique (AnimalName)

alter table Animals
add constraint default_ArrivalDate
default getdate() for ArrivalDate

insert into Zones values
(N'Cúc Phương','80000','5000'),
(N'Bảo Ngọc','100000','7000'),
(N'Phương Nam','130000','7600')

insert into Animals (AnimalName, Species,Age,ZoneID) values
(N'Hổ đông bắc',N'Hổ','6','1'),
(N'Hổ châu phi',N'Hổ','4','1'),
(N'Báo hoa mai',N'Báo','5','2'),
(N'Chim chào mào',N'Chim','1','2'),
(N'Chim họa mi',N'Chim','1','3'),
(N'Gấu trúc',N'Gấu','7','3')

INSERT INTO Animals (AnimalName,Species,Age,ZoneID) VALUES
(N'Voi châu phi',N'Elephant','5','2')

INSERT INTO Animals (AnimalName,Species,Age,ZoneID) VALUES
(N'Voi châu á',N'Elephant','5','3')
SELECT 
	Z.ZoneID,
	Z.ZoneName,
	COUNT(A.AnimalID) AS SpeciesCount
FROM Zones Z
JOIN Animals A ON A.ZoneID = Z.ZoneID
GROUP BY Z.ZoneID, Z.ZoneName
ORDER BY SpeciesCount DESC


UPDATE Zones 
Set NumOfAnimals = ( 
	SELECT count(*)
	from Animals A
	where A.ZoneID = Zones.ZoneID
);

UPDATE A
SET Age = Age + 2
FROM Animals A
JOIN Zones Z ON Z.ZoneID = A.ZoneID
WHERE A.Species = N'Elephant'
  AND Z.ZoneName = N'Phuong Nam';

CREATE TRIGGER TRG_UPDATE_age
on Animals
after update 
as 
begin
	if exists (select 1 from inserted where Age <=0)
		begin
			print N'Age phải lớn hơn 0';
			rollback transaction;
		end
end;

CREATE TRIGGER TRG_DELETE_NumOfAnimals
on Zones
after delete
as 
begin
	update Z
		set NumOfAnimals = NumOfAnimals -1
		from Zones Z
		Join Animals A on Z.ZoneID = A.ZoneID;
end;

CREATE TRIGGER TRG_INSERT_ArrivalDate
on Animals
after insert
as 
begin 
	if exists ( select 1 from inserted where ArrivalDate > GETDATE())
		begin
			print N'ArrivalDate phải nhỏ hơn hoặc bằng hôm nay';
			rollback transaction;
		end
end;


CREATE VIEW vw_AnimalSummary
as
select A.AnimalID,A.AnimalName,A.Species,Z.ZoneName,A.Age
from Animals A
join Zones Z on A.ZoneID = Z.ZoneID
where A.Age >5;

select * from vw_AnimalSummary

UPDATE vw_AnimalSummary
set Species ='Voi'
where AnimalID ='2'

DELETE vw_AnimalSummary
where Age >10

CREATE PROC sp_AddAnimal
	@AnimalName nvarchar(225),
	@Species nvarchar(225),
	@Age int,
	@ZoneID int
as
begin 
	begin try
		if @Age <=0
			begin 
				print N'Age phải lớn hơn 0'
				return 
			end

		insert into Animals (AnimalName, Species, Age, ZoneID) values (@AnimalName,@Species,@Age,@ZoneID)
		print N'Thêm động vật thành công'

	end try
	begin catch
		print N'Mã lỗi: ' + cast(error_number() as varchar(10))
		print N'Chi tiết lỗi: ' + error_message() 
	end catch
end

EXEC sp_AddAnimal N'Chó rừng',N'Chó','3','2';

CREATE PROC sp_DeleteOldAnimals
as
begin
	begin try
		delete from Animals
		where Age >20

		print N'Đã xóa tất cả động vật có tuổi > 20'

	end try
	begin catch
		print N'Mã lỗi: ' + cast (error_number () as varchar(10));
		print N'Chi tiết lỗi: ' + error_message();
	end catch
end

EXEC sp_DeleteOldAnimals ;