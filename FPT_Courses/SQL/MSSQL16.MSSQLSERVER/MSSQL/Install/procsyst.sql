/*
** ProcSyst.SQL
** Copyright Microsoft, Inc. 1994 - 2000
** All Rights Reserved.
*/

go
use master
go

----- DO NOT ADD SYSTEM OBJECTS HERE. Place them in a script for the resource-database.

set nocount on
set implicit_transactions off
set ansi_nulls on	-- default for osql (consistent for suites)
set quoted_identifier on	-- Force all ye devs to do this correctly!
go


----- DO NOT ADD SYSTEM OBJECTS HERE. Place them in a script for the resource-database.


-- Drop client-side tables in master. They have been moved to resouce database.
--
if object_id('spt_provider_types', 'local') is not null
	drop table spt_provider_types
if object_id('spt_datatype_info_ext', 'local') is not null
	drop table spt_datatype_info_ext
if object_id('spt_datatype_info', 'local') is not null
	drop table spt_datatype_info
if object_id('spt_server_info', 'local') is not null
	drop table spt_server_info
go


-- Drop stored procedures no longer in use
if object_id('sp_msupg_removesystemcomputedcolumns', 'local') is not null
	drop procedure sp_msupg_removesystemcomputedcolumns
if object_id('sp_msupg_recreatecatalogfaketables', 'local') is not null
	drop procedure sp_msupg_recreatecatalogfaketables
if object_id('sp_msupg_dosystabcatalogupgrades', 'local') is not null
	drop procedure sp_msupg_dosystabcatalogupgrades
if object_id('sp_msupg_dropcatalogcomputedcols', 'local') is not null
	drop procedure sp_msupg_dropcatalogcomputedcols
if object_id('sp_msupg_createcatalogcomputedcols', 'local') is not null
	drop procedure sp_msupg_createcatalogcomputedcols
if object_id('sp_msupg_recreatesystemviews', 'local') is not null
	drop procedure sp_msupg_recreatesystemviews
if object_id('sp_msupg_upgradecatalog', 'local') is not null
	drop procedure sp_msupg_upgradecatalog
if object_id('sp_db_upgrade', 'local') is not null
	drop procedure sp_db_upgrade
if object_id('sp_MS_upd_sysobj_category', 'local') is not null
	drop procedure sp_MS_upd_sysobj_category
if object_id('sp_remove_tempdb_file', 'local') is not null
	drop procedure sp_remove_tempdb_file
if object_id('sp_validatepropertyinputs', 'local') is not null
	drop procedure sp_validatepropertyinputs
if object_id('sp_helplog', 'local') is not null
	drop procedure sp_helplog
if object_id('sp_helpsql', 'local') is not null
	drop procedure sp_helpsql
if object_id('sp_fixindex', 'local') is not null
	drop procedure sp_fixindex
if object_id('sp_diskdefault', 'local') is not null
	drop procedure sp_diskdefault	
if object_id('sp_logdevice', 'local') is not null
	drop procedure sp_logdevice
if object_id('sp_sdidebug', 'local') is not null
	drop procedure sp_sdidebug
if object_id('xp_MSFullText', 'local') is not null
	drop procedure xp_MSFullText	
go

if object_id('xp_getprotocoldllinfo', 'local') is not null
	drop procedure xp_getprotocoldllinfo	
if object_id('xp_sqlagent_proxy_account', 'local') is not null
	drop procedure xp_sqlagent_proxy_account	
if object_id('xp_sqlagent_msx_account', 'local') is not null
	drop procedure xp_sqlagent_msx_account	
if object_id('xp_ntsec_enumdomains', 'local') is not null
	drop procedure xp_ntsec_enumdomains	
if object_id('xp_updateFTSSQLAccount', 'local') is not null
	drop procedure xp_updateFTSSQLAccount	
if object_id('xp_unc_to_drive', 'local') is not null
	drop procedure xp_unc_to_drive	
go

if object_id('sp_add_server_sortinfo', 'local') is not null
	drop procedure sp_add_server_sortinfo	
if object_id('sp_add_server_sortinfo75', 'local') is not null
	drop procedure sp_add_server_sortinfo75	
if object_id('sp_MScheck_uid_owns_anything', 'local') is not null
	drop procedure sp_MScheck_uid_owns_anything	
if object_id('sp_MSget_current_activity', 'local') is not null
	drop procedure sp_MSget_current_activity	
if object_id('sp_MSset_current_activity', 'local') is not null
	drop procedure sp_MSset_current_activity	
if object_id('sp_MSobjsearch', 'local') is not null
	drop procedure sp_MSobjsearch	
go

if object_id('sp_blockcnt', 'local') is not null
	drop procedure sp_blockcnt	
if object_id('sp_tempdbspace', 'local') is not null
	drop procedure sp_tempdbspace	
if object_id('sp_fallback_MS_sel_fb_svr', 'local') is not null
	drop procedure sp_fallback_MS_sel_fb_svr	
if object_id('sp_checknames', 'local') is not null
	drop procedure sp_checknames	
if object_id('sp_oledb_column_constraints', 'local') is not null
	drop procedure sp_oledb_column_constraints	
if object_id('sp_oledb_indexinfo', 'local') is not null
	drop procedure sp_oledb_indexinfo
go

if object_id('MS_sqlctrs_users', 'local') is not null
	drop procedure MS_sqlctrs_users
if object_id('sp_addalias','P') IS NOT NULL
	drop procedure sp_addalias
if object_id('sp_addgroup','P') IS NOT NULL
	drop procedure sp_addgroup
if object_id('sp_dropgroup','P') IS NOT NULL
	drop procedure sp_dropgroup
if object_id('sp_changegroup','P') IS NOT NULL
	drop procedure sp_changegroup
if object_id('sp_helpgroup','P') IS NOT NULL
	drop procedure sp_helpgroup
go

-- From 7.0, dropped in 8.0
if object_id('spt_committab','local') is not null
	drop table spt_committab
if object_id('sysalternates','local') is not null
	drop view sysalternates
if object_id('sp_abort_xact','local') is not null
	drop procedure sp_abort_xact
if object_id('sp_checkdbtempsize','local') is not null
	drop procedure sp_checkdbtempsize
if object_id('sp_checktabletempsize','local') is not null
	drop procedure sp_checktabletempsize
if object_id('sp_commit_xact','local') is not null
	drop procedure sp_commit_xact
if object_id('sp_helpstartup','local') is not null
	drop procedure sp_helpstartup
if object_id('sp_makestartup','local') is not null
	drop procedure sp_makestartup
if object_id('sp_probe_xact','local') is not null
	drop procedure sp_probe_xact
if object_id('sp_remove_xact','local') is not null
	drop procedure sp_remove_xact
if object_id('sp_scan_xact','local') is not null
	drop procedure sp_scan_xact
if object_id('sp_start_xact','local') is not null
	drop procedure sp_start_xact
if object_id('sp_stat_xact','local') is not null
	drop procedure sp_stat_xact
if object_id('sp_unmakestartup','local') is not null
	drop procedure sp_unmakestartup
go

checkpoint
go


----- DO NOT ADD SYSTEM OBJECTS HERE. Place them in a script for the resource-database.

