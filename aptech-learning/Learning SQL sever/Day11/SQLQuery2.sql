CREATE DATABASE JobTrackingSystem

Use JobTrackingSystem

create table Applicants(
	ApplicantID int identity(1,1) not null,
	FullName varchar(225) unique not null,
	Email varchar(225) not null,
	Contact varchar(20) not null, 
	AppliedDate date default getdate() not null,
	JobID int not null
)
create table Jobs(
	JobID int identity(1,1) not null,
	Title varchar(100) not null,
	Division varchar(100) not null,
	Openings int not null,
	ApplicantCount int default 0
)

alter table Applicants
add constraint pk_Applicants
primary key (ApplicantID)

alter table Jobs
add constraint pk_Jobs
primary key (JobID)

alter table Applicants
add constraint fk_JobID
foreign key (JobID) references Jobs (JobID)

alter table Jobs
add constraint ck_Openings
check (Openings >0)

alter table Applicants 
add constraint default_appliedDate
default getdate() for AppliedDate

INSERT INTO Applicants (FullName, Email, Contact, JobID)
VALUES ('Nguyen Thi F', 'thif@example.com', '0911122233', 1)

INSERT INTO Applicants (FullName, Email, Contact, JobID)
VALUES ('Hoang Van G', 'vang@example.com', '0933344455', 2)

INSERT INTO Applicants (FullName, Email, Contact, JobID)
VALUES ('Le Thi H', 'thih@example.com', '0977766677', 3)

INSERT INTO Applicants (FullName, Email, Contact, JobID)
VALUES ('Tran Van I', 'vani@example.com', '0909988776', 1)

INSERT INTO Applicants (FullName, Email, Contact, JobID)
VALUES ('Pham Minh J', 'minhj@example.com', '0944556677', 2)

INSERT INTO Jobs (Title, Division, Openings, ApplicantCount) VALUES
('Software Engineer', 'Engineering', 5, 0),
('Marketing Specialist', 'Marketing', 3, 0),
('HR Assistant', 'Human Resources', 2, 0)

select 
	J.Title,
	count(A.ApplicantID) as NumOfApplicant
from Jobs J
join Applicants A on A.JobID = J.JobID
group by 
	J.Title
order by
	NumOfApplicant DESC

update Jobs
set ApplicantCount = (select count(*)
						from Applicants A
						where A.ApplicantID = Jobs.JobID)

alter table Applicants
add Shortlisted bit default 0 not null

update Applicants
set Shortlisted = 1

CREATE TRIGGER tg_Applicants_update
on Applicants
after update
as 
begin 
	if exists (select 1 from inserted i
							join Applicants A on A.Email = i.Email
							where A.ApplicantID <> i.ApplicantID)
		begin 
			print N'Email đã tồn tại';
			rollback transaction;
		end
end;

drop trigger tg_Applicants_update

CREATE TRIGGER tg_delete
on Jobs
after delete
as
begin
	update Z
		set J.ApplicantCount =J.ApplicantCount -1
		from Jobs J
		join Applicants A on A.JobID = J.JobID
end

CREATE TRIGGER