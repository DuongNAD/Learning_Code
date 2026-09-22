/*
**  SSIS_hotfix_install.SQL
**  Patch install script for the SSIS server catalog (SSISDB).
*/

PRINT '------------------------------------------------------'
PRINT 'Starting execution of SSIS_HOTFIX_INSTALL.SQL         '
PRINT '------------------------------------------------------'

DECLARE @run_script BIT
SET @run_script=1

DECLARE @ssis_database_name SYSNAME
SET @ssis_database_name = N'SSISDB'

-- Check whether SSISDB exists
IF(DB_ID(@ssis_database_name) IS NULL)
BEGIN
    SET @run_script=0
    PRINT 'Database SSISDB does not exist in current SQL Server instance'
END

-- Check whether SSISDB is online
IF @run_script <> 0
BEGIN
	DECLARE @state_online SYSNAME
	SET @state_online = 'ONLINE'
	SELECT @state_online = UPPER(@state_online COLLATE SQL_Latin1_General_CP1_CI_AS)

	IF NOT EXISTS (SELECT state_desc FROM master.sys.databases WHERE name = @ssis_database_name AND
										 UPPER(state_desc COLLATE SQL_Latin1_General_CP1_CI_AS) LIKE @state_online)
	BEGIN
		SET @run_script=0    
		PRINT 'WARNING! The database SSISDB is not ONLINE. SSIS_HOTFIX_INSTALL.SQL will not be applied. Please run the script manually after the upgrade.'
	END
END

-- Check SSISDB is not in always-on group
IF @run_script <> 0
BEGIN
	IF EXISTS (SELECT hadr.database_state FROM master.sys.dm_hadr_database_replica_states AS hadr 
			JOIN master.sys.databases AS dbs 
			ON hadr.database_id = dbs.database_id 
			WHERE dbs.name = @ssis_database_name)
	BEGIN
		SET @run_script=0
		PRINT 'WARNING! The database SSISDB is in alwayson group. So skipping execution of ISServer_upgrade.sql on it. Please run the script manually after the upgrade.'
	END
END

-- Check whether SSISDB is corrupted
IF @run_script <> 0
BEGIN
	IF OBJECT_ID (N'SSISDB.internal.catalog_properties', N'U') IS NULL
	BEGIN
		SET @run_script=0
		PRINT 'Database SSISDB is missing the catalog properties table. The database may be corrupted, or it is not an SSIS Catalog.'
	END
END

IF  @run_script <> 0
BEGIN
	PRINT 'Start applying SSIS_HOTFIX_INSTALL changes.'

	DECLARE @rawCmd NVARCHAR(MAX), @cmd NVARCHAR(MAX)

	DECLARE @targetVersion NVARCHAR(256)
	SELECT @targetVersion = CONVERT(NVARCHAR,SERVERPROPERTY(N'ProductVersion'))
		
    --CU 9
    IF NOT EXISTS (SELECT * FROM SSISDB.sys.indexes WHERE name = 'IX_EventMessageContext_EventMessageId'  AND object_id = OBJECT_ID('[SSISDB].[internal].[event_message_context]'))
    BEGIN
        SET @rawCmd = N'CREATE NONCLUSTERED INDEX [IX_EventMessageContext_EventMessageId]
ON [SSISDB].[internal].[event_message_context] 
([event_message_id] ASC)'
        SET @cmd = N'EXEC SSISDB.dbo.sp_executesql @statement=N''' + @rawCmd + ''''
	    EXEC sp_executesql @cmd
    END

    IF NOT EXISTS (SELECT * FROM SSISDB.sys.indexes WHERE name = 'IX_ExecutionPropertyOverrideValues_ExecutionId'  AND object_id = OBJECT_ID('[SSISDB].[internal].[execution_property_override_values]'))
    BEGIN
        SET @rawCmd = N'CREATE NONCLUSTERED INDEX [IX_ExecutionPropertyOverrideValues_ExecutionId]
ON [SSISDB].[internal].[execution_property_override_values]
([execution_id] ASC)'
        SET @cmd = N'EXEC SSISDB.dbo.sp_executesql @statement=N''' + @rawCmd + ''''
	    EXEC sp_executesql @cmd
    END

    --1. drop the old SP

    IF OBJECT_ID (N'SSISDB.[catalog].[set_execution_property_override_value]', N'P') IS NOT NULL
	BEGIN
		SET @rawCmd = N'DROP PROCEDURE [catalog].[set_execution_property_override_value]'
		SET @cmd = N'EXEC SSISDB.dbo.sp_executesql @statement=N''' + @rawCmd + ''''
		EXEC sp_executesql @cmd

		PRINT 'Stored procedure [catalog].[set_execution_property_override_value] has been dropped.'
	END

    --2. create the new SP
    IF OBJECT_ID (N'SSISDB.[catalog].[set_execution_property_override_value]', N'P') IS NULL
	BEGIN
		SET @rawCmd = N'
        CREATE PROCEDURE [catalog].[set_execution_property_override_value]
        @execution_id       bigint,   
        @property_path      nvarchar(4000), 
        @property_value     nvarchar(max),  
	    @sensitive			bit

WITH EXECUTE AS ''''AllSchemaOwner''''
AS 
    SET NOCOUNT ON
    
    
    DECLARE @caller_id     int
    DECLARE @caller_name   [internal].[adt_sname]
    DECLARE @caller_sid    [internal].[adt_sid]
    DECLARE @suser_name    [internal].[adt_sname]
    DECLARE @suser_sid     [internal].[adt_sid]
    
    EXECUTE AS CALLER
        EXEC [internal].[get_user_info]
            @caller_name OUTPUT,
            @caller_sid OUTPUT,
            @suser_name OUTPUT,
            @suser_sid OUTPUT,
            @caller_id OUTPUT;
          
          
        IF(
            EXISTS(SELECT [name]
                    FROM sys.server_principals
                    WHERE [sid] = @suser_sid AND [type] = ''''S'''')  
            OR
            EXISTS(SELECT [name]
                    FROM sys.database_principals
                    WHERE ([sid] = @caller_sid AND [type] = ''''S'''')) 
            )
        BEGIN
            RAISERROR(27123, 16, 1) WITH NOWAIT
            RETURN 1
        END
    REVERT
    
    IF(
            EXISTS(SELECT [name]
                    FROM sys.server_principals
                    WHERE [sid] = @suser_sid AND [type] = ''''S'''')  
            OR
            EXISTS(SELECT [name]
                    FROM sys.database_principals
                    WHERE ([sid] = @caller_sid AND [type] = ''''S'''')) 
            )
    BEGIN
            RAISERROR(27123, 16, 1) WITH NOWAIT
            RETURN 1
    END
    
    DECLARE @result int
    DECLARE @id bigint
    DECLARE @sensitive_value varbinary(MAX)
    DECLARE @calculated_property_value nvarchar(MAX)
    DECLARE @return_value           bit = 1
    
    IF (@execution_id IS NULL OR @property_path IS NULL OR @property_value IS NULL)
    BEGIN
        RAISERROR(27138, 16 , 1) WITH NOWAIT 
        RETURN 1 
    END   
    
    IF @execution_id <= 0
    BEGIN
        RAISERROR(27101, 16 , 1, N''''execution_id'''') WITH NOWAIT
        RETURN 1;
    END
    
    DECLARE @sqlString              nvarchar(1024)
    DECLARE @key_name               [internal].[adt_name]
    DECLARE @certificate_name       [internal].[adt_name]
    DECLARE @encryption_algorithm   nvarchar(255)    
    DECLARE @server_operation_encryption_level int

    
    SET TRANSACTION ISOLATION LEVEL REPEATABLE READ
    
    
    
    DECLARE @tran_count INT = @@TRANCOUNT;
    DECLARE @savepoint_name NCHAR(32);
    IF @tran_count > 0
    BEGIN
        SET @savepoint_name = REPLACE(CONVERT(NCHAR(36), NEWID()), N''''-'''', N'''''''');
        SAVE TRANSACTION @savepoint_name;
    END
    ELSE
        BEGIN TRANSACTION;                                                                                      
    BEGIN TRY 
        EXECUTE AS CALLER   
            SET @result = [internal].[check_permission] 
                (
                    4,
                    @execution_id,
                    2
                ) 
        REVERT
        
        IF @result = 0
        BEGIN
            RAISERROR(27103 , 16 , 1, @execution_id) WITH NOWAIT        
        END  
        
        DECLARE @project_id bigint
        DECLARE @status int
        EXECUTE AS CALLER
            SELECT @project_id = [object_id], @status = [status]
            FROM [catalog].[operations]
            WHERE [operation_id] = @execution_id 
                  AND [object_type] = 20
                  AND [operation_type] = 200
        REVERT
        
        IF (@project_id IS NULL)
        BEGIN
            RAISERROR(27103 , 16 , 1, @execution_id) WITH NOWAIT
        END
       
        IF  @status <> 1
        BEGIN
            RAISERROR(27225 , 16 , 1) WITH NOWAIT
        END
       
        SELECT @server_operation_encryption_level = CONVERT(int,property_value)  
                FROM [catalog].[catalog_properties]
                WHERE property_name = ''''SERVER_OPERATION_ENCRYPTION_LEVEL''''

        IF @server_operation_encryption_level NOT in (1, 2)        
        BEGIN
            RAISERROR(27163    ,16,1,''''SERVER_OPERATION_ENCRYPTION_LEVEL'''')
        END
       
        IF @sensitive = 1
        BEGIN
            IF @server_operation_encryption_level = 1
            BEGIN
            SET @key_name = ''''MS_Enckey_Exec_''''+CONVERT(varchar,@execution_id)
            SET @certificate_name = ''''MS_Cert_Exec_''''+CONVERT(varchar,@execution_id) 
            END
            ELSE BEGIN
                SET @key_name = ''''MS_Enckey_Proj_Param_''''+CONVERT(varchar,@project_id)
                SET @certificate_name = ''''MS_Cert_Proj_Param_''''+CONVERT(varchar,@project_id)
            END
     
            SET @sqlString = ''''OPEN SYMMETRIC KEY '''' + @key_name 
                + '''' DECRYPTION BY CERTIFICATE '''' + @certificate_name  
            EXECUTE sp_executesql @sqlString
            
            SET @sensitive_value = EncryptByKey(KEY_GUID(@key_name),CONVERT(varbinary(MAX),@property_value))
			SET @calculated_property_value = NULL
            
            SET @sqlString = ''''CLOSE SYMMETRIC KEY ''''+ @key_name
            EXECUTE sp_executesql @sqlString  
		END

		ELSE

		BEGIN
            SET @sensitive_value = NULL
			SET @calculated_property_value = @property_value
		END
            
		IF EXISTS 
		(
			SELECT 1
			FROM [internal].[execution_property_override_values] WITH (NOLOCK)
			WHERE execution_id = @execution_id
			AND property_path = @property_path
		)
		BEGIN
			UPDATE [internal].[execution_property_override_values]
			SET
				property_value = @calculated_property_value,
				sensitive_property_value = @sensitive_value,
				sensitive = @sensitive
		END

		ELSE

		BEGIN
			INSERT INTO [internal].[execution_property_override_values]
			(
				execution_id,
				property_path,
				sensitive,
				property_value,
				sensitive_property_value
			)
			VALUES
			(
				@execution_id,
				@property_path,
				@sensitive,
				@calculated_property_value,
				@sensitive_value
			)
        END
               
        
        IF @tran_count = 0
            COMMIT TRANSACTION;                                                                                 
    END TRY
    
    BEGIN CATCH
        
        IF @tran_count = 0 
            ROLLBACK TRANSACTION;
        
        ELSE IF XACT_STATE() <> -1
            ROLLBACK TRANSACTION @savepoint_name;                                                                           
        THROW;
    END CATCH
     
    RETURN 0'

        SET @cmd = N'EXEC SSISDB.dbo.sp_executesql @statement=N''' + @rawCmd + ''''
		EXEC sp_executesql @cmd
		PRINT 'Stored procedure [catalog].[set_execution_property_override_value] has been recreated.'
	END
    --3. grant the permission on new one

	IF OBJECT_ID (N'SSISDB.[catalog].[set_execution_property_override_value]', N'P') IS NOT NULL
	BEGIN
		SET @rawCmd = N'GRANT EXECUTE ON [catalog].[set_execution_property_override_value] TO [PUBLIC]'
		SET @cmd = N'EXEC SSISDB.dbo.sp_executesql @statement=N''' + @rawCmd + ''''
		EXEC sp_executesql @cmd
		PRINT 'Permissions on [catalog].[set_execution_property_override_value] has been granted.'
	END

	--4. Finally update the schema build number to server's build number
	SET @cmd = 'UPDATE [SSISDB].[internal].[catalog_properties] SET property_value = N'''+@targetVersion+''' WHERE property_name = N''SCHEMA_BUILD'''
	EXEC sp_executesql @cmd
	PRINT 'Schema build in SSISDB has been updated to ' + @targetVersion

END

PRINT '------------------------------------------------------'
PRINT 'Execution of SSIS_HOTFIX_INSTALL.SQL completed'
PRINT '------------------------------------------------------'
GO


