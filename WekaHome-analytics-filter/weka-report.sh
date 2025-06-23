#!/bin/bash

CLUSTER_ID="$1"

if [ -z "$CLUSTER_ID" ]; then
	echo "Usage: bash $0 <cluster_id>"	
	exit 1
fi

function get_usage_data() {
	USAGE_REPORT_JSON=$(homecli usage-report --cluster $CLUSTER_ID)
}

function get_analytics() {
	ANALYTICS_JSON=$(homecli analytics --cluster $CLUSTER_ID)
}

function md_title() {
	echo '![WEKA](https://cdn.cookielaw.org/logos/95d47dcf-fb9f-4850-94f4-4e80083055a2/44150a6a-2de8-4689-b1b4-957bbca2746b/4958ac07-db8a-4924-92d9-f1f4fbff6e35/weka-logo-cookielaw.png)'
	echo
	echo "# WEKA Health Report"
	
	RAW_TIMESTAMP=$(jq -r '.timestamp' <<<"$USAGE_REPORT_JSON")
	CLEANED_TIMESTAMP=$(echo "$RAW_TIMESTAMP" | sed -E 's/\..*Z$//')
	
	LOCAL_TZ=$(readlink /etc/localtime 2>/dev/null | sed -E 's|.*/zoneinfo/||' )
	
	if [[ -z "$LOCAL_TZ" ]]; then
	    LOCAL_TZ=${TZ:-$(date +%Z)}
	fi
	
	if date --version >/dev/null 2>&1; then
	    # GNU date (Linux)
	    LOCAL_TIME=$(TZ="$LOCAL_TZ" date -d "$RAW_TIMESTAMP" "+%Y-%m-%d %H:%M:%S")
	else
	    # BSD date (macOS)
	    UTC_EPOCH=$(TZ=UTC date -j -f "%Y-%m-%dT%H:%M:%S" "$CLEANED_TIMESTAMP" "+%s")
	    LOCAL_TIME=$(TZ="$LOCAL_TZ" date -r "$UTC_EPOCH" "+%Y-%m-%d %H:%M:%S")
	fi

	CLUSTER_GUID=$(jq -r '.report.guid' <<< "$USAGE_REPORT_JSON")
	
	echo "**CLUSTER GUID**: $CLUSTER_GUID"
	echo "**Report Time**: $LOCAL_TIME ($LOCAL_TZ)"
	echo ""
}

function md_cluster_status() {
	CLUSTER_NAME=$(jq -r '.report.name' <<<"$USAGE_REPORT_JSON")
	VERSION=$(jq -r '.report.software_version' <<<"$USAGE_REPORT_JSON")
	UPTIME_RAW=$(jq -r '.report.uptime.backends_uptime_secs.max' <<<"$USAGE_REPORT_JSON")
	WEKA_STATUS=$(jq -r '.report.status.status' <<<"$USAGE_REPORT_JSON")
	ALERT_CNT=$(jq -r '[.report.alerts[] | select(.muted == false)] | length' <<<"$USAGE_REPORT_JSON")
	LINK_LAYER=$(jq -r '.report.status.net.link_layer' <<< "$USAGE_REPORT_JSON")
	
	BUCKETS_ACTIVE=$(jq -r '.report.status.buckets.active' <<<"$USAGE_REPORT_JSON")
	BUCKETS_TOTAL=$( jq -r '.report.status.buckets.total'  <<<"$USAGE_REPORT_JSON")
	BUCKETS_DISPLAY="${BUCKETS_ACTIVE}/${BUCKETS_TOTAL}"
	
	if [[ "$UPTIME_RAW" =~ ^[0-9]+$ ]]; then
	    DAYS=$((UPTIME_RAW / 86400))
	    HOURS=$(( (UPTIME_RAW % 86400) / 3600 ))
	    MINUTES=$(( (UPTIME_RAW % 3600) / 60 ))
	    SECONDS=$((UPTIME_RAW % 60))
	    UPTIME_FMT="${DAYS}d ${HOURS}h ${MINUTES}m ${SECONDS}s"
	else
	    UPTIME_FMT="N/A"
	fi
	
	if [[ "$WEKA_STATUS" =~ ^[Oo][Kk]$ ]]; then
	    WEKA_STATUS_DISPLAY="🟢 $WEKA_STATUS"
	else
	    WEKA_STATUS_DISPLAY="🔴 $WEKA_STATUS"
	fi
	
	echo "## Cluster Status"
	echo "| Name | Version | Uptime | Link Layer | Buckets | Alerts | Status |"
	echo "|------|---------|--------|------------|--------|---------|--------|"
	echo "| $CLUSTER_NAME | $VERSION | $UPTIME_FMT | $LINK_LAYER | $BUCKETS_DISPLAY | $ALERT_CNT | $WEKA_STATUS_DISPLAY |"
	echo ""
}

function md_protocols_summary() {
	echo "### Protocols Summary"
	echo
	echo "| Protocol | Enabled | Details |"
	echo "|----------|---------|---------|"
	
	P_S3=$(   jq -r '.report.protocols.is_s3'   <<<"$USAGE_REPORT_JSON")
	P_SMBW=$( jq -r '.report.protocols.is_smbw' <<<"$USAGE_REPORT_JSON")
	P_NFS=$(  jq -r '.report.protocols.is_nfs'  <<<"$USAGE_REPORT_JSON")
	
	S3_HOSTS=$(jq -r '.report.protocols_servers_Status.s3 | keys | length' \
	               <<<"$USAGE_REPORT_JSON")
	[[ "$S3_HOSTS" == "null" ]] && S3_HOSTS=0
	S3_DETAILS=$([[ "$P_S3" == "true" ]] && \
	             printf "Enabled on %s host%s" "$S3_HOSTS" \
	                    $([[ "$S3_HOSTS" -ne 1 ]] && echo "s") || echo "-")
	
	SMB_ENC=$(jq -r '.report.protocols.is_smb_encrypted' <<<"$USAGE_REPORT_JSON")
	SMBW_DETAILS=$([[ "$P_SMBW" == "true" ]] && \
	               printf "Encrypted: %s" $([[ "$SMB_ENC" == "true" ]] && echo "Yes" || echo "No") \
	               || echo "-")
	
	NFS_IG=$( jq -r '.report.protocols_servers_Status.nfs.interface_groups        | length' \
	               <<<"$USAGE_REPORT_JSON")
	[[ "$NFS_IG" == "null" ]] && NFS_IG=0
	NFS_IPS=$(jq -r '.report.protocols_servers_Status.nfs.interface_groups[]?.ips | length' \
	               <<<"$USAGE_REPORT_JSON" | awk '{sum+=$1} END{print sum+0}')
	NFS_DETAILS=$([[ "$P_NFS" == "true" ]] && \
	              printf "%s interface-group%s, %s Floating IP%s" "$NFS_IG" $([[ "$NFS_IG" -ne 1 ]] && echo "s") \
	                                           "$NFS_IPS" $([[ "$NFS_IPS" -ne 1 ]] && echo "s") \
	              || echo "-")
	
	enabled () { [[ "$1" == "true" ]] && echo "Yes" || echo "No"; }
	
	printf '| S3   | %s | %s |\n'  "$(enabled $P_S3)"  "$S3_DETAILS"
	printf '| SMBW | %s | %s |\n'  "$(enabled $P_SMBW)" "$SMBW_DETAILS"
	printf '| NFS  | %s | %s |\n'  "$(enabled $P_NFS)"  "$NFS_DETAILS"
	echo
}


function md_alerts_by_host() {
	echo "## Alerts"
	echo "| Hostname | Alert Messages |"
	echo "|----------|----------------|"
	
	jq -r '
	  .report.alerts[]
	  | select(.muted == false)
	  | .params as $p
	  | {
	      host: ($p.hostname // "Cluster Wide"),
	      message:
	        (
	          reduce ($p | to_entries[]) as $kv (.fmt;
	                 gsub("\\{" + $kv.key + "\\}"; ($kv.value|tostring)))
	          | gsub("\\s*\\(?\\{host_id\\}\\)?"; "")
	          | gsub("\\{[A-Za-z0-9_]+\\}"; "")
	          | gsub("  +"; " ")
	          | gsub("^[ \\t]+|[ \\t]+$"; "")
	        )
	    }
	  | .host + "\t" + .message
	' <<< "$USAGE_REPORT_JSON" \
	| sort \
	| awk -F'\t' '
	    {
	        host=$1; msg=$2
	        if (seen[host, msg]++ == 0)
	            summary[host] = summary[host] ? summary[host] "<br>⚠️ " msg : "⚠️ " msg
	    }
	    END {
	        PROCINFO["sorted_in"] = "@ind_str_asc"
	        for (h in summary)
	            printf "| %s | %s |\n", h, summary[h]
	    }'
	echo ""
}

function md_hw_status() {

	echo "## Servers Summary"
	echo ""
	echo "### BACKENDS"
	echo "| Category   | Value | Details |"
	echo "|------------|-------|---------|"
	
	SERVERS_ACTIVE=$(jq -r '.report.status.servers.backends.active'      <<<"$USAGE_REPORT_JSON")
	SERVERS_TOTAL=$( jq -r '.report.status.servers.backends.total'       <<<"$USAGE_REPORT_JSON")
	CONTAINERS_ACTIVE=$(jq -r '.report.status.containers.backends.active'<<<"$USAGE_REPORT_JSON")
	CONTAINERS_TOTAL=$( jq -r '.report.status.containers.backends.total' <<<"$USAGE_REPORT_JSON")
	PROCESSES_ACTIVE=$(jq -r '.report.status.io_nodes.active'            <<<"$USAGE_REPORT_JSON")
	PROCESSES_TOTAL=$( jq -r '.report.status.io_nodes.total'             <<<"$USAGE_REPORT_JSON")
	DRIVES_ACTIVE=$(jq -r '.report.status.drives.active'                 <<<"$USAGE_REPORT_JSON")
	DRIVES_TOTAL=$( jq -r '.report.status.drives.total'                  <<<"$USAGE_REPORT_JSON")
	OBS_ACTIVE=$(jq -r '.report.status.servers.obs.active // 0'          <<<"$USAGE_REPORT_JSON")
	OBS_TOTAL=$( jq -r '.report.status.servers.obs.total  // 0'          <<<"$USAGE_REPORT_JSON")
	
	status_icon() {           # $1 active  $2 total
	    (( $1 < $2 )) && echo "🟡" || echo "🟢"
	}
	details_text() {          # $1 active  $2 total
	    local diff=$(( $2 - $1 ))
	    if (( diff > 0 )); then
	        printf "%d degraded, %d active of %d total" "$diff" "$1" "$2"
	    else
	        printf "%d active of %d total" "$1" "$2"
	    fi
	}
	
	echo "| Servers    | ${SERVERS_ACTIVE}/${SERVERS_TOTAL} | $(status_icon $SERVERS_ACTIVE $SERVERS_TOTAL) $(details_text $SERVERS_ACTIVE $SERVERS_TOTAL) |"
	echo "| Containers | ${CONTAINERS_ACTIVE}/${CONTAINERS_TOTAL} | $(status_icon $CONTAINERS_ACTIVE $CONTAINERS_TOTAL) $(details_text $CONTAINERS_ACTIVE $CONTAINERS_TOTAL) |"
	echo "| Processes  | ${PROCESSES_ACTIVE}/${PROCESSES_TOTAL} | $(status_icon $PROCESSES_ACTIVE $PROCESSES_TOTAL) $(details_text $PROCESSES_ACTIVE $PROCESSES_TOTAL) |"
	echo "| Drives     | ${DRIVES_ACTIVE}/${DRIVES_TOTAL} | $(status_icon $DRIVES_ACTIVE $DRIVES_TOTAL) $(details_text $DRIVES_ACTIVE $DRIVES_TOTAL) |"
	echo "| OBS        | ${OBS_ACTIVE}/${OBS_TOTAL} | $(status_icon $OBS_ACTIVE $OBS_TOTAL) $(details_text $OBS_ACTIVE $OBS_TOTAL) |"
	echo ""
	
	echo "### CLIENTS"
	echo "| Category   | Value | Details |"
	echo "|------------|-------|---------|"
	
	C_SERVERS_ACTIVE=$(jq -r '.report.status.servers.clients.active'      <<<"$USAGE_REPORT_JSON")
	C_SERVERS_TOTAL=$( jq -r '.report.status.servers.clients.total'       <<<"$USAGE_REPORT_JSON")
	C_CONTAINERS_ACTIVE=$(jq -r '.report.status.containers.clients.active'<<<"$USAGE_REPORT_JSON")
	C_CONTAINERS_TOTAL=$( jq -r '.report.status.containers.clients.total' <<<"$USAGE_REPORT_JSON")
	C_PROCESSES_ACTIVE=$(jq -r '.report.total_active_client_nodes'        <<<"$USAGE_REPORT_JSON")
	C_PROCESSES_TOTAL=$( jq -r '.report.total_client_nodes'               <<<"$USAGE_REPORT_JSON")
	
	echo "| Clients    | ${C_SERVERS_ACTIVE}/${C_SERVERS_TOTAL} | $(status_icon $C_SERVERS_ACTIVE $C_SERVERS_TOTAL) $(details_text $C_SERVERS_ACTIVE $C_SERVERS_TOTAL) |"
	echo "| Containers | ${C_CONTAINERS_ACTIVE}/${C_CONTAINERS_TOTAL} | $(status_icon $C_CONTAINERS_ACTIVE $C_CONTAINERS_TOTAL) $(details_text $C_CONTAINERS_ACTIVE $C_CONTAINERS_TOTAL) |"
	echo "| Processes  | ${C_PROCESSES_ACTIVE}/${C_PROCESSES_TOTAL} | $(status_icon $C_PROCESSES_ACTIVE $C_PROCESSES_TOTAL) $(details_text $C_PROCESSES_ACTIVE $C_PROCESSES_TOTAL) |"
	echo ""
}


function md_capacity_bar() {
	local total=$(jq -r '.report.status.capacity.total_bytes'          <<<"$USAGE_REPORT_JSON")
	local unprov=$(jq -r '.report.status.capacity.unprovisioned_bytes' <<<"$USAGE_REPORT_JSON")
	local prov=$(( total - unprov ))        
	
	local used=$(jq -r '[.fs.filesystems[].used_ssd_capacity] | add // 0' \
	                  <<<"$ANALYTICS_JSON")
	
	human() {
	    (( $1 >= 1000000000000000 )) \
	      && awk -v v="$1" 'BEGIN{printf "%.1f PB", v/1e15}' \
	      || awk -v v="$1" 'BEGIN{printf "%.1f TB", v/1e12}'
	}
	pct(){ awk -v a="$1" -v b="$2" 'BEGIN{printf "%.1f%%", (b==0?0:a*100/b)}'; }
	seg(){ awk -v a="$1" -v t="$2" -v n=30 'BEGIN{printf "%d", int(a/t*n)}'; }
	
	barlen=30
	used_seg=$(seg "$used" "$total")
	prov_seg=$(seg "$prov" "$total")
	bar() {
	    printf "%*s" "$used_seg" ""              | tr ' ' '█'   
	    printf "%*s" "$((prov_seg-used_seg))" "" | tr ' ' '▒'   
	    printf "%*s" "$((barlen-prov_seg))" ""   | tr ' ' '░'  
	}
	
	local avail=$(( prov - used ))
	local unprov_bytes=$unprov
	
	echo "\`\`\`text"
	echo "SSD Capacity : $(human "$total")"
	echo "[ $(bar) ]"
	echo "█ Used        : $(human "$used")  — $(pct "$used" "$prov") of Provisioned SSD"
	echo "▒ Available   : $(human "$avail") — $(pct "$avail" "$prov") of Provisioned SSD"
	echo "░ Unprovision : $(human "$unprov_bytes") — $(pct "$unprov_bytes" "$total") of Total SSD"
	echo "\`\`\`"
	echo ""
}

function md_fs_table() {
	human() {
	    local b=$1
	    if   (( b >= 1000000000000000 )); then
	        awk -v v="$b" 'BEGIN{printf "%.1f PB", v/1e15}'
	    elif (( b >= 1000000000000 )); then
	        awk -v v="$b" 'BEGIN{printf "%.1f TB", v/1e12}'
	    else
	        awk -v v="$b" 'BEGIN{printf "%.1f GB", v/1e9}'
	    fi
	}
	fmt_pct() { awk -v p="$1" 'BEGIN{printf "%.1f%%", p}'; }
	
	echo "### Filesystems"
	echo
	echo "| FS Name | SSD Capacity | Used SSD | Used % | Snapshots |"
	echo "|---------|--------------:|---------:|-------:|----------:|"
	
	jq -r '
	  .fs.filesystems[]
	  | [
	      .fs_name,
	      (.ssd_capacity      // 0),
	      (.used_ssd_capacity // 0),
	      ((.snapshots.count  // 1) - 1)
	    ]
	  | @tsv
	' <<<"$ANALYTICS_JSON" |
	{
	    total_cap=0
	    total_used=0
	    total_snaps=0
	    declare -a rows
	
	    while IFS=$'\t' read -r name cap used snaps; do
	        pct=$(awk -v u="$used" -v c="$cap" 'BEGIN{printf "%.1f", (c==0?0:u*100/c)}')
	        row="| $name | $(human "$cap") | $(human "$used") | $(fmt_pct "$pct") | $snaps |"
	        rows+=("$pct"$'\t'"$row")
	
	        total_cap=$(( total_cap + cap ))
	        total_used=$(( total_used + used ))
	        total_snaps=$(( total_snaps + snaps ))
	    done
	
	    printf "%s\n" "${rows[@]}" | sort -nr -k1,1 | cut -f2-
	
	    # -------- Total row --------
	    total_pct=$(awk -v u="$total_used" -v c="$total_cap" 'BEGIN{printf "%.1f", (c==0?0:u*100/c)}')
	    echo "| **Total** | **$(human "$total_cap")** | **$(human "$total_used")** | **$(fmt_pct "$total_pct")** | **$total_snaps** |"
	}
	
	echo
}


function md_media_errors() {
	local err_cnt
	err_cnt=$(jq '
	    (.drive.drives // .drives // .report.drives // [])
	    | map(select(.media_errors? and (.media_errors|tonumber) > 0))
	    | length
	  ' <<<"$ANALYTICS_JSON")
	
	[[ "$err_cnt" -eq 0 ]] && return
	
	echo "### Top 10 Drives by Media Errors"
	echo '| id | model | firmware | target_state | spares_remaining | media_errors |'
	echo '|----|-------|----------|--------------|------------------|--------------|'
	
	jq -r '
	  (.drive.drives // .drives // .report.drives // [])[]
	  | select(.media_errors? and (.media_errors | tonumber) > 0)
	  | [.media_errors, .id, .model, .firmware_version, .target_state, .spares_remaining]
	  | @tsv
	' <<<"$ANALYTICS_JSON" |
	sort -nr -k1,1 |
	head -n 10 |
	while IFS=$'\t' read -r errs id model fw tgt spare; do
	    printf '| %s | %s | %s | %s | %s | %s |\n' \
	           "$id" "$model" "$fw" "$tgt" "$spare" "$errs"
	done
	
	echo
}

function md_warning_events() {
	if date --version >/dev/null 2>&1; then
	    START=$(date -u -d "$(date +%Y-%m-01) -3 months" '+%Y-%m-01T00:00:00Z')
	else
	    START=$(TZ=UTC date -u -v-3m -v1d -v0H -v0M -v0S '+%Y-%m-01T00:00:00Z')
	fi
	
	EVENTS=$(homecli events "$CLUSTER_ID" \
	  --hide-internal -s WARNING \
	  --start "$START" \
	  --exclude-type NodeUnreachable \
	  --exclude-type DedupEventsDiscarded \
	  --exclude-type HugepagesAllocationRetries \
	  --exclude-type DriveMediumError \
	  --limit 100 --wide --json)
	
	if ! grep -q '"timestamp"' <<<"$EVENTS"; then
	  echo "## Events (since $START)"
	  echo
	  echo "* No WARNING events in the last 3 months."
	  echo
	  return
	fi
	
	echo "## Events (since $START)"
	echo
	echo '| Time | Type | Category | Backend | Node | Severity | Params |'
	echo '|------|------|----------|---------|------|----------|--------|'
	
	jq -r '
	  [
	    .timestamp,
	    .type,
	    .category,
	    (if .is_backend then "Yes" else "No" end),
	    (.nid | sub("NodeId<(?<id>\\d+)>"; "\(.id)")),
	    .severity,
	    (.params | tostring)
	  ]
	  | @tsv
	' <<<"$EVENTS" |
	while IFS=$'\t' read -r ts type cat backend node sev params; do
	  printf '| %s | %s | %s | %s | %s | %s | %s |\n' \
	         "$ts" "$type" "$cat" "$backend" "$node" "$sev" "$params"
	done
	
	echo
}

function md_summary() {
	echo "## Summary and Recommendations"
	echo "* "
}

function md_output() {
	md_title
	md_cluster_status
	md_capacity_bar
	md_fs_table
	md_protocols_summary
	md_hw_status
	#md_media_errors
	md_alerts_by_host
	md_warning_events
	md_summary
}

get_usage_data
get_analytics

md_output 
