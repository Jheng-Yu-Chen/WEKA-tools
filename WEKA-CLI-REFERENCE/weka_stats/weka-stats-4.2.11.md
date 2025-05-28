Category|Category Label|Identifier|Description|Label|Type|Unit|Parameters|Related Rate Parameter|Permission|For Node Type|Can Accumulate|Histogram|Histogram Unit
------------------|---------------------|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-------------|-------------------------|-----------------------------|--------------------------------------------------------------------------------|------------|---------------|----------------|-----------|-----------------
_test_stats_|_|TEST_STAT_ABSOLUTE|Absolute stat used in the tests|Test Stat Absolute (total)|Absolute|Undefined|||WEKA|ANY|True|False|
_test_stats_|_|TEST_STAT_MOMENTARY|Momentary stat used in the tests|Test Stat Momentary (total)|Accumulated|Undefined|||WEKA|ANY|False|False|
attr_cache|Attribute Cache|GP_GETATTR_CACHE_MISS|Number of general purpose getAttr cache misses per second|Cache misses for general purpose getAttr ops (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
attr_cache|Attribute Cache|GP_GETATTR|Number of general purpose getAttr calls per second|General purpose getAttr ops (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
block_cache|Block Cache|BUCKET_CACHED_METADATA_BLOCKS|Bucket number of cached metadata blocks|Bucket Cached Metadata Blocks (total)|Absolute|Blocks|||WEKA|IO|True|False|
block_cache|Block Cache|BUCKET_REGISTRY_L2_BLOCKS_NUM|Bucket number of registry L2 blocks|Bucket L2 Registry Blocks Number (total)|Absolute|Blocks|||WEKA|IO|True|False|
block_cache|Block Cache|BUCKET_CACHE_REGISTRY_L2_HITS|Bucket block cache registry L2 hits|Block Cache Registry L2 Hits (total)|Absolute|Queries|||WEKA|IO|True|False|
block_cache|Block Cache|BUCKET_CACHE_REGISTRY_L2_MISSES|Bucket block cache registry L2 misses|Block Cache Registry L2 Misses (total)|Absolute|Queries|||WEKA|IO|True|False|
block_cache|Block Cache|BUCKET_CACHE_METADATA_MISSES|Bucket block cache metadata misses|Block Cache Metadata Misses (total)|Absolute|Queries|||WEKA|IO|True|False|
block_cache|Block Cache|BUCKET_CACHE_METADATA_HITS|Bucket block cache metadata hits|Block Cache Metadata Hits (total)|Absolute|Queries|||WEKA|IO|True|False|
block_cache|Block Cache|BUCKET_CACHED_REGISTRY_L2_BLOCKS|Bucket number of cached registry L2 blocks|Bucket Cached Registry L2 Blocks (total)|Absolute|Blocks|||WEKA|IO|True|False|
block_writes|Block Writes|BLOCK_FULL_WRITES|Number of full block writes|Block Full Writes (total)|Absolute|Writes|||WEKA|IO|True|False|
block_writes|Block Writes|BLOCK_PARTIAL_WRITES|Number of partial block writes|Block Partial Writes (total)|Absolute|Writes|||WEKA|IO|True|False|
bucket|Bucket|SNAPSHOT_CREATION_TIME|Time to complete a snapshot creation|Snapshot Creation Duration (total)|Histogram|Snapshots|||WEKA|IO|True|True|Milliseconds
bucket|Bucket|CHOKING_LEVEL_ALL|Throttling level applied on all types of IOs|Choking Level All (average)|Accumulated|%|||WEKA|IO|False|False|
bucket|Bucket|READ_LATENCY|Average latency of READ operations|Read Latency (per read)|Measured|Microseconds||READS|WEKA|IO|False|False|
bucket|Bucket|HASH_BLOCKS_COUNT|Difference in number of HASH blocks|HASH Blocks Count (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
bucket|Bucket|SINGLE_HOP_RDMA_MISMATCH_DPDK_FALLBACK|1HOP prefix mismatch RDMA fail|1HOP prefix mismatch RDMA fail (total)|Accumulated|Issues|||WEKA|IO|False|False|
bucket|Bucket|WRITE_LATENCY|Average latency of WRITE operations|Write Latency (per write)|Measured|Microseconds||WRITES|WEKA|IO|False|False|
bucket|Bucket|REGISTRY_L1_BLOCKS_COUNT|Difference in number of REGISTRY_L1 blocks|REGISTRY_L1 Blocks Count (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
bucket|Bucket|COALESCED_MAY_CREATE_EXTENT|Number of mayCreateExtent calls coalesced|mayCreateExtent Coalesced (total)|Absolute|Calls|||WEKA|IO|True|False|
bucket|Bucket|INODE_BLOCKS_COUNT|Difference in number of INODE blocks|INODE Blocks Count (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
bucket|Bucket|FREEABLE_LRU_BUFFERS|Number of unused blocks in LRU cache|Freeable LRU Buffers (total)|Accumulated|Buffers|||WEKA|IO|False|False|
bucket|Bucket|REGISTRY_L2_BLOCKS_COUNT|Difference in number of REGISTRY_L2 blocks|REGISTRY_L2 Blocks Count (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
bucket|Bucket|TEMPORAL_SQUELCH_BLOCKS_COUNT|Difference in number of TEMPORAL_SQUELCH blocks|TEMPORAL_SQUELCH Blocks Count (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
bucket|Bucket|EXTENT_BLOCKS_COUNT|Difference in number of EXTENT blocks|EXTENT Blocks Count (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
bucket|Bucket|SPATIAL_SQUELCH_BLOCKS_COUNT|Difference in number of SPATIAL_SQUELCH blocks|SPATIAL_SQUELCH Blocks Count (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
bucket|Bucket|ODL_BLOCKS_COUNT|Difference in number of ODL blocks|ODL Blocks Count (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
bucket|Bucket|EXTENT_BLOCK_SEQUENCES|Histogram of number of consecutive sequences of blocks in a single extent|Data Blocks Sequences in Extents (total)|Histogram|Extents|||WEKA|IO|True|True|Sequences
bucket|Bucket|TRANSIENT_INTEGRITY_ISSUES|Number of transient filesystem integrity issues detected|Transient Integrity Issues (total)|Absolute|Issues|||WEKA|IO|True|False|
bucket|Bucket|DIR_MOVE_TIME|Time to complete a directory move|Directory Move Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
bucket|Bucket|WRITES|Number of write operations per second|Writes (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
bucket|Bucket|SUPERBLOCK_BLOCKS_COUNT|Difference in number of SUPERBLOCK blocks|SUPERBLOCK Blocks Count (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
bucket|Bucket|BUCKET_START_TIME|Duration of bucket activation on step up|Bucket Activation Duration (total)|Histogram|Startups|||WEKA|IO|True|True|Seconds
bucket|Bucket|USER_DATA_BUFFERS_IN_USE|Number of data buffers used for serving ongoing IOs|User Data Buffers In Use (total)|Accumulated|Buffers|||WEKA|IO|False|False|
bucket|Bucket|DESTAGE_COUNT|Number of destages per second|Destage Count (total)|Rate|Destages/Sec|||WEKA|IO|True|False|
bucket|Bucket|READ_BYTES|Number of bytes read per second|Read Bytes (total)|Rate|Bytes/Sec|||WEKA|IO|True|False|
bucket|Bucket|JOURNAL_BLOCKS_COUNT|Difference in number of JOURNAL blocks|JOURNAL Blocks Count (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
bucket|Bucket|FAIRNESS_DELAYED_MAY_CREATE_EXTENT|Number of mayCreateExtent calls not coalesced to prevent starvation|mayCreateExtent Coalesce Fairness Delays (total)|Absolute|Calls|||WEKA|IO|True|False|
bucket|Bucket|RESIDENT_BLOCKS_COUNT|Number of blocks in resident blocks table|Resident Blocks Count (total)|Accumulated|Blocks|||WEKA|IO|False|False|
bucket|Bucket|WRITE_BYTES|Number of byte writes per second|Write Bytes (total)|Rate|Bytes/Sec|||WEKA|IO|True|False|
bucket|Bucket|REGISTRY_SEARCHES_COUNT|Number of registry searches per second|Registry Searches Count (total)|Rate|Queries/Sec|||WEKA|IO|True|False|
bucket|Bucket|SUCCESSFUL_DATA_WEDGINGS|Number of successful attempts to wedge data blocks in journal per second|Successful Data Wedging Attempts (total)|Rate|Attempts/Sec|||WEKA|IO|True|False|
bucket|Bucket|SINGLE_HOP_MISMATCH_RECOVERY|1HOP prefix mismatch recoveries|1HOP prefix mismatch recoveries (total)|Accumulated|Issues|||WEKA|IO|False|False|
bucket|Bucket|UNSUCCESSFUL_DATA_WEDGINGS|Number of unsuccessful attempts to wedge data blocks in journal per second|Unsuccessful Data Wedging Attempts (total)|Rate|Attempts/Sec|||WEKA|IO|True|False|
bucket|Bucket|INTEGRITY_ISSUES|Number of filesystem integrity issues detected|Integrity Issues (total)|Absolute|Issues|||WEKA|IO|True|False|
bucket|Bucket|ODL_PAYLOAD_BLOCKS_COUNT|Difference in number of ODL_PAYLOAD blocks|ODL_PAYLOAD Blocks Count (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
bucket|Bucket|DESTAGED_BLOCKS_COUNT|Number of destaged blocks per second|Destaged Blocks Count (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
bucket|Bucket|READS|Number of read operations per second|Reads (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
bucket|Bucket|CHOKING_LEVEL_NON_MUTATING|Throttling level applied on non-mutating only types of IOs|Choking Level Non-Mutating (average)|Accumulated|%|||WEKA|IO|False|False|
bucket_failovers|Bucket Failovers|REMOTE_BUCKET_IS_SECONDARY|Number of times a remote bucket reported it is secondary and cannot serve us|Remote Bucket is Secondary (total)|Absolute|Exceptions|||WEKA|IO|True|False|
bucket_failovers|Bucket Failovers|BUCKET_FAILOVERS|Number of failovers detected in remote buckets|Bucket Failovers (total)|Absolute|Failovers|||WEKA|IO|True|False|
bucket_rebalances|Bucket Rebalances|BUCKET_INIT_LATENCY_HIST|Duration of bucket initialization|Bucket Initialization Latency (total)|Histogram|Initializations|||WEKA|IO|True|True|Milliseconds
bucket_rebalances|Bucket Rebalances|BUCKET_INITS|Number of bucket initializations|Initializations (total)|Absolute|Times|||WEKA|IO|True|False|
bucket_rebalances|Bucket Rebalances|LEGACY_DENY_BUCKET_ACCESS|Number of old-style NotBucketLeader exceptions|Legacy NotBucketLeader (total)|Absolute|Exceptions|||WEKA|IO|True|False|
bucket_rebalances|Bucket Rebalances|BUCKET_INIT_LATENCY|Average latency of bucket initialization|Initialization Latency (per init)|Measured|Seconds||BUCKET_INITS|WEKA|IO|False|False|
bucket_rebalances|Bucket Rebalances|INFORMATIVE_DENY_BUCKET_ACCESS|Number of new-style NotBucketLeaderEx exceptions|New-style NotBucketLeaderEx (total)|Absolute|Exceptions|||WEKA|IO|True|False|
choking|Choking|CHOKING_LEVEL_ALL|Throttling level applied on all types of IOs, both mutating and non-mutating|Choking Level All (total)|Histogram|Processes|||WEKA|IO|True|True|Level
choking|Choking|CHOKING_LEVEL_NON_MUTATING|Throttling level applied on non-mutating only types of IOs|Choking Level Non-Mutating (total)|Histogram|Processes|||WEKA|IO|True|True|Level
clients|Clients|CLIENTS_RECONNECTED|The number of clients reconnected instead of their previous connection instance|Clients reconnected (total)|Rate|Clients/Sec|||WEKA|MANAGEMENT|True|False|
clients|Clients|CLIENTS_CONNECTED|Clients connected|Clients connected (total)|Rate|Clients/Sec|||WEKA|MANAGEMENT|True|False|
clients|Clients|CLIENTS_LEFT|The number of clients left|Clients left (total)|Rate|Clients/Sec|||WEKA|MANAGEMENT|True|False|
clients|Clients|CLIENTS_DISCONNECTED|The number of clients left or removed|Clients disconnected (total)|Rate|Clients/Sec|||WEKA|MANAGEMENT|True|False|
clients|Clients|CLIENTS_REMOVED|The number of clients removed|Clients removed (total)|Rate|Clients/Sec|||WEKA|MANAGEMENT|True|False|
cluster|Processes|ABRUPT_EXITS|How many abrupt exits of a process (node) occured|Abrupt process exits detected (total)|Accumulated|Abrupt process exits|||WEKA|ANY|False|False|
cluster|Processes|PEER_CONFIGURE_FAILURES|How many times the node failed to configure peers in order to sync with them|Peer configure failures detected (total)|Absolute|Peer configure failures|||WEKA|ANY|True|False|
config|Config|LEADER_HEARTBEAT_PROCESSING_TIME_OLD|The number of leader heartbeats per processing time range (OLD)|Leader heartbeat processing time (total)|Histogram|Number of heartbeats|||WEKA|MANAGEMENT|True|True|secs
config|Config|HEARTBEAT_PROCESSING_TIME|The number of non-leader heartbeats per processing time range|Non-leader heartbeat processing time (total)|Histogram|Number of heartbeats|||WEKA|MANAGEMENT|True|True|secs
config|Config|OVERLAY_INCREMENTAL_SHIFTS|The number of incremental overlay shifts|Incremental overlay shifts (total)|Absolute|Changes|||WEKA|MANAGEMENT|True|False|
config|Config|CLIENT_NODE_REJOIN_TIME|The number of client rejoin attempts per completion time range|Client node rejoin time (total)|Histogram|Number of rejoins|||WEKA|MANAGEMENT|True|True|mSecs
config|Config|OVERLAY_TRACKER_INCREMENTALS|The number of incremental OverlayTracker applications|Incremental OverlayTracker applications (total)|Absolute|Changes|||WEKA|MANAGEMENT|True|False|
config|Config|AVERAGE_CHANGES_IN_GENERATION|The average number of changes in generation|Average (total)|Rate|Changes/Sec|||WEKA|MANAGEMENT|True|False|
config|Config|HEARTBEAT_PROCESSING_TIME_OLD|The number of non-leader heartbeats per processing time range (OLD)|Non-leader heartbeat processing time (total)|Histogram|Number of heartbeats|||WEKA|MANAGEMENT|True|True|secs
config|Config|OVERLAY_FULL_SHIFTS|The number of full overlay shifts|Full overlay shifts (total)|Absolute|Changes|||WEKA|MANAGEMENT|True|False|
config|Config|GENERATION_COMMIT_LATENCY|The average latency of committing a configuration generation|Commit changeset latency (per changeset commits)|Measured|Microseconds||TOTAL_GENERATIONS_COMMITTED|WEKA|MANAGEMENT|False|False|
config|Config|CHANGESET_COMMIT_LATENCY|The average latency of committing a configuration changeset|Commit changeset latency (per changeset commits)|Measured|Microseconds||TOTAL_CHANGESETS_COMMITTED|WEKA|MANAGEMENT|False|False|
config|Config|TOTAL_COMMITTED_CHANGES|The total number of committed configuration changes|Changes (total)|Absolute|Changes|||WEKA|MANAGEMENT|True|False|
config|Config|AVERAGE_CHANGES_IN_CHANGESET|The average number of changes in a changeset|Average (total)|Rate|Changes/Sec|||WEKA|MANAGEMENT|True|False|
config|Config|TOTAL_GENERATIONS_COMMITTED|The number of committed generations per second|Config generation commits (total)|Absolute|Generations|||WEKA|MANAGEMENT|True|False|
config|Config|CONFIG_PROPAGATION_LATENCY|The latencies of propagation of a configuration generation|Config Propagation latency (total)|Histogram|Generation|||WEKA|MANAGEMENT|True|True|Milliseconds
config|Config|BACKEND_NODE_REJOIN_TIME|The number of backend rejoin attempts per completion time range|Backend node rejoin time (total)|Histogram|Number of rejoins|||WEKA|MANAGEMENT|True|True|mSecs
config|Config|OVERLAY_TRACKER_RESYNCS|The number of OverlayTracker full-resyncs|OverlayTracker resyncs (total)|Absolute|Changes|||WEKA|MANAGEMENT|True|False|
config|Config|LEADER_HEARTBEAT_PROCESSING_TIME|The number of leader heartbeats per processing time range|Leader heartbeat processing time (total)|Histogram|Number of heartbeats|||WEKA|MANAGEMENT|True|True|secs
config|Config|TOTAL_CHANGESETS_COMMITTED|The total number of committed changesets|Changeset commits (total)|Absolute|Change Sets|||WEKA|MANAGEMENT|True|False|
cpu|CPU|CPU_UTILIZATION|The percentage of the CPU time used for handling I/Os|CPU Utilization (average)|Custom|%|||USER|IO|False|False|
data_reduction|Data Reduction|GC_PROMOTIONS|Number of times data was rewritten to a next GC tree level|Gc Promotions (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|SEGMENT_PROMOTES|Promoted Compressed Blocks|Promoted Compressed Blocks (rate)|Custom|Blocks|||WEKA|IO|False|False|
data_reduction|Data Reduction|NEW_DELTAS|Number of new delta blocks created|New Deltas (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|DELTA_PROMOTES|Number of delta blocks promoted by GC|Delta Promotions (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|COMPRESS_TASK_TIME|Average time to complete compress task|Compress Task Time (per compress tasks)|Measured|Milliseconds||COMPRESS_TASK_CALLS|WEKA|IO|False|False|
data_reduction|Data Reduction|INGEST_START_CALLS|Ingest Start Calls|Ingest Start Calls (total)|Rate|Calls/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|DROPPED_SEGMENTS|Number of blocks dropped during clusterization|Dropped Segments (total)|Rate|Blocks/Sec|dataReductionPhase||WEKA|IO|True|False|
data_reduction|Data Reduction|DELTAS_COMPLETE_RELOCS|Number of delta blocks notified about a relocation of both delta and ref segments at the same time|Delta Complete Relocations (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|DELTA_RELOCS|Number of delta blocks relocated by GC|Delta Relocations (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|DELTA_REMOVAL_BACKPTR_COLLISIONS|Number of times delta blocks with the same backptr were encountered during deletions flush|Delta Removal Backptr Collisions (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|ACCEPTED_SEGMENTS|Number of blocks accepted for clusterization|Accepted Segments (total)|Rate|Blocks/Sec|dataReductionPhase||WEKA|IO|True|False|
data_reduction|Data Reduction|INGEST_START_TIME|Average time to start ingest|Ingest Start Time (per ingest starts)|Measured|Milliseconds||INGEST_START_CALLS|WEKA|IO|False|False|
data_reduction|Data Reduction|SINGLES_MARKED_AS_REFS|Number of single blocks marked as references due to new matches|Signles Marked As References (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|DELTA_BACKPTR_COLLISIONS|Number of times delta blocks with the same backptr were encountered during GC|Delta Backptr Collisions (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|COMPRESS_TASK_CALLS|Compress Task Calls|Compress Task Calls (total)|Rate|Calls/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|REFERENCE_PROMOTES|Number of reference blocks promoted by GC|Reference Promotions (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|AVG_DELTAS|Average deltas per reference during ingestion (excluding history)|Average Deltas/Refs (average)|Custom|deltas/ref|||WEKA|IO|False|False|
data_reduction|Data Reduction|CLUSTERIZE_CALLS|Clusterize Calls|Clusterize Calls (total)|Rate|Calls/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|HISTORY_MATCHES|Number of new delta blocks matched with references from history|History Matches (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|NEW_REFERENCES|Number of new reference blocks created|New References (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|DELTAS_REF_RELOCS|Number of delta blocks notified about reference relocations|Delta Ref Relocations (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|CLUSTERIZE_TIME|Average time to clusterize|Clusterize Time (per clusterizations)|Measured|Milliseconds||CLUSTERIZE_CALLS|WEKA|IO|False|False|
data_reduction|Data Reduction|DELTAS_GC|Number of delta blocks removed by GC|Delta  Deletions (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|NEW_SINGLES|Number of new reference blocks created|New Signles (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|REFERENCE_RELOCS|Number of reference blocks relocated by GC|Reference Relocations (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|REF_BACKPTR_COLLISIONS|Number of times blocks with the same reference-backptr were encountered during GC|Reference Backptr Collisions (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|SEGMENT_RELOCS|Relocated Compressed Blocks|Relocated Compressed Blocks (rate)|Custom|Blocks|||WEKA|IO|False|False|
data_reduction|Data Reduction|REFERENCE_GC|Number of reference blocks removed by GC|Reference Deletions (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
data_reduction|Data Reduction|NEW_INGESTED|Ingested Blocks|Ingested Blocks (rate)|Custom|Blocks|||WEKA|IO|False|False|
fe_encryption|Frontend Encryption|FE_FILENAMES_ENCRYPTED|Number of filenames encrypted in the frontend|Filenames encrypted (total)|Absolute|Filenames|||WEKA|IO|True|False|
fe_encryption|Frontend Encryption|FE_BLOCK_DECRYPT_DURATION|Duration of decryption of blocks in the frontend|Frontend Block Decrypt Duration (total)|Absolute|Microseconds|||WEKA|IO|True|False|
fe_encryption|Frontend Encryption|FE_BLOCKS_DECRYPTED|Number of blocks decrypted in the frontend|Blocks decryption in frontend (total)|Absolute|Blocks|||WEKA|IO|True|False|
fe_encryption|Frontend Encryption|FE_BLOCK_ENCRYPT_DURATION|Duration of encryption of blocks in the frontend|Frontend Block Encrypt Duration (total)|Absolute|Microseconds|||WEKA|IO|True|False|
fe_encryption|Frontend Encryption|FE_FILENAME_CRYPTO_LATENCY|Average latency of frontend filename crypto|Filename crypto latency (per filename_crypto)|Measured|Microseconds||FE_FILENAMES_ENCRYPTED + FE_FILENAMES_DECRYPTED|WEKA|IO|False|False|
fe_encryption|Frontend Encryption|FE_FILENAMES_DECRYPTED|Number of filenames decrypted in the frontend|Filenames decrypted (total)|Absolute|Filenames|||WEKA|IO|True|False|
fe_encryption|Frontend Encryption|FE_FILENAME_DECRYPT_DURATION|Duration of decryption of filenames in the frontend|Frontend Filename Decrypt Duration (total)|Absolute|Microseconds|||WEKA|IO|True|False|
fe_encryption|Frontend Encryption|FE_BLOCKS_ENCRYPTED|Number of blocks encrypted in the frontend|Blocks encrypted in frontend (total)|Absolute|Blocks|||WEKA|IO|True|False|
fe_encryption|Frontend Encryption|FE_FILENAME_ENCRYPT_DURATION|Duration of encryption of filenames in the frontend|Frontend Filename Encrypt Duration (total)|Absolute|Microseconds|||WEKA|IO|True|False|
fe_encryption|Frontend Encryption|FE_BLOCK_CRYPTO_LATENCY|Average latency of frontend block crypto|Block crypto latency (per block_crypto)|Measured|Microseconds||FE_BLOCKS_ENCRYPTED + FE_BLOCKS_DECRYPTED|WEKA|IO|False|False|
frontend|Frontend|FE_IDLE_TIME|The percentage of the CPU time not used for handling I/Os on the frontend|Frontend Idle Time (average)|Custom|%|||WEKA|FRONTEND|False|False|
frontend|Frontend|FE_IDLE_CYCLES|The number of idle cycles on the frontend|Frontend Idle Cycles (total)|Rate|Cycles/Sec|||WEKA|FRONTEND|True|False|
fs_obs|Filesystem OBS|UPLOADS|Number of upload attempts per second|Uploads (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_RECLAMATION_SCAVENGED_BLOBS|Number of blobs scavenged per second|Reclamation Scavenged Blobs (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_SHARED_DOWNLOADS_LATENCY|Average latency of shared downloads from object-store|Shared Download Latency (per objects)|Measured|Microseconds||OBS_SHARED_DOWNLOADS|WEKA|IO|False|False|
fs_obs|Filesystem OBS|OBS_INODES_RELEASE|Number of file released to object-store per second|Files Release (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_PROMOTE_EXTENT_WRITE|Number of extents promoted from object-store per second|Promoted Extents (total)|Rate|Extents/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_SCAVENGED_BLOB_WASTE_LEVEL|Waste level found in blobs|Scavenged Blob Waste Level (total)|Histogram|Blobs|||WEKA|IO|True|True|Waste Level
fs_obs|Filesystem OBS|DOWNLOADS|Number of downloads per second|Downloads (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|DEMOTE_EXTENT_OBS_FETCH_STOW|Number of extent STOW object-store fetch operations per second|Demote Extent Fetch for STOW (total)|Rate|Ops/Sec|uploadSource||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_RECLAMATION_SCAVENGED_BYTES|Number of bytes scavenged per second|Reclamation Scavenged Bytes (total)|Rate|Bytes/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_BLOB_SCAVENGE_LATENCY|Average latency of blob scavenges|Reclamation Scavenge Latency (per blob)|Measured|Microseconds||OBS_RECLAMATION_SCAVENGED_BLOBS|WEKA|IO|False|False|
fs_obs|Filesystem OBS|OBS_RECLAMATION_WAIT_FOR_DESTAGE|Average time waiting for destage on space reclamation|Reclamation Wait for Destage (total)|Absolute|Microseconds|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_POLICY_FREED|Number of bytes freed from disk due to policy per second|Policy Freed (total)|Rate|Bytes/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|STOW_SERIALIZED_EXTENT_REDIRECTS|Number of extent descriptors uploaded that redirect to previous snapshot|Uploaded Extent Redirect Descriptors (total)|Absolute|Extent Descriptors|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|STOW_SERIALIZED_EXTENT_DATA|Number of extent descriptors uploaded that contain data|Uploaded Extent Data Descriptors (total)|Absolute|Extent Descriptors|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_SHARED_DOWNLOADS|Number of shared downloads from object-store per second|Shared Downloads (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|UNEXPECTED_BLOCK_VERSION_POST_UPGRADE|Number of unexpected block version found after upgrade completed|Unexpected Block Version (total)|Absolute|Occurrences|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|DEMOTE_EXTENT_OBS_FETCH|Number of extent object-store fetch operations per second|Demote Extent Fetch (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_PROMOTE_WRITE|Number of bytes promoted from object-store per second|Promote Bytes (total)|Rate|Bytes/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|TIERED_FS_BREAKING_POLICY|Number of tiered filesystems breaking policy|Filesystems Backpressure Activations (total)|Absolute|Activations|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_RECLAMATION_PURGED_BYTES|Number of bytes purged per second|Reclamation Purged Bytes (total)|Rate|Bytes/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_INODES_PREFETCH|Number of files prefetched from object-store per second|Files Prefetch (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|TIMEOUT_DOWNLOADS|Number of timed out downloads per second|Timeout Download (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|UPLOAD_CHOKING_LATENCY|Average latency of waiting for upload choking budget|Upload Choking Latency (total)|Absolute|Microseconds|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_EXTENTS_PREFETCH|Number of extents prefetched from object-store per second|Extents Prefetch (total)|Rate|Extents/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_BACKPRESSURE_FREED|Number of bytes freed from disk due to backpressure per second|Backpressure Freed (total)|Rate|Bytes/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_READ|Number of reads that needed data from the object-store per second|Object-Store Dependent Reads (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|DOWNLOAD_LATENCY|Average latency of downloads|Download Latency (per download)|Measured|Microseconds||DOWNLOADS|WEKA|IO|False|False|
fs_obs|Filesystem OBS|DEMOTE_WAITING_FOR_SLOT|Average time waiting for a demotion concurrency slot|Demote Concurrency Slot Wait Duration (total)|Absolute|Microseconds|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_COMPLETELY_DEAD_BLOBS|Percentage of blobs with no live extent linked to them|Blobs Completely Dead (per scavenged blob)|Measured|%||OBS_RECLAMATION_SCAVENGED_BLOBS / 100|WEKA|IO|False|False|
fs_obs|Filesystem OBS|EXTENTS_WITH_FAKE_RETENTION_TAG|Number of scanned extents with fake retention tag|Invalid Retention Extents (total)|Absolute|Extents|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|DEMOTE_EXTENT_OBS_FETCH_RECLAMATION_REUPLOAD|Number of extent RECLAMATION_REUPLOAD object-store fetch operations per second|Demote Extent Fetch for RECLAMATION_REUPLOAD (total)|Rate|Ops/Sec|uploadSource||WEKA|IO|True|False|
fs_obs|Filesystem OBS|FAILED_DOWNLOADS|Number of failed downloads per second|Failed Downloads (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|DESERIALIZED_EXTENTS_WITH_INVALID_BLOBS|Number of deserialized extents with invalid blob id|Invalid Downloaded Extents (total)|Absolute|Extents|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|STOW_METADATA_DESERIALIZATION_LATENCY|Average latency of metadata blob deserialization|Metadata Blob Deserialization Latency (per seed)|Measured|Milliseconds||STOW_METADATA_SEED_DOWNLOADS|WEKA|IO|False|False|
fs_obs|Filesystem OBS|DEMOTE_EXTENT_OBS_FETCH_IMMEDIATE_RELEASE|Number of extent IMMEDIATE_RELEASE object-store fetch operations per second|Demote Extent Fetch for IMMEDIATE_RELEASE (total)|Rate|Ops/Sec|uploadSource||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_RELOC_UPLOAD|Number of relocation blobs uploaded per second|Reloc Uploads (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|STOW_SERIALIZED_EXTENT_DESCS|Number of extent descriptors uploaded|Uploaded Extent Descriptors (total)|Absolute|Extent Descriptors|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|UPLOAD_LATENCY|Average latency of uploads|Upload Latency (per upload)|Measured|Microseconds||UPLOADS|WEKA|IO|False|False|
fs_obs|Filesystem OBS|TIMEOUT_OPERATIONS|Total number of timed out operations per second|Timeout Operations (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_RELOC_DOWNLOAD|Number of relocation blobs downloaded per second|Reloc Downloads (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_PROMOTE_EXTENT_WRITE_LATENCY|Average latency of extent promote writes|Promote Write Latency (per objects)|Measured|Microseconds||OBS_PROMOTE_EXTENT_WRITE|WEKA|IO|False|False|
fs_obs|Filesystem OBS|DEMOTE_EXTENT_OBS_FETCH_BACKPRESSURE|Number of extent BACKPRESSURE object-store fetch operations per second|Demote Extent Fetch for BACKPRESSURE (total)|Rate|Ops/Sec|uploadSource||WEKA|IO|True|False|
fs_obs|Filesystem OBS|STOW_COMMIT_QUEUE_HANG|Number of times metadata download queue was hanging full|Metadata Queue Hang (total)|Absolute|Occurrences|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_BLOB_TIERING_DURATION|Duration of tiering blobs to object-store|Blob Tiering Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
fs_obs|Filesystem OBS|OBS_IMMEDIATE_RELEASE_FREED|Number of bytes freed from disk due to immediate release per second|Immediate Release Freed (total)|Rate|Bytes/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_TRUNCATE|Number of truncates that needed data from the object-store per second|Object-Store Dependent Truncates (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|CONCURRENT_DEMOTES|Number of demotes executed concurrently|Concurrent Demotes (total)|Accumulated|Demotes|||WEKA|IO|False|False|
fs_obs|Filesystem OBS|OBS_FREED|Number of bytes freed from disk because they are in the object-store per second|Object-Store Freed (total)|Rate|Bytes/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|DEMOTE_EXTENT_OBS_FETCH_MANHOLE|Number of extent MANHOLE object-store fetch operations per second|Demote Extent Fetch for MANHOLE (total)|Rate|Ops/Sec|uploadSource||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_4K_IOPS_READ|Number of object store dedicated 4K read operations per second|Demote 4K IOPs Read (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|TIMEOUT_UPLOADS|Number of timed out uploads per second|Timeout Uploads (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_BLOB_HEADER_DOWNLOAD_LATENCY|Average latency of blob header download|Blob Header Download Latency (per blob)|Measured|Microseconds||OBS_RECLAMATION_SCAVENGED_BLOBS|WEKA|IO|False|False|
fs_obs|Filesystem OBS|BACKPRESSURED_BUCKETS_IN_FSS|Number of backpressured buckets|Backpressured Buckets (total)|Accumulated|Buckets|||WEKA|IO|False|False|
fs_obs|Filesystem OBS|DEMOTE_EXTENT_OBS_FETCH_POLICY|Number of extent POLICY object-store fetch operations per second|Demote Extent Fetch for POLICY (total)|Rate|Ops/Sec|uploadSource||WEKA|IO|True|False|
fs_obs|Filesystem OBS|DEMOTE_EXTENT_OBS_FETCH_MIGRATE|Number of extent MIGRATE object-store fetch operations per second|Demote Extent Fetch for MIGRATE (total)|Rate|Ops/Sec|uploadSource||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_COMPLETELY_ALIVE_BLOBS|Percentage of blobs with only live extents linked to them|Blobs Completely Alive (per scavenged blob)|Measured|%||OBS_RECLAMATION_SCAVENGED_BLOBS / 100|WEKA|IO|False|False|
fs_obs|Filesystem OBS|OBS_WRITE|Number of writes that needed data from the object-store per second|Object-Store Dependent Writes (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|FAILED_UPLOADS|Number of failed uploads per second|Failed Uploads (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|STOW_METADATA_SEED_DOWNLOADS|Number of seed downloads per second|Metadata Seed Downloads (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_UNEXPECTED_TAG_ON_DOWNLOAD|Number of unexpected tags found when downloading extents|Unexpected Tag on Download (total)|Absolute|Occurrences|||WEKA|IO|True|False|
fs_obs|Filesystem OBS|OBS_ONGOING_RECLAMATIONS|Number of ongoing reclamations|Ongoing Space Reclamations (total)|Accumulated|Ops|||WEKA|IO|False|False|
gc|Garbage Collection|GC_USED_SIZE_BEFORE_SCAN|GC used size before the scan starts|GC Used Size Before Scan (total)|Accumulated|Bytes|||WEKA|IO|False|False|
gc|Garbage Collection|GC_USED_SIZE_AFTER_SCAN|GC used size after the scan ends|GC Used Size After Scan (total)|Accumulated|Bytes|||WEKA|IO|False|False|
gc|Garbage Collection|GC_SCANS|Number of GC scans|GC scans (total)|Absolute|Scans|||WEKA|IO|True|False|
gc|Garbage Collection|GC_SCAN_TIME|GC scan time|GC Scan Time (total)|Absolute|Msec|||WEKA|IO|True|False|
gc|Garbage Collection|GC_FREE_SIZE_BEFORE_SCAN|GC pool size before the scan starts|GC Pool Size Before Scan (total)|Accumulated|Bytes|||WEKA|IO|False|False|
gc|Garbage Collection|GC_FREE_SIZE_AFTER_SCAN|GC pool size after the scan ends|GC Pool Size After Scan (total)|Accumulated|Bytes|||WEKA|IO|False|False|
jrpc|JRPC|JRPC_SERVER_PROCESSING_AVG|The average time the JRPC server processed the JRPC requests.|JRPC Server Processing AVG (per JRPC call)|Measured|Microseconds|method|JRPC_SERVER_PROCESSING_TIME[<method>][..]|WEKA|MANAGEMENT|False|False|
jrpc|JRPC|JRPC_SERVER_PROCESSING_TIME|The number of JRPC requests processed by the server per each time range.|JRPC Server Processing Time (total)|Histogram|Requests|method||WEKA|MANAGEMENT|True|True|Microseconds
memory|Memory|RSS_PEAK|The process (node) memory resident size, peak over process lifetime.|RSS Peak (average)|Accumulated|MB|||WEKA|ANY|False|False|
memory|Memory|RSS_CURRENT|The process (node) memory resident size, current in sample time.|RSS Current (average)|Accumulated|MB|||WEKA|ANY|False|False|
network|Network|RDMA_COMP_FAILURES|Number of RDMA requests that completed with an error|RDMA completion failures (total)|Rate|Failures/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|TIMELY_RESENDS|Number of packets resent due to timely resend|Timely Resends (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|FAULT_SENT_DELAYED_PACKETS|Number of sent packets delayed due to a fault injection|Fault Sent Delayed Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|PUMPS_TXQ_PARTIAL|Number of times we only sent some of our queued packets to the NIC queue|# Pumps (total)|Rate|Pumps/Sec|||WEKA|ANY|True|False|
network|Network|POISON_DETECTED_EXPECTED|Expected number of poisoned netbufs detected|Expected poisoned Netbufs Detected (total)|Absolute|Occurrences|||WEKA|ANY|True|False|
network|Network|RDMA_POOL_LOW_CAPACITY|Number of times an RDMA request was not issued due to low RDAM pool memory|RDMA pool low capacity (total)|Rate|Failures/Sec|||WEKA|ANY|True|False|
network|Network|PORT_TX_ERRORS|Number of packet TX errors|Port TX errors (total)|Rate|Packets/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|RECEIVED_CONTROL_PACKETS|Number of received control packets|Received Control Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|TIME_TO_FIRST_SEND|Time from queueing to first send|Time to first send (total)|Histogram|Requests|||WEKA|ANY|True|True|Microseconds
network|Network|FAULT_RECV_DELAYED_PACKETS|Number of received packets delayed due to a fault injection|Fault Recv Delayed Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|SENT_REJECTS|Number of rejects sent|Sent Rejects (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|MBUF_DUP_ITER|Duplicate mbuf check completions|Duplicate mbuf check completions (total)|Absolute|Occurences|||WEKA|ANY|True|False|
network|Network|FAULT_SENT_DROPPED_PACKETS|Number of sent packets dropped due to a fault injection|Fault Sent Dropped Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|TIME_TO_ACK|Histogram of time to ack a data packet|Time to ACK (total)|Histogram|Requests|||WEKA|ANY|True|True|Microseconds
network|Network|DROPPED_PACKETS|Number of packets received that we dropped|Dropped Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|ZERO_CSUM|Number of checksum zero received|Zero checksum received (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|RECEIVED_PACKET_GENERATIONS|The generation ("resend count") of the first incarnation of the packet seen by the receiver (indicates packet loss)|Received Packet Generations (total)|Histogram|Packets|||WEKA|ANY|True|True|PacketGeneration
network|Network|RDMA_SUBMIT_FAILURES|Number of RDMA submit failures, likely indicating a fabric issue|RDMA submit failures (total)|Rate|Failures/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|RDMA_NET_ERR_RETRY_EXCEEDED|Number of RDMA requests with error retries exceeded|RDMA net error retries exceeded (total)|Rate|Occurences/Sec|||WEKA|ANY|True|False|
network|Network|NODE_RECONNECTED|Number of reconnections|Node Reconnections (total)|Rate|Reconnects/Sec|||WEKA|ANY|True|False|
network|Network|PORT_TX_PACKETS|Number of packets transmitted|Port TX Packets (total)|Rate|Packets/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|DOUBLY_RECEIVED_PACKETS|Number of packets that were received multiple times|Doubly Received Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|RESEND_BATCH_SIZE|Number of packets sent in a resend batch|Resend Batch Size (total)|Histogram|Batches|||WEKA|ANY|True|True|Packets
network|Network|SENT_ACKS|Number of ACK packets sent|Sent ACKs (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|MBUF_DUP_COUNT|Numer of Duplicate mbufs found|Duplicate mbufs found (total)|Absolute|Occurences|||WEKA|ANY|True|False|
network|Network|RDMA_REQUESTS|Number of RDMA requests sent to the NIC|RDMA requests sent (total)|Rate|Requests/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|GW_MAC_RESOLVE_SUCCESSES|Number of times we succeeded to ARP resolve the gateway IP|GW MAC resolve succeeded (total)|Accumulated|Successes|||WEKA|ANY|False|False|
network|Network|RDMA_PORT_WAITING_FIBERS|Number of fibers pending to send an RDMA request|RDMA pending send (total)|Accumulated|Waiting fibers|rdmaPort||WEKA|ANY|False|False|
network|Network|RECEIVED_DATA_PACKETS|Number of received data packets|Received Data Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|UDP_SENDMSG_FAILED_OTHER|Number of packets that failed to be sent on the socket backend with an unknown error|UDP sendmsg Failed Other (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|SEND_BATCH_SIZE|Number of packets sent in a first send batch|First send batch size (total)|Histogram|Batches|||WEKA|ANY|True|True|Packets
network|Network|RDMA_POOL_MBUF_LEAKED|RDMA leaked mbufs|RDMA Leaked mbufs (total)|Absolute|Occurences|||WEKA|ANY|True|False|
network|Network|RDMA_SUBMIT_TIMEOUTS|Number of RDMA submit timeouts|RDMA submit timeouts (total)|Rate|Timeouts/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|PUMP_INTERVAL|Interval between pumps|Pump Interval (total)|Histogram|Requests|||WEKA|ANY|True|True|Microseconds
network|Network|UDP_SENDMSG_FAILED_EAGAIN|Number of packets that failed to be sent on the socket backend with EAGAIN|UDP sendmsg Failed EAGAIN (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|SENT_DATA_PACKETS|Number of data packets sent|Sent Data Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|RDMA_TX_BYTES|Number of bytes sent with RDMA|RDMA TX bytes (total)|Rate|Bytes/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|RDMA_SERVER_RECV_FAILURES|Number of failed RDMA server-side receive attempts|RDMA server recv failures (total)|Rate|Failures/Sec|||WEKA|ANY|True|False|
network|Network|RDMA_WAIT_PREMATURE_WAKEUP|RDMA Wait premature wakeup|RDMA Wait premature wakeup (total)|Accumulated|Issues|||WEKA|ANY|False|False|
network|Network|RDMA_COMPLETIONS|Number of RDMA requests that completed|RDMA completions (total)|Rate|Completions/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|RDMA_COMP_DURATION|Histogram of RDMA completion duration times|RDMA Completion Duration (total)|Histogram|Requests|networkPortId||WEKA|ANY|True|True|uSecs
network|Network|DROPPED_LARGE_PACKETS|Number of large packets dropped in the socket backend|Dropped large packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|PEER_RTT|RTT per peer node|Peer RTT (average)|Accumulated|Microseconds|peer_node_id||WEKA|ANY|False|False|
network|Network|PACKETS_PUMPED|Number of packets received in each call to recvPackets|Packets Pumped (total)|Histogram|Batches|||WEKA|ANY|True|True|Packets
network|Network|RDMA_POOL_ALLOC_FAILED|Number of times an RDMA request was not issued due to a pool allocation failure|RDMA pool alloc failures (total)|Rate|Failures/Sec|||WEKA|ANY|True|False|
network|Network|FAULT_RECV_DROPPED_PACKETS|Number of received packets dropped due to a fault injection|Fault Recv Dropped Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|SEND_QUEUE_TIMEOUTS|Number of packets cancelled due to envelope timeout and were not in the send window|Send-queue Timeouts (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|RDMA_COMP_STATUSES|Histogram of RDMA completion statuses|RDMA completion statuses (total)|Rate|Completions/Sec|rDMACompStatus||WEKA|ANY|True|False|
network|Network|SLOW_PATH_CSUM|Number of packets that went through checksum calculation on the CPU|Slow Path Checksum (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|PORT_RX_PACKETS|Number of packets received|Port RX Packets (total)|Rate|Packets/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|BAD_RECV_CSUM|Number of packets received with a bad checksum|Bad UDP checksum (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|RECEIVED_PACKETS|Number of packets received|Received Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|RDMA_SERVER_SEND_FAILURES|Number of failed RDMA server-side send attempts|RDMA server send failures (total)|Rate|Failures/Sec|||WEKA|ANY|True|False|
network|Network|GOODPUT_TX_RATIO|Percentage of goodput TX packets out of total data packets sent|Goodput TX (percentage)|Custom|%|||WEKA|ANY|False|False|
network|Network|SENT_CONTROL_PACKETS|Number of control packets sent|Sent Control Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|CORRUPT_PACKETS|Number of packets received and deemed corrupted|Corrupt Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|RDMA_ADD_CHUNK_FAILURES|Number of RDMA cookie setting failurs|RDMA add cookie chunks failures (total)|Rate|Failures/Sec|||WEKA|ANY|True|False|
network|Network|UNACKED_RESENDS|Number of packets resent after receiving an ack|Unacked Resends (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|SHORT_CIRCUIT_SENDS|Number of packets sent to the same node|Short-circuit Sends (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|RDMA_BINDING_FAILOVERS|Number of RDMA High-Availability fail overs|RDMA HA fail-overs (total)|Rate|Fail-overs/Sec|||WEKA|ANY|True|False|
network|Network|PORT_EXT_RX_PACKETS|Number of external packets received|Port external RX Packets (total)|Rate|Packets/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|RDMA_SERVER_BINDING_RESTARTS|Number of RDMA server binding restarts|RDMA server binding restarts (total)|Rate|Restarts/Sec|||WEKA|ANY|True|False|
network|Network|POISON_DETECTED_UNEXPECTED|Unexpected number of poisoned netbufs detected|Unexpected poisoned Netbufs Detected (total)|Absolute|Occurrences|||WEKA|ANY|True|False|
network|Network|PUMPS_TXQ_FULL|Number of times we couldn't send any new packets to the NIC queue|# Pumps (total)|Rate|Pumps/Sec|||WEKA|ANY|True|False|
network|Network|RDMA_COMP_LATENCY|Average time of RDMA requests completion|RDMA completion latency (per requests)|Measured|Microseconds|networkPortId|RDMA_REQUESTS|WEKA|ANY|False|False|
network|Network|GW_MAC_RESOLVE_FAILURES|Number of times we failed to ARP resolve the gateway IP|GW MAC resolve failures (total)|Accumulated|Failures|||WEKA|ANY|False|False|
network|Network|PORT_RX_ERRORS|Number of packet RX errors|Port RX errors (total)|Rate|Packets/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|RDMA_WAIT_TIMEOUT|RDMA Wait timeouts|RDMA Wait timeouts (total)|Accumulated|Issues|||WEKA|ANY|False|False|
network|Network|PORT_RX_BYTES|Number of bytes received|Port RX Bytes (total)|Rate|Bytes/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|PORT_TX_BYTES|Number of bytes transmitted|Port TX Bytes (total)|Rate|Bytes/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|PUMP_DURATION|Duration of each pump|Pump Duration (total)|Histogram|Requests|||WEKA|ANY|True|True|Microseconds
network|Network|REORDERED_PACKETS|Number of reordered packets|Reordered Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|PORT_RX_MISSED|Number of packets lost due to RX queue full|Port RX missed packets (total)|Rate|Packets/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|SEND_WINDOW_TIMEOUTS|Number of packets cancelled due to envelope timeout while in the send window|Send-window Timeouts (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|PORT_RX_NO_MBUFS|Number of packets lost due to no mbufs|Port RX no mbufs packets (total)|Rate|Packets/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|RDMA_WAIT_INTERRUPTED|RDMA Wait interruptions|RDMA Wait interruptions (total)|Accumulated|Issues|||WEKA|ANY|False|False|
network|Network|RDMA_RX_BYTES|Number of bytes received with RDMA|RDMA RX bytes (total)|Rate|Bytes/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|INVALID_FIRST_FRAGMENT|Number of times we got an invalid first fragment|# Invalid First Fragment (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|SEND_BATCH_SIZE_BYTES|Number of bytes sent in a first send batch|First send batch size in bytes (total)|Histogram|Batches|||WEKA|ANY|True|True|Packets
network|Network|RESENT_DATA_PACKETS|Number of data packets resent|Resent Data Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|SENT_PACKETS|Number of sent packets|Sent Packets (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|GOODPUT_RX_RATIO|Percentage of goodput RX packets out of total data packets received|Goodput RX (percentage)|Custom|%|||WEKA|ANY|False|False|
network|Network|ECN_ENCOUNTERED|Number of ECN Encountered packets|ECN Encountered (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
network|Network|RDMA_CLIENT_BINDING_INVALIDATIONS|Number of RDMA client binding invalidations|RDMA client binding invalidations (total)|Rate|Invalidations/Sec|||WEKA|ANY|True|False|
network|Network|RDMA_CANCELED_COMPLETIONS|Number of RDMA completions that were cancelled|RDMA completions on canceled requests (total)|Rate|Completions/Sec|networkPortId||WEKA|ANY|True|False|
network|Network|UDP_SENDMSG_PARTIAL_SEND|Number of packets that we failed to send but in the same pump some packets were sent|UDP sendmsg Partial Send (total)|Rate|Packets/Sec|||WEKA|ANY|True|False|
object_storage|Object Storage|OBJECT_UPLOAD_BYTES_STOW|Number of STOW bytes sent to the object store per second|Upload Bytes by STOW (total)|Rate|Bytes/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|OBJECT_UPLOAD_BYTES_POLICY|Number of POLICY bytes sent to the object store per second|Upload Bytes by POLICY (total)|Rate|Bytes/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_OK|Number of HTTP OK responses per second|Response Count OK (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|WRITE_BYTES|Number of bytes sent to object storage|Write Bytes (total)|Rate|Bytes/Sec|||USER|IO|True|False|
object_storage|Object Storage|ONGOING_REMOVES|Number of ongoing removes|Ongoing Removes (total)|Accumulated|Ops|||USER|IO|False|False|
object_storage|Object Storage|OBJECT_DELETES|Number of object deletes per second|Object Deletes (total)|Rate|Ops/Sec|||USER|IO|True|False|
object_storage|Object Storage|OBJECT_DOWNLOADS_FOREGROUND|Number of FOREGROUND objects downloaded per second|Object Downloads - FOREGROUND (total)|Rate|Ops/Sec|downloadPriority||USER|IO|True|False|
object_storage|Object Storage|OBJECT_DOWNLOAD_BYTES_BACKGROUND|Number of BACKGROUND bytes sent to the object store per second|Object Downloads Bytes - BACKGROUND (total)|Rate|Bytes/Sec|downloadPriority||USER|IO|True|False|
object_storage|Object Storage|OBJECT_HEAD_QUERIES|Number of object head queries per second|Object HEAD Queries (total)|Rate|Ops/Sec|||USER|IO|True|False|
object_storage|Object Storage|FAILED_OBJECT_DELETES|Number of failed object deletes per second (any failure reason)|Failed Object Deletes (total)|Rate|Ops/Sec|||USER|IO|True|False|
object_storage|Object Storage|WAITING_FOR_GROUP_UPLOAD_BANDWIDTH|Time requests wait for the object store group upload bandwidth|Group Upload Bandwidth Wait Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|RESPONSE_COUNT_HTTP_VERSION_NOT_SUPPORTED|Number of HTTP HTTP_VERSION_NOT_SUPPORTED responses per second|Response Count HTTP_VERSION_NOT_SUPPORTED (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|REQUEST_COUNT_HEAD|Number of HTTP HEAD requests per second|Request Count HEAD (total)|Rate|Requests/Sec|hTTPMethod||USER|IO|True|False|
object_storage|Object Storage|WAITING_IN_GROUP_DOWNLOAD_QUEUE|Time requests wait in the object store group download queue|Group Download Queue Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|RESPONSE_COUNT_UNSUPPORTED_MEDIA_TYPE|Number of HTTP UNSUPPORTED_MEDIA_TYPE responses per second|Response Count UNSUPPORTED_MEDIA_TYPE (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|WAITING_FOR_GROUP_REMOVE_BANDWIDTH|Time requests wait for the object store group remove bandwidth|Group Remove Bandwidth Wait Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|OBJECT_DOWNLOAD_SIZE|Size of downloaded object ranges|Successful Download Size (total)|Histogram|Ops|||USER|IO|True|True|Bytes
object_storage|Object Storage|OBJECT_UPLOADS_STOW|Number of STOW upload attempts per second|Uploads by STOW (total)|Rate|Ops/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|OBJECT_HEAD_LATENCY|Average latency of deleting an object|Head Latency (per head)|Measured|Microseconds||OBJECT_HEAD_QUERIES|USER|IO|False|False|
object_storage|Object Storage|RESPONSE_COUNT_URI_TOO_LONG|Number of HTTP URI_TOO_LONG responses per second|Response Count URI_TOO_LONG (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|OBJECT_UPLOADS_MIGRATE|Number of MIGRATE upload attempts per second|Uploads by MIGRATE (total)|Rate|Ops/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_NOT_MODIFIED|Number of HTTP NOT_MODIFIED responses per second|Response Count NOT_MODIFIED (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|FAILED_OBJECT_UPLOADS|Number of failed object uploads per second (any failure reason)|Failed Object Uploads (total)|Rate|Ops/Sec|||USER|IO|True|False|
object_storage|Object Storage|OBJECT_UPLOADS_BACKPRESSURE|Number of BACKPRESSURE upload attempts per second|Uploads by BACKPRESSURE (total)|Rate|Ops/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_REQUEST_HEADER_FIELDS_TOO_LARGE|Number of HTTP REQUEST_HEADER_FIELDS_TOO_LARGE responses per second|Response Count REQUEST_HEADER_FIELDS_TOO_LARGE (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|OBJECT_DOWNLOAD_BYTES_FOREGROUND|Number of FOREGROUND bytes sent to the object store per second|Object Downloads Bytes - FOREGROUND (total)|Rate|Bytes/Sec|downloadPriority||USER|IO|True|False|
object_storage|Object Storage|OBJECT_UPLOADS_POLICY|Number of POLICY upload attempts per second|Uploads by POLICY (total)|Rate|Ops/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|OBJECT_DOWNLOAD_DURATION|Duration of object download request|Download Duration (total)|Histogram|Ops|||USER|IO|True|True|Milliseconds
object_storage|Object Storage|OBJECT_DOWNLOAD_LATENCY|Average latency of downloading an object|Download Latency (per download)|Measured|Microseconds||OBJECT_DOWNLOADS|USER|IO|False|False|
object_storage|Object Storage|RESPONSE_COUNT_NO_CONTENT|Number of HTTP NO_CONTENT responses per second|Response Count NO_CONTENT (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_MOVED_PERMANENTLY|Number of HTTP MOVED_PERMANENTLY responses per second|Response Count MOVED_PERMANENTLY (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|REQUEST_COUNT_PUT|Number of HTTP PUT requests per second|Request Count PUT (total)|Rate|Requests/Sec|hTTPMethod||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_NOT_FOUND|Number of HTTP NOT_FOUND responses per second|Response Count NOT_FOUND (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|WAITING_IN_GROUP_UPLOAD_QUEUE|Time requests wait in object-store group upload queue|Group Upload Queue Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|RESPONSE_COUNT_NOT_ACCEPTABLE|Number of HTTP NOT_ACCEPTABLE responses per second|Response Count NOT_ACCEPTABLE (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_REQUESTED_RANGE_NOT_SATISFIABLE|Number of HTTP REQUESTED_RANGE_NOT_SATISFIABLE responses per second|Response Count REQUESTED_RANGE_NOT_SATISFIABLE (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|OBS_READ_BYTES|Number of bytes read from object storage|OBS Read Bytes (total)|Rate|Bytes/Sec|||USER|IO|True|False|
object_storage|Object Storage|REQUEST_COUNT_GET|Number of HTTP GET requests per second|Request Count GET (total)|Rate|Requests/Sec|hTTPMethod||USER|IO|True|False|
object_storage|Object Storage|WAITING_FOR_BUCKET_REMOVE_BANDWIDTH|Time requests wait for the object store bucket remove bandwidth|Bucket Remove Bandwidth Wait Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|RESPONSE_COUNT_CONFLICT|Number of HTTP CONFLICT responses per second|Response Count CONFLICT (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_UNAUTHORIZED|Number of HTTP UNAUTHORIZED responses per second|Response Count UNAUTHORIZED (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_ACCEPTED|Number of HTTP ACCEPTED responses per second|Response Count ACCEPTED (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_FOUND|Number of HTTP FOUND responses per second|Response Count FOUND (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_INVALID|Number of HTTP INVALID responses per second|Response Count INVALID (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|WAITING_IN_GROUP_REMOVE_QUEUE|Time requests wait in the object store group remove queue|Group Remove Queue Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|OBJECT_UPLOAD_BYTES_BACKPRESSURE|Number of BACKPRESSURE bytes sent to the object store per second|Upload Bytes by BACKPRESSURE (total)|Rate|Bytes/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|REQUEST_COUNT_INVALID|Number of HTTP INVALID requests per second|Request Count INVALID (total)|Rate|Requests/Sec|hTTPMethod||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_SWITCHING_PROTOCOL|Number of HTTP SWITCHING_PROTOCOL responses per second|Response Count SWITCHING_PROTOCOL (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_SEE_OTHER|Number of HTTP SEE_OTHER responses per second|Response Count SEE_OTHER (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|OBJECT_HEAD_DURATION|Duration of object head request|Head Duration (total)|Histogram|Ops|||USER|IO|True|True|Milliseconds
object_storage|Object Storage|WAITING_IN_BUCKET_REMOVE_QUEUE|Time requests wait in the object store bucket remove queue|Bucket Remove Queue Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|RESPONSE_COUNT_TEMP_REDIRECT|Number of HTTP TEMP_REDIRECT responses per second|Response Count TEMP_REDIRECT (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_REQUEST_TOO_LARGE|Number of HTTP REQUEST_TOO_LARGE responses per second|Response Count REQUEST_TOO_LARGE (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|OBJECT_UPLOADS_IMMEDIATE_RELEASE|Number of IMMEDIATE_RELEASE upload attempts per second|Uploads by IMMEDIATE_RELEASE (total)|Rate|Ops/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|REMOVE_BYTES|Number of bytes removed from object storage|Remove Bytes (total)|Rate|Bytes/Sec|||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_REQUEST_TIMEOUT|Number of HTTP REQUEST_TIMEOUT responses per second|Response Count REQUEST_TIMEOUT (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_PRECONDITION_FAILED|Number of HTTP PRECONDITION_FAILED responses per second|Response Count PRECONDITION_FAILED (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|WAITING_FOR_BUCKET_UPLOAD_BANDWIDTH|Time requests wait for the object store bucket upload bandwidth|Bucket Upload Bandwidth Wait Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|OBJECT_UPLOAD_DURATION|Duration of object upload request|Upload Duration (total)|Histogram|Ops|||USER|IO|True|True|Milliseconds
object_storage|Object Storage|RESPONSE_COUNT_PARTIAL_CONTENT|Number of HTTP PARTIAL_CONTENT responses per second|Response Count PARTIAL_CONTENT (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_EXPECTATION_FAILED|Number of HTTP EXPECTATION_FAILED responses per second|Response Count EXPECTATION_FAILED (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|OBJECT_DOWNLOADS|Number of objects downloaded per second|Object Downloads (total)|Rate|Ops/Sec|||USER|IO|True|False|
object_storage|Object Storage|FAILED_OBJECT_OPERATIONS|Total number of failed operations per second|Failed Object Operations (total)|Rate|Ops/Sec|||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_USE_PROXY|Number of HTTP USE_PROXY responses per second|Response Count USE_PROXY (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|WAITING_FOR_GROUP_UPLOAD_FLOW|Time requests wait for the object store group upload flow|Group Upload Flow Wait Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|WAITING_FOR_GROUP_REMOVE_FLOW|Time requests wait for the object store group remove flow|Group Remove Flow Wait Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|RESPONSE_COUNT_PAYMENT_REQUIRED|Number of HTTP PAYMENT_REQUIRED responses per second|Response Count PAYMENT_REQUIRED (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|REQUEST_COUNT_DELETE|Number of HTTP DELETE requests per second|Request Count DELETE (total)|Rate|Requests/Sec|hTTPMethod||USER|IO|True|False|
object_storage|Object Storage|OBJECT_UPLOADS_RECLAMATION_REUPLOAD|Number of RECLAMATION_REUPLOAD upload attempts per second|Uploads by RECLAMATION_REUPLOAD (total)|Rate|Ops/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_CREATED|Number of HTTP CREATED responses per second|Response Count CREATED (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|OBJECT_UPLOAD_BYTES_IMMEDIATE_RELEASE|Number of IMMEDIATE_RELEASE bytes sent to the object store per second|Upload Bytes by IMMEDIATE_RELEASE (total)|Rate|Bytes/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|FAILED_OBJECT_DOWNLOADS|Number of failed object download per second (any failure reason)|Failed Object Downloads (total)|Rate|Ops/Sec|||USER|IO|True|False|
object_storage|Object Storage|WAITING_FOR_GROUP_DOWNLOAD_BANDWIDTH|Time requests wait for the object store group download bandwidth|Group Download Bandwidth Wait Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|FAILED_OBJECT_HEAD_QUERIES|Number of failed object head queries per second (any failure reason)|Failed Object Head Queries (total)|Rate|Ops/Sec|||USER|IO|True|False|
object_storage|Object Storage|ONGOING_UPLOADS|Number of ongoing uploads|Ongoing Uploads (total)|Accumulated|Ops|||USER|IO|False|False|
object_storage|Object Storage|OBJECT_UPLOAD_LATENCY|Average latency of uploading an object|Upload Latency (per upload)|Measured|Microseconds||OBJECT_UPLOADS|USER|IO|False|False|
object_storage|Object Storage|READ_BYTES|Number of bytes read from object storage|Read Bytes (total)|Rate|Bytes/Sec|||USER|IO|True|False|
object_storage|Object Storage|WAITING_FOR_BUCKET_UPLOAD_FLOW|Time requests wait for the object store bucket upload flow|Bucket Upload Flow Wait Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|REQUEST_COUNT_POST|Number of HTTP POST requests per second|Request Count POST (total)|Rate|Requests/Sec|hTTPMethod||USER|IO|True|False|
object_storage|Object Storage|WAITING_IN_BUCKET_UPLOAD_QUEUE|Time requests wait in the object store bucket upload queue|Bucket Upload Queue Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|RESPONSE_COUNT_BAD_GATEWAY|Number of HTTP BAD_GATEWAY responses per second|Response Count BAD_GATEWAY (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|OBJECT_REMOVE_SIZE|Size of removed objects|Successful Remove Size (total)|Histogram|Ops|||USER|IO|True|True|Bytes
object_storage|Object Storage|OBJECT_UPLOADS_MANHOLE|Number of MANHOLE upload attempts per second|Uploads by MANHOLE (total)|Rate|Ops/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|WAITING_IN_BUCKET_DOWNLOAD_QUEUE|Time requests wait in the object store bucket download queue|Bucket Download Queue Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|OBJECT_UPLOAD_SIZE|Size of uploaded objects|Successful Blob Upload Size (total)|Histogram|Ops|||USER|IO|True|True|Bytes
object_storage|Object Storage|RESPONSE_COUNT_RESET_CONTENT|Number of HTTP RESET_CONTENT responses per second|Response Count RESET_CONTENT (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|OBJECT_UPLOAD_BYTES_MANHOLE|Number of MANHOLE bytes sent to the object store per second|Upload Bytes by MANHOLE (total)|Rate|Bytes/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_SERVICE_UNAVAILABLE|Number of HTTP SERVICE_UNAVAILABLE responses per second|Response Count SERVICE_UNAVAILABLE (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|OBJECT_DOWNLOADS_BACKGROUND|Number of BACKGROUND objects downloaded per second|Object Downloads - BACKGROUND (total)|Rate|Ops/Sec|downloadPriority||USER|IO|True|False|
object_storage|Object Storage|OBJECT_UPLOAD_BYTES_RECLAMATION_REUPLOAD|Number of RECLAMATION_REUPLOAD bytes sent to the object store per second|Upload Bytes by RECLAMATION_REUPLOAD (total)|Rate|Bytes/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|OBJECT_OPERATIONS|Total number of operations per second|Object Operations (total)|Rate|Ops/Sec|||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_SERVER_ERROR|Number of HTTP SERVER_ERROR responses per second|Response Count SERVER_ERROR (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|WAITING_FOR_BUCKET_REMOVE_FLOW|Time requests wait for the object store bucket remove flow|Bucket Remove Flow Wait Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|RESPONSE_COUNT_BAD_REQUEST|Number of HTTP BAD_REQUEST responses per second|Response Count BAD_REQUEST (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|OBJECT_UPLOAD_BYTES_MIGRATE|Number of MIGRATE bytes sent to the object store per second|Upload Bytes by MIGRATE (total)|Rate|Bytes/Sec|uploadSource||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_UNPROCESSABLE_ENTITY|Number of HTTP UNPROCESSABLE_ENTITY responses per second|Response Count UNPROCESSABLE_ENTITY (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_NON_AUTH_INFO|Number of HTTP NON_AUTH_INFO responses per second|Response Count NON_AUTH_INFO (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_REDIRECT_MULTIPLE_CHOICES|Number of HTTP REDIRECT_MULTIPLE_CHOICES responses per second|Response Count REDIRECT_MULTIPLE_CHOICES (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_PROXY_AUTH_REQUIRED|Number of HTTP PROXY_AUTH_REQUIRED responses per second|Response Count PROXY_AUTH_REQUIRED (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_LENGTH_REQUIRED|Number of HTTP LENGTH_REQUIRED responses per second|Response Count LENGTH_REQUIRED (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|OBS_WRITE_BYTES|Number of bytes sent to object storage|OBS Write Bytes (total)|Rate|Bytes/Sec|||USER|IO|True|False|
object_storage|Object Storage|OBJECT_DELETE_LATENCY|Average latency of deleting an object|Delete Latency (per delete)|Measured|Microseconds||OBJECT_DELETES|USER|IO|False|False|
object_storage|Object Storage|WAITING_FOR_BUCKET_DOWNLOAD_FLOW|Time requests wait for the object store bucket download flow|Bucket Download Flow Wait Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|RESPONSE_COUNT_FORBIDDEN|Number of HTTP FORBIDDEN responses per second|Response Count FORBIDDEN (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|WAITING_FOR_BUCKET_DOWNLOAD_BANDWIDTH|Time requests wait for the object tore bucket download bandwidth|Bucket Download Bandwidth Wait Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|OBJECT_UPLOADS|Number of object uploads per second|Object Uploads (total)|Rate|Ops/Sec|||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_METHOD_NOT_ALLOWED|Number of HTTP METHOD_NOT_ALLOWED responses per second|Response Count METHOD_NOT_ALLOWED (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_GATEWAY_TIMEOUT|Number of HTTP GATEWAY_TIMEOUT responses per second|Response Count GATEWAY_TIMEOUT (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|ONGOING_DOWNLOADS|Number of ongoing downloads|Ongoing Downloads (total)|Accumulated|Ops|||USER|IO|False|False|
object_storage|Object Storage|RESPONSE_COUNT_GONE|Number of HTTP GONE responses per second|Response Count GONE (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_INSUFFICIENT_STORAGE|Number of HTTP INSUFFICIENT_STORAGE responses per second|Response Count INSUFFICIENT_STORAGE (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|WAITING_FOR_GROUP_DOWNLOAD_FLOW|Time requests wait for the object store group download flow|Group Download Flow Wait Duration (total)|Histogram|Ops|||WEKA|IO|True|True|Milliseconds
object_storage|Object Storage|RESPONSE_COUNT_CONTINUE|Number of HTTP CONTINUE responses per second|Response Count CONTINUE (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|RESPONSE_COUNT_NOT_IMPLEMENTED|Number of HTTP NOT_IMPLEMENTED responses per second|Response Count NOT_IMPLEMENTED (total)|Rate|Responses/Sec|hTTPCode||USER|IO|True|False|
object_storage|Object Storage|OBJECT_DELETE_DURATION|Duration of object delete request|Delete Duration (total)|Histogram|Ops|||USER|IO|True|True|Milliseconds
ops|Operations|MKNOD_LATENCY|Average latency of MKNOD operations|MKNOD Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[MKNOD] + ops_nfs/METADATA_OPS[MKNOD]|USER|IO|False|False|
ops|Operations|STATFS_OPS|Number of STATFS operation per second|STATFS OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|FLOCK_LATENCY|Average latency of FLOCK operations|FLOCK Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[FLOCK] + ops_nfs/METADATA_OPS[FLOCK]|USER|IO|False|False|
ops|Operations|UNLINK_OPS|Number of UNLINK operation per second|UNLINK OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|WRITE_BYTES|Number of byte writes per second|Write Bytes (total)|Rate|Bytes/Sec|||USER|IO|True|False|
ops|Operations|FILEATOMICOPEN_OPS|Number of FILEATOMICOPEN operation per second|FILEATOMICOPEN OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|RENAME_LATENCY|Average latency of RENAME operations|RENAME Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[RENAME] + ops_nfs/METADATA_OPS[RENAME]|USER|IO|False|False|
ops|Operations|SETATTR_OPS|Number of SETATTR operation per second|SETATTR OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|COMMIT_LATENCY|Average latency of COMMIT operations|COMMIT Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[COMMIT] + ops_nfs/METADATA_OPS[COMMIT]|USER|IO|False|False|
ops|Operations|READDIR_LATENCY|Average latency of READDIR operations|READDIR Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[READDIR] + ops_nfs/METADATA_OPS[READDIR]|USER|IO|False|False|
ops|Operations|FILEOPEN_LATENCY|Average latency of FILEOPEN operations|FILEOPEN Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[FILEOPEN] + ops_nfs/METADATA_OPS[FILEOPEN]|USER|IO|False|False|
ops|Operations|LINK_LATENCY|Average latency of LINK operations|LINK Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[LINK] + ops_nfs/METADATA_OPS[LINK]|USER|IO|False|False|
ops|Operations|READLINK_OPS|Number of READLINK operation per second|READLINK OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|PATHCONF_OPS|Number of PATHCONF operation per second|PATHCONF OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|REMOVE_OPS|Number of REMOVE operation per second|REMOVE OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|MKDIR_LATENCY|Average latency of MKDIR operations|MKDIR Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[MKDIR] + ops_nfs/METADATA_OPS[MKDIR]|USER|IO|False|False|
ops|Operations|WRITE_DURATION|The number of writes per completion duration|Write Duration (total)|Histogram|Writes|||USER|IO|True|True|uSecs
ops|Operations|CREATE_OPS|Number of CREATE operation per second|CREATE OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|FILEOPEN_OPS|Number of FILEOPEN operation per second|FILEOPEN OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|READ_LATENCY|Average latency of READ operations|Read Latency (per read)|Measured|Microseconds||ops_driver/READS + ops_nfs/READS|USER|IO|False|False|
ops|Operations|FILECLOSE_LATENCY|Average latency of FILECLOSE operations|FILECLOSE Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[FILECLOSE] + ops_nfs/METADATA_OPS[FILECLOSE]|USER|IO|False|False|
ops|Operations|SETATTR_LATENCY|Average latency of SETATTR operations|SETATTR Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[SETATTR] + ops_nfs/METADATA_OPS[SETATTR]|USER|IO|False|False|
ops|Operations|ACCESS_OPS|Number of ACCESS operation per second|ACCESS OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|ACCESS_LATENCY|Average latency of ACCESS operations|ACCESS Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[ACCESS] + ops_nfs/METADATA_OPS[ACCESS]|USER|IO|False|False|
ops|Operations|READDIR_OPS|Number of READDIR operation per second|READDIR OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|UNLINK_LATENCY|Average latency of UNLINK operations|UNLINK Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[UNLINK] + ops_nfs/METADATA_OPS[UNLINK]|USER|IO|False|False|
ops|Operations|FILEATOMICOPEN_LATENCY|Average latency of FILEATOMICOPEN operations|FILEATOMICOPEN Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[FILEATOMICOPEN] + ops_nfs/METADATA_OPS[FILEATOMICOPEN]|USER|IO|False|False|
ops|Operations|WRITE_LATENCY|Average latency of WRITE operations|Write Latency (per write)|Measured|Microseconds||ops_driver/WRITES + ops_nfs/WRITES|USER|IO|False|False|
ops|Operations|THROUGHPUT|Number of byte read/writes per second|Throughput (total)|Rate|Bytes/Sec|||USER|IO|True|False|
ops|Operations|STATFS_LATENCY|Average latency of STATFS operations|STATFS Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[STATFS] + ops_nfs/METADATA_OPS[STATFS]|USER|IO|False|False|
ops|Operations|READ_DURATION|The number of reads per completion duration|Read Duration (total)|Histogram|Reads|||USER|IO|True|True|uSecs
ops|Operations|PATHCONF_LATENCY|Average latency of PATHCONF operations|PATHCONF Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[PATHCONF] + ops_nfs/METADATA_OPS[PATHCONF]|USER|IO|False|False|
ops|Operations|FLOCK_OPS|Number of FLOCK operation per second|FLOCK OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|GETATTR_LATENCY|Average latency of GETATTR operations|GETATTR Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[GETATTR] + ops_nfs/METADATA_OPS[GETATTR]|USER|IO|False|False|
ops|Operations|SYMLINK_LATENCY|Average latency of SYMLINK operations|SYMLINK Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[SYMLINK] + ops_nfs/METADATA_OPS[SYMLINK]|USER|IO|False|False|
ops|Operations|SYMLINK_OPS|Number of SYMLINK operation per second|SYMLINK OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|REMOVE_LATENCY|Average latency of REMOVE operations|REMOVE Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[REMOVE] + ops_nfs/METADATA_OPS[REMOVE]|USER|IO|False|False|
ops|Operations|FILECLOSE_OPS|Number of FILECLOSE operation per second|FILECLOSE OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|LOOKUP_OPS|Number of LOOKUP operation per second|LOOKUP OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|LINK_OPS|Number of LINK operation per second|LINK OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|COMMIT_OPS|Number of COMMIT operation per second|COMMIT OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|WRITES|Number of write operations per second|Writes (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|MKDIR_OPS|Number of MKDIR operation per second|MKDIR OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|LOOKUP_LATENCY|Average latency of LOOKUP operations|LOOKUP Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[LOOKUP] + ops_nfs/METADATA_OPS[LOOKUP]|USER|IO|False|False|
ops|Operations|FSINFO_LATENCY|Average latency of FSINFO operations|FSINFO Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[FSINFO] + ops_nfs/METADATA_OPS[FSINFO]|USER|IO|False|False|
ops|Operations|READ_BYTES|Number of bytes read per second|Read Bytes (total)|Rate|Bytes/Sec|||USER|IO|True|False|
ops|Operations|FSINFO_OPS|Number of FSINFO operation per second|FSINFO OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|RMDIR_LATENCY|Average latency of RMDIR operations|RMDIR Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[RMDIR] + ops_nfs/METADATA_OPS[RMDIR]|USER|IO|False|False|
ops|Operations|GETATTR_OPS|Number of GETATTR operation per second|GETATTR OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|OPS|Total number of operations|OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|MKNOD_OPS|Number of MKNOD operation per second|MKNOD OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|CREATE_LATENCY|Average latency of CREATE operations|CREATE Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[CREATE] + ops_nfs/METADATA_OPS[CREATE]|USER|IO|False|False|
ops|Operations|RMDIR_OPS|Number of RMDIR operation per second|RMDIR OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|READLINK_LATENCY|Average latency of READLINK operations|READLINK Latency (per operation)|Measured|Microseconds||ops_driver/METADATA_OPS[READLINK] + ops_nfs/METADATA_OPS[READLINK]|USER|IO|False|False|
ops|Operations|READS|Number of read operations per second|Reads (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops|Operations|RENAME_OPS|Number of RENAME operation per second|RENAME OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops_driver|Operations (driver)|READLINK_OPS|Number of READLINK operation per second|READLINK OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|RENAME_LATENCY|Average latency of RENAME operations|RENAME Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|FILEATOMICOPEN_OPS|Number of FILEATOMICOPEN operation per second|FILEATOMICOPEN OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|UNLINK_OPS|Number of UNLINK operation per second|UNLINK OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|SYMLINK_QOS_DELAY|Average QoS delay for SYMLINK operations|SYMLINK QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|READLINK_QOS_DELAY|Average QoS delay for READLINK operations|READLINK QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|STATFS_OPS|Number of STATFS operation per second|STATFS OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|READ_RDMA_SIZES|The number of RDMA reads per each read size range|Read RDMA Sizes (total)|Histogram|Reads|||USER|IO|True|True|Blocks
ops_driver|Operations (driver)|MKNOD_LATENCY|Average latency of MKNOD operations|MKNOD Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|SUCCEEDED_1HOP_READS|Number of succesfull single hop reads per second|Reads-1HOP (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops_driver|Operations (driver)|READDIR_QOS_DELAY|Average QoS delay for READDIR operations|READDIR QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|FILEATOMICOPEN_LATENCY|Average latency of FILEATOMICOPEN operations|FILEATOMICOPEN Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|THROUGHPUT|Number of byte read/writes per second|Throughput (total)|Rate|Bytes/Sec|||USER|IO|True|False|
ops_driver|Operations (driver)|MKNOD_QOS_DELAY|Average QoS delay for MKNOD operations|MKNOD QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|SYMLINK_OPS|Number of SYMLINK operation per second|SYMLINK OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|FILECLOSE_OPS|Number of FILECLOSE operation per second|FILECLOSE OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|RDMA_WRITE_REQUESTS|Number of RDMA write request operations per second|Writes RDMA (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops_driver|Operations (driver)|WRITE_SIZES|The number of writes per each read size range|Write Sizes (total)|Histogram|Writes|||USER|IO|True|True|Blocks
ops_driver|Operations (driver)|WRITE_RDMA_SIZES_RATE|The number of RDMA writes per each read size range per second|Write RDMA Sizes per second (total)|Histogram|Writes|||USER|IO|True|True|Blocks/Sec
ops_driver|Operations (driver)|LISTXATTR_LATENCY|Average latency of LISTXATTR operations|LISTXATTR Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|RMXATTR_LATENCY|Average latency of RMXATTR operations|RMXATTR Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|FILEOPEN_QOS_DELAY|Average QoS delay for FILEOPEN operations|FILEOPEN QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|GETATTR_OPS|Number of GETATTR operation per second|GETATTR OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|WRITES_NO_LEASE|Number of direct writes while we have no lease|Writes-No-Lease (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops_driver|Operations (driver)|DIRECT_WRITE_SIZES_RATE|The number of O_DIRECT writes per each read size range per second|Direct Write Sizes per second (total)|Histogram|Writes|||USER|IO|True|True|Blocks/Sec
ops_driver|Operations (driver)|WRITE_LATENCY_NO_QOS|Average latency of WRITE operations without QoS delay|Write latency (no qos) (per read)|Measured|Microseconds||ops_driver/WRITES|USER|IO|False|False|
ops_driver|Operations (driver)|SETXATTR_QOS_DELAY|Average QoS delay for SETXATTR operations|SETXATTR QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|RENAME_OPS|Number of RENAME operation per second|RENAME OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|FILECLOSE_LATENCY|Average latency of FILECLOSE operations|FILECLOSE Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|GETATTR_QOS_DELAY|Average QoS delay for GETATTR operations|GETATTR QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|WRITE_BYTES|Number of byte writes per second|Write Bytes (total)|Rate|Bytes/Sec|||USER|IO|True|False|
ops_driver|Operations (driver)|RMXATTR_OPS|Number of RMXATTR operation per second|RMXATTR OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|WRITE_QOS_DELAY|Average QoS delay for WRITE operations|Write QoS Delay (per write)|Measured|Microseconds||WRITES|USER|IO|False|False|
ops_driver|Operations (driver)|WRITES|Number of write operations per second|Writes (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops_driver|Operations (driver)|RMDIR_LATENCY|Average latency of RMDIR operations|RMDIR Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|READ_CORRUPTIONS_DETECTED_IN_1HOP|The number of corrupt data blocks encountered during 1-hop read|Single-hop read checksum error (total)|Absolute|Ops|||WEKA|IO|True|False|
ops_driver|Operations (driver)|LOOKUP_OPS|Number of LOOKUP operation per second|LOOKUP OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|IOCTL_OBS_RELEASE_QOS_DELAY|Average QoS delay for IOCTL_OBS_RELEASE operations|IOCTL_OBS_RELEASE QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|GETATTR_LATENCY|Average latency of GETATTR operations|GETATTR Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|READ_DURATION|The number of reads per each time duration|Read Duration (total)|Histogram|Reads|||USER|IO|True|True|uSecs
ops_driver|Operations (driver)|FLOCK_QOS_DELAY|Average QoS delay for FLOCK operations|FLOCK QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|RMDIR_QOS_DELAY|Average QoS delay for RMDIR operations|RMDIR QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|UNLINK_LATENCY|Average latency of UNLINK operations|UNLINK Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|IOCTL_OBS_PREFETCH_LATENCY|Average latency of IOCTL_OBS_PREFETCH operations|IOCTL_OBS_PREFETCH Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|SETATTR_LATENCY|Average latency of SETATTR operations|SETATTR Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|IOCTL_OBS_PREFETCH_QOS_DELAY|Average QoS delay for IOCTL_OBS_PREFETCH operations|IOCTL_OBS_PREFETCH QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|LISTXATTR_OPS|Number of LISTXATTR operation per second|LISTXATTR OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|READ_SIZES_RATE|The number of reads per each read size range per second|Read Sizes per second (total)|Histogram|Reads|||USER|IO|True|True|Blocks/Sec
ops_driver|Operations (driver)|REQUESTS_COMPLETED|The number of completions frontends sent to driver's queue|Requests Completed (total)|Absolute|Ops|||WEKA|IO|True|False|
ops_driver|Operations (driver)|GETXATTR_QOS_DELAY|Average QoS delay for GETXATTR operations|GETXATTR QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|FAILED_1HOP_READS|Number of failed single hop reads per second|Failed-Reads-1HOP (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops_driver|Operations (driver)|DOORBELL_RING_COUNT|The number of times the driver queue's doorbell was ringed|Doorbell Ring Count (total)|Absolute|Ops|||WEKA|IO|True|False|
ops_driver|Operations (driver)|KEEPALIVES_NO_LEASE|Number of driver keepalives sent while we have no lease|Keepalives-No-Lease (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops_driver|Operations (driver)|DIRECT_READ_SIZES|The number of O_DIRECT reads per each read size range|Direct Read Sizes (total)|Histogram|Reads|||USER|IO|True|True|Blocks
ops_driver|Operations (driver)|SETATTR_QOS_DELAY|Average QoS delay for SETATTR operations|SETATTR QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|MKNOD_OPS|Number of MKNOD operation per second|MKNOD OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|RMDIR_OPS|Number of RMDIR operation per second|RMDIR OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|IOCTL_OBS_PREFETCH_OPS|Number of IOCTL_OBS_PREFETCH operation per second|IOCTL_OBS_PREFETCH OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|READLINK_LATENCY|Average latency of READLINK operations|READLINK Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|LINK_LATENCY|Average latency of LINK operations|LINK Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|READ_LATENCY_NO_QOS|Average latency of READ operations without QoS delay|Read latency (no qos) (per read)|Measured|Microseconds||ops_driver/READS|USER|IO|False|False|
ops_driver|Operations (driver)|READ_CHECKSUM_ERRORS|The number of times the driver's checksum validation failed upon the read's content|Read Checksum Errors (total)|Absolute|Ops|||WEKA|IO|True|False|
ops_driver|Operations (driver)|FLOCK_LATENCY|Average latency of FLOCK operations|FLOCK Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|READ_LATENCY|Average latency of READ operations|Read Latency (per read)|Measured|Microseconds||READS|USER|IO|False|False|
ops_driver|Operations (driver)|FILEOPEN_OPS|Number of FILEOPEN operation per second|FILEOPEN OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|WRITE_LATENCY|Average latency of WRITE operations|Write Latency (per write)|Measured|Microseconds||WRITES|USER|IO|False|False|
ops_driver|Operations (driver)|STATFS_LATENCY|Average latency of STATFS operations|STATFS Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|FILEATOMICOPEN_QOS_DELAY|Average QoS delay for FILEATOMICOPEN operations|FILEATOMICOPEN QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|REQUESTS_FETCHED|The number of operations frontends fetched from driver's queue|Requests Fetched (total)|Absolute|Ops|||WEKA|IO|True|False|
ops_driver|Operations (driver)|SETXATTR_LATENCY|Average latency of SETXATTR operations|SETXATTR Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|READDIR_LATENCY|Average latency of READDIR operations|READDIR Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|WRITE_RDMA_SIZES|The number of RDMA writes per each read size range|Write RDMA Sizes (total)|Histogram|Writes|||USER|IO|True|True|Blocks
ops_driver|Operations (driver)|READ_SIZES|The number of reads per each read size range|Read Sizes (total)|Histogram|Reads|||USER|IO|True|True|Blocks
ops_driver|Operations (driver)|SETXATTR_OPS|Number of SETXATTR operation per second|SETXATTR OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|LINK_OPS|Number of LINK operation per second|LINK OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|IOCTL_OBS_RELEASE_LATENCY|Average latency of IOCTL_OBS_RELEASE operations|IOCTL_OBS_RELEASE Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|LOOKUP_LATENCY|Average latency of LOOKUP operations|LOOKUP Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|WRITE_SIZES_RATE|The number of writes per each read size range per second|Write Sizes per second (total)|Histogram|Writes|||USER|IO|True|True|Blocks/Sec
ops_driver|Operations (driver)|READ_BYTES|Number of bytes read per second|Read Bytes (total)|Rate|Bytes/Sec|||USER|IO|True|False|
ops_driver|Operations (driver)|IOCTL_OBS_RELEASE_OPS|Number of IOCTL_OBS_RELEASE operation per second|IOCTL_OBS_RELEASE OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|READS_NO_LEASE|Number of direct reads while we have no lease|Reads-No-Lease (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops_driver|Operations (driver)|READS|Number of read operations per second|Reads (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops_driver|Operations (driver)|WRITE_DURATION|The number of writes per each time duration|Write Duration (total)|Histogram|Writes|||USER|IO|True|True|uSecs
ops_driver|Operations (driver)|STATFS_QOS_DELAY|Average QoS delay for STATFS operations|STATFS QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|READ_QOS_DELAY|Average QoS delay for READ operations|Read QoS Delay (per read)|Measured|Microseconds||READS|USER|IO|False|False|
ops_driver|Operations (driver)|LISTXATTR_QOS_DELAY|Average QoS delay for LISTXATTR operations|LISTXATTR QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|FILEOPEN_LATENCY|Average latency of FILEOPEN operations|FILEOPEN Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|SETATTR_OPS|Number of SETATTR operation per second|SETATTR OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|LOOKUP_QOS_DELAY|Average QoS delay for LOOKUP operations|LOOKUP QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|UNLINK_QOS_DELAY|Average QoS delay for UNLINK operations|UNLINK QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|GETXATTR_LATENCY|Average latency of GETXATTR operations|GETXATTR Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|READDIR_OPS|Number of READDIR operation per second|READDIR OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|GETXATTR_OPS|Number of GETXATTR operation per second|GETXATTR OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|LINK_QOS_DELAY|Average QoS delay for LINK operations|LINK QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|READ_RDMA_SIZES_RATE|The number of RDMA reads per each read size range per second|Read RDMA Sizes per second (total)|Histogram|Reads|||USER|IO|True|True|Blocks/Sec
ops_driver|Operations (driver)|DIRECT_READ_SIZES_RATE|The number of O_DIRECT reads per each read size range per second|Direct Read Sizes per second (total)|Histogram|Reads|||USER|IO|True|True|Blocks/Sec
ops_driver|Operations (driver)|FLOCK_OPS|Number of FLOCK operation per second|FLOCK OPS (total)|Rate|Ops/Sec|metaDataOpType||USER|IO|True|False|
ops_driver|Operations (driver)|RENAME_QOS_DELAY|Average QoS delay for RENAME operations|RENAME QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|FILECLOSE_QOS_DELAY|Average QoS delay for FILECLOSE operations|FILECLOSE QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|RMXATTR_QOS_DELAY|Average QoS delay for RMXATTR operations|RMXATTR QoS Delay (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_driver|Operations (driver)|DIRECT_WRITE_SIZES|The number of O_DIRECT writes per each read size range|Direct Write Sizes (total)|Histogram|Writes|||USER|IO|True|True|Blocks
ops_driver|Operations (driver)|OPS|Total number of operations|OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops_driver|Operations (driver)|SYMLINK_LATENCY|Average latency of SYMLINK operations|SYMLINK Latency (per operation)|Measured|Microseconds|metaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_envoy|Operations (Envoy)|TOTAL_rejected_via_ip_detection_RQ|Total Rejected by IP Detection replies|Total Rejected by IP Detection replies (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|TOTAL_max_duration_RQ|Total Max Duration Reached replies|Total Max Duration replies (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|TOTAL_rx_reset_RQ|Total User RX Reset Connection replies|Total User RX Reset Connection replies (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|TOTAL_2xx_RQ|Total 2xx replies|Total 2xx replies (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|TOTAL_1xx_RQ|Total 1xx replies|Total 1xx replies (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|TOTAL_3xx_RQ|Total 3xx replies|Total 3xx replies (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|AVG_1xx_RQ|Average 1xx replies per second|Average 1xx replies per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|TOTAL_4xx_RQ|Total 4xx replies|Total 4xx replies (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|AVG_4xx_RQ|Average 4xx replies per second|Average 4xx replies per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|TOTAL_5xx_RQ|Total 5xx replies|Total 5xx replies (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|TOTAL_tx_reset_RQ|Total Envoy TX Reset Connection replies|Total Envoy TX Reset Connection replies (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|AVG_2xx_RQ|Average 2xx replies per second|Average 2xx replies per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|TOTAL_response_before_complete_RQ|Total S3 Responses before Complete replies|Total S3 Responses before Complete replies (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|AVG_5xx_RQ|Average 5xx replies per second|Average 5xx replies per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_envoy|Operations (Envoy)|AVG_3xx_RQ|Average 3xx replies per second|Average 3xx replies per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_nfs|Operations (NFS)|ACCESS_LATENCY|Average latency of ACCESS operations|ACCESS Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|REMOVE_LATENCY|Average latency of REMOVE operations|REMOVE Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|READ_LATENCY|Average latency of READ operations|Read Latency (per read)|Measured|Microseconds||READS|USER|IO|False|False|
ops_nfs|Operations (NFS)|CREATE_OPS|Number of CREATE operation per second|CREATE OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|MKNOD_LATENCY|Average latency of MKNOD operations|MKNOD Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|READDIR_OPS|Number of READDIR operation per second|READDIR OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|WRITE_LATENCY|Average latency of WRITE operations|Write Latency (per write)|Measured|Microseconds||WRITES|USER|IO|False|False|
ops_nfs|Operations (NFS)|THROUGHPUT|Number of byte read/writes per second|Throughput (total)|Rate|Bytes/Sec|||USER|IO|True|False|
ops_nfs|Operations (NFS)|STATFS_LATENCY|Average latency of STATFS operations|STATFS Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|READ_DURATION|The number of reads per completion duration|Read Duration (total)|Histogram|Reads|||USER|IO|True|True|uSecs
ops_nfs|Operations (NFS)|PATHCONF_LATENCY|Average latency of PATHCONF operations|PATHCONF Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|GETATTR_LATENCY|Average latency of GETATTR operations|GETATTR Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|SYMLINK_OPS|Number of SYMLINK operation per second|SYMLINK OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|SYMLINK_LATENCY|Average latency of SYMLINK operations|SYMLINK Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|LOOKUP_OPS|Number of LOOKUP operation per second|LOOKUP OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|READ_SIZES|NFS read sizes histogram|NFS read sizes (total)|Histogram|Reads|||USER|IO|True|True|Bytes
ops_nfs|Operations (NFS)|LINK_OPS|Number of LINK operation per second|LINK OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|WRITES|Number of write operations per second|Writes (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops_nfs|Operations (NFS)|COMMIT_OPS|Number of COMMIT operation per second|COMMIT OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|MKDIR_OPS|Number of MKDIR operation per second|MKDIR OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|WRITE_SIZES|NFS write sizes histogram|NFS write sizes (total)|Histogram|Writes|||USER|IO|True|True|Bytes
ops_nfs|Operations (NFS)|LOOKUP_LATENCY|Average latency of LOOKUP operations|LOOKUP Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|GETATTR_OPS|Number of GETATTR operation per second|GETATTR OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|READ_BYTES|Number of bytes read per second|Read Bytes (total)|Rate|Bytes/Sec|||USER|IO|True|False|
ops_nfs|Operations (NFS)|ACCESS_OPS|Number of ACCESS operation per second|ACCESS OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|SETATTR_LATENCY|Average latency of SETATTR operations|SETATTR Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|STATFS_OPS|Number of STATFS operation per second|STATFS OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|WRITE_BYTES|Number of byte writes per second|Write Bytes (total)|Rate|Bytes/Sec|||USER|IO|True|False|
ops_nfs|Operations (NFS)|COMMIT_LATENCY|Average latency of COMMIT operations|COMMIT Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|SETATTR_OPS|Number of SETATTR operation per second|SETATTR OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|READDIR_LATENCY|Average latency of READDIR operations|READDIR Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|RENAME_LATENCY|Average latency of RENAME operations|RENAME Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|LINK_LATENCY|Average latency of LINK operations|LINK Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|READLINK_OPS|Number of READLINK operation per second|READLINK OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|PATHCONF_OPS|Number of PATHCONF operation per second|PATHCONF OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|FSINFO_OPS|Number of FSINFO operation per second|FSINFO OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|FSINFO_LATENCY|Average latency of FSINFO operations|FSINFO Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|OPS|Total number of operations|OPS (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops_nfs|Operations (NFS)|MKNOD_OPS|Number of MKNOD operation per second|MKNOD OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|CREATE_LATENCY|Average latency of CREATE operations|CREATE Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|READLINK_LATENCY|Average latency of READLINK operations|READLINK Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfs|Operations (NFS)|REMOVE_OPS|Number of REMOVE operation per second|REMOVE OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|READS|Number of read operations per second|Reads (total)|Rate|Ops/Sec|||USER|IO|True|False|
ops_nfs|Operations (NFS)|RENAME_OPS|Number of RENAME operation per second|RENAME OPS (total)|Rate|Ops/Sec|nfsMetaDataOpType||USER|IO|True|False|
ops_nfs|Operations (NFS)|WRITE_DURATION|The number of writes per completion duration|Write Duration (total)|Histogram|Writes|||USER|IO|True|True|uSecs
ops_nfs|Operations (NFS)|MKDIR_LATENCY|Average latency of MKDIR operations|MKDIR Latency (per operation)|Measured|Microseconds|nfsMetaDataOpType|METADATA_OPS|USER|IO|False|False|
ops_nfsw|Operations (NFSw)|NFS4_SECINFO_NO_NAME_LATENCY|Average latency of NFS4_SECINFO_NO_NAME operations|NFS4_SECINFO_NO_NAME Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_PUTPUBFH_OPS|Number of NFS4_PUTPUBFH operation per second|NFS4_PUTPUBFH OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_OPEN_CONFIRM_LATENCY|Average latency of NFS4_OPEN_CONFIRM operations|NFS4_OPEN_CONFIRM Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_LOCKU_LATENCY|Average latency of NFS4_LOCKU operations|NFS4_LOCKU Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_SECINFO_NO_NAME_OPS|Number of NFS4_SECINFO_NO_NAME operation per second|NFS4_SECINFO_NO_NAME OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_CREATE_SESSION_OPS|Number of NFS4_CREATE_SESSION operation per second|NFS4_CREATE_SESSION OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_RESTOREFH_OPS|Number of NFS4_RESTOREFH operation per second|NFS4_RESTOREFH OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_DELEGPURGE_OPS|Number of NFS4_DELEGPURGE operation per second|NFS4_DELEGPURGE OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS3_CLIENT_READ_BYTES|Number of NFSV3 bytes read per second|Read Bytes (total)|Rate|Bytes/Sec|NfsClientId||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_SET_SSV_OPS|Number of NFS4_SET_SSV operation per second|NFS4_SET_SSV OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_CLIENT_READ_BYTES|Number of NFSV4 bytes read per second|Read Bytes (total)|Rate|Bytes/Sec|NfsClientId||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_SAVEFH_OPS|Number of NFS4_SAVEFH operation per second|NFS4_SAVEFH OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|OPS|Total number of operations|OPS (total)|Rate|Ops/Sec|nFSVersions||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS3_PATHCONF_LATENCY|Average latency of NFS3_PATHCONF operations|NFS3_PATHCONF Latency (per operation)|Measured|Microseconds|nFSv3Stats|NFS3_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|CREATE_LATENCY|Average latency of CREATE operations|CREATE Latency (per operation)|Measured|Microseconds|nFSVersions, nFSWBasicStats|BASIC_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|REMOVE_OPS|Number of REMOVE operation per second|REMOVE OPS (total)|Rate|Ops/Sec|nFSVersions, nFSWBasicStats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_FREE_STATEID_LATENCY|Average latency of NFS4_FREE_STATEID operations|NFS4_FREE_STATEID Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_RECLAIM_COMPLETE_LATENCY|Average latency of NFS4_RECLAIM_COMPLETE operations|NFS4_RECLAIM_COMPLETE Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_CREATE_SESSION_LATENCY|Average latency of NFS4_CREATE_SESSION operations|NFS4_CREATE_SESSION Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|READLINK_OPS|Number of READLINK operation per second|READLINK OPS (total)|Rate|Ops/Sec|nFSVersions, nFSWBasicStats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|RENAME_LATENCY|Average latency of RENAME operations|RENAME Latency (per operation)|Measured|Microseconds|nFSVersions, nFSWBasicStats|BASIC_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS3_MKNOD_LATENCY|Average latency of NFS3_MKNOD operations|NFS3_MKNOD Latency (per operation)|Measured|Microseconds|nFSv3Stats|NFS3_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_DESTROY_CLIENTID_OPS|Number of NFS4_DESTROY_CLIENTID operation per second|NFS4_DESTROY_CLIENTID OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_FREE_STATEID_OPS|Number of NFS4_FREE_STATEID operation per second|NFS4_FREE_STATEID OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_PUTFH_LATENCY|Average latency of NFS4_PUTFH operations|NFS4_PUTFH Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|ACCESS_OPS|Number of ACCESS operation per second|ACCESS OPS (total)|Rate|Ops/Sec|nFSVersions, nFSWBasicStats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|REMOVE_LATENCY|Average latency of REMOVE operations|REMOVE Latency (per operation)|Measured|Microseconds|nFSVersions, nFSWBasicStats|BASIC_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_NVERIFY_OPS|Number of NFS4_NVERIFY operation per second|NFS4_NVERIFY OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_LAYOUTGET_LATENCY|Average latency of NFS4_LAYOUTGET operations|NFS4_LAYOUTGET Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_LAYOUTCOMMIT_LATENCY|Average latency of NFS4_LAYOUTCOMMIT operations|NFS4_LAYOUTCOMMIT Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|THROUGHPUT|Number of byte read/writes per second|Throughput (total)|Rate|Bytes/Sec|nFSVersions||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_SAVEFH_LATENCY|Average latency of NFS4_SAVEFH operations|NFS4_SAVEFH Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_BACKCHANNEL_CTL_OPS|Number of NFS4_BACKCHANNEL_CTL operation per second|NFS4_BACKCHANNEL_CTL OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS3_SYMLINK_OPS|Number of NFS3_SYMLINK operation per second|NFS3_SYMLINK OPS (total)|Rate|Ops/Sec|nFSv3Stats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_NVERIFY_LATENCY|Average latency of NFS4_NVERIFY operations|NFS4_NVERIFY Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS3_FSINFO_LATENCY|Average latency of NFS3_FSINFO operations|NFS3_FSINFO Latency (per operation)|Measured|Microseconds|nFSv3Stats|NFS3_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_RENEW_LATENCY|Average latency of NFS4_RENEW operations|NFS4_RENEW Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_GETDEVICEINFO_OPS|Number of NFS4_GETDEVICEINFO operation per second|NFS4_GETDEVICEINFO OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS3_SYMLINK_LATENCY|Average latency of NFS3_SYMLINK operations|NFS3_SYMLINK Latency (per operation)|Measured|Microseconds|nFSv3Stats|NFS3_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_LAYOUTCOMMIT_OPS|Number of NFS4_LAYOUTCOMMIT operation per second|NFS4_LAYOUTCOMMIT OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|GETATTR_OPS|Number of GETATTR operation per second|GETATTR OPS (total)|Rate|Ops/Sec|nFSVersions, nFSWBasicStats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS3_PATHCONF_OPS|Number of NFS3_PATHCONF operation per second|NFS3_PATHCONF OPS (total)|Rate|Ops/Sec|nFSv3Stats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_BIND_CONN_TO_SESSION_LATENCY|Average latency of NFS4_BIND_CONN_TO_SESSION operations|NFS4_BIND_CONN_TO_SESSION Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_LAYOUTRETURN_OPS|Number of NFS4_LAYOUTRETURN operation per second|NFS4_LAYOUTRETURN OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_DELEGPURGE_LATENCY|Average latency of NFS4_DELEGPURGE operations|NFS4_DELEGPURGE Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_PUTFH_OPS|Number of NFS4_PUTFH operation per second|NFS4_PUTFH OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_RELEASE_LOCKOWNER_LATENCY|Average latency of NFS4_RELEASE_LOCKOWNER operations|NFS4_RELEASE_LOCKOWNER Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_LOCKU_OPS|Number of NFS4_LOCKU operation per second|NFS4_LOCKU OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|RENAME_OPS|Number of RENAME operation per second|RENAME OPS (total)|Rate|Ops/Sec|nFSVersions, nFSWBasicStats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_SEQUENCE_OPS|Number of NFS4_SEQUENCE operation per second|NFS4_SEQUENCE OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_DELEGRETURN_LATENCY|Average latency of NFS4_DELEGRETURN operations|NFS4_DELEGRETURN Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_SET_SSV_LATENCY|Average latency of NFS4_SET_SSV operations|NFS4_SET_SSV Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|WRITE_BYTES|Number of byte writes per second|Write Bytes (total)|Rate|Bytes/Sec|nFSVersions||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_CLOSE_OPS|Number of NFS4_CLOSE operation per second|NFS4_CLOSE OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_GETDEVICEINFO_LATENCY|Average latency of NFS4_GETDEVICEINFO operations|NFS4_GETDEVICEINFO Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_SETCLIENTID_LATENCY|Average latency of NFS4_SETCLIENTID operations|NFS4_SETCLIENTID Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|SETATTR_LATENCY|Average latency of SETATTR operations|SETATTR Latency (per operation)|Measured|Microseconds|nFSVersions, nFSWBasicStats|BASIC_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS3_MKNOD_OPS|Number of NFS3_MKNOD operation per second|NFS3_MKNOD OPS (total)|Rate|Ops/Sec|nFSv3Stats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_VERIFY_OPS|Number of NFS4_VERIFY operation per second|NFS4_VERIFY OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_BIND_CONN_TO_SESSION_OPS|Number of NFS4_BIND_CONN_TO_SESSION operation per second|NFS4_BIND_CONN_TO_SESSION OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_DESTROY_SESSION_OPS|Number of NFS4_DESTROY_SESSION operation per second|NFS4_DESTROY_SESSION OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_SECINFO_LATENCY|Average latency of NFS4_SECINFO operations|NFS4_SECINFO Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_GETFH_LATENCY|Average latency of NFS4_GETFH operations|NFS4_GETFH Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_RENEW_OPS|Number of NFS4_RENEW operation per second|NFS4_RENEW OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_LOCKT_OPS|Number of NFS4_LOCKT operation per second|NFS4_LOCKT OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_OPEN_OPS|Number of NFS4_OPEN operation per second|NFS4_OPEN OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_EXCHANGE_ID_LATENCY|Average latency of NFS4_EXCHANGE_ID operations|NFS4_EXCHANGE_ID Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_LOCK_LATENCY|Average latency of NFS4_LOCK operations|NFS4_LOCK Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_DESTROY_SESSION_LATENCY|Average latency of NFS4_DESTROY_SESSION operations|NFS4_DESTROY_SESSION Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_CLIENT_WRITE_BYTES|Number of NFSV4 bytes written per second|Write Bytes (total)|Rate|Bytes/Sec|NfsClientId||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|GETATTR_LATENCY|Average latency of GETATTR operations|GETATTR Latency (per operation)|Measured|Microseconds|nFSVersions, nFSWBasicStats|BASIC_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS3_MKDIR_LATENCY|Average latency of NFS3_MKDIR operations|NFS3_MKDIR Latency (per operation)|Measured|Microseconds|nFSv3Stats|NFS3_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS3_CLIENT_WRITE_BYTES|Number of NFSV3 bytes written per second|Write Bytes (total)|Rate|Bytes/Sec|NfsClientId||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|LOOKUP_OPS|Number of LOOKUP operation per second|LOOKUP OPS (total)|Rate|Ops/Sec|nFSVersions, nFSWBasicStats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_SETCLIENTID_CONFIRM_OPS|Number of NFS4_SETCLIENTID_CONFIRM operation per second|NFS4_SETCLIENTID_CONFIRM OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|COMMIT_OPS|Number of COMMIT operation per second|COMMIT OPS (total)|Rate|Ops/Sec|nFSVersions, nFSWBasicStats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_OPEN_DOWNGRADE_OPS|Number of NFS4_OPEN_DOWNGRADE operation per second|NFS4_OPEN_DOWNGRADE OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_LAYOUTRETURN_LATENCY|Average latency of NFS4_LAYOUTRETURN operations|NFS4_LAYOUTRETURN Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_TEST_STATEID_OPS|Number of NFS4_TEST_STATEID operation per second|NFS4_TEST_STATEID OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS3_STATFS_OPS|Number of NFS3_STATFS operation per second|NFS3_STATFS OPS (total)|Rate|Ops/Sec|nFSv3Stats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_OPENATTR_LATENCY|Average latency of NFS4_OPENATTR operations|NFS4_OPENATTR Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_SECINFO_OPS|Number of NFS4_SECINFO operation per second|NFS4_SECINFO OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_LOOKUPP_OPS|Number of NFS4_LOOKUPP operation per second|NFS4_LOOKUPP OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_LOCK_OPS|Number of NFS4_LOCK operation per second|NFS4_LOCK OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_GET_DIR_DELEGATION_LATENCY|Average latency of NFS4_GET_DIR_DELEGATION operations|NFS4_GET_DIR_DELEGATION Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_LAYOUTGET_OPS|Number of NFS4_LAYOUTGET operation per second|NFS4_LAYOUTGET OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_GETDEVICELIST_OPS|Number of NFS4_GETDEVICELIST operation per second|NFS4_GETDEVICELIST OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|READLINK_LATENCY|Average latency of READLINK operations|READLINK Latency (per operation)|Measured|Microseconds|nFSVersions, nFSWBasicStats|BASIC_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS3_FSINFO_OPS|Number of NFS3_FSINFO operation per second|NFS3_FSINFO OPS (total)|Rate|Ops/Sec|nFSv3Stats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|LINK_LATENCY|Average latency of LINK operations|LINK Latency (per operation)|Measured|Microseconds|nFSVersions, nFSWBasicStats|BASIC_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_LOOKUPP_LATENCY|Average latency of NFS4_LOOKUPP operations|NFS4_LOOKUPP Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|READDIR_LATENCY|Average latency of READDIR operations|READDIR Latency (per operation)|Measured|Microseconds|nFSVersions, nFSWBasicStats|BASIC_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|COMMIT_LATENCY|Average latency of COMMIT operations|COMMIT Latency (per operation)|Measured|Microseconds|nFSVersions, nFSWBasicStats|BASIC_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_EXCHANGE_ID_OPS|Number of NFS4_EXCHANGE_ID operation per second|NFS4_EXCHANGE_ID OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_LOCKT_LATENCY|Average latency of NFS4_LOCKT operations|NFS4_LOCKT Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS3_STATFS_LATENCY|Average latency of NFS3_STATFS operations|NFS3_STATFS Latency (per operation)|Measured|Microseconds|nFSv3Stats|NFS3_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_WANT_DELEGATION_LATENCY|Average latency of NFS4_WANT_DELEGATION operations|NFS4_WANT_DELEGATION Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_OPENATTR_OPS|Number of NFS4_OPENATTR operation per second|NFS4_OPENATTR OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|READDIR_OPS|Number of READDIR operation per second|READDIR OPS (total)|Rate|Ops/Sec|nFSVersions, nFSWBasicStats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_DELEGRETURN_OPS|Number of NFS4_DELEGRETURN operation per second|NFS4_DELEGRETURN OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_DESTROY_CLIENTID_LATENCY|Average latency of NFS4_DESTROY_CLIENTID operations|NFS4_DESTROY_CLIENTID Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|ACCESS_LATENCY|Average latency of ACCESS operations|ACCESS Latency (per operation)|Measured|Microseconds|nFSVersions, nFSWBasicStats|BASIC_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS3_MKDIR_OPS|Number of NFS3_MKDIR operation per second|NFS3_MKDIR OPS (total)|Rate|Ops/Sec|nFSv3Stats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_CLOSE_LATENCY|Average latency of NFS4_CLOSE operations|NFS4_CLOSE Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|SETATTR_OPS|Number of SETATTR operation per second|SETATTR OPS (total)|Rate|Ops/Sec|nFSVersions, nFSWBasicStats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_PUTROOTFH_LATENCY|Average latency of NFS4_PUTROOTFH operations|NFS4_PUTROOTFH Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_OPEN_DOWNGRADE_LATENCY|Average latency of NFS4_OPEN_DOWNGRADE operations|NFS4_OPEN_DOWNGRADE Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_OPEN_CONFIRM_OPS|Number of NFS4_OPEN_CONFIRM operation per second|NFS4_OPEN_CONFIRM OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|WRITE_OPS|Number of WRITE operation per second|WRITE OPS (total)|Rate|Ops/Sec|nFSVersions, nFSWBasicStats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|READ_OPS|Number of READ operation per second|READ OPS (total)|Rate|Ops/Sec|nFSVersions, nFSWBasicStats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_SETCLIENTID_OPS|Number of NFS4_SETCLIENTID operation per second|NFS4_SETCLIENTID OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_VERIFY_LATENCY|Average latency of NFS4_VERIFY operations|NFS4_VERIFY Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_RELEASE_LOCKOWNER_OPS|Number of NFS4_RELEASE_LOCKOWNER operation per second|NFS4_RELEASE_LOCKOWNER OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|READ_LATENCY|Average latency of READ operations|READ Latency (per operation)|Measured|Microseconds|nFSVersions, nFSWBasicStats|BASIC_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_WANT_DELEGATION_OPS|Number of NFS4_WANT_DELEGATION operation per second|NFS4_WANT_DELEGATION OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|CREATE_OPS|Number of CREATE operation per second|CREATE OPS (total)|Rate|Ops/Sec|nFSVersions, nFSWBasicStats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_BACKCHANNEL_CTL_LATENCY|Average latency of NFS4_BACKCHANNEL_CTL operations|NFS4_BACKCHANNEL_CTL Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|WRITE_LATENCY|Average latency of WRITE operations|WRITE Latency (per operation)|Measured|Microseconds|nFSVersions, nFSWBasicStats|BASIC_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_GETDEVICELIST_LATENCY|Average latency of NFS4_GETDEVICELIST operations|NFS4_GETDEVICELIST Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_RESTOREFH_LATENCY|Average latency of NFS4_RESTOREFH operations|NFS4_RESTOREFH Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_SETCLIENTID_CONFIRM_LATENCY|Average latency of NFS4_SETCLIENTID_CONFIRM operations|NFS4_SETCLIENTID_CONFIRM Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_SEQUENCE_LATENCY|Average latency of NFS4_SEQUENCE operations|NFS4_SEQUENCE Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_PUTROOTFH_OPS|Number of NFS4_PUTROOTFH operation per second|NFS4_PUTROOTFH OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_PUTPUBFH_LATENCY|Average latency of NFS4_PUTPUBFH operations|NFS4_PUTPUBFH Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|READ_BYTES|Number of bytes read per second|Read Bytes (total)|Rate|Bytes/Sec|nFSVersions||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_GETFH_OPS|Number of NFS4_GETFH operation per second|NFS4_GETFH OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_OPEN_LATENCY|Average latency of NFS4_OPEN operations|NFS4_OPEN Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|LINK_OPS|Number of LINK operation per second|LINK OPS (total)|Rate|Ops/Sec|nFSVersions, nFSWBasicStats||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_RECLAIM_COMPLETE_OPS|Number of NFS4_RECLAIM_COMPLETE operation per second|NFS4_RECLAIM_COMPLETE OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_nfsw|Operations (NFSw)|NFS4_TEST_STATEID_LATENCY|Average latency of NFS4_TEST_STATEID operations|NFS4_TEST_STATEID Latency (per operation)|Measured|Microseconds|nfsV4OpType|NFS4_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|LOOKUP_LATENCY|Average latency of LOOKUP operations|LOOKUP Latency (per operation)|Measured|Microseconds|nFSVersions, nFSWBasicStats|BASIC_OPS|USER|MANAGEMENT|False|False|
ops_nfsw|Operations (NFSw)|NFS4_GET_DIR_DELEGATION_OPS|Number of NFS4_GET_DIR_DELEGATION operation per second|NFS4_GET_DIR_DELEGATION OPS (total)|Rate|Ops/Sec|nfsV4OpType||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_BUCKET_LIST_OPS|Total bucket list operations per second|Total bucket list operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|AVG_PUT_OPS|Average put operations per second|Average put Operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_PUT_OBJECTPART_OPS|Total put objectpart operations|Total put objectpart operations (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_GET_BUCKET_ACL_OPS|Total get bucket acl operations per second|Total get bucket acl operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_BUCKET_CREATE_OPS|Total bucket create operations per second|Total bucket create operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|THROUGHPUT|Throughput|Throughput (total)|Rate|Bytes/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_MULTIPART_UPLOAD_LATENCY|Average latency of Multipart upload operations|Multipart upload latency (per multipartupload)|Measured|Microseconds||TOTAL_MULTIPART_UPLOAD_OPS|USER|MANAGEMENT|False|False|
ops_s3|Operations (S3)|TOTAL_GET_BUCKET_NOTIFICATION_OPS|Total get bucket notifications operations per second|Total get bucket notifications operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_PUT_LATENCY|Average latency of Put operations|Put latency (per put)|Measured|Microseconds||TOTAL_PUT_OPS|USER|MANAGEMENT|False|False|
ops_s3|Operations (S3)|TOTAL_COPY_OPS|Total Copy operations|Total copy Operations (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|AVG_PUT_OBJECTPART_OPS|Average put objectpart operations per second|Average put objectpart operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_BUCKET_DELETE_OPS|Total bucket delete operation per seconds|Total bucket delete Operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|AVG_GET_OPS|Average get operations per second|Average get Operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_PUT_BUCKET_ACL_OPS|Total put bucket acl operations per second|Total put bucket acl operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|READ_BYTES|Number of byte reads per second|Read Bytes per second (total)|Rate|Bytes/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_COPY_LATENCY|Average latency of Copy operations|Copy latency (per copy)|Measured|Microseconds||TOTAL_COPY_OPS|USER|MANAGEMENT|False|False|
ops_s3|Operations (S3)|TOTAL_PUT_OPS|Total put operations|Total put Operations (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_MULTIPART_UPLOAD_OPS|Total multipart upload operations|Total multipart upload operations (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|AVG_MULTIPART_UPLOAD_OPS|Average multipart upload operations per second|Average multipart upload operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|AVG_LIST_V1_OPS|Average list v1 operations per second|Average list (v1) Operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|AVG_DELETE_OPS|Average delete operations per second|Average delete Operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_LIST_V2_OPS|Total list v2 operations|Total list (v2) Operations (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_GET_OPS|Total Get operations|Total get Operations (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_LIST_V1_OPS|Total list v1 operations|Total list (v1) Operations (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_GET_LATENCY|Average latency of Get operations|Get latency (per get)|Measured|Microseconds||TOTAL_GET_OPS|USER|MANAGEMENT|False|False|
ops_s3|Operations (S3)|WRITE_BYTES|Number of byte writes per seconds|Write Bytes per second (total)|Rate|Bytes/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|AVG_COPY_OPS|Average copy operations per second|Average copy Operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|TOTAL_DELETE_OPS|Total delete operations|Total delete Operations (total)|Absolute|Ops|||USER|MANAGEMENT|True|False|
ops_s3|Operations (S3)|AVG_LIST_V2_OPS|Average list v2 operations per second|Average list (v2) Operations per second (total)|Rate|Ops/Sec|||USER|MANAGEMENT|True|False|
process|Assert failures|ASSERTION_FAILURES_STALL_AND_KILL_NODE|Assertion failures count with "STALL_AND_KILL_NODE" behaviour|Assertion failures count STALL_AND_KILL_NODE (total)|Absolute|Assertion failures|||WEKA|ANY|True|False|
process|Assert failures|ASSERTION_FAILURES_IGNORE|Assertion failures count with "IGNORE" behaviour|Assertion failures count IGNORE (total)|Absolute|Assertion failures|||WEKA|ANY|True|False|
process|Assert failures|ASSERTION_FAILURES_KILL_FIBER|Assertion failures count with "KILL_FIBER" behaviour|Assertion failures count KILL_FIBER (total)|Absolute|Assertion failures|||WEKA|ANY|True|False|
process|Assert failures|ASSERTION_FAILURES_THROW_EXCEPTION|Assertion failures count with "THROW_EXCEPTION" behaviour|Assertion failures count THROW_EXCEPTION (total)|Absolute|Assertion failures|||WEKA|ANY|True|False|
process|Assert failures|ASSERTION_FAILURES_STALL|Assertion failures count with "STALL" behaviour|Assertion failures count STALL (total)|Absolute|Assertion failures|||WEKA|ANY|True|False|
process|Assert failures|ASSERTION_FAILURES_KILL_NODE|Assertion failures count with "KILL_NODE" behaviour|Assertion failures count KILL_NODE (total)|Absolute|Assertion failures|||WEKA|ANY|True|False|
process|Assert failures|ASSERTION_FAILURES|Assertion failures count of all available types|Assertion failures total count (total)|Custom|Assertion failures|||WEKA|ANY|False|False|
process|Assert failures|ASSERTION_FAILURES_KILL_BUCKET|Assertion failures count with "KILL_BUCKET" behaviour|Assertion failures count KILL_BUCKET (total)|Absolute|Assertion failures|||WEKA|ANY|True|False|
process|Assert failures|ASSERTION_FAILURES_KILL_NODE_WITH_CORE_DUMP|Assertion failures count with "KILL_NODE_WITH_CORE_DUMP" behaviour|Assertion failures count KILL_NODE_WITH_CORE_DUMP (total)|Absolute|Assertion failures|||WEKA|ANY|True|False|
raft|RAFT|Configuration_LEADER_CHANGES|Changes of leader|Configuration Leader Changes (total)|Absolute|Changes|councilType||WEKA|ANY|True|False|
raft|RAFT|Invalid_LEADER_CHANGES|Changes of leader|Invalid Leader Changes (total)|Absolute|Changes|councilType||WEKA|ANY|True|False|
raft|RAFT|SYNCLOG_TIMEOUTS|The number of timeouts of syncing logs to a process|Sync-log Timeouts (total)|Absolute|Timeouts|peer_node_id||WEKA|ANY|True|False|
raft|RAFT|Bucket_LEADER_CHANGES|Changes of leader|Bucket Leader Changes (total)|Absolute|Changes|councilType||WEKA|ANY|True|False|
raft|RAFT|Configuration_REQUESTS_COMPLETED|Requests to leader completed successfully|Configuration Requests Completed (total)|Absolute|Requests|councilType||WEKA|ANY|True|False|
raft|RAFT|Test_REQUESTS_COMPLETED|Requests to leader completed successfully|Test Requests Completed (total)|Absolute|Requests|councilType||WEKA|ANY|True|False|
raft|RAFT|Invalid_REQUESTS_COMPLETED|Requests to leader completed successfully|Invalid Requests Completed (total)|Absolute|Requests|councilType||WEKA|ANY|True|False|
raft|RAFT|Bucket_REQUESTS_COMPLETED|Requests to leader completed successfully|Bucket Requests Completed (total)|Absolute|Requests|councilType||WEKA|ANY|True|False|
raft|RAFT|Test_LEADER_CHANGES|Changes of leader|Test Leader Changes (total)|Absolute|Changes|councilType||WEKA|ANY|True|False|
raid|RAID|RAID_COMMITTED_STRIPES|Number of stripes written|RAID Committed Stripes (total)|Accumulated|Stripes|||WEKA|IO|False|False|
raid|RAID|RAID_READ_BATCHES_PER_REQUEST_HISTOGRAM|Histogram of the number of batches of stripes read in a single request|Batches in single request (total)|Histogram|Request|||WEKA|IO|True|True|Batches
raid|RAID|WRONG_DRIVE_REFS|Reference segments written to wrong drive|Wrong drive refs (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
raid|RAID|RAID_CHUNKS_SHIFTED|Dirty chunks that shifted out|Placement chunks shifted out (total)|Absolute|Occurences|||WEKA|IO|True|False|
raid|RAID|RAID_READ_IOS|Raw read blocks performed by the RAID|RAID read IOs (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
raid|RAID|LONG_RPC_TIMEOUTS|Long RPC timeouts encountered|Leaks of IOs/RPCs are likely (total)|Absolute|Occurences|||WEKA|IO|True|False|
raid|RAID|RAID_BLOCKS_IN_PREPARED_STRIPE|Free blocks in prepared stripe|RAID Blocks in Prepared Stripe (total)|Histogram|Blocks|||WEKA|IO|True|True|Blocks
raid|RAID|RAID_CORRUPTION_RECOVERY_FAILURE|Corrupt data could not be recovered|RAID corruption recovery failed (total)|Absolute|Occurences|||WEKA|IO|True|False|
raid|RAID|RAID_COMPRESSED_BLOCKS_WRITTEN|Physical blocks written containing compressed data|Physical compressed block written (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
raid|RAID|IS_BLOCK_USED_USED_LATENCY|Average latency of handling an isBlockUsed of a used block|isBlockUsed returning used latency (per block)|Measured|Micros||IS_BLOCK_USED_USED|WEKA|IO|False|False|
raid|RAID|RAID_READ_FREE|Read Free|RAID reads of free blocks (total)|Absolute|Occurences|||WEKA|IO|True|False|
raid|RAID|RAID_STALE_WRITES_REPROTECTIONS|Stale write reprotections in read|RAID Stale Writes Reprotected (total)|Absolute|Occurences|||WEKA|IO|True|False|
raid|RAID|RAID_STALE_WRITES_DETECTED|Stale write detected in read|RAID Stale Writes Detected (total)|Absolute|Occurences|||WEKA|IO|True|False|
raid|RAID|RAID_READ_DEGRADED|Degraded mode reads|RAID Read Degraded (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
raid|RAID|RAID_READ_BLOCKS_STRIPE_HISTOGRAM|Histogram of the number of blocks read from a single stripe|Read from single stripe (total)|Histogram|Reads|||WEKA|IO|True|True|Blocks
raid|RAID|IS_BLOCK_USED_USED|Number of isBlockUsed returning used|IS_BLOCK_USED_USED (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
raid|RAID|IS_BLOCK_USED_FREE_LATENCY|Average latency of handling an isBlockUsed of a free block|isBlockUsed returning free latency (per block)|Measured|Micros||IS_BLOCK_USED_FREE|WEKA|IO|False|False|
raid|RAID|RAID_CHUNKS_CLEANED_BY_SHIFT|Dirty chunks cleaned by being shifted out|Placement dirty chunks shifted out (total)|Absolute|Occurences|||WEKA|IO|True|False|
raid|RAID|RAID_PLACEMENT_SWITCHES|Number of placement switches|RAID Placement Switches (total)|Accumulated|Switches|||WEKA|IO|False|False|
raid|RAID|RAID_READ_BLOCKS|Number of blocks read by the RAID|RAID read blocks (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
raid|RAID|WRONG_DRIVE_DELTAS|Delta segments written to wrong drive|Wrong drive deltas (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
raid|RAID|IS_BLOCK_USED_FREE|Number of isBlockUsed returning free|IS_BLOCK_USED_FREE (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
reactor|Reactor|BucketInvocationState_STRUCT_SIZE|Number of bytes in each struct of the BucketInvocationState pool|BucketInvocationState Struct Size (total)|Accumulated|Bytes|pool||WEKA|ANY|False|False|
reactor|Reactor|ObsGateway_USED|Number of structs in the ObsGateway pool which are currently being used|ObsGateway #Structs Used (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|rdmaNetworkBuffers_USED|Number of structs in the rdmaNetworkBuffers pool which are currently being used|rdmaNetworkBuffers #Structs Used (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|UploadFileInfo_CAPACITY|Number of data structures allocated to the UploadFileInfo pool|UploadFileInfo #Structs Capacity (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|TIMER_CALLBACKS|Current number of timer callbacks|Timer Callbacks (total)|Accumulated|Callbacks|||WEKA|ANY|False|False|
reactor|Reactor|NODE_RUN_TIME|Time process is running.|Running Time (total)|Accumulated|usecs|||WEKA|ANY|False|False|
reactor|Reactor|SSD_USED|Number of structs in the SSD pool which are currently being used|SSD #Structs Used (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|ObsGateway_STRUCT_SIZE|Number of bytes in each struct of the ObsGateway pool|ObsGateway Struct Size (total)|Accumulated|Bytes|pool||WEKA|ANY|False|False|
reactor|Reactor|SSD_CAPACITY|Number of data structures allocated to the SSD pool|SSD #Structs Capacity (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|BACKGROUND_FIBERS|Number of background fibers that are ready to run and eager to get CPU cycles|Background Fibers (total)|Accumulated|Fibers|||WEKA|ANY|False|False|
reactor|Reactor|SLEEPY_FIBERS|Number of SLEEPY fibers|SLEEPY fibers (total)|Accumulated|Fibers|||WEKA|IO|False|False|
reactor|Reactor|DeferredTask2_STRUCT_SIZE|Number of bytes in each struct of the DeferredTask2 pool|DeferredTask2 Struct Size (total)|Accumulated|Bytes|pool||WEKA|ANY|False|False|
reactor|Reactor|SCHEDULED_FIBERS|Number of current fibers that are ready to run and eager to get CPU cycles|Scheduled Fibers (total)|Accumulated|Fibers|||WEKA|ANY|False|False|
reactor|Reactor|IDLE_CALLBACK_INVOCATIONS|Number of background work invocations|Idle Callback Invocations (total)|Rate|Invocations/Sec|||WEKA|ANY|True|False|
reactor|Reactor|STEP_CYCLES|Histogram of time spent in a fiber|Step Cycles (total)|Histogram|Fiber steps|||WEKA|ANY|True|True|K Cycles
reactor|Reactor|EXCEPTIONS|Number of excpetions caught by the reactor|Exceptions (total)|Rate|Exceptions/Sec|||WEKA|ANY|True|False|
reactor|Reactor|NODE_HANG|The number of process (node) hangs per hang time range.|Node Hung Time (total)|Histogram|Number of hangs|||WEKA|IO|True|True|Milliseconds
reactor|Reactor|DeferredTask2_USED|Number of structs in the DeferredTask2 pool which are currently being used|DeferredTask2 #Structs Used (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|ObsBucketManagement_STRUCT_SIZE|Number of bytes in each struct of the ObsBucketManagement pool|ObsBucketManagement Struct Size (total)|Accumulated|Bytes|pool||WEKA|ANY|False|False|
reactor|Reactor|UploadFileInfo_USED|Number of structs in the UploadFileInfo pool which are currently being used|UploadFileInfo #Structs Used (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|NODE_CONTEXT_SWITCHES|Number of context switches.|Context Switches (total)|Accumulated|Switches|||WEKA|ANY|False|False|
reactor|Reactor|IDLE_CYCLES|Number of cycles spent in idle|Idle Cycles (total)|Rate|Cycles/Sec|||WEKA|IO|True|False|
reactor|Reactor|CYCLES_PER_SECOND|Number of cycles the cpu runs per second|Cycles per Second (total)|Accumulated|Cycles/Sec|||WEKA|IO|False|False|
reactor|Reactor|networkBuffers_CAPACITY|Number of data structures allocated to the networkBuffers pool|networkBuffers #Structs Capacity (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|networkBuffers_USED|Number of structs in the networkBuffers pool which are currently being used|networkBuffers #Structs Used (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|OUTRAGEOUS_HOGGERS|Number of hoggers taking excessive amount of time to run|Outrageous Hoggers (total)|Absolute|Invocations|||WEKA|ANY|True|False|
reactor|Reactor|BucketInvocationState_CAPACITY|Number of data structures allocated to the BucketInvocationState pool|BucketInvocationState #Structs Capacity (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|BACKGROUND_TIME|The percentage of the CPU time used for background operations|Background Time (average)|Custom|%|||WEKA|IO|False|False|
reactor|Reactor|rdmaNetworkBuffers_CAPACITY|Number of data structures allocated to the rdmaNetworkBuffers pool|rdmaNetworkBuffers #Structs Capacity (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|SSD_STRUCT_SIZE|Number of bytes in each struct of the SSD pool|SSD Struct Size (total)|Accumulated|Bytes|pool||WEKA|ANY|False|False|
reactor|Reactor|TimedCallback_STRUCT_SIZE|Number of bytes in each struct of the TimedCallback pool|TimedCallback Struct Size (total)|Accumulated|Bytes|pool||WEKA|ANY|False|False|
reactor|Reactor|TimedCallback_CAPACITY|Number of data structures allocated to the TimedCallback pool|TimedCallback #Structs Capacity (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|ObsGateway_CAPACITY|Number of data structures allocated to the ObsGateway pool|ObsGateway #Structs Capacity (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|BucketInvocationState_USED|Number of structs in the BucketInvocationState pool which are currently being used|BucketInvocationState #Structs Used (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|NODE_WAIT_TIME|Time process is waiting on waitqueue.|Waiting Time (total)|Accumulated|usecs|||WEKA|ANY|False|False|
reactor|Reactor|PENDING_FIBERS|Number of fibers pending for external events, such as a network packet or SSD response. Upon such an external event, they change state to scheduled fibers|Pending Fibers (total)|Accumulated|Fibers|||WEKA|ANY|False|False|
reactor|Reactor|DeferredTask2_CAPACITY|Number of data structures allocated to the DeferredTask2 pool|DeferredTask2 #Structs Capacity (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|NODE_RUN_PERCENTAGE|Percentage of time process is running|Running Percentage (percentage)|Custom|percentage|||WEKA|ANY|False|False|
reactor|Reactor|BACKGROUND_CYCLES|Number of cycles spent in background fibers|Background Cycles (total)|Rate|Cycles/Sec|||WEKA|IO|True|False|
reactor|Reactor|NODE_POLL_TIME|Time of scheduler stats polling.|Interval Time (total)|Accumulated|usecs|||WEKA|ANY|False|False|
reactor|Reactor|TOTAL_FIBERS_COUNT|Number of fibers|Total Fibers Count (total)|Absolute|Fibers|||WEKA|ANY|True|False|
reactor|Reactor|IDLE_TIME|The percentage of the CPU time not used for handling I/Os|Idle Time (average)|Custom|%|||WEKA|IO|False|False|
reactor|Reactor|ObsBucketManagement_CAPACITY|Number of data structures allocated to the ObsBucketManagement pool|ObsBucketManagement #Structs Capacity (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|DEFUNCT_FIBERS|Number of defunct buffers, which are just memory structures allocated for future fiber needs|Defunct Fibers (total)|Accumulated|Fibers|||WEKA|ANY|False|False|
reactor|Reactor|UploadFileInfo_STRUCT_SIZE|Number of bytes in each struct of the UploadFileInfo pool|UploadFileInfo Struct Size (total)|Accumulated|Bytes|pool||WEKA|ANY|False|False|
reactor|Reactor|TimedCallback_USED|Number of structs in the TimedCallback pool which are currently being used|TimedCallback #Structs Used (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|NODE_WAIT_PERCENTAGE|Percentage of time process is waiting on waitqueue|Waiting Percentage (percentage)|Custom|percentage|||WEKA|ANY|False|False|
reactor|Reactor|ObsBucketManagement_USED|Number of structs in the ObsBucketManagement pool which are currently being used|ObsBucketManagement #Structs Used (total)|Accumulated|Structs|pool||WEKA|ANY|False|False|
reactor|Reactor|SLEEPY_RPC_SERVER_FIBERS|Number of SLEEPY RPC server fibers|SLEEPY RPC server fibers (total)|Accumulated|Sleepy fiber detections|||WEKA|IO|False|False|
rpc|RPC|CLIENT_RPC_CALLS|Number of all priorities of RPC calls|Client RPC Calls (both priorities) (RPC call)|Rate|RPC/Sec|method||WEKA|IO|True|False|
rpc|RPC|SERVER_RPC_CALLS_UPGRADED|Number of server-upgraded RPC calls|Server upgraded RPC Calls (total)|Rate|RPC/Sec|method||WEKA|IO|True|False|
rpc|RPC|CLIENT_RECEIVED_RESPONSES|Number of responses received by the client|Client Received Responses (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|SERVER_SENT_EXCEPTIONS|Number of exceptions sent by the server as a response|Server Sent Exceptions (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|SERVER_SENT_RESPONSES|Number of responses the server sent|Server Sent Responses (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|CLIENT_ROUNDTRIP_AVG_NORM|Roundtrip average of client normal priority RPC calls|Client Roundtrip AVG (normal priotity) (per RPC call)|Measured|Microseconds|method|CLIENT_RPC_CALLS_NORM|WEKA|IO|False|False|
rpc|RPC|CLIENT_MISSING_ENCRYPTION_KEY|Number of times client was missing an encryption key|Client Missing Encryption Key (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|CLIENT_RPC_CALLS_DOWNGRADED|Number of client-downgraded RPC calls|Client downgraded RPC Calls (total)|Rate|RPC/Sec|method||WEKA|IO|True|False|
rpc|RPC|SERVER_UNENCRYPTED_REFUSALS|Number of requests refused due to missing encryption at the server|Server Unencrypted Requests Refusals (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|SERVER_REJECTS|Number of times the server rejected a request|Server Rejects (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|SERVER_ENCRYPTION_AUTH_FAILURES|Number of encryption authentication failures at the server|Server Authentication Failures (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|CLIENT_ROUNDTRIP_AVG|Roundtrip average of client normal and low priority RPC calls|Client Roundtrip AVG (both priorities) (per RPC call)|Measured|Microseconds|method|CLIENT_RPC_CALLS_LOW[<method>] + CLIENT_RPC_CALLS_NORM[<method>]|WEKA|IO|False|False|
rpc|RPC|SERVER_MISSING_ENCRYPTION_KEY|Number of requests missing encryption key at the server|Server Missing Encryption Key (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|SERVER_RPC_CALLS|Number of server RPC calls|Server RPC Calls (total)|Rate|RPC/Sec|method||WEKA|IO|True|False|
rpc|RPC|CLIENT_DROPPED_RESPONSES|Number of responses dropped by the client|Client Dropped Responses (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|FIRST_RESULTS|Number of first results per second|First Results (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
rpc|RPC|CLIENT_RECEIVED_TIMEOUTS|Number of timeouts experienced by the client|Client Received Timeouts (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|SERVER_DROPPED_REQUESTS|Number of requests dropped by the server|Server Dropped Requests (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|MBUF_LIMITED_SLOWDOWN|Number of RPCs slow down due to low MBuf reserves|MBuf limited slowdowns (total)|Rate|Ops/Sec|||WEKA|IO|True|False|
rpc|RPC|RPC_ENCRYPTION_SETUP_FAILURES|Number of encryptiuon key setup failures|Encryption Key Setup Failures (total)|Absolute|Failures|||WEKA|ANY|True|False|
rpc|RPC|CLIENT_ENCRYPTION_AUTH_FAILURES|Number of authentication failures by the client|Client Authentication Failures (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|CLIENT_RECEIVED_EXCEPTIONS|Number of exceptions received by the client|Client Received Exceptions (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|TIME_TO_FIRST_RESULT|Average latency to the first result of a MultiCall|Time to first result (per Result)|Measured|Microseconds||FIRST_RESULTS|WEKA|IO|False|False|
rpc|RPC|CLIENT_SENT_REQUESTS|Number of requests sent by the client|Client Sent Requests (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|SERVER_ABORTS|Number of server received aborts|Server Aborts (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|SERVER_PROCESSING_TIME|Histogram of the time it took the server to process a request|Server Processing Time (total)|Histogram|RPCs|method||WEKA|ANY|True|True|Microseconds
rpc|RPC|SERVER_PROCESSING_AVG|Average time to process server RPC calls|Server Processing AVG (per RPC call)|Measured|Microseconds|method|SERVER_PROCESSING_TIME[<method>][..]|WEKA|IO|False|False|
rpc|RPC|MBUF_LIMITED_SLEEP|Number of times wait due to low MBuf reserves|MBuf limited sleeps (total)|Rate|Actions/Sec|||WEKA|IO|True|False|
rpc|RPC|CLIENT_CANCELED_REQUESTS|Number of requests cancelled by the client|Client Canceled Requests (total)|Rate|Calls/Sec|||WEKA|ANY|True|False|
rpc|RPC|CLIENT_RPC_CALLS_LOW|Number of low priority RPC calls|Client RPC Calls (low priority) (total)|Rate|RPC/Sec|method||WEKA|IO|True|False|
rpc|RPC|CLIENT_ROUNDTRIP_AVG_LOW|Roundtrip average of client low-priority RPC calls|Client Roundtrip AVG (low priority) (per RPC call)|Measured|Microseconds|method|CLIENT_RPC_CALLS_LOW|WEKA|IO|False|False|
rpc|RPC|CLIENT_RPC_CALLS_NORM|Number of normal priority RPC calls|Client RPC Calls (normal priority) (total)|Rate|RPC/Sec|method||WEKA|IO|True|False|
scrubber|Scrubber|SFU_CHECK_FREE|Number of blocks that were detected as false-used and freed|Marked used but was actually free (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|WRITE_BATCH_TARGET_BLOCKS|Number of target blocks to write in batch|RAID Target Blocks to write each batch (total)|Histogram|Batches|||WEKA|IO|True|True|Blocks
scrubber|Scrubber|PLACEMENT_SELECTION_LATENCY|Average latency of scrubbed placement selection|PlacementSelectionTime (per selections)|Measured|Micros||PLACEMENT_SELECTIONS|WEKA|IO|False|False|
scrubber|Scrubber|SFU_CHECKS|Number of blocks that were scrubbed-false-used|Number of blocks we checked if are false-used (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SFU_CHECK_SECONDARY|Number of blocks that were detected as secondary|Secondary marked used (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SCRUB_FALSE_USED_WAS_UNPROTECTED|Number of blocks that were false marked used and unprotected|Number of false-used blocks that were unprotected (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|FALSE_USED_EXTRA_NOTIFIED|Number of blocks that were notified as used by the mark-extra-used mechanism|Number of blocks we marked-extra-used (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|STRIPE_DATA_IS_BLOCK_USED|Number of isBlockUsed during stripe verification|STRIPE_DATA_IS_BLOCK_USED (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SFU_FREE_STRIPES|Number of free stripes that were scrubbed-false-used|SFU_FREE_STRIPES (total)|Rate|Stripes/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|WRITE_BATCH_SOURCE_BLOCKS|Number of source blocks to write in batch|RAID Source Blocks to write each batch (total)|Histogram|Batches|||WEKA|IO|True|True|Blocks
scrubber|Scrubber|UPDATE_PLACEMENT_INFO_LATENCY|Average latency of updating the placement info quorum|UpdatePlacementInfoTime (per updatePlacementInfo)|Measured|Micros||UPDATE_PLACEMENT_INFO|WEKA|IO|False|False|
scrubber|Scrubber|UPDATE_PLACEMENT_INFO|Number of times we ran updatePlacementInfo|UpdatePlacementInfo count (total)|Rate|Occurences/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SCRUB_FALSE_USED_FAILED|Number of placements we failed to fully scrub-false-used|Failed to scrub-false-used on placements (total)|Rate|Occurences/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SCRUB_FALSE_USED_FAILED_READS|Number of blocks that we failed to read for scrub-false-used|Number of blocks that we failed to read for scrub-false-used (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|NUM_SCRUBBER_DISCARD_INTERMEDIATES|Number of times we discarded all intermediate scrubber work|IntermediateDiscards (total)|Rate|Occurences/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|NUM_SMW_DISCARDS|Number of times we discarded scrubber SMW work|SMWDiscards (total)|Rate|Occurences/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|RELOCATED_BLOCKS|Number of blocks that were relocated for eviction|Relocated blocks (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|INTERRUPTS|Number of scrubs that were interrupted|Interrupts (total)|Rate|Occurences/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SCRUB_FALSE_USED_PLACEMENTS|Number of placements we finished scrub-false-used|Finished scrub-false-used on placements (total)|Rate|Occurences/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|DEGRADED_READS|Number of degraded reads for scrubbing|Degraded reads (total)|Rate|Requests/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SCAN_LIKELY_LEAKED_BLOCKS|Number of free blocks encountered during scan that were marked as KnownUsed in the RAID|Likely Leaked Blocks (total)|Absolute|Occurences|||WEKA|IO|True|False|
scrubber|Scrubber|NUM_INVENTED_STRIPES_DISCARD_BLOCKS|Number of blocks that were discarded due to invented stripes|InventedDiscardBlocks (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|NETWORK_BUDGET_WAIT_LATENCY|Average latency of waiting for our network budget|NetworkBudgetWaitTime (per waits)|Measured|Micros||NETWORK_BUDGET_WAITS|WEKA|IO|False|False|
scrubber|Scrubber|RETRUSTED_UNPROTECTED_DIRTY_BLOCKS|Number of dirty blocks that ScrubMissingWrites retrusted because they were unprotected|Unprotected blocks retrusted by scrubber (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|READ_BLOCKS_LATENCY|Average latency of read blocks|Latency of reading all of a batch's blocks (per block)|Measured|Micros||READS_CALLED|WEKA|IO|False|False|
scrubber|Scrubber|REWRITTEN_DIRTY_BLOCKS|Number of dirty blocks that ScrubMissingWrites rewrote to clean them|Blocks cleaned by scrubber (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|WRITES_CALLED|Number of blocks that were written|Written blocks (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SCRUB_PREPARATION_FAILED|Number of times we failed to prepare() a task and aborted scrub of placement|Scrubber task preparation failed (total)|Rate|Occurences/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|NUM_COPY_DISCARDED_BLOCKS|Number of copied blocks that were discarded|Copied blocks (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SOURCE_READS|Number of source/committed superset blocks directly read by the scrubber|Scrubber read source blocks (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|BLOCK_CONSISTENCY_CHECKS|Number of blocks that were checked for consistency against their block-used-state|Number of blocks we checked are consistently used/free and have a correct checksum if used (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SFU_USED_STRIPES|Number of used stripes that were scrubbed-false-used|SFU_USED_STRIPES (total)|Rate|Stripes/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|NUM_SMW_DISCARDED_BLOCKS|Number of SMW'd blocks that were discarded|Discarded blocks (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|READS_CALLED|Number of blocks that were read|Read blocks (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SFU_CHECK_USED_CKSUM_ERR|Number of blocks that were detected as used with checksum error|Marked used, content mismatched expected (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|RELOCATE_BLOCKS_LATENCY|Average latency of relocating blocks|RelocateBlocksLatency (per block)|Measured|Micros||RELOCATED_BLOCKS|WEKA|IO|False|False|
scrubber|Scrubber|SCRUB_IN_FLIGHT_CORRUPTION_DETECTED|Number of in-flight corruptions detected when scrubbing|In-flight corruption detected by scrubber (total)|Absolute|Occurences|||WEKA|IO|True|False|
scrubber|Scrubber|WRITE_BLOCKS_LATENCY|Average latency of writing blocks|Latency of writing all of a batch's blocks (per block)|Measured|Micros||WRITES_CALLED|WEKA|IO|False|False|
scrubber|Scrubber|NOT_REALLY_DIRTY_BLOCKS|Number of marked dirty blocks that ScrubMissingWrites found were actually clean|Dirty blocks that had the right content (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|NUM_COPY_DISCARDS|Number of times we discarded scrubber copy work|CopyDiscards (total)|Rate|Occurences/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|CLEANED_CHUNKS|Number of chunks that were cleaned by the scrubber|Chunks cleaned by scrubber (total)|Rate|Chunks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SCRUB_BATCHES_LATENCY|Average latency of scrub batches|ScrubBatchesTime (per batches)|Measured|Millis||SCRUB_BATCHES|WEKA|IO|False|False|
scrubber|Scrubber|WONT_CLEAN_COPYING|Number of actually dirty blocks that ScrubMissingWrites refused to clean because they will be moved to target anyway|Dirty blocks on copying disks (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SFU_CHECK_USED|Number of blocks that were detected as used|Correctly marked used (total)|Rate|Blocks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|BLOCK_CONSISTENCY_CHECK_LATENCY|Average latency of checking block consistency|BlockConsistencyCheckTime (per block)|Measured|Micros||BLOCK_CONSISTENCY_CHECKS|WEKA|IO|False|False|
scrubber|Scrubber|READ_BATCH_SOURCE_BLOCKS|Number of source blocks read per batch|RAID Source Blocks to read each batch (total)|Histogram|Batches|||WEKA|IO|True|True|Blocks
scrubber|Scrubber|TARGET_COPIED_CHUNKS|Number of chunks that were copied to target by the scrubber|Chunks copied by scrubber (total)|Rate|Chunks/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|SFU_USED_STRIPE_LATENCY|Average latency of handling a read of a used stripe|False used handle read used stripe latency (per stripe)|Measured|Micros||SFU_USED_STRIPES|WEKA|IO|False|False|
scrubber|Scrubber|SFU_FREE_STRIPE_LATENCY|Average latency of handling a read of a free stripe|False used handle read free stripe latency (per stripe)|Measured|Micros||SFU_FREE_STRIPES|WEKA|IO|False|False|
scrubber|Scrubber|FALSE_USED_CHECK_LATENCY|Average latency of checking false used per block|FalseUsedCheckTime (per block)|Measured|Micros||SFU_CHECKS|WEKA|IO|False|False|
scrubber|Scrubber|NUM_INVENTED_STRIPES_DISCARDS|Number of times we discarded all scrubber work due to invented stripes|InventedDiscards (total)|Rate|Occurences/Sec|||WEKA|IO|True|False|
scrubber|Scrubber|STRIPE_DATA_IS_BLOCK_USED_LATENCY|Average latency of isBlockUsed during stripe verification|STRIPE_DATA_IS_BLOCK_USED_LATENCY (per block)|Measured|Micros||STRIPE_DATA_IS_BLOCK_USED|WEKA|IO|False|False|
squelch|Squelch|BLOCKS_PER_DESQUELCH|Number of squelch blocks per desquelch|Blocks per Desquelch (total)|Histogram|Desquelches|||WEKA|IO|True|True|Blocks
squelch|Squelch|HASH_SQUELCH_BLOCKS_READ|Number of squelch blocks desquelched|HASH Squelch Blocks Read (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
squelch|Squelch|ODL_DESQUELCHES_NUM|Number of desquelches|ODL Desquelches (total)|Absolute|Times|blockType||WEKA|IO|True|False|
squelch|Squelch|ODL_SQUELCH_BLOCKS_READ|Number of squelch blocks desquelched|ODL Squelch Blocks Read (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
squelch|Squelch|SPATIAL_SQUELCH_SQUELCH_BLOCKS_READ|Number of squelch blocks desquelched|SPATIAL_SQUELCH Squelch Blocks Read (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
squelch|Squelch|HASH_DESQUELCHES_NUM|Number of desquelches|HASH Desquelches (total)|Absolute|Times|blockType||WEKA|IO|True|False|
squelch|Squelch|SUPERBLOCK_SQUELCH_BLOCKS_READ|Number of squelch blocks desquelched|SUPERBLOCK Squelch Blocks Read (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
squelch|Squelch|MAX_TEMPORAL_SQUELCH_ITEMS_IN_BUCKET|Number temporal squelch items in bucket|Temporal Squelch Items In Bucket (total)|Absolute|Squelch items|||WEKA|IO|True|False|
squelch|Squelch|EXTENT_DESQUELCHES_NUM|Number of desquelches|EXTENT Desquelches (total)|Absolute|Times|blockType||WEKA|IO|True|False|
squelch|Squelch|EXTENT_SQUELCH_BLOCKS_READ|Number of squelch blocks desquelched|EXTENT Squelch Blocks Read (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
squelch|Squelch|ODL_PAYLOAD_SQUELCH_BLOCKS_READ|Number of squelch blocks desquelched|ODL_PAYLOAD Squelch Blocks Read (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
squelch|Squelch|REGISTRY_L1_DESQUELCHES_NUM|Number of desquelches|REGISTRY_L1 Desquelches (total)|Absolute|Times|blockType||WEKA|IO|True|False|
squelch|Squelch|INODE_DESQUELCHES_NUM|Number of desquelches|INODE Desquelches (total)|Absolute|Times|blockType||WEKA|IO|True|False|
squelch|Squelch|TEMPORAL_SQUELCH_DESQUELCHES_NUM|Number of desquelches|TEMPORAL_SQUELCH Desquelches (total)|Absolute|Times|blockType||WEKA|IO|True|False|
squelch|Squelch|SUPERBLOCK_DESQUELCHES_NUM|Number of desquelches|SUPERBLOCK Desquelches (total)|Absolute|Times|blockType||WEKA|IO|True|False|
squelch|Squelch|JOURNAL_DESQUELCHES_NUM|Number of desquelches|JOURNAL Desquelches (total)|Absolute|Times|blockType||WEKA|IO|True|False|
squelch|Squelch|SPATIAL_SQUELCH_DESQUELCHES_NUM|Number of desquelches|SPATIAL_SQUELCH Desquelches (total)|Absolute|Times|blockType||WEKA|IO|True|False|
squelch|Squelch|REGISTRY_L2_SQUELCH_BLOCKS_READ|Number of squelch blocks desquelched|REGISTRY_L2 Squelch Blocks Read (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
squelch|Squelch|REGISTRY_L1_SQUELCH_BLOCKS_READ|Number of squelch blocks desquelched|REGISTRY_L1 Squelch Blocks Read (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
squelch|Squelch|JOURNAL_SQUELCH_BLOCKS_READ|Number of squelch blocks desquelched|JOURNAL Squelch Blocks Read (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
squelch|Squelch|TEMPORAL_SQUELCH_SQUELCH_BLOCKS_READ|Number of squelch blocks desquelched|TEMPORAL_SQUELCH Squelch Blocks Read (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
squelch|Squelch|MAX_BLOCKS_WITH_TEMPORAL_SQUELCH_ITEMS_IN_BUCKET|Number of block with temporal squelch items in bucket|Bucket Blocks with Temporal Squelch Items (total)|Absolute|Blocks|||WEKA|IO|True|False|
squelch|Squelch|INODE_SQUELCH_BLOCKS_READ|Number of squelch blocks desquelched|INODE Squelch Blocks Read (total)|Absolute|Blocks|blockType||WEKA|IO|True|False|
squelch|Squelch|REGISTRY_L2_DESQUELCHES_NUM|Number of desquelches|REGISTRY_L2 Desquelches (total)|Absolute|Times|blockType||WEKA|IO|True|False|
squelch|Squelch|ODL_PAYLOAD_DESQUELCHES_NUM|Number of desquelches|ODL_PAYLOAD Desquelches (total)|Absolute|Times|blockType||WEKA|IO|True|False|
ssd|SSD|DRIVE_REMAINING_IOS|Number of requests still in the drive after a pump|# Left Requests (total)|Histogram|Pumps|||WEKA|IO|True|True|IO
ssd|SSD|DRIVE_MEDIA_BLOCKS_READ|Blocks read from the SSD media|Blocks Read from SSD media (total)|Rate|Blocks/Sec|disk||WEKA|IO|True|False|
ssd|SSD|SSD_CHUNK_ALLOCS_TRIMMED|Number of chunk allocations from the trimmed queue|Trimmed Chunk Allocations (total)|Absolute|Chunks|disk||WEKA|IO|True|False|
ssd|SSD|SSDS_IOS|IOs performed on the SSD service|Disks IOs (total)|Rate|IO/Sec|disk||WEKA|IO|True|False|
ssd|SSD|SSD_CHUNK_ALLOCS|Number of chunk allocations|Chunks Allocated (total)|Absolute|Chunks|disk||WEKA|IO|True|False|
ssd|SSD|DRIVE_MEDIA_ERRORS|SSD Media Errors|SSD Media Errors (total)|Rate|IO/Sec|disk||USER|IO|True|False|
ssd|SSD|SSD_WRITE_LATENCY|Latency of writes to the SSD service|SSD Write Latency (per write)|Measured|Microseconds|disk|SSD_WRITES - SSD_WRITE_ERRORS|USER|IO|False|False|
ssd|SSD|DRIVE_PENDING_IOS|The number of IOs waiting to start executing during sampling|Disks Queue Num Pending (average)|Accumulated|IOs|disk||WEKA|IO|False|False|
ssd|SSD|SSD_E2E_BAD_CSUM|End-to-End checksum failures|E2E Checksum error (total)|Rate|IO/Sec|||WEKA|IO|True|False|
ssd|SSD|DRIVE_ACTIVE_IOS|The number of in-flight IO against the SSD during sampling|Disks Queue Length (average)|Accumulated|IOs|disk||WEKA|IO|False|False|
ssd|SSD|DRIVE_STALLS|Number of overlapping IOs stalling progress|Disks IOs (total)|Rate|IO/Sec|||WEKA|IO|True|False|
ssd|SSD|CLEAN_CHUNK_SKIPPED|Number of clean chunks skips|Clean Chunks Skipped (total)|Absolute|Chunks|||WEKA|IO|True|False|
ssd|SSD|SSDS_IO_ERRORS|IO errors on the SSD service|Disks IO Errors (total)|Rate|Blocks/Sec|disk||WEKA|IO|True|False|
ssd|SSD|DRIVE_IDLE_TIME|Percentage of the CPU time not used for handling I/Os|Idle Time (average)|Custom|%|disk||WEKA|IO|False|False|
ssd|SSD|SSD_BLOCKS_READ|Number of blocks read from the SSD service|SSD Blocks Read (total)|Rate|Blocks/Sec|disk||USER|IO|True|False|
ssd|SSD|DRIVE_LOAD|Drive Load at sampling time|Drive Load (average)|Accumulated|Load|disk||WEKA|IO|False|False|
ssd|SSD|DRIVE_COMPLETED_OVER_COUNT|Drive completed count > 1 detected|Drive completed count (total)|Absolute|Occurrences|||USER|IO|True|False|
ssd|SSD|DRIVE_READ_OPS|Drive Read Operations|Drive Read Operations (total)|Rate|IO/Sec|disk||USER|IO|True|False|
ssd|SSD|NVKV_CHUNK_OUT_OF_SPACE|Number of failed attempts to allocate a stripe in an NVKV chunk|NVKV stripe allocation attempts (total)|Rate|Attempts/Sec|||WEKA|IO|True|False|
ssd|SSD|DRIVE_AER_RECEIVED|Number of AER reports|# AER reports (total)|Absolute|reports|disk||WEKA|IO|True|False|
ssd|SSD|SSD_SCRATCH_BUFFERS_USED|Number of scratch blocks used|Scratch buffers used (total)|Absolute|Blocks|||WEKA|IO|True|False|
ssd|SSD|DRIVE_WRITE_OPS|Drive Write Operations|Drive Write Operations (total)|Rate|IO/Sec|disk||USER|IO|True|False|
ssd|SSD|DRIVE_SSD_PUMPS|Number of drive pumps that resulted in the data flow from/to drive|Number of SSD pump that did something (total)|Rate|Pump/Sec|||WEKA|IO|True|False|
ssd|SSD|SSD_CHUNK_ALLOCS_UNTRIMMED|Number of chunk allocations from the untrimmed queue|Untrimmed Chunk Allocations (total)|Absolute|Chunks|disk||WEKA|IO|True|False|
ssd|SSD|DRIVE_WRITE_RATIO_PER_SSD_WRITE|Drive Write OPS Per SSD Request|Drive Write per SSD write (IO)|Custom|Ratio|disk||USER|IO|False|False|
ssd|SSD|DRIVE_MEDIA_BLOCKS_WRITE|Blocks written to the SSD media|Blocks Written to SSD media  (total)|Rate|Blocks/Sec|disk||WEKA|IO|True|False|
ssd|SSD|SSD_CHUNK_FREE_UNTRIMMED|Number of free untrimmed chunks|# Free Untrimmed Chunks (total)|Accumulated|Chunks|disk||WEKA|IO|False|False|
ssd|SSD|DRIVE_PUMP_LATENCY|Latency between SSD pumps|Latency between SSD pumps (per Pump)|Measured|Microseconds||DRIVE_SSD_PUMPS|WEKA|IO|False|False|
ssd|SSD|DRIVE_PUMPED_IOS|Number of requests returned in a pump|# Returned Requests (total)|Histogram|Pumps|||WEKA|IO|True|True|IO
ssd|SSD|SSD_READ_LATENCY|Avg. latency of read requests from the SSD service|SSD Read Latency (per read)|Measured|Microseconds|disk|SSD_READ_REQS - SSD_READ_ERRORS|USER|IO|False|False|
ssd|SSD|DRIVE_READ_LATENCY|Drive Read Execution Latency|Drive Read Latency (per IO)|Measured|Microseconds|disk|DRIVE_READ_OPS|USER|IO|False|False|
ssd|SSD|SSD_READ_REQS|Number of read requests from the SSD service|SSD Reads (total)|Rate|IO/Sec|disk||USER|IO|True|False|
ssd|SSD|SSD_CHUNK_TRIMS|Number of trims performed|# Trims Performed (total)|Absolute|Chunks|disk||WEKA|IO|True|False|
ssd|SSD|SSD_WRITES_REQS_LARGE_NORMAL|Number of large normal priority write requests to the SSD service|SSD Large Normal Priority Writes (total)|Rate|IO/Sec|disk||WEKA|IO|True|False|
ssd|SSD|DRIVE_NON_MEDIA_ERRORS|SSD Non-Media Errors|SSD Non-Media Errors (total)|Rate|IO/Sec|disk||USER|IO|True|False|
ssd|SSD|SSD_WRITE_ERRORS|Errors in writing blocks to the SSD service|SSD Write Errors (total)|Rate|Blocks/Sec|disk||USER|IO|True|False|
ssd|SSD|DRIVE_IO_OVERLAPPED|Number of overlapping IOs|Drive IOs overlapped (stall) (total)|Accumulated|Operations|||WEKA|IO|False|False|
ssd|SSD|NVKV_OUT_OF_SUPERBLOCK_ENTRIES|Number of failed attempts to allocate a superblock NVKV entry|NVKV superblock entry allocation attempts (total)|Rate|Attempts/Sec|||WEKA|IO|True|False|
ssd|SSD|DRIVE_PUMPS_DELAYED|Number of Drive pumps that got delayed|Drive Pumps Delayed (total)|Rate|Operations/Sec|||WEKA|IO|True|False|
ssd|SSD|DRIVE_UTILIZATION|Percentage of time the drive had an active IO submitted to it|Drive Utilization (average)|Custom|%|disk||USER|IO|False|False|
ssd|SSD|SSD_CHUNK_FREE_TRIMMED|Number of free trimmed chunks|# Free Trimmed Chunks (total)|Accumulated|Chunks|disk||WEKA|IO|False|False|
ssd|SSD|DRIVE_IDLE_CYCLES|Number of cycles spent in idle|Idle Cycles (total)|Rate|Cycles/Sec|disk||WEKA|IO|True|False|
ssd|SSD|SSD_READ_ERRORS|Errors in reading blocks from the SSD service|SSD Read Errors (total)|Rate|Blocks/Sec|disk||USER|IO|True|False|
ssd|SSD|SSD_TRIM_TIMEOUTS|Number of trim timeouts|# Trim Timeouts (total)|Accumulated|Timeouts|||WEKA|IO|False|False|
ssd|SSD|SSD_READ_REQS_LARGE_NORMAL|Number of large normal read requests from the SSD service|SSD Large Normal Reads (total)|Rate|IO/Sec|disk||WEKA|IO|True|False|
ssd|SSD|DRIVE_READ_RATIO_PER_SSD_READ|Drive Read OPS Per SSD Request|Drive Read per SSD read (IO)|Custom|Ratio|disk||USER|IO|False|False|
ssd|SSD|DRIVE_PUMPS_SEVERELY_DELAYED|Number of Drive pumps that got severely delayed|Drive Pumps Severely Delayed (total)|Rate|Operations/Sec|||WEKA|IO|True|False|
ssd|SSD|DRIVE_LATENCY|Measure the latencies up to 5ms (higher latencies are grouped)|Drive Latency Histogram (total)|Histogram|Requests|disk||WEKA|IO|True|True|Microseconds
ssd|SSD|SSD_WRITES|Number of write requests to the SSD service|SSD Writes (total)|Rate|IO/Sec|disk||USER|IO|True|False|
ssd|SSD|SSD_CHUNK_FREES|Number of chunk frees|Chunks Freed (total)|Absolute|Chunks|disk||WEKA|IO|True|False|
ssd|SSD|DRIVE_REQUEST_BLOCKS|Measure drive request size distribution|Num Blocks (total)|Histogram|Requests|||WEKA|IO|True|True|Blocks
ssd|SSD|NVKV_OUT_OF_CHUNKS|Number of failed attempts to allocate an NVKV chunk|NVKV chunk allocation attempts (total)|Rate|Attempts/Sec|||WEKA|IO|True|False|
ssd|SSD|DRIVE_FORFEITS|Number of IOs forfeited due to lack of memory buffers|Drive Forfeits IOs (total)|Rate|Operations/Sec|||WEKA|IO|True|False|
ssd|SSD|DRIVE_WRITE_LATENCY|Drive Write Execution Latency|Drive Write Latency (per IO)|Measured|Microseconds|disk|DRIVE_WRITE_OPS|USER|IO|False|False|
ssd|SSD|SSD_BLOCKS_WRITTEN|Number of blocks written to the SSD service|SSD Blocks Written (total)|Rate|Blocks/Sec|disk||USER|IO|True|False|
ssd|SSD|DRIVE_IO_TOO_LONG|Number of IOs that took longer than expected|Drive IO taking too Long (total)|Rate|Operations/Sec|||WEKA|IO|True|False|
statistics|Statistics|GATHER_FROM_NODE_LATENCY_NET|Time spent on responding to a stats-gathering request (not including metadata)|Gather from Node Latency Neto (total)|Rate|Seconds/Sec|||WEKA|ANY|True|False|
statistics|Statistics|GATHER_FROM_NODE_SLEEP|Time spent in-between responding to a stats-gathering request (not including metadata)|Gather from Node Sleep (total)|Rate|Seconds/Sec|||WEKA|ANY|True|False|
statistics|Statistics|TIMES_QUERIED_STATS|Number of times the process queried other processes for stats|Times Queried Others (total)|Absolute|Times|peer_node_id||WEKA|MANAGEMENT|True|False|
statistics|Statistics|GATHER_FROM_NODE_LATENCY|Time spent responding to a stats-gathering request (not including metadata)|Gather from Node Latency (total)|Rate|Seconds/Sec|||WEKA|ANY|True|False|
statistics|Statistics|TIMES_QUERIED|Number of times the process was queried for stats (not including metadata)|Times Queried (total)|Absolute|Times|||WEKA|ANY|True|False|
