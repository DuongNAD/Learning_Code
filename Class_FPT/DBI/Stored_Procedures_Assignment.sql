USE COMPANY;
GO

-- ======================================================================
-- Question 1: Input/Output Parameters + Group By + Multiple Tables
-- ======================================================================
IF OBJECT_ID('GetDepartmentProjectStats', 'P') IS NOT NULL
    DROP PROCEDURE GetDepartmentProjectStats;
GO

CREATE PROCEDURE GetDepartmentProjectStats
    @DeptNum INT,
    @TotalHoursWorked INT OUTPUT
AS
BEGIN
    SELECT @TotalHoursWorked = ISNULL(SUM(w.Hours), 0)
    FROM works_on w
    JOIN project p ON w.Pno = p.Pnumber
    WHERE p.Dnum = @DeptNum;
END;
GO

-- ======================================================================
-- Question 2: Input Parameter + Nested Subquery + Multi-Table Join
-- ======================================================================
IF OBJECT_ID('GetHighEffortEmployeesByManager', 'P') IS NOT NULL
    DROP PROCEDURE GetHighEffortEmployeesByManager;
GO

CREATE PROCEDURE GetHighEffortEmployeesByManager
    @ManagerSsn CHAR(9)
AS
BEGIN
    SELECT DISTINCT e.Fname, e.Lname, e.Ssn
    FROM employee e
    JOIN works_on w ON e.Ssn = w.Essn
    WHERE e.Super_ssn = @ManagerSsn
      AND w.Hours > (SELECT AVG(Hours) FROM works_on);
END;
GO


exec GetHighEffortEmployeesByManager @ManagerSsn = '333445555'


-- ======================================================================
-- Question 3: Data Modification (UPDATE) + Input Parameter + Nested Subquery
-- ======================================================================
IF OBJECT_ID('AdjustSalaryForProjectLoad', 'P') IS NOT NULL
    DROP PROCEDURE AdjustSalaryForProjectLoad;
GO

CREATE PROCEDURE AdjustSalaryForProjectLoad
    @MinProjects INT
AS
BEGIN
    UPDATE employee
    SET Salary = Salary * 1.10
    WHERE (SELECT COUNT(Pno) FROM works_on WHERE Essn = employee.Ssn) >= @MinProjects;
END;
GO

-- ======================================================================
-- Question 4: Advanced Group By + HAVING Clause + Input Parameter
-- ======================================================================
IF OBJECT_ID('GetOverburdenedDepartments', 'P') IS NOT NULL
    DROP PROCEDURE GetOverburdenedDepartments;
GO

CREATE PROCEDURE GetOverburdenedDepartments
    @MaxTotalSalary DECIMAL(10,2)
AS
BEGIN
    SELECT d.Dname, SUM(e.Salary) AS TotalSalaryExpenditure
    FROM department d
    JOIN employee e ON d.Dnumber = e.Dno
    GROUP BY d.Dname, d.Dnumber
    HAVING COUNT(e.Ssn) > 5 AND SUM(e.Salary) > @MaxTotalSalary;
END;
GO

-- ======================================================================
-- Question 5: Multi-Table Join + UPDATE + Conditional Case Logic + Output Parameter
-- ======================================================================
IF OBJECT_ID('PromoteDepartmentManagers', 'P') IS NOT NULL
    DROP PROCEDURE PromoteDepartmentManagers;
GO

CREATE PROCEDURE PromoteDepartmentManagers
    @Location VARCHAR(50),
    @UpdatedCount INT OUTPUT
AS
BEGIN
    UPDATE e
    SET e.Salary = e.Salary * 
        CASE 
            WHEN (SELECT COUNT(*) FROM dependent WHERE Essn = e.Ssn) >= 1 THEN 1.15
            ELSE 1.05
        END
    FROM employee e
    JOIN department d ON e.Ssn = d.Mgr_ssn
    JOIN dept_locations dl ON d.Dnumber = dl.Dnumber
    WHERE dl.Dlocation = @Location;

    SET @UpdatedCount = @@ROWCOUNT;
END;
GO
