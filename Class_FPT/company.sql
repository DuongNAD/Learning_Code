
create database COMPANY;

use COMPANY;

create table employee(
	Ssn char(9) not null primary key,
	Fname varchar(15) not null,
	Minit char,
	Lname varchar(15),
	Bdate Date,
	Address varchar(30),
	Sex Decimal(10,2),
	Super_ssn char(9),
	Dno int not null,
	)

	create table department(
	Dnumber int not null primary key,
	Dname varchar(15) not null,
	Mgr_ssn char(9) not null,
	Mgr_start_date date,
	)

	create table dept_locations(
	Dnumber int not null,
	Dlocation varchar(15) not null,
	primary key(Dnumber, Dlocation),
	foreign key(Dnumber) References department(Dnumber),
	)

	create table project(
	Pnumber int not null primary key,
	Pname varchar(15) not null unique,
	Plocation varchar(15),
	Dnum int not null,
	foreign key(Dnum) References department(Dnumber),
	)

	create table works_on(
	Essn char(9) not null,
	Pno int not null,
	Hours decimal(3,1) not null,
	primary key (Essn,pno),
	foreign key(Essn) References employee(Ssn),
	foreign key(Pno) References project(Pnumber),
	)

	create table dependent(
	Essn char(9) not null,
	Dependent_name varchar(15) not null,
	Sex char,
	Bdate date,
	Relationship varchar(8),
	primary key(Essn,Dependent_name),
	foreign key(Essn) References employee(Ssn),
	)

ALTER TABLE employee ALTER COLUMN Sex CHAR(1);

ALTER TABLE employee ADD Salary DECIMAL(10,2);

INSERT INTO employee(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno)
VALUES 
    ('John', 'B', 'Smith', '123456789', '1965-09-01', '731 Fondren, Houston, TX', 'M', 30000, '333445555', 5),
    ('Franklin', 'T', 'Wong', '333445555', '1955-12-08', '638 Voss, Houston, TX', 'M', 40000, '888665555', 5),
    ('Ramesh', 'K', 'Narayan', '666884444', '1962-09-15', '975 Fire Oak, Humble, TX', 'M', 38000, '333445555', 5),
    ('Joyce', 'A', 'English', '453453453', '1972-07-31', '5631 Rice, Houston, TX', 'F', 25000, '333445555', 5);

	INSERT INTO department (Dnumber, Dname, Mgr_ssn, Mgr_start_date)
VALUES 
    (1, 'Headquarters', '888665555', '1981-06-19'),
    (4, 'Administration', '987654321', '1995-01-01'),
    (5, 'Research', '333445555', '1988-05-22');

	INSERT INTO dept_locations (Dnumber, Dlocation)
VALUES 
    (1, 'Houston'),
    (4, 'Stafford'),
    (5, 'Bellaire'),
    (5, 'Sugarland'),
    (5, 'Houston');

	INSERT INTO project (Pnumber, Pname, Plocation, Dnum)
VALUES 
    (1, 'ProductX', 'Bellaire', 5),
    (2, 'ProductY', 'Sugarland', 5),
    (3, 'ProductZ', 'Houston', 5),
    (10, 'Computerization', 'Stafford', 4),
    (20, 'Reorganization', 'Houston', 1),
    (30, 'Newbenefits', 'Stafford', 4);

	INSERT INTO works_on (Essn, Pno, Hours)
VALUES 
    ('123456789', 1, 32.5),
    ('123456789', 2, 7.5),
    ('333445555', 2, 10.0),
    ('333445555', 3, 10.0),
    ('333445555', 10, 10.0),
    ('333445555', 20, 10.0),
    ('666884444', 3, 40.0),
    ('453453453', 1, 20.0),
    ('453453453', 2, 20.0);

	INSERT INTO dependent (Essn, Dependent_name, Sex, Bdate, Relationship)
VALUES 
    ('333445555', 'Alice', 'F', '1986-04-05', 'Daughter'),
    ('333445555', 'Theodore', 'M', '1983-10-25', 'Son'),
    ('333445555', 'Joy', 'F', '1958-05-03', 'Spouse'),
    ('123456789', 'Michael', 'M', '1988-01-04', 'Son'),
    ('123456789', 'Alice', 'F', '1988-12-30', 'Daughter');

	SELECT Bdate, Address
FROM EMPLOYEE
WHERE Fname = 'John' AND Minit = 'B' AND Lname = 'Smith';

SELECT Fname, Lname, Address
FROM EMPLOYEE, DEPARTMENT
WHERE Dname = 'Research' AND Dnumber = Dno;

SELECT Pnumber, Dnum, Lname, Address, Bdate
FROM PROJECT, DEPARTMENT, EMPLOYEE
WHERE Dnum = Dnumber AND Mgr_ssn = Ssn AND Plocation = 'Stafford';

SELECT EMPLOYEE.Fname, EMPLOYEE.Lname, EMPLOYEE.Address
FROM EMPLOYEE, DEPARTMENT
WHERE DEPARTMENT.DName = 'Research' AND DEPARTMENT.Dnumber = EMPLOYEE.Dno;

SELECT EMPLOYEE.Fname, EMPLOYEE.Lname, EMPLOYEE.Address
FROM EMPLOYEE, DEPARTMENT
WHERE DEPARTMENT.DName = 'Research' AND DEPARTMENT.Dnumber = EMPLOYEE.Dno;

SELECT E.Fname, E.LName, E.Address
FROM EMPLOYEE AS E, DEPARTMENT AS D
WHERE D.DName = 'Research' AND D.Dnumber = E.Dno;

SELECT E.Fname, E.Lname, S.Fname, S.Lname
FROM EMPLOYEE AS E, EMPLOYEE AS S
WHERE E.Super_ssn = S.Ssn;

SELECT Ssn 
FROM EMPLOYEE;

SELECT Ssn, Dname 
FROM EMPLOYEE, DEPARTMENT;

SELECT * FROM EMPLOYEE, DEPARTMENT;

SELECT * FROM EMPLOYEE 
WHERE Dno = 5;

SELECT * FROM EMPLOYEE, DEPARTMENT 
WHERE Dname = 'Research' AND Dno = Dnumber;

SELECT ALL Salary 
FROM EMPLOYEE;

SELECT DISTINCT Salary 
FROM EMPLOYEE;

( SELECT DISTINCT Pnumber 
  FROM PROJECT, DEPARTMENT, EMPLOYEE 
  WHERE Dnum = Dnumber AND Mgr_ssn = Ssn AND Lname = 'Smith' )
UNION
( SELECT DISTINCT Pnumber 
  FROM PROJECT, WORKS_ON, EMPLOYEE 
  WHERE Pnumber = Pno AND Essn = Ssn AND Lname = 'Smith' );

SELECT Fname, Lname 
FROM EMPLOYEE 
WHERE Address LIKE '%Houston,TX%';

SELECT Fname, Lname 
FROM EMPLOYEE 
WHERE Bdate LIKE '__7_______';

SELECT E.Fname, E.Lname, 1.1 * E.Salary AS Increased_sal
FROM EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P
WHERE E.Ssn = W.Essn AND W.Pno = P.Pnumber AND P.Pname = 'ProductX';

SELECT * FROM EMPLOYEE 
WHERE (Salary BETWEEN 30000 AND 40000) AND Dno = 5;

SELECT D.Dname, E.Lname, E.Fname, P.Pname
FROM DEPARTMENT AS D, EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P
WHERE D.Dnumber = E.Dno AND E.Ssn = W.Essn AND W.Pno = P.Pnumber
ORDER BY D.Dname, E.Lname, E.Fname;