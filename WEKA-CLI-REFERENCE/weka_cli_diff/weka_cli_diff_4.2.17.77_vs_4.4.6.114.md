| Command | 4.2.17.77 | 4.4.6.114 |
|---------|------------|------------|
| `weka access-group` | ❌ Missing | Commands that manage the cluster access-groups |
| `weka access-group disable` | ❌ Missing | Disable access-groups |
| `weka access-group enable` | ❌ Missing | Enable access-groups |
| `weka access-group status` | ❌ Missing | Show the status of the access-groups |
| `weka agent supported-specs` | List the Weka spec versions that are supported by this agent version | ❌ Missing |
| `weka alerts mute` | Mute an alert-type. Muted alerts will not be prompted when listing active alerts. Alerts cannot be | Mute an alert-type. Muted alerts will not appear in the list of active alerts. It is required to specify |
| `weka cluster add` | ❌ Missing | Form a Weka cluster from hosts that just had Weka installed on them |
| `weka cluster container deactivation-check` | ❌ Missing | Check if the provided containers can be deactivated |
| `weka cluster container factory-reset` | Factory resets the containers. NOTE! This can't be undone! | ❌ Missing |
| `weka cluster container join-secret` | ❌ Missing | Set secret this container will use when joining or validating other backends |
| `weka cluster container requested-action` | ❌ Missing | Set the requested action of the supplied containers to one of: STOP, RESTART, APPLY_RESOURCES |
| `weka cluster create` | Form a Weka cluster from hosts that just has Weka installed on them | ❌ Missing |
| `weka cluster license payg` | Enable pay-as-you-go for the cluster | ❌ Missing |
| `weka cluster task bucket` | ❌ Missing | List the status of a background task on specific buckets |
| `weka cluster task throttle` | ❌ Missing | Slow down the rate of progress of a currently running background task |
| `weka dataservice` | ❌ Missing | Commands that manage dataservice |
| `weka dataservice global-config` | ❌ Missing | Dataservice Global Configuration |
| `weka dataservice global-config set` | ❌ Missing | Set Dataservice global configuration options |
| `weka dataservice global-config show` | ❌ Missing | Show the Dataservice global configuration |
| `weka debug blacklist` | Commands used to control blacklisting of weka nodes, causing them to be rejected from the cluster | ❌ Missing |
| `weka debug blacklist add` | Blacklist the processes and containers specified so they will become fenced and no longer be allowed to | ❌ Missing |
| `weka debug blacklist list` | List the cluster blacklisted processes | ❌ Missing |
| `weka debug blacklist remove` | Unblacklist the nodes and hosts specified so they will now be allowed to rejoin the cluster | ❌ Missing |
| `weka debug callhome` | ❌ Missing | Enable/Disable call-home (use by dark sites) |
| `weka debug config assign` | Assign specific keys in config | ❌ Missing |
| `weka debug config attach` | ❌ Missing | Assign specific keys in config |
| `weka debug dataserv` | ❌ Missing | Commands used to debug the DataServ |
| `weka debug dataserv shards` | ❌ Missing | List the DataServ shards, logical units used to divide the DataServ workload in the cluster |
| `weka debug denylist` | ❌ Missing | Commands used to control blacklisting of weka nodes, causing them to be rejected from the cluster |
| `weka debug denylist add` | ❌ Missing | Blacklist the processes and containers specified so they will become fenced and no longer be allowed to |
| `weka debug denylist list` | ❌ Missing | List the cluster blacklisted processes |
| `weka debug denylist remove` | ❌ Missing | Unblacklist the nodes and hosts specified so they will now be allowed to rejoin the cluster |
| `weka debug drive info` | ❌ Missing | Retrieve drive information commands for debugging purposes. |
| `weka debug drive info error` | ❌ Missing | Retrieve the NVMe error log for specified drives. |
| `weka debug drive info ocp-smart` | ❌ Missing | Retrieve the OCP-SMART log page for specified drives. OCP-SMART (Open Compute Project - Self-Monitoring, |
| `weka debug drive info raw` | ❌ Missing | Retrieve NVMe raw log page for specified drives. |
| `weka debug drive info smart` | ❌ Missing | Retrieve the NVMe SMART log for specified drives. SMART (Self-Monitoring, Analysis, and Reporting |
| `weka debug net ofed-override` | Commands used to override the host's detected OFED version | ❌ Missing |
| `weka debug net ofed-override clear` | remove host OFED version is overrides if there are any | ❌ Missing |
| `weka debug net ofed-override set` | Specify a mapping of OFED versions to override the host installed one | ❌ Missing |
| `weka debug net ofed-override status` | List host OFED version overrides, if any exist | ❌ Missing |
| `weka debug node` | Commands used to debug nodes | ❌ Missing |
| `weka debug node restart` | Kill nodes gradually and wait for them to restart | ❌ Missing |
| `weka debug override update` | ❌ Missing | Update manual override |
| `weka debug performance` | ❌ Missing | Performance |
| `weka debug performance stats` | ❌ Missing | Provide server performance statistics to identify I/O issues and perform optimizations. |
| `weka debug process` | ❌ Missing | Commands used to debug nodes |
| `weka debug process restart` | ❌ Missing | Kill nodes gradually and wait for them to restart |
| `weka debug s3` | ❌ Missing | Commands that allow more information on S3 servers |
| `weka debug task` | ❌ Missing | Commands used to debug tasks |
| `weka debug task old-progress` | ❌ Missing | Show details on oldest progress report on a task |
| `weka debug task status` | ❌ Missing | List the status of tasks on specific buckets |
| `weka debug traces freeze events` | ❌ Missing | Commands used to setup events to freeze traces on |
| `weka debug traces freeze events add` | ❌ Missing | Add event to freeze traces on |
| `weka debug traces freeze events list` | ❌ Missing | List events to freeze traces on |
| `weka debug traces freeze events rearm` | ❌ Missing | Rearm event that has already triggered |
| `weka debug traces freeze events remove` | ❌ Missing | Remove event to not freeze traces on anymore |
| `weka debug traces remote-endpoint` | ❌ Missing | Remote traces debugging commands |
| `weka debug traces remote-endpoint disable` | ❌ Missing | Disable the remote-endpoint connectivity for traces |
| `weka debug traces remote-endpoint enable` | ❌ Missing | Enable the remote-endpoint connectivity for traces |
| `weka debug traces remote-endpoint status` | ❌ Missing | Query remote traces status |
| `weka debug upgrade accepted-versions refresh` | ❌ Missing | Refreshes the accepted upgrade versions to align with the functional backend versions |
| `weka debug upgrade accepted-versions reset` | Reset upgrade accepted versions | ❌ Missing |
| `weka debug upgrade minimal-backend-version` | ❌ Missing | Get minimal backend version |
| `weka debug viewer` | ❌ Missing | Run the traces viewer on a local container |
| `weka driver` | ❌ Missing | Manage Weka drivers |
| `weka driver build` | ❌ Missing | Compiles drivers for the machine where this command is executed. |
| `weka driver download` | ❌ Missing | Downloads drivers from a distribution server. |
| `weka driver export` | ❌ Missing | Exports drivers from this machine to an archive. |
| `weka driver import` | ❌ Missing | Imports drivers from a previously exported archive to this machine. |
| `weka driver install` | ❌ Missing | Installs drivers on the machine where this command is executed. |
| `weka driver kernel` | ❌ Missing | Shows the kernel signature of the system. This signature is used to identify the specific kernel. |
| `weka driver pack` | ❌ Missing | Creates driver package. |
| `weka driver ready` | ❌ Missing | Checks if kernel drivers are loaded and ready for Weka. |
| `weka driver sign` | ❌ Missing | Signs drivers with a private key. |
| `weka fs add` | ❌ Missing | Create a filesystem |
| `weka fs create` | Create a filesystem | ❌ Missing |
| `weka fs delete` | Delete a filesystem | ❌ Missing |
| `weka fs group add` | ❌ Missing | Create a filesystem group |
| `weka fs group create` | Create a filesystem group | ❌ Missing |
| `weka fs group delete` | Delete a filesystem group | ❌ Missing |
| `weka fs group remove` | ❌ Missing | Delete a filesystem group |
| `weka fs kms-rewrap` | ❌ Missing | Rewrap the key of Filesystem |
| `weka fs protection` | ❌ Missing | Commands used to manage file system protection |
| `weka fs protection snapshot-policy` | ❌ Missing | Snapshot policy management commands |
| `weka fs protection snapshot-policy add` | ❌ Missing | Create a new snapshot policy |
| `weka fs protection snapshot-policy attach` | ❌ Missing | Attach existing filesystems to snapshot policy |
| `weka fs protection snapshot-policy detach` | ❌ Missing | Detach existing filesystems from the snapshot policy |
| `weka fs protection snapshot-policy duplicate` | ❌ Missing | Duplicates an existing snapshot policy, creating a new one. |
| `weka fs protection snapshot-policy export` | ❌ Missing | Export snapshot policy configuration, use policy sys-default to export the cluster default configuration |
| `weka fs protection snapshot-policy list` | ❌ Missing | List snapshot policies |
| `weka fs protection snapshot-policy remove` | ❌ Missing | Delete a snapshot policy |
| `weka fs protection snapshot-policy run-once` | ❌ Missing | Runs the snapshot policy schedule once immediately. |
| `weka fs protection snapshot-policy show` | ❌ Missing | Show snapshot policy configuration |
| `weka fs protection snapshot-policy update` | ❌ Missing | Update a snapshot policy |
| `weka fs quota reset` | ❌ Missing | Unsets a directory quota in a filesystem |
| `weka fs quota unset` | Unsets a directory quota in a filesystem | ❌ Missing |
| `weka fs remove` | ❌ Missing | Delete a filesystem |
| `weka fs reserve reset` | ❌ Missing | Unset an organization's thin provisioning SSD's reserve |
| `weka fs reserve unset` | Unset an organization's thin provisioning SSD's reserve | ❌ Missing |
| `weka fs security` | ❌ Missing | Manage filesystem security |
| `weka fs security policy` | ❌ Missing | Manages filesystem security policies. |
| `weka fs security policy attach` | ❌ Missing | Attaches new security policies to a filesystem, adding them to the existing policies. |
| `weka fs security policy detach` | ❌ Missing | Removes security policies from a filesystem. |
| `weka fs security policy list` | ❌ Missing | Lists filesystem security policies. |
| `weka fs security policy reset` | ❌ Missing | Removes all security policies from a filesystem. |
| `weka fs security policy set` | ❌ Missing | Sets security policies for a filesystem, replacing the existing list of policies. |
| `weka fs snapshot add` | ❌ Missing | Create a snapshot |
| `weka fs snapshot create` | Create a snapshot | ❌ Missing |
| `weka fs snapshot delete` | Delete a snapshot | ❌ Missing |
| `weka fs snapshot remove` | ❌ Missing | Delete a snapshot |
| `weka fs tier s3 delete` | Delete an existing S3 object store connection | ❌ Missing |
| `weka fs tier s3 remove` | ❌ Missing | Delete an existing S3 object store connection |
| `weka interface-group delete` | Delete an interface group | ❌ Missing |
| `weka interface-group ip-range delete` | Delete an ip range from an interface group | ❌ Missing |
| `weka interface-group ip-range remove` | ❌ Missing | Delete an ip range from an interface group |
| `weka interface-group port delete` | Delete a server port from an interface group | ❌ Missing |
| `weka interface-group port remove` | ❌ Missing | Delete a server port from an interface group |
| `weka interface-group remove` | ❌ Missing | Delete an interface group |
| `weka local resources auto-remove-timeout` | ❌ Missing | Configure the auto-remove-timeout (in seconds) to remove inactive client containers. |
| `weka local resources dedicate` | Set the host as dedicated to weka. For example it can be rebooted whenever needed, and configured | Set the host as dedicated to weka. For example it can be rebooted whenever needed, and |
| `weka local resources fqdn` | ❌ Missing | Configure the fqdn to be used by other containers for TLS hostname verification when |
| `weka local resources join-ips` | Set the IPs and ports of all hosts in the cluster. This will enable the host to join the cluster | Set the IPs and ports of all hosts in the cluster. This will enable the host to join the |
| `weka local resources join-secret` | ❌ Missing | Configure the secret used when joining a cluster as a backend |
| `weka local setup client` | ❌ Missing | Setup a local weka client container |
| `weka local setup envoy` | ❌ Missing | Setup a local envoy container |
| `weka local setup services` | ❌ Missing | Setup a local services container |
| `weka local setup taskmon` | ❌ Missing | Setup a local taskmon container |
| `weka nfs client-group delete` | Delete an NFS client group | ❌ Missing |
| `weka nfs client-group remove` | ❌ Missing | Delete an NFS client group |
| `weka nfs interface-group delete` | Delete an interface group | ❌ Missing |
| `weka nfs interface-group ip-range delete` | Delete an ip range from an interface group | ❌ Missing |
| `weka nfs interface-group ip-range remove` | ❌ Missing | Delete an ip range from an interface group |
| `weka nfs interface-group port delete` | Delete a server port from an interface group | ❌ Missing |
| `weka nfs interface-group port remove` | ❌ Missing | Delete a server port from an interface group |
| `weka nfs interface-group remove` | ❌ Missing | Delete an interface group |
| `weka nfs kerberos` | ❌ Missing | NFS Kerberos Commands |
| `weka nfs kerberos registration` | ❌ Missing | NFS Kerberos service registration |
| `weka nfs kerberos registration setup-ad` | ❌ Missing | Register NFS Kerberos service with Microsoft Active Directory. Running this command with the `restart` |
| `weka nfs kerberos registration setup-mit` | ❌ Missing | Register NFS Kerberos service with MIT KDC. Running this command with the `restart` option can disrupt |
| `weka nfs kerberos registration show` | ❌ Missing | Show NFS Kerberos service registration information |
| `weka nfs kerberos reset` | ❌ Missing | Wipe out NFS Kerberos Service configuration information. Running this command without the |
| `weka nfs kerberos service` | ❌ Missing | NFS Kerberos service |
| `weka nfs kerberos service setup` | ❌ Missing | Setup the NFS Kerberos Service information. Running this command with the `restart` option can disrupt IO |
| `weka nfs kerberos service show` | ❌ Missing | Show NFS Kerberos service setup information |
| `weka nfs ldap` | ❌ Missing | NFS LDAP Commands |
| `weka nfs ldap export-openldap` | ❌ Missing | Export in use configuration information for NFS to use OpenLDAP. |
| `weka nfs ldap import-openldap` | ❌ Missing | Import configuration information for NFS to use OpenLDAP. Running this command without the |
| `weka nfs ldap reset` | ❌ Missing | Wipe out NFS LDAP configuration information, This action may disrupt IO service for connected NFS |
| `weka nfs ldap setup-ad` | ❌ Missing | Setup configuration information for NFS to use Active Directory LDAP. Running this command without |
| `weka nfs ldap setup-ad-nokrb` | ❌ Missing | Setup configuration information for NFS to use Active Directory LDAP for ACL only when kerberos is |
| `weka nfs ldap setup-openldap` | ❌ Missing | Setup configuration information for NFS to use OpenLDAP. Running this command without the |
| `weka nfs ldap show` | ❌ Missing | Show NFS LDAP setup information |
| `weka nfs permission delete` | Delete a file system permission | ❌ Missing |
| `weka nfs permission remove` | ❌ Missing | Delete a file system permission |
| `weka nfs rules delete` | Commands for deleting NFS-rules | ❌ Missing |
| `weka nfs rules delete dns` | Delete a DNS rule from an NFS client group | ❌ Missing |
| `weka nfs rules delete ip` | Delete an IP rule from an NFS client group | ❌ Missing |
| `weka nfs rules remove` | ❌ Missing | Commands for deleting NFS-rules |
| `weka nfs rules remove dns` | ❌ Missing | Delete a DNS rule from an NFS client group |
| `weka nfs rules remove ip` | ❌ Missing | Delete an IP rule from an NFS client group |
| `weka org add` | ❌ Missing | Create a new organization in the Weka cluster |
| `weka org create` | Create a new organization in the Weka cluster | ❌ Missing |
| `weka org delete` | Delete an organization | ❌ Missing |
| `weka org remove` | ❌ Missing | Delete an organization |
| `weka org security` | ❌ Missing | Manages organization security |
| `weka org security policy` | ❌ Missing | Manages organization security policies. |
| `weka org security policy attach` | ❌ Missing | Attaches new security policies to an organization, adding them to the existing policies. |
| `weka org security policy detach` | ❌ Missing | Removes security policies from an organization. |
| `weka org security policy list` | ❌ Missing | List organization security policies. |
| `weka org security policy reset` | ❌ Missing | Removes all security policies from an organization. |
| `weka org security policy set` | ❌ Missing | Sets security policies for an organization, replacing the existing list of policies. |
| `weka org security revoke-tokens` | ❌ Missing | Revokes all API tokens issued for this organization. |
| `weka s3 bucket add` | ❌ Missing | Create an S3 bucket |
| `weka s3 bucket create` | Create an S3 bucket | ❌ Missing |
| `weka s3 bucket destroy` | Destroy an S3 bucket | ❌ Missing |
| `weka s3 bucket policy reset` | ❌ Missing | Unset the configured S3 policy for bucket |
| `weka s3 bucket policy unset` | Unset the configured S3 policy for bucket | ❌ Missing |
| `weka s3 bucket quota reset` | ❌ Missing | Remove the hard limit on bucket's disk usage |
| `weka s3 bucket quota unset` | Remove the hard limit on bucket's disk usage | ❌ Missing |
| `weka s3 bucket remove` | ❌ Missing | Destroy an S3 bucket |
| `weka s3 cluster add` | ❌ Missing | Create an S3 cluster managed by weka |
| `weka s3 cluster container` | ❌ Missing | Commands that manage Weka's S3 cluster's containers |
| `weka s3 cluster container add` | ❌ Missing | Add S3 containers to S3 cluster |
| `weka s3 cluster container list` | ❌ Missing | Lists containers in S3 cluster |
| `weka s3 cluster container remove` | ❌ Missing | Remove S3 containers from S3 cluster |
| `weka s3 cluster containers` | Commands that manage Weka's S3 cluster's containers | ❌ Missing |
| `weka s3 cluster containers add` | Add S3 containers to S3 cluster | ❌ Missing |
| `weka s3 cluster containers list` | Lists containers in S3 cluster | ❌ Missing |
| `weka s3 cluster containers remove` | Remove S3 containers from S3 cluster | ❌ Missing |
| `weka s3 cluster create` | Create an S3 cluster managed by weka | ❌ Missing |
| `weka s3 cluster destroy` | Destroy the S3 cluster managed by weka. This will not delete the data, just stop exposing it via S3 | ❌ Missing |
| `weka s3 cluster remove` | ❌ Missing | Destroy the S3 cluster managed by weka. This will not delete the data, just stop exposing it via S3 |
| `weka security ca-cert reset` | ❌ Missing | Unsets custom CA signed certificate from cluster |
| `weka security ca-cert unset` | Unsets custom CA signed certificate from cluster | ❌ Missing |
| `weka security cors-trusted-sites` | ❌ Missing | Commands for handling Cross Origin Resource Sharing weka apis |
| `weka security cors-trusted-sites add` | ❌ Missing | Add a trusted site to list, provide url with http or https prefix and port number if not a standard |
| `weka security cors-trusted-sites list` | ❌ Missing | Lists the set of trusted sites where CORS in configured |
| `weka security cors-trusted-sites remove` | ❌ Missing | Remove the specified site from the trusted list. |
| `weka security cors-trusted-sites remove-all` | ❌ Missing | Removes all trusted sites for Cross Origin Resource Sharing |
| `weka security kms reset` | ❌ Missing | Remove external KMS configurations. This will fail if there are any encrypted filesystems that rely on the |
| `weka security kms unset` | Remove external KMS configurations. This will fail if there are any encrypted filesystems that rely on the | ❌ Missing |
| `weka security policy` | ❌ Missing | Manages security policies. |
| `weka security policy add` | ❌ Missing | Creates a new security policy. |
| `weka security policy duplicate` | ❌ Missing | Duplicates an existing security policy, creating a new one. |
| `weka security policy join` | ❌ Missing | Manages security policies related to cluster joining. |
| `weka security policy join attach` | ❌ Missing | Adds new security policies applied when joining cluster, adding them to the existing policies. |
| `weka security policy join detach` | ❌ Missing | Removes security policies applied when joining cluster. |
| `weka security policy join list` | ❌ Missing | Lists security policies applied when joining containers. |
| `weka security policy join reset` | ❌ Missing | Removes all security policies applied when joining cluster. |
| `weka security policy join set` | ❌ Missing | Sets security policies for joining cluster, replacing the existing set of policies. |
| `weka security policy list` | ❌ Missing | List security policies defined in the Weka cluster. |
| `weka security policy remove` | ❌ Missing | Deletes a security policy. |
| `weka security policy show` | ❌ Missing | Displays information about a specific security policy. |
| `weka security policy test` | ❌ Missing | Simulates the effect of one or more security policies. |
| `weka security policy update` | ❌ Missing | Updates the settings of an existing security policy. |
| `weka security tls local` | ❌ Missing | TLS local configuration commands |
| `weka security tls local reset` | ❌ Missing | Removes the local TLS configuration. |
| `weka security tls local set` | ❌ Missing | Make HTTP server use local TLS configuration. If local TLS already configured, updates the configuration. |
| `weka security tls reset` | ❌ Missing | Make Ngnix not use TLS when accessing UI |
| `weka security tls unset` | Make Ngnix not use TLS when accessing UI | ❌ Missing |
| `weka security token-expiry` | ❌ Missing | Commands used to interact with the auth token expiration parameters |
| `weka security token-expiry set` | ❌ Missing | Configure the times for which auth tokens will be valid |
| `weka security token-expiry show` | ❌ Missing | Show the current expiration limits for auth tokens |
| `weka smb cluster add` | ❌ Missing | Create a SMB cluster managed by weka |
| `weka smb cluster container` | ❌ Missing | Update an SMB cluster containers |
| `weka smb cluster container add` | ❌ Missing | Update an SMB cluster |
| `weka smb cluster container remove` | ❌ Missing | Update an SMB cluster |
| `weka smb cluster containers` | Update an SMB cluster containers | ❌ Missing |
| `weka smb cluster containers add` | Update an SMB cluster | ❌ Missing |
| `weka smb cluster containers remove` | Update an SMB cluster | ❌ Missing |
| `weka smb cluster create` | Create a SMB cluster managed by weka | ❌ Missing |
| `weka smb cluster destroy` | Destroy the SMB cluster managed by weka. This will not delete the data, just stop exposing it via | ❌ Missing |
| `weka smb cluster host-access` | Show host access help | ❌ Missing |
| `weka smb cluster host-access add` | Add hosts to host access lists | ❌ Missing |
| `weka smb cluster host-access list` | Show host access list | ❌ Missing |
| `weka smb cluster host-access remove` | Remove hosts from a user list | ❌ Missing |
| `weka smb cluster host-access reset` | Reset host access lists | ❌ Missing |
| `weka smb cluster remove` | ❌ Missing | Destroy the SMB cluster managed by weka. This will not delete the data, just stop exposing it via |
| `weka smb share host-access add` | Add hosts to host access lists | Add hosts IPs to host access list |
| `weka smb share host-access remove` | Remove hosts from a user list | Remove hosts IPs from a user list |
| `weka smb share list` | ❌ Missing | Show lists help |
| `weka smb share list add` | ❌ Missing | Add users to a user list |
| `weka smb share list remove` | ❌ Missing | Remove users from a user list |
| `weka smb share list reset` | ❌ Missing | Reset a user list |
| `weka smb share list show` | ❌ Missing | Show user lists |
| `weka smb share lists` | Show lists help | ❌ Missing |
| `weka smb share lists add` | Add users to a user list | ❌ Missing |
| `weka smb share lists remove` | Remove users from a user list | ❌ Missing |
| `weka smb share lists reset` | Reset a user list | ❌ Missing |
| `weka smb share lists show` | Show user lists | ❌ Missing |
| `weka upgrade pause` | ❌ Missing | Pause the upgrade process |
| `weka upgrade resume` | ❌ Missing | Resume the upgrade process |
| `weka user delete` | Delete user from the Weka cluster | ❌ Missing |
| `weka user remove` | ❌ Missing | Delete user from the Weka cluster |
| `weka version reset` | ❌ Missing | Unset the current version. Containers must be stopped before setting the current version and the new |
| `weka version set` | Set the current version. Containers must be stopped before setting the current version and the new | Set the current version. Containers must be stopped before setting the current version and the new version |
| `weka version supported-specs` | List the Weka spec versions that are supported by this agent version | ❌ Missing |
| `weka version unset` | Unset the current version. Containers must be stopped before setting the current version and the | ❌ Missing |
