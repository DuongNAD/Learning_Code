USE COMPANY;
GO

-- ======================================================================
-- Question 1: No Parameters (Không có tham số)
-- ======================================================================
IF OBJECT_ID('GetHighEarningEmployees', 'P') IS NOT NULL
    DROP PROCEDURE GetHighEarningEmployees;
GO

CREATE PROCEDURE GetHighEarningEmployees
AS
BEGIN
    SELECT Fname, Lname, Salary
    FROM employee
    WHERE Salary > 50000
    ORDER BY Salary DESC;
END;
GO

-- ======================================================================
-- Question 2: One Parameter (Có 1 tham số)
-- ======================================================================
IF OBJECT_ID('GetEmployeesByDepartment', 'P') IS NOT NULL
    DROP PROCEDURE GetEmployeesByDepartment;
GO

CREATE PROCEDURE GetEmployeesByDepartment
    @DeptNumber INT
AS
BEGIN
    SELECT Fname, Lname, Salary
    FROM employee
    WHERE Dno = @DeptNumber;
END;
GO

-- ======================================================================
-- Question 3: Two Parameters (Có 2 tham số)
-- ======================================================================
IF OBJECT_ID('GetProjectsByLocationAndDept', 'P') IS NOT NULL
    DROP PROCEDURE GetProjectsByLocationAndDept;
GO

CREATE PROCEDURE GetProjectsByLocationAndDept
    @Location VARCHAR(50),
    @DeptNum INT
AS
BEGIN
    SELECT Pname, Pnumber
    FROM project
    WHERE Plocation = @Location AND Dnum = @DeptNum;
END;
GO

-- ======================================================================
-- Question 4: Parameter with a Default Value (Tham số có giá trị Default)
-- ======================================================================
IF OBJECT_ID('GetOvertimeWorkers', 'P') IS NOT NULL
    DROP PROCEDURE GetOvertimeWorkers;
GO

CREATE PROCEDURE GetOvertimeWorkers
    @MinHours INT = 40
AS
BEGIN
    SELECT Essn, Pno, Hours
    FROM works_on
    WHERE Hours > @MinHours;
END;
GO

-- ======================================================================
-- Question 5: Input and Output Parameters (Có tham số Input và tham số Output)
-- ======================================================================
IF OBJECT_ID('GetEmployeeDependentCount', 'P') IS NOT NULL
    DROP PROCEDURE GetEmployeeDependentCount;
GO

CREATE PROCEDURE GetEmployeeDependentCount
    @EmpSsn CHAR(9),
    @DependentCount INT OUTPUT
AS
BEGIN
    SELECT @DependentCount = COUNT(*)
    FROM dependent
    WHERE Essn = @EmpSsn;
END;
GO
