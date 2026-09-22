/*
** U_Tables.CQL    --- 1996/09/16 12:22
** Copyright Microsoft, Inc. 1994 - 2000
** All Rights Reserved.
** ***********************
** If this file is updated for Denali, then do not forget to update the target level for u_table.sql
** in sql\ntdbms\mkmaster\scriptdlls\upgradesrc\sqlscriptupgrade.cpp
**
*/

go
use master
go
set nocount on
go


declare @vdt varchar(99)
select  @vdt = convert(varchar,getdate(),113)
raiserror('Starting u_Tables.SQL at  %s',0,1,@vdt) with nowait
raiserror('This file creates all the system tables in master.',0,1)
go

-- Create a synonym spt_values in master pointing to spt_master in Resource DB,
-- for backward compat

if object_id('spt_values','U') IS NOT NULL
	begin
	print 'drop table spt_values ....'
	drop table spt_values
	end
go

if object_id('spt_values','SN') IS NOT NULL
	begin
	print 'drop synonym spt_values ....'
	drop synonym spt_values
	end
go

if object_id('spt_values','V') IS NOT NULL
	begin
	print 'drop view spt_values ....'
	drop view spt_values
	end
go

raiserror('Creating view ''%s''.', -1,-1,'spt_values')
go

create view spt_values as
select name collate database_default as name,
	number,
	type collate database_default as type,
	low, high, status
from sys.spt_values
go

EXEC sp_MS_marksystemobject 'spt_values'
go

grant select on spt_values to public
go

------------------------------------------------------------------

if object_id('spt_monitor','U') IS NOT NULL
	begin
	print 'drop table spt_monitor ....'
	drop table spt_monitor
	end
go

------------------------------------------------------------------
------------------------------------------------------------------

raiserror('Creating ''%s''.', -1,-1,'spt_monitor')
go

create table spt_monitor
(
	lastrun		datetime	NOT NULL,
	cpu_busy	int		NOT NULL,
	io_busy		int		NOT NULL,
	idle		int		NOT NULL,
	pack_received	int		NOT NULL,
	pack_sent	int		NOT NULL,
	connections	int		NOT NULL,
	pack_errors	int		NOT NULL,
	total_read	int		NOT NULL,
	total_write 	int		NOT NULL,
	total_errors 	int		NOT NULL
)
go

EXEC sp_MS_marksystemobject 'spt_monitor'
go

------------------------------------------------------------------

raiserror('Grant Select on spt_monitor',0,1)
go

grant select on spt_monitor to public
go


------------------------------------------------------------------
------------------------------------------------------------------


raiserror('Insert into spt_monitor ....',0,1)
go

insert into spt_monitor
	select
	lastrun = getdate(),
	cpu_busy = @@cpu_busy,
	io_busy = @@io_busy,
	idle = @@idle,
	pack_received = @@pack_received,
	pack_sent = @@pack_sent,
	connections = @@connections,
	pack_errors = @@packet_errors,
	total_read = @@total_read,
	total_write = @@total_write,
	total_errors = @@total_errors
go


-------------------------------------------------------------------------------------------------------
-- Extended Events Default Session: system_health
--
-- All wait types in this session use <= and >= for ranges in order to reduce the dependency on 
-- wait types outside of a range.
-- If wait type values are changed in future in \Sql\Ntdbms\dk\sos\include\sc_waittypes.h then this
-- session definition could break as it has a dependency on the values within ranges of wait types.
-- The only complete mitigation would be to only use = predicates but that would be a huge perf hit
-- as events are fired for this session very frequently in perf-sensitive code paths.
-- As a partial mitigation, static_asserts were added to InitXE() in \Sql\Ntdbms\ksource\serverma.cpp to
-- generate compile-time errors if any of the ranges are changed in future.
---------------------------------------------------------------------------------------------------------

    if exists(select * from sys.server_event_sessions where name='system_health')
        drop event session system_health on server
    go
    -- The predicates in this session have been carefully crafted to minimize impact of event collection
    -- Changing the predicate definition may impact system performance
    --
    create event session system_health on server
    add event sqlserver.error_reported
    (
        action (package0.callstack_rva, sqlserver.session_id, sqlserver.database_id, sqlserver.sql_text, sqlserver.tsql_stack)
        -- Get callstack, SPID, and query for all high severity errors ( above sev 20 )
        where severity >= 20
        -- Get callstack, SPID, and query for OOM errors ( 17803 , 701 , 802 , 8645 , 8651 , 8657 , 8902 ), Hekaton checkpoint/merge errors (41354, 41355, 41367, 41384), Hekaton compilation related errors (41336, 41309, 41312, 41313)
        or (error_number = 17803 or error_number = 701 or error_number = 802 or error_number = 8645 or error_number = 8651 or error_number = 8657 or error_number = 8902 or error_number = 41354 or error_number = 41355 or error_number = 41367 or error_number = 41384 or error_number = 41336 or error_number = 41309 or error_number = 41312 or error_number = 41313)
    ),
    add event sqlclr.clr_allocation_failure
        (action (package0.callstack_rva, sqlserver.session_id)),
    add event sqlclr.clr_virtual_alloc_failure
        (action (package0.callstack_rva, sqlserver.session_id)),
    add event sqlos.scheduler_monitor_non_yielding_ring_buffer_recorded,
    add event sqlserver.xml_deadlock_report,
    add event sqlos.wait_info
    (
        action (package0.callstack_rva, sqlserver.session_id, sqlserver.sql_text)
        where 
        (duration > 15000 and 
            (   
                (wait_type >= N'LATCH_NL' -- Waits for latches and important wait resources (not locks ) that have exceeded 15 seconds. 
                    and
                    (
                        (wait_type >= N'PAGELATCH_NL' and wait_type <= N'PAGELATCH_DT') --PAGELATCH_NL;PAGELATCH_KP;PAGELATCH_SH;PAGELATCH_UP;PAGELATCH_EX;PAGELATCH_DT
                        or (wait_type <= N'LATCH_DT') --LATCH_NL;LATCH_KP;LATCH_SH;LATCH_UP;LATCH_EX;LATCH_DT
                        or (wait_type >= N'PAGEIOLATCH_NL' and wait_type <= N'PAGEIOLATCH_DT') --PAGEIOLATCH_NL;PAGEIOLATCH_KP;PAGEIOLATCH_SH;PAGEIOLATCH_UP;PAGEIOLATCH_EX;PAGEIOLATCH_DT
                        or (wait_type >= N'IO_COMPLETION' and wait_type <= N'NETWORK_IO') --IO_COMPLETION;ASYNC_IO_COMPLETION;NETWORK_IO
                        or (wait_type = N'RESOURCE_SEMAPHORE')
                        or (wait_type = N'SOS_WORKER')
                        or (wait_type >= N'FCB_REPLICA_WRITE' and wait_type <= N'WRITELOG') --FCB_REPLICA_WRITE;FCB_REPLICA_READ;WRITELOG
                        or (wait_type = N'CMEMTHREAD')
                        or (wait_type = N'TRACEWRITE')
                        or (wait_type = N'RESOURCE_SEMAPHORE_MUTEX')
                    )
                )
                or 
                (duration > 30000       -- Waits for locks that have exceeded 30 secs.
                    and wait_type <= N'LCK_M_RX_X' -- all lock waits
                ) 
            )
        )
    ),
    add event sqlos.wait_info_external
    (
        action (package0.callstack_rva, sqlserver.session_id, sqlserver.sql_text)
        where 
        (duration > 5000 and
            (   
                (   -- Login related preemptive waits that have exceeded 5 seconds.
                    (wait_type >= N'PREEMPTIVE_OS_GENERICOPS' and wait_type <= N'PREEMPTIVE_OS_ENCRYPTMESSAGE') --PREEMPTIVE_OS_GENERICOPS;PREEMPTIVE_OS_AUTHENTICATIONOPS;PREEMPTIVE_OS_ACCEPTSECURITYCONTEXT;PREEMPTIVE_OS_ACQUIRECREDENTIALSHANDLE;PREEMPTIVE_OS_COMPLETEAUTHTOKEN;PREEMPTIVE_OS_DECRYPTMESSAGE;PREEMPTIVE_OS_DELETESECURITYCONTEXT;PREEMPTIVE_OS_ENCRYPTMESSAGE
                    or  (wait_type >= N'PREEMPTIVE_OS_INITIALIZESECURITYCONTEXT' and wait_type <= N'PREEMPTIVE_OS_QUERYSECURITYCONTEXTTOKEN') --PREEMPTIVE_OS_INITIALIZESECURITYCONTEXT;PREEMPTIVE_OS_LOGONUSER;PREEMPTIVE_OS_QUERYSECURITYCONTEXTTOKEN
                    or  (wait_type >= N'PREEMPTIVE_OS_AUTHZGETINFORMATIONFROMCONTEXT' and wait_type <= N'PREEMPTIVE_OS_REVERTTOSELF') --PREEMPTIVE_OS_AUTHZGETINFORMATIONFROMCONTEXT;PREEMPTIVE_OS_AUTHZINITIALIZECONTEXTFROMSID;PREEMPTIVE_OS_AUTHZINITIALIZERESOURCEMANAGER;PREEMPTIVE_OS_LOOKUPACCOUNTSID;PREEMPTIVE_OS_REVERTTOSELF
                    or  (wait_type >= N'PREEMPTIVE_OS_CRYPTACQUIRECONTEXT' and wait_type <= N'PREEMPTIVE_OS_DEVICEOPS') --PREEMPTIVE_OS_CRYPTACQUIRECONTEXT;PREEMPTIVE_OS_CRYPTIMPORTKEY;PREEMPTIVE_OS_DEVICEOPS
                    or  (wait_type >= N'PREEMPTIVE_OS_NETGROUPGETUSERS' and wait_type <= N'PREEMPTIVE_OS_NETUSERMODALSGET') --PREEMPTIVE_OS_NETGROUPGETUSERS;PREEMPTIVE_OS_NETLOCALGROUPGETMEMBERS;PREEMPTIVE_OS_NETUSERGETGROUPS;PREEMPTIVE_OS_NETUSERGETLOCALGROUPS;PREEMPTIVE_OS_NETUSERMODALSGET
                    or  (wait_type >= N'PREEMPTIVE_OS_NETVALIDATEPASSWORDPOLICYFREE' and wait_type <= N'PREEMPTIVE_OS_DOMAINSERVICESOPS') --PREEMPTIVE_OS_NETVALIDATEPASSWORDPOLICYFREE;PREEMPTIVE_OS_DOMAINSERVICESOPS
                    or (wait_type = N'PREEMPTIVE_OS_VERIFYSIGNATURE')
                )
                or 
                (duration > 45000   -- Preemptive OS waits that have exceeded 45 seconds. 
                    and 
                    (   
                        (wait_type >= N'PREEMPTIVE_OS_SETNAMEDSECURITYINFO' and wait_type <= N'PREEMPTIVE_CLUSAPI_CLUSTERRESOURCECONTROL') --PREEMPTIVE_OS_SETNAMEDSECURITYINFO;PREEMPTIVE_OS_CLUSTEROPS;PREEMPTIVE_CLUSAPI_CLUSTERRESOURCECONTROL
                        or  (wait_type >= N'PREEMPTIVE_OS_RSFXDEVICEOPS' and wait_type <= N'PREEMPTIVE_OS_DSGETDCNAME') --PREEMPTIVE_OS_RSFXDEVICEOPS;PREEMPTIVE_OS_DIRSVC_NETWORKOPS;PREEMPTIVE_OS_DSGETDCNAME
                        or  (wait_type >= N'PREEMPTIVE_OS_DTCOPS' and wait_type <= N'PREEMPTIVE_DTC_ABORT') --PREEMPTIVE_OS_DTCOPS;PREEMPTIVE_DTC_ABORT
                        or  (wait_type >= N'PREEMPTIVE_OS_CLOSEHANDLE' and wait_type <= N'PREEMPTIVE_OS_FINDFILE') --PREEMPTIVE_OS_CLOSEHANDLE;PREEMPTIVE_OS_COPYFILE;PREEMPTIVE_OS_CREATEDIRECTORY;PREEMPTIVE_OS_CREATEFILE;PREEMPTIVE_OS_DELETEFILE;PREEMPTIVE_OS_DEVICEIOCONTROL;PREEMPTIVE_OS_FINDFILE
                        or  (wait_type >= N'PREEMPTIVE_OS_GETCOMPRESSEDFILESIZE' and wait_type <= N'PREEMPTIVE_ODBCOPS') --PREEMPTIVE_OS_GETCOMPRESSEDFILESIZE;PREEMPTIVE_OS_GETDISKFREESPACE;PREEMPTIVE_OS_GETFILEATTRIBUTES;PREEMPTIVE_OS_GETFILESIZE;PREEMPTIVE_OS_GETLONGPATHNAME;PREEMPTIVE_OS_GETVOLUMEPATHNAME;PREEMPTIVE_OS_GETVOLUMENAMEFORVOLUMEMOUNTPOINT;PREEMPTIVE_OS_MOVEFILE;PREEMPTIVE_OS_OPENDIRECTORY;PREEMPTIVE_OS_REMOVEDIRECTORY;PREEMPTIVE_OS_SETENDOFFILE;PREEMPTIVE_OS_SETFILEPOINTER;PREEMPTIVE_OS_SETFILEVALIDDATA;PREEMPTIVE_OS_WRITEFILE;PREEMPTIVE_OS_WRITEFILEGATHER;PREEMPTIVE_OS_LIBRARYOPS;PREEMPTIVE_OS_FREELIBRARY;PREEMPTIVE_OS_GETPROCADDRESS;PREEMPTIVE_OS_LOADLIBRARY;PREEMPTIVE_OS_MESSAGEQUEUEOPS;PREEMPTIVE_ODBCOPS
                        or  (wait_type >= N'PREEMPTIVE_OS_DISCONNECTNAMEDPIPE' and wait_type <= N'PREEMPTIVE_CLOSEBACKUPMEDIA') --PREEMPTIVE_OS_DISCONNECTNAMEDPIPE;PREEMPTIVE_OS_PROCESSOPS;PREEMPTIVE_OS_SECURITYOPS;PREEMPTIVE_OS_SERVICEOPS;PREEMPTIVE_OS_SQLCLROPS;PREEMPTIVE_OS_WINSOCKOPS;PREEMPTIVE_OS_GETADDRINFO;PREEMPTIVE_OS_WSASETLASTERROR;PREEMPTIVE_OS_FORMATMESSAGE;PREEMPTIVE_OS_REPORTEVENT;PREEMPTIVE_OS_BACKUPREAD;PREEMPTIVE_OS_WAITFORSINGLEOBJECT;PREEMPTIVE_OS_QUERYREGISTRY;PREEMPTIVE_CLOSEBACKUPMEDIA
                        or wait_type = N'PREEMPTIVE_OS_AUTHENTICATIONOPS'
                        or wait_type = N'PREEMPTIVE_OS_FREECREDENTIALSHANDLE'
                        or wait_type = N'PREEMPTIVE_OS_AUTHORIZATIONOPS'
                        or wait_type = N'PREEMPTIVE_COM_COCREATEINSTANCE'
                        or wait_type = N'PREEMPTIVE_OS_NETVALIDATEPASSWORDPOLICY'
                        or wait_type = N'PREEMPTIVE_VSS_CREATESNAPSHOT'
                    )
                )
            )
        )
    ),
    add event sqlos.memory_broker_ring_buffer_recorded,
    add event sqlos.scheduler_monitor_deadlock_ring_buffer_recorded,
    add event sqlos.scheduler_monitor_system_health_ring_buffer_recorded,
    add event sqlos.scheduler_monitor_non_yielding_iocp_ring_buffer_recorded,
    add event sqlos.scheduler_monitor_non_yielding_rm_ring_buffer_recorded,
    add event sqlos.scheduler_monitor_stalled_dispatcher_ring_buffer_recorded,
    add event sqlos.memory_node_oom_ring_buffer_recorded
        (action (package0.callstack_rva, sqlserver.session_id, sqlserver.sql_text, sqlserver.tsql_stack)),
    add event sqlserver.security_error_ring_buffer_recorded
        (set collect_call_stack = (0)
         action (package0.callstack_rva)),
    add event sqlserver.connectivity_ring_buffer_recorded
        (set collect_call_stack = (0)
         action (package0.callstack_rva)),
add event sqlserver.sp_server_diagnostics_component_result
    (
        set collect_data = 1
        where
            sqlserver.is_system = 1 and
            component != 4 /* DiagnoseComponent::DCCI_EVENTS */
    ),
    add event sqlserver.job_object_ring_buffer_stats,
    add event sqlserver.nonyield_copiedstack_ring_buffer_recorded
    add target package0.event_file      -- Store events on disk (in the LOG folder of the instance)
    (
        set filename           = N'system_health.xel',
            max_file_size      = 5, /* MB */
            max_rollover_files = 4
    ),
    add target package0.ring_buffer     -- Store events in the ring buffer target
        (set max_memory = 4096, max_events_limit = 5000)
    with
    (
        MAX_DISPATCH_LATENCY = 120 SECONDS,
        startup_state = on
    )
    go

    if not exists (select * from sys.dm_xe_sessions where name = 'system_health')
        alter event session system_health on server state=start
    go


-- AlwaysOn default session: AlwaysOn_health
-- The session start state is based on old session state.
create table #ahsession_start_state
(
    session_name    VARCHAR(20)     NOT NULL,
    old_session_state    int        NOT NULL
)

insert into #ahsession_start_state select 'AlwaysOn_health', 0
go

if exists (select * from sys.server_event_sessions where name = 'AlwaysOn_health' and startup_state = 1)
    update #ahsession_start_state
    set old_session_state = 1
    where session_name = 'AlwaysOn_health'
go

if exists(select * from sys.server_event_sessions where name='AlwaysOn_health')
	drop event session AlwaysOn_health on server;
go

create event session AlwaysOn_health on server 
    add event sqlserver.alwayson_ddl_executed,
    add event sqlserver.availability_group_lease_expired,
    add event sqlserver.availability_replica_automatic_failover_validation,
    add event sqlserver.availability_replica_manager_state_change,
    add event sqlserver.availability_replica_state,
    add event sqlserver.availability_replica_state_change,
    add event sqlserver.hadr_db_partner_set_sync_state,
    add event lock_redo_blocked,
    -- to help debug replica connection timeout issue.
    add event ucs.ucs_connection_setup,
    -- to also print hadr 3605 TF enabled messages to alwayson_health xevent session
    add event sqlserver.hadr_trace_message,
    -- to capture sp_server_diagnostics XEvent when STATE=3
    add event sqlserver.sp_server_diagnostics_component_result(set collect_data=(1)
    where ([state]=(3))),
    add event sqlserver.error_reported
    (
        where 
        (
            --endpoint issue:stopped
            [error_number]=(9691)  
            or [error_number]=(35204) 
        
            --endpoint issue:invalid ip address
            or [error_number]=(9693) 
            or [error_number]=(26024)
         
            --endpoint issue:encryption and handshake issue
            or [error_number]=(28047)

            --endpoint issue:port conflict
            or [error_number]=(26023)
            or [error_number]=(9692) 

            --endpoint issue:authentication failure
            or [error_number]=(28034) 
            or [error_number]=(28036) 
            or [error_number]=(28048) 
            or [error_number]=(28080) 
            or [error_number]=(28091) 

            --endpoint:listening
            or [error_number]=(26022) 

            --endpoint issue:generic message
            or [error_number]=(9642) 

            --alwayson connection timeout information
            or [error_number]=(35201) --new connection timeout
            or [error_number]=(35202) --connected
            or [error_number]=(35206) --existing connection timeout
            or [error_number]=(35207) --general connection issue message

            --alwayson listener state
            or [error_number]=(26069) --started 
            or [error_number]=(26070) --stopped

            --wsfc cluster issues
            or [error_number]>(41047) and [error_number]<(41056)

            --failover validation message
            or [error_number]=(41142) 

            --availability group resource failure
            or [error_number]=(41144) 
            
            --database replica role change	
            or [error_number]=(1480) 

            --automatic page repair event
            or [error_number]=(823) 
            or [error_number]=(824) 
            or [error_number]=(829) 
            
            --database replica suspended resumed
            or [error_number]=(35264) 
            or [error_number]=(35265)

            --alwayson alter ag rollback
            or [error_number]=(41188) 
            or [error_number]=(41189) 

            --alwayson not enough worker threads
            or [error_number]=(35217)
        )
    ) 

    add target package0.event_file
    (
        set filename = N'AlwaysOn_health.xel',
            max_file_size = 5,
            max_rollover_files = 4
    )
    with 
    (
        max_memory = 4 mb,
        event_retention_mode = allow_single_event_loss,
        max_dispatch_latency = 30 seconds,
        max_event_size = 0 mb,
        memory_partition_mode = none,
        track_causality = off,
        startup_state=off
    );
go

-- Set new AlwaysOn_health session start state based on old session state.
declare @oldAlwaysonHealthSessionState int;
select @oldAlwaysonHealthSessionState = old_session_state 
from #ahsession_start_state
where session_name = 'AlwaysOn_health'

if @oldAlwaysonHealthSessionState = 1
begin
    print 'Alter AlwaysOn_health session default start state.';

    alter event session AlwaysOn_health on server drop target package0.event_file;
    alter event session AlwaysOn_health on server
    add target package0.event_file
    (
        set filename = N'AlwaysOn_health.xel',
            max_file_size = 5,
            max_rollover_files = 4
    )
    with 
    (
        max_memory = 4 mb,
        event_retention_mode = allow_single_event_loss,
        max_dispatch_latency = 30 seconds,
        max_event_size = 0 mb,
        memory_partition_mode = none,
        track_causality = off,
        startup_state=on
    );

    alter event session AlwaysOn_health on server state=start;
end
go

drop table #ahsession_start_state
go

-------------------------------------------------------------------------------------------------------
-- Extended Events Telemetry Session: telemetry_xevents
--
---------------------------------------------------------------------------------------------------------

if exists(select * from sys.server_event_sessions where name='telemetry_xevents')
    drop event session telemetry_xevents on server
go
-- The above code here is only for historical reasons. telemetry_xevents is not 
-- defined in $\Sql\Ntdbms\sqlceip\EventSessionDefinition.sql

declare @vdt varchar(99)
select  @vdt = convert(varchar,getdate(),113)
raiserror('Finishing at  %s',0,1,@vdt)
go

checkpoint
go



