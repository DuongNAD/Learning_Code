CREATE DATABASE LAB5_2

USE LAB5_2

CREATE TABLE Student (
	RN VARCHAR(5) NOT NULL,
	NAME VARCHAR(20) NOT NULL,
	AGE INT NOT NULL,
)

ALTER TABLE Student 
	DROP COLUMN NAME;

ALTER TABLE Student 
	ADD Name VARCHAR(5) NOT NULL;

CREATE TABLE Test (
	TestID INT NOT NULL,
	Name VARCHAR(5) NOT NULL,
)

CREATE TABLE StudentTest(
	RN VARCHAR(5) NOT NULL,
	TestID  INT NOT NULL,
	Date DATE NOT NULL,
	Mark FLOAT NOT NULL,
)

ALTER TABLE Student 
ADD CONSTRAINT PK_Student
PRIMARY KEY (RN);

ALTER TABLE Test 
ADD CONSTRAINT PK_Test 
PRIMARY KEY (TestID);

ALTER TABLE StudentTest
ADD CONSTRAINT PK_StudentTest
PRIMARY KEY (RN,TestID);

ALTER TABLE Student
ADD CONSTRAINT CK_Age
CHECK (Age >0);

ALTER TABLE Student
ADD CONSTRAINT CK_RN
CHECK (RN >0);

ALTER TABLE Test
ADD CONSTRAINT CK_TestID
CHECK (TestID >0);

ALTER TABLE StudentTest
ADD CONSTRAINT CK_RN_st
CHECK (RN >0);

ALTER TABLE StudentTest
ADD CONSTRAINT CK_Test_st
CHECK (TestID >0);

ALTER TABLE StudentTest
ADD CONSTRAINT CK_Date
CHECK (Date >= CAST (GETDATE () AS DATE));

ALTER TABLE StudentTest
ADD CONSTRAINT CK_Mark
CHECK (Mark >=0);

ALTER TABLE StudentTest
ADD CONSTRAINT FK_RN FOREIGN KEY (RN) REFERENCES Student (RN),
	CONSTRAINT FK_TestID FOREIGN KEY (TestID) REFERENCES Test (TestID);

ALTER TABLE Student
ALTER COLUMN Name VARCHAR(225);

INSERT INTO Student VALUES 
	('1','Nguyen Hong Ha','20'),
	('2','Truong Ngoc Anh','30'),
	('3','Tuan Minh','25'),
	('4','Dan Truong','22');

INSERT INTO Test VALUES 
	('1','EPC'),
	('2','DWMX'),
	('3','SQL1'),
	('4','SQL2');

ALTER TABLE StudentTest
DROP CONSTRAINT CK_Date;

ALTER TABLE StudentTest
ADD CONSTRAINT CK_Date
CHECK (Date >= '2006-07-17')

INSERT INTO StudentTest VALUES 
	('1','1','2006-07-17','8'),
	('1','2','2006-07-18','5'),
	('1','3','2006-07-19','7'),
	('2','1','2006-07-17','7'),
	('2','2','2006-07-18','4'),
	('2','3','2006-07-19','2'),
	('3','1','2006-07-17','10'),
	('3','3','2006-07-18','1');


SELECT 
    S.Name AS [Student Name], 
    T.Name AS [Test Name], 
    ST.Mark, 
    ST.Date
FROM 
    Student S
JOIN 
    StudentTest ST ON S.RN = ST.RN
JOIN 
    Test T ON T.TestID = ST.TestID;

SELECT 
	S.RN,
	S.Name,
	S.AGE
FROM 
	Student S
WHERE
	S.RN NOT IN (SELECT RN FROM StudentTest);

SELECT 
	S.Name AS [Student Name],
	T.Name AS [Test Name],
	ST.Mark,
	ST.Date
FROM
	Student S
JOIN 
    StudentTest ST ON S.RN = ST.RN
JOIN 
    Test T ON T.TestID = ST.TestID
WHERE 
	ST.Mark <5;

SELECT 
	S.Name AS [Student Name],
	AVG(ST.Mark) AS [Average]
FROM 
	Student S
JOIN 
	StudentTest ST ON S.RN = ST.RN
GROUP BY 
    S.Name
ORDER BY 
    [Average] DESC;

SELECT TOP 1
	S.Name AS [Student Name],
	AVG(ST.Mark) AS [Average]
FROM 
	Student S
JOIN
	StudentTest ST ON S.RN = ST.RN
GROUP BY
	S.Name
ORDER BY 
    [Average] DESC;

SELECT
	T.Name AS [Test Name],
	MAX(ST.Mark) AS [MAX Mark]
FROM
	Test T
JOIN 
	StudentTest ST ON T.TestID = ST.TestID
GROUP BY 
    T.Name
ORDER BY 
    T.Name;

SELECT 
	S.Name AS [Student Name],
	T.Name AS [Test Name]
FROM
	Student S
LEFT JOIN
	StudentTest ST ON S.RN = ST.RN
LEFT JOIN
	Test T ON T.TestID = ST.TestID
ORDER BY
	S.Name,T.Name;
	

