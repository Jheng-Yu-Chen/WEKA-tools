import argparse
import requests
import datetime
from urllib.parse import urljoin, urlencode

# Define a list of cluster names to be excluded from the report
CLUSTER_EXCLUSION_LIST = [
    "upgrade-extended",
    "weka-cst"
]

def format_duration(seconds):
    """
    Converts a duration in seconds to a human-readable Dd Hh Mm Ss format.
    """
    if seconds is None or not isinstance(seconds, (int, float)):
        return "N/A"
    
    seconds = int(seconds)
    
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    parts = []
    if days > 0:
        parts.append(f"{days}d")
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    
    # Always display seconds unless the duration is exactly 0 and other parts are empty.
    if seconds > 0 or not parts:
        parts.append(f"{seconds}s")
    
    return " ".join(parts)

def get_upgrade_history(token, site, from_ts, end_ts, cluster_id):
    """
    Fetches upgrade history from the API, handling pagination.
    """
    print("Fetching upgrade history...")
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json; charset=utf-8",
        "Authorization": f"Token {token}"
    }

    all_history = []
    page = 1
    page_size = 50
    total_records = -1

    base_url = urljoin(site, "/api/v4/clusters/upgrades-history")

    while total_records == -1 or (page - 1) * page_size < total_records:
        params = {
            "is_backend": "true",
            "from": from_ts,
            "to": end_ts,
            "page_size": page_size,
            "page": page
        }
        if cluster_id:
            params["cluster_id"] = cluster_id

        try:
            response = requests.get(base_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            records = data.get("data", [])
            all_history.extend(records)
            
            meta = data.get("meta", {})
            total_records = meta.get("total", len(all_history))
            page += 1
            
            print(f"  Fetched page {page-1}, total records {len(all_history)} / {total_records}...")
            if not records:
                break

        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None

    print(f"Found {len(all_history)} upgrade history records.")
    
    # Sort history records by timestamp in descending order before returning
    return sorted(all_history, key=lambda x: x.get('timestamp', '0'), reverse=True)

def get_upgrade_events(token, site, cluster_id, from_ts, end_ts):
    """
    Fetches upgrade events for a specific cluster, handling pagination.
    """
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json; charset=utf-8",
        "Authorization": f"Token {token}"
    }

    event_types = [
        "ComputeUpgradeFinished", "ComputeUpgradeStarted",
        "DrivesUpgradeFinished", "DrivesUpgradeStarted",
        "FrontendUpgradeFinished", "FrontendUpgradeStarted",
        "DataservUpgradeStarted", "DataservUpgradeFinished"
    ]

    all_events = []
    has_next_page = True
    next_cursor = None

    base_url = urljoin(site, f"/api/{cluster_id}/events/list")

    while has_next_page:
        params = {
            "cluster_id": cluster_id,
            "meta": "true",
            "tc": "true",
            "fve": "false",
            "page_size": 100,
            "lmt": 100,
            "intr": "true",
            "svr": "DEBUG",
            "srt": "asc",
            "last": "false",
            "from": from_ts,
            "to": end_ts
        }
        for et in event_types:
            params.setdefault("et[]", []).append(et)
        
        if next_cursor:
            params["cursor"] = next_cursor

        try:
            encoded_params = urlencode(params, doseq=True)
            response = requests.get(f"{base_url}?{encoded_params}", headers=headers)
            response.raise_for_status()
            data = response.json()

            events = data.get("entries", [])
            all_events.extend(events)

            meta = data.get("meta", {})
            has_next_page = meta.get("has_next_page", False)
            next_cursor = meta.get("next_cursor")

        except requests.exceptions.RequestException as e:
            print(f"Failed to get events for {cluster_id}: {e}")
            return None
    
    return all_events

def get_column_widths(headers, records):
    """
    Dynamically calculates the required width for each column based on headers and data.
    """
    widths = []
    for header in headers:
        max_width = len(header)
        for record in records:
            value = record.get(header, "N/A")
            max_width = max(max_width, len(str(value)))
        widths.append(max_width + 2)  # Add a small buffer for padding
    return widths

def generate_and_print_report(history_data, token, site):
    """
    Processes history and event data, calculates durations, and prints the report.
    """
    if not history_data:
        print("No upgrade history found to generate report.")
        return
    
    # Group history entries by cluster_id and the first part of previous_versions
    upgrades_by_job = {}
    for entry in history_data:
        cluster_name = entry.get("cluster_name", "")
        if cluster_name in CLUSTER_EXCLUSION_LIST:
            print(f"Skipping cluster '{cluster_name}' as it is in the exclusion list.")
            continue
            
        cluster_id = entry.get("cluster_id")
        source_version_key = entry.get("previous_versions", "").split(',')[0].strip()
        job_key = (cluster_id, source_version_key)
        if job_key not in upgrades_by_job:
            upgrades_by_job[job_key] = {'starts': [], 'ends': []}
        
        if ',' in entry.get("versions", ""):
            upgrades_by_job[job_key]['starts'].append(entry)
        else:
            upgrades_by_job[job_key]['ends'].append(entry)
    
    processed_records = []

    for job_key, entries in upgrades_by_job.items():
        start_entry = None
        end_entry = None
        
        if entries['starts']:
            entries['starts'].sort(key=lambda x: x.get('timestamp', '0'), reverse=False)
            start_entry = entries['starts'][0]
        
        if entries['ends']:
            entries['ends'].sort(key=lambda x: x.get('timestamp', '0'), reverse=True)
            end_entry = entries['ends'][0]
        
        overall_duration = "N/A"
        if start_entry and end_entry:
            start_dt_overall = datetime.datetime.fromisoformat(start_entry.get('timestamp').replace('Z', '+00:00'))
            end_dt_overall = datetime.datetime.fromisoformat(end_entry.get('timestamp').replace('Z', '+00:00'))
            overall_seconds = (end_dt_overall - start_dt_overall).total_seconds()
            overall_duration = format_duration(overall_seconds)
        
        if not end_entry:
            continue
        
        entry_to_process = end_entry
        cluster_name = entry_to_process.get("cluster_name", "N/A")

        start_ts_display = "N/A"
        if start_entry:
            start_dt_overall = datetime.datetime.fromisoformat(start_entry.get('timestamp').replace('Z', '+00:00'))
            start_ts_display = start_dt_overall.astimezone().strftime("%Y-%m-%d %H:%M:%S")

        end_ts_display = "N/A"
        end_dt_events = datetime.datetime.fromisoformat(end_entry.get('timestamp').replace('Z', '+00:00'))
        end_ts_display = end_dt_events.astimezone().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"\nProcessing upgrade for '{cluster_name}' ({job_key[0]}) from version {job_key[1]}...")
        
        start_dt_events = start_dt_overall if start_entry else end_dt_events - datetime.timedelta(days=2) # Default to 2 days if start is missing
        events_end_dt = end_dt_events
        
        # We still need to call get_upgrade_events to calculate stage durations
        events = get_upgrade_events(token, site, entry_to_process.get("cluster_id"), start_dt_events.isoformat(), events_end_dt.isoformat())
        
        stage_durations = {
            "Drives": "N/A", "Compute": "N/A", "Frontend": "N/A",
            "Dataserv": "N/A"
        }

        # New: Hotfix versions are still identified from events
        hotfix_versions = set()
        
        if events:
            event_timestamps = {}
            for event in events:
                event_type = event.get("type")
                event_ts = datetime.datetime.fromisoformat(event.get("timestamp").replace('Z', '+00:00'))
                target_release = event.get("params", {}).get("targetRelease")
                
                # We only need to check for hotfixes here
                if target_release and '-' in target_release:
                    hotfix_versions.add(target_release)

                # Corrected filter logic
                if target_release and not entry_to_process.get("versions").startswith(target_release):
                    continue
                
                if "Started" in event_type:
                    event_timestamps[event_type] = event_ts
                elif "Finished" in event_type:
                    event_timestamps[event_type] = event_ts

            for stage in ["Drives", "Compute", "Frontend", "Dataserv"]:
                started = event_timestamps.get(f"{stage}UpgradeStarted")
                finished = event_timestamps.get(f"{stage}UpgradeFinished")
                if started and finished:
                    duration = (finished - started).total_seconds()
                    stage_durations[stage] = format_duration(duration)

        source_display = entry_to_process.get("previous_versions", "").split(',')[0].strip()
        
        # New: Get Target Version directly from the history record
        target_display = end_entry.get("versions", "N/A")
        
        hotfix_display = ", ".join(sorted(list(hotfix_versions)))
        # Note: Hotfixes from events will still appear, but target version will be from history.
        
        processed_records.append({
            "Cluster Name": cluster_name,
            "Cluster ID": entry_to_process.get("cluster_id"),
            "Upgrade Start": start_ts_display,
            "Upgrade End": end_ts_display,
            "Source Version": source_display,
            "Target Version": target_display,
            "Drives Stage": stage_durations["Drives"],
            "Compute Stage": stage_durations["Compute"],
            "Frontend Stage": stage_durations["Frontend"],
            "Dataserv Stage": stage_durations["Dataserv"],
            "Overall": overall_duration,
            "Hotfix": hotfix_display
        })
    
    # Sort final records by upgrade start time, descending
    processed_records.sort(key=lambda x: x.get("Upgrade Start", "0"), reverse=True)

    print("\n### Weka Upgrade Report")
    headers = ["Cluster Name", "Cluster ID", "Upgrade Start", "Upgrade End", "Source Version", "Target Version", 
               "Drives Stage", "Compute Stage", "Frontend Stage", "Dataserv Stage", "Overall", "Hotfix"]
    
    widths = get_column_widths(headers, processed_records)
    
    header_str = " | ".join(f"{h:<{w}}" for h, w in zip(headers, widths))
    print(header_str)
    separator_str = "-|-".join("-" * w for w in widths)
    print(separator_str)
    for row in processed_records:
        row_str = " | ".join(f"{row.get(h, 'N/A'):<{w}}" for h, w in zip(headers, widths))
        print(row_str)

def print_history_only(history_data):
    """
    Prints a simplified table for the --upgrades-history-only flag.
    """
    if not history_data:
        print("No upgrade history found.")
        return

    print("\n### Weka Upgrade History (Simplified)")

    headers = ["Cluster Name", "Cluster ID", "History Timestamp (Local)", "Source Version", "Target Version"]

    simplified_records = []
    for entry in history_data:
        source_version = entry.get("previous_versions", "")
        target_version = entry.get("versions", "")
        
        if source_version == target_version:
            continue

        history_timestamp_utc = entry.get("timestamp")
        if history_timestamp_utc:
            try:
                dt_utc = datetime.datetime.fromisoformat(history_timestamp_utc.replace('Z', '+00:00'))
                dt_local = dt_utc.astimezone()
                history_timestamp_display = dt_local.strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                history_timestamp_display = "Invalid Timestamp"
        else:
            history_timestamp_display = "N/A"
        
        source_display = source_version.split(',')[0].strip()
        target_display = target_version.split(',')[0].strip()
        
        simplified_records.append({
            "Cluster Name": entry.get("cluster_name", "N/A"),
            "Cluster ID": entry.get("cluster_id", "N/A"),
            "History Timestamp (Local)": history_timestamp_display,
            "Source Version": source_display,
            "Target Version": target_display
        })

    widths = get_column_widths(headers, simplified_records)
    
    header_str = " | ".join(f"{h:<{w}}" for h, w in zip(headers, widths))
    print(header_str)
    
    separator_str = "-|-".join("-" * w for w in widths)
    print(separator_str)

    for row in simplified_records:
        row_str = " | ".join(f"{row.get(h, 'N/A'):<{w}}" for h, w in zip(headers, widths))
        print(row_str)


def main():
    """
    Main function to parse arguments and drive the program logic.
    """
    parser = argparse.ArgumentParser(description="Weka upgrade history and event analysis script.")
    parser.add_argument("--token", required=True, help="API authentication token.")
    parser.add_argument("--from", dest="from_ts", help="Start timestamp in local timezone (e.g., '2025-07-01 00:00:00').")
    parser.add_argument("--end", dest="end_ts", help="End timestamp in local timezone (e.g., '2025-07-10 23:59:59').")
    parser.add_argument("--cluster", help="Filter by a specific cluster UUID.")
    parser.add_argument("--site", default="https://api.home.weka.io", help="API site URL (default: https://api.home.weka.io).")
    parser.add_argument("--upgrades-history-only", action="store_true", help="Only list upgrade history, without detailed event analysis.")

    args = parser.parse_args()

    now_local = datetime.datetime.now().astimezone()
    
    from_ts_utc = None
    end_ts_utc = None

    if args.end_ts:
        try:
            dt_local = datetime.datetime.fromisoformat(args.end_ts)
            end_ts_utc = dt_local.astimezone(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')
        except ValueError:
            print(f"Invalid --end timestamp format: {args.end_ts}. Using default (now).")
    
    if not end_ts_utc:
        end_ts_utc = now_local.astimezone(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')

    if args.from_ts:
        try:
            dt_local = datetime.datetime.fromisoformat(args.from_ts)
            from_ts_utc = dt_local.astimezone(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')
        except ValueError:
            print(f"Invalid --from timestamp format: {args.from_ts}. Using default (7 days ago).")

    if not from_ts_utc:
        seven_days_ago_local = now_local - datetime.timedelta(days=7)
        from_ts_utc = seven_days_ago_local.astimezone(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')

    print(f"Querying API for UTC range: {from_ts_utc} to {end_ts_utc}")
    history_data = get_upgrade_history(
        args.token,
        args.site,
        from_ts_utc,
        end_ts_utc,
        args.cluster
    )
    
    if not history_data:
        print("No upgrade history found, program exiting.")
        return

    if args.upgrades_history_only:
        print_history_only(history_data)
    else:
        generate_and_print_report(history_data, args.token, args.site)

if __name__ == "__main__":
    main()
