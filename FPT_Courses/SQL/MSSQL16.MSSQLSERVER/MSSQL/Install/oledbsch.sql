/****************************************************************************
//		Copyright (c) Microsoft Corporation.
//
// @File: oledbsch.sql
//
// Purpose:
//		CREATE OLE-DB SYSTEM FUNCTIONS
//
// Notes:
//	run by runsyssql.bat
//	
// History:
//
//     @Version: Yukon
//     86123 AXZ  08/31/01 Remove system fake tables and oledb remote tables
//     00000 AXZ  08/20/01 Created from shiloh-version oledbsch.sql
//
// @EndHeader@
*****************************************************************************/

raiserror(15339,-1,-1,'sys.fn_remote_catalogs')
go

if object_id('sys.fn_remote_catalogs') is not null
    drop function sys.fn_remote_catalogs
go
create function sys.fn_remote_catalogs(
	@server		sysname,
	@catalog	sysname = NULL)
returns table
as
return	select * from OpenRowset(SYSREMOTE_CATALOGS, @server, @catalog)
go

raiserror(15339,-1,-1,'sys.fn_remote_schemata')
go

if object_id('sys.fn_remote_schemata') is not null
    drop function sys.fn_remote_schemata
go
create function sys.fn_remote_schemata(
	@server		sysname,
	@catalog	sysname = NULL,
	@name		sysname = NULL,
	@owner		sysname = NULL)
returns table
as
return	select * from OpenRowset(SYSREMOTE_SCHEMATA, @server, @catalog, @name, @owner)
go

raiserror(15339,-1,-1,'sys.fn_remote_tables')
go

if object_id('sys.fn_remote_tables') is not null
    drop function sys.fn_remote_tables
go
create function sys.fn_remote_tables(
	@server		sysname,
	@catalog	sysname = NULL,
	@schema		sysname = NULL,
	@name		sysname = NULL,
	@type		sysname = NULL)
returns table
as
return select * from OpenRowset(SYSREMOTE_TABLES, @server, @catalog, @schema, @name, @type)
go

raiserror(15339,-1,-1,'sys.fn_remote_views')
go

if object_id('sys.fn_remote_views') is not null
    drop function sys.fn_remote_views
go
create function sys.fn_remote_views(
	@server		sysname,
	@catalog	sysname = NULL,
	@schema		sysname = NULL,
	@name		sysname = NULL)
returns table
as
return select * from OpenRowset(SYSREMOTE_VIEWS, @server, @catalog, @schema, @name)
go

raiserror(15339,-1,-1,'sys.fn_remote_columns')
go

if object_id('sys.fn_remote_columns') is not null
    drop function sys.fn_remote_columns
go
create function sys.fn_remote_columns(
	@server		sysname,
	@catalog	sysname = NULL,
	@schema		sysname = NULL,
	@table		sysname = NULL,
	@name		sysname = NULL)
returns table
as
return select * from OpenRowset(SYSREMOTE_COLUMNS, @server, @catalog, @schema, @table, @name)
go

raiserror(15339,-1,-1,'sys.fn_remote_indexes')
go

if object_id('sys.fn_remote_indexes') is not null
    drop function sys.fn_remote_indexes
go
create function sys.fn_remote_indexes(
	@server		sysname,
	@catalog	sysname = NULL,
	@tbl_schema	sysname = NULL,
	@name		sysname = NULL,
	@type		smallint = NULL,
	@table		sysname = NULL)
returns table
as
return select * from OpenRowset(SYSREMOTE_INDEXES, @server, @catalog, @tbl_schema, @name, @type, @table)
go

raiserror(15339,-1,-1,'sys.fn_remote_statistics')
go

if object_id('sys.fn_remote_statistics') is not null
    drop function sys.fn_remote_statistics
go
create function sys.fn_remote_statistics(
	@server		sysname,
	@catalog	sysname = NULL,
	@schema		sysname = NULL,
	@name		sysname = NULL)
returns table
as
return select * from OpenRowset(SYSREMOTE_STATISTICS, @server, @catalog, @schema, @name)
go

raiserror(15339,-1,-1,'sys.fn_remote_provider_types')
go

if object_id('sys.fn_remote_provider_types') is not null
    drop function sys.fn_remote_provider_types
go
create function sys.fn_remote_provider_types(
	@server		sysname,
	@data_type	smallint = NULL,
	@best_match	bit = NULL)
returns table
as
return select * from OpenRowset(SYSREMOTE_PROVIDER_TYPES, @server, @data_type, @best_match)
go

raiserror(15339,-1,-1,'sys.fn_remote_table_privileges')
go

if object_id('sys.fn_remote_table_privileges') is not null
    drop function sys.fn_remote_table_privileges
go
create function sys.fn_remote_table_privileges(
	@server		sysname,
	@catalog	sysname = NULL,	
	@schema		sysname = NULL,
	@name		sysname = NULL,
	@grantor	sysname = NULL,
	@grantee	sysname = NULL)
returns table
as
return select * from OpenRowset(SYSREMOTE_TABLE_PRIVILEGES, @server, @catalog, @schema, @name, @grantor, @grantee)
go

raiserror(15339,-1,-1,'sys.fn_remote_column_privileges')
go

if object_id('sys.fn_remote_column_privileges') is not null
    drop function sys.fn_remote_column_privileges
go
create function sys.fn_remote_column_privileges(
	@server		sysname,
	@catalog	sysname = NULL,	
	@schema		sysname = NULL,
	@table		sysname = NULL,
	@name		sysname = NULL,
	@grantor	sysname = NULL,
	@grantee	sysname = NULL)
returns table
as
return select * from OpenRowset(SYSREMOTE_COLUMN_PRIVILEGES, @server, @catalog, @schema, @table, @name, @grantor, @grantee)
go

raiserror(15339,-1,-1,'sys.fn_remote_primary_keys')
go

if object_id('sys.fn_remote_primary_keys') is not null
    drop function sys.fn_remote_primary_keys
go
create function sys.fn_remote_primary_keys(
	@server		sysname,
	@catalog	sysname = NULL,
	@schema		sysname = NULL,
	@tbl_name	sysname = NULL)
returns table
as
return select * from OpenRowset(SYSREMOTE_PRIMARY_KEYS, @server, @catalog, @schema, @tbl_name)
go

raiserror(15339,-1,-1,'sys.fn_remote_foreign_keys')
go

if object_id('sys.fn_remote_foreign_keys') is not null
    drop function sys.fn_remote_foreign_keys
go
create function sys.fn_remote_foreign_keys(
	@server		sysname,
	@pk_catalog	sysname = NULL,
	@pk_schema	sysname = NULL,
	@pk_name	sysname = NULL,
	@fk_catalog	sysname = NULL,
	@fk_schema	sysname = NULL,
	@fk_name	sysname = NULL)
returns table
as
return select * from OpenRowset(SYSREMOTE_FOREIGN_KEYS, @server, @pk_catalog, @pk_schema, @pk_name,
		@fk_catalog, @fk_schema, @fk_name)
go
