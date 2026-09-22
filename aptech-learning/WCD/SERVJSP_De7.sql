CREATE TABLE tblEmployee(
    employeeNo VARCHAR(80) PRIMARY KEY,
    employeeName  VARCHAR(100) NOT NULL, 
    placeOfWork VARCHAR(100),
    phoneNo  VARCHAR(30)
);
INSERT INTO tblEmployee (employeeNo, employeeName, placeOfWork, phoneNo)
VALUES
    ('E001', 'John Doe', 'Company A', '123-456-7890'),
    ('E002', 'Jane Smith', 'Company B', '987-654-3210'),
    ('E003', 'Mike Johnson', 'Company C', '555-555-5555'),
    ('E004', 'Emily Davis', 'Company A', '111-222-3333'),
    ('E005', 'Chris Wilson', 'Company D', '777-888-9999'),
    ('E006', 'Linda Brown', 'Company B', '444-555-6666'),
    ('E007', 'Tom Anderson', 'Company C', '666-999-1111'),
    ('E008', 'Jessica Lee', 'Company A', '123-987-6543'),
    ('E009', 'David White', 'Company D', '555-444-3333'),
    ('E010', 'Susan Miller', 'Company B', '111-333-5555'),
    ('E011', 'Paul Taylor', 'Company C', '777-888-9999'),
    ('E012', 'Sarah Clark', 'Company A', '555-111-2222'),
    ('E013', 'Michael Johnson', 'Company D', '123-456-7890'),
    ('E014', 'Emily Wilson', 'Company B', '222-333-4444'),
    ('E015', 'Jennifer Brown', 'Company C', '888-777-6666'),
    ('E016', 'Mark Davis', 'Company A', '666-555-4444'),
    ('E017', 'Laura Harris', 'Company D', '777-888-9999'),
    ('E018', 'Kevin Hall', 'Company B', '111-222-3333'),
    ('E019', 'Amanda Smith', 'Company C', '555-444-3333'),
    ('E020', 'Richard Anderson', 'Company A', '123-987-6543');
 

