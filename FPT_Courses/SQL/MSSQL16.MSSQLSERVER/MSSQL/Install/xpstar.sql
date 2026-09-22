/********************************************************************************************/
/* XPSTAR.SQL - Extended Stored Procedures for the SQL Server Enterprise Components         */
/*
** Copyright (c) Microsoft Corporation
** All Rights Reserved.
*/
/********************************************************************************************/

use master

----------------------------------------------------------------------------------------
-- drop legacy procedures that are not used anymore
----------------------------------------------------------------------------------------

create table #procs (name sysname NOT NULL)
go

insert into #procs values (N'sp_sqlregister')
insert into #procs values (N'xp_getfiledetails')
insert into #procs values (N'xp_eventlog')
insert into #procs values (N'sp_eventlog')
insert into #procs values (N'sp_IsMBCSLeadByte')
insert into #procs values (N'sp_GetMBCSCharLen')
insert into #procs values (N'xp_enum_activescriptengines')
insert into #procs values (N'xp_MSPlatform')
insert into #procs values (N'xp_IsNTAdmin')
insert into #procs values (N'xp_SetSQLSecurity')
insert into #procs values (N'xp_GetAdminGroupName')
insert into #procs values (N'xp_MSnt2000')
insert into #procs values (N'xp_MSLocalSystem')


declare proc_cursor cursor for select name from #procs
open proc_cursor

declare @name as sysname

fetch next from proc_cursor into @name
while @@fetch_status = 0
begin
	if object_id(@name, 'X') is not null
	begin	
	    --print N'DEBUG: dropping ' + @name + '...'
		exec sp_dropextendedproc @functname = @name
	end

	if object_id('dbo.' + @name, 'P') is not null	
	begin
		--print N'DEBUG: dropping ' + @name + '...'
		execute ('drop procedure dbo.' + @name)
	end

	fetch next from proc_cursor into @name
end

close proc_cursor
deallocate proc_cursor

go

drop table #procs
go

/********************************************************************************************/
/* EOF XPSTAR.SQL                                                                           */
/********************************************************************************************/
