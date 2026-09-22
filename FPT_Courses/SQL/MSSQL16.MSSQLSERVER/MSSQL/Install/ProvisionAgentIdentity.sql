/**********************************************************************/
/* ProvisionAgentIdentity.sql                                            */
/*                                                                    */
/* This script is called during setup to provision SQL Server Agent   */
/* user group on SQL Server                                           */
/*                                                                    */
/* Copyright (c) Microsoft Corporation                                */
/* All Rights Reserved.                                               */
/*                                                                    */
/**********************************************************************/

-- push and enable option state for xp_instance_regread in case categories are off
DECLARE @advopt_old_value INT;
DECLARE @comp_old_value   INT;
SELECT @advopt_old_value=cast(value_in_use as int) from sys.configurations where name = 'show advanced options';
SELECT @comp_old_value=cast(value_in_use as int) from sys.configurations where name = 'Agent XPs';
EXEC sp_configure 'show advanced options', 1; 
RECONFIGURE WITH OVERRIDE;
EXEC sp_configure 'Agent XPs', 1;
RECONFIGURE WITH OVERRIDE; 

DECLARE @AgentLoginSID nvarchar(256) -- SID of service account or service principal representing agent service
DECLARE @AGTGroupSID nvarchar (256) -- Name of the agent group SID
EXEC master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'SOFTWARE\Microsoft\MSSQLServer\Setup', N'AGTService', @AgentLoginSID OUTPUT, no_output
EXEC master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'SOFTWARE\Microsoft\MSSQLServer\Setup', N'AGTGroup', @AGTGroupSID OUTPUT

-- restore option state
EXEC sp_configure 'Agent XPs', @comp_old_value;
RECONFIGURE WITH OVERRIDE; 
EXEC sp_configure 'show advanced options', @advopt_old_value; 
RECONFIGURE WITH OVERRIDE;

BEGIN
	IF (@AgentLoginSID IS NOT NULL)
	BEGIN
	    --we get the login name from SID. Ensures that we always get the login name with correct casing
	    --with respect to sql server collation.
	    DECLARE @AgentLoginSIDBinary varbinary(256)
	    DECLARE @AgentLoginName nvarchar(256)
	    
	    SELECT @AgentLoginSIDBinary = sid_binary(@AgentLoginSID);
	    SELECT @AgentLoginName = suser_sname(@AgentLoginSIDBinary);
	    
	    IF NOT EXISTS (SELECT * FROM sys.server_principals WHERE name = @AgentLoginName)
		BEGIN
			-- Create a new login. Standalone install or S/K upgrade scenario
            DECLARE @cmd1 nvarchar(max)
            SELECT @cmd1 = 'CREATE LOGIN ' + QUOTENAME(@AgentLoginName) + ' FROM WINDOWS'
            print 'Running command to create login: ' + @cmd1
            EXEC (@cmd1)
            EXEC sys.sp_addsrvrolemember @AgentLoginName, N'sysadmin'
		END
	END
	
	IF (@AGTGroupSID IS NOT NULL)
	BEGIN
		--this is the case on upgrade. Basically, if a login already exists representing the AGTGroup,
		--if its current name on windows is different from what we have on SQL, we alter the name. Needed in Y->K upgrade,
		--in which we rename the agent local group
		DECLARE @AGTGroupSIDBinary varbinary(256) -- binary representation of AGTGroupSID
		DECLARE @AGTGroupName nvarchar (256) -- name of the group
		DECLARE @existing_name as sysname
		
		SELECT @AGTGroupSIDBinary = sid_binary(@AGTGroupSID);
		SELECT @AGTGroupName = suser_sname(@AGTGroupSIDBinary);
		SELECT @existing_name = name FROM sys.server_principals WHERE sid = suser_sid(@AGTGroupName);
		
		--note that if the login does not exist, we don't add it.
		IF (@existing_name IS NOT NULL)
		BEGIN
			IF (QUOTENAME(@existing_name) <> QUOTENAME(@AGTGroupName))
			BEGIN
				-- Drop this login. Not used anymore (only using SID).
				DECLARE @newcmd nvarchar(max)
				SELECT @newcmd = 'DROP LOGIN ' + QUOTENAME(@existing_name)
				print 'Running command to drop login: ' + @newcmd
				EXEC (@newcmd)
			END
		END	
	END
END
