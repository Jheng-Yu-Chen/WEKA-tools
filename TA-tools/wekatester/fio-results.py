#!/usr/bin/env python3
import os
import json
import glob
import argparse
import csv
import fnmatch
from collections import defaultdict
from datetime import datetime, timedelta

def get_rack_name_for_ip(ip):
    if not ip or '.' not in ip: return "RACK-invalid"
    try:
        parts = ip.split('.')
        subnet = ".".join(parts[:3])
        last_octet = int(parts[3])
        group_number = (last_octet - 1) // 18 + 1
        return f"RACK-{subnet}-{group_number}"
    except (IndexError, ValueError):
        return "RACK-invalid-format"

def summarize_nodes_by_group(nodes):
    if not nodes: return "N/A"
    rack_names = set(get_rack_name_for_ip(ip) for ip in nodes)
    return ", ".join(sorted(list(rack_names)))

def process_fio_json_files(file_paths, no_rack_grouping=False):
    summary_results, detailed_client_results = [], []
    if not file_paths:
        print("No files to process.")
        return [], []

    for file_path in file_paths:
        filename = os.path.basename(file_path)
        try:
            with open(file_path, 'r') as f: data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not read or parse {filename}: {e}")
            continue

        for job_key, job_section in data.items():
            if not isinstance(job_section, dict) or 'client_stats' not in job_section: continue

            client_stats_list = job_section.get('client_stats', [])
            nodes = sorted(list(set(cs.get('hostname') for cs in client_stats_list if cs.get('hostname'))))
            
            global_opts_val = job_section.get('global options', {})
            opts_list = global_opts_val if isinstance(global_opts_val, list) else [global_opts_val]
            if not nodes:
                nodes = sorted(list(set(opt.get('hostname') for opt in opts_list if opt.get('hostname'))))

            node_count = len(nodes)
            if node_count == 0: continue

            global_opts = opts_list[0] if opts_list else {}
            runtime_config = global_opts.get('runtime', 'N/A')
            ioengine = global_opts.get('ioengine', 'N/A')
            filesize = global_opts.get('filesize', 'N/A')
            numjobs = global_opts.get('numjobs', 'N/A')
            timestamp = job_section.get("timestamp")
            
            grouping_str = ", ".join(nodes) if no_rack_grouping else summarize_nodes_by_group(nodes)
            grouping_count = node_count if no_rack_grouping else (len(grouping_str.split(',')) if grouping_str != "N/A" else 0)

            job_names_in_section = {cs.get('jobname') for cs in client_stats_list if cs.get('jobname') and 'fio-createfiles' not in cs.get('jobname')}
            has_specific_jobs = len(job_names_in_section - {'All clients'}) > 0

            summary_job_stats = defaultdict(lambda: {'read_iops': 0, 'write_iops': 0, 'read_bw': 0, 'write_bw': 0, 'read_lat_sum': 0, 'write_lat_sum': 0, 'read_client_count': 0, 'write_client_count': 0, 'max_runtime_ms': 0, 'workers': 0})

            for client_stat in client_stats_list:
                jobname = client_stat.get('jobname')
                if not jobname or 'fio-createfiles' in jobname or (has_specific_jobs and jobname == 'All clients'): continue
                
                client_ip = client_stat.get('hostname', 'N/A')
                read_stats, write_stats = client_stat.get('read', {}), client_stat.get('write', {})
                
                runtime_sec = max(read_stats.get('runtime', 0), write_stats.get('runtime', 0)) / 1000
                start_time = datetime.fromtimestamp(timestamp) if timestamp else None
                end_time = start_time + timedelta(seconds=runtime_sec) if start_time else None
                test_time_str = f"{start_time.strftime('%H:%M:%S')}-{end_time.strftime('%H:%M:%S')}" if start_time and end_time else "N/A"

                detailed_data = {'timestamp': start_time.strftime('%Y-%m-%d %H:%M:%S') if start_time else "N/A", 'filename': filename, 'jobname': jobname, 'hostname': client_ip, 'rack_name': get_rack_name_for_ip(client_ip) if not no_rack_grouping else client_ip, 'runtime_config': runtime_config, 'numjobs': numjobs, 'ioengine': ioengine, 'filesize': filesize, 'test_time': test_time_str, 'read_bw_mbps': read_stats.get('bw_bytes', 0) / (1024**2), 'write_bw_mbps': write_stats.get('bw_bytes', 0) / (1024**2), 'read_iops': read_stats.get('iops', 0), 'write_iops': write_stats.get('iops', 0), 'read_lat_us': read_stats.get('lat_ns', {}).get('mean', 0) / 1000, 'write_lat_us': write_stats.get('lat_ns', {}).get('mean', 0) / 1000}
                detailed_client_results.append(detailed_data)

                stats = summary_job_stats[jobname]
                stats['workers'] += 1
                stats['max_runtime_ms'] = max(stats['max_runtime_ms'], read_stats.get('runtime', 0), write_stats.get('runtime', 0))

                if read_stats.get('io_bytes', 0) > 0:
                    stats.update({'read_iops': stats['read_iops'] + read_stats.get('iops', 0), 'read_bw': stats['read_bw'] + read_stats.get('bw_bytes', 0), 'read_lat_sum': stats['read_lat_sum'] + read_stats.get('lat_ns', {}).get('mean', 0), 'read_client_count': stats['read_client_count'] + 1})
                if write_stats.get('io_bytes', 0) > 0:
                    stats.update({'write_iops': stats['write_iops'] + write_stats.get('iops', 0), 'write_bw': stats['write_bw'] + write_stats.get('bw_bytes', 0), 'write_lat_sum': stats['write_lat_sum'] + write_stats.get('lat_ns', {}).get('mean', 0), 'write_client_count': stats['write_client_count'] + 1})
            
            for jobname, stats in summary_job_stats.items():
                runtime_sec = stats['max_runtime_ms'] / 1000
                start_time = datetime.fromtimestamp(timestamp) if timestamp else None
                end_time = start_time + timedelta(seconds=runtime_sec) if start_time else None
                test_time_str = f"{start_time.strftime('%H:%M:%S')}-{end_time.strftime('%H:%M:%S')}" if start_time and end_time else "N/A"
                avg_read_lat_us = (stats['read_lat_sum'] / stats['read_client_count'] / 1000) if stats['read_client_count'] > 0 else 0
                avg_write_lat_us = (stats['write_lat_sum'] / stats['write_client_count'] / 1000) if stats['write_client_count'] > 0 else 0
                summary_results.append({'timestamp': start_time.strftime('%Y-%m-%d %H:%M:%S') if start_time else "N/A", 'filename': filename, 'jobname': jobname, 'racks_count': grouping_count, 'node_count': node_count, 'workers': stats['workers'], 'read_bw_gib': stats['read_bw'] / (1024**3), 'write_bw_gib': stats['write_bw'] / (1024**3), 'avg_read_host_bw': (stats['read_bw'] / (1024**3)) / node_count if node_count > 0 else 0, 'avg_write_host_bw': (stats['write_bw'] / (1024**3)) / node_count if node_count > 0 else 0, 'read_iops_k': stats['read_iops'] / 1000, 'write_iops_k': stats['write_iops'] / 1000, 'avg_read_host_iops': (stats['read_iops'] / 1000) / node_count if node_count > 0 else 0, 'avg_write_host_iops': (stats['write_iops'] / 1000) / node_count if node_count > 0 else 0, 'read_lat_us': avg_read_lat_us, 'write_lat_us': avg_write_lat_us, 'runtime_config': runtime_config, 'numjobs': numjobs, 'ioengine': ioengine, 'filesize': filesize, 'test_time': test_time_str, 'racks_str': grouping_str})
    return summary_results, detailed_client_results

def print_summary_table(title, results_list, sort_by=None, no_rack_grouping=False):
    if not results_list: return
    print(f"### {title} ###\n")
    rack_header = "Nodes" if no_rack_grouping else "Racks"
    rack_names_header = "Node IPs" if no_rack_grouping else "Rack Names"
    headers = ["Timestamp", "Source File", "Job Name", rack_header, "Workers", "NumJobs", "Read BW (GiB/s)", "Write BW (GiB/s)", "Avg Read/Host (GiB/s)", "Avg Write/Host (GiB/s)", "Read IOPS (k)", "Write IOPS (k)", "Avg Read/Host IOPS (k)", "Avg Write/Host IOPS (k)", "Read Lat (µs)", "Write Lat (µs)", "Runtime (Config)", "IOEngine", "Filesize", "Test Time", rack_names_header]
    col_widths = {h: len(h) for h in headers}
    col_widths.update({"Timestamp": 19, "Source File": 28, "Job Name": 25, rack_header: 5, "Workers": 7, "NumJobs": 7, "Read BW (GiB/s)": 20, "Write BW (GiB/s)": 20, "Avg Read/Host (GiB/s)": 25, "Avg Write/Host (GiB/s)": 25, "Read IOPS (k)": 15, "Write IOPS (k)": 15, "Avg Read/Host IOPS (k)": 25, "Avg Write/Host IOPS (k)": 25, "Read Lat (µs)": 15, "Write Lat (µs)": 15, "Runtime (Config)": 16, "IOEngine": 10, "Filesize": 10, "Test Time": 18, rack_names_header: 30})
    header_line = " | ".join([f"{h:<{col_widths[h]}}" for h in headers])
    print(header_line)
    print('-' * len(header_line))
    if sort_by == 'bw': sorted_results = sorted(results_list, key=lambda x: x['read_bw_gib'] + x['write_bw_gib'], reverse=True)
    elif sort_by == 'iops': sorted_results = sorted(results_list, key=lambda x: x['read_iops_k'] + x['write_iops_k'], reverse=True)
    elif sort_by == 'latency': sorted_results = sorted(results_list, key=lambda x: x['read_lat_us'] + x['write_lat_us'])
    else: sorted_results = sorted(results_list, key=lambda x: x['timestamp'])
    for data in sorted_results:
        row = [f"{data['timestamp']:<{col_widths['Timestamp']}}", f"{data['filename']:<{col_widths['Source File']}}", f"{data['jobname']:<{col_widths['Job Name']}}", f"{data['racks_count']:<{col_widths[rack_header]}}", f"{data['workers']:<{col_widths['Workers']}}", f"{data['numjobs']:<{col_widths['NumJobs']}}", f"{data['read_bw_gib']:>{col_widths['Read BW (GiB/s)']}.2f}", f"{data['write_bw_gib']:>{col_widths['Write BW (GiB/s)']}.2f}", f"{data['avg_read_host_bw']:>{col_widths['Avg Read/Host (GiB/s)']}.2f}", f"{data['avg_write_host_bw']:>{col_widths['Avg Write/Host (GiB/s)']}.2f}", f"{data['read_iops_k']:>{col_widths['Read IOPS (k)']}.2f}", f"{data['write_iops_k']:>{col_widths['Write IOPS (k)']}.2f}", f"{data['avg_read_host_iops']:>{col_widths['Avg Read/Host IOPS (k)']}.2f}", f"{data['avg_write_host_iops']:>{col_widths['Avg Write/Host IOPS (k)']}.2f}", f"{data['read_lat_us']:>{col_widths['Read Lat (µs)']}.2f}", f"{data['write_lat_us']:>{col_widths['Write Lat (µs)']}.2f}", f"{data['runtime_config']:<{col_widths['Runtime (Config)']}}", f"{data['ioengine']:<{col_widths['IOEngine']}}", f"{data['filesize']:<{col_widths['Filesize']}}", f"{data['test_time']:<{col_widths['Test Time']}}", f"{data['racks_str']:<{col_widths[rack_names_header]}}"]
        print(" | ".join(row))
    print("\n")

def print_detailed_table(title, results_list, no_rack_grouping=False):
    if not results_list: return
    print(f"### {title} ###\n")
    rack_name_header = "Node IP" if no_rack_grouping else "Rack Name"
    headers = ["Timestamp", "Source File", "Job Name", "Client IP", "Read BW (MB/s)", "Write BW (MB/s)", "Read IOPS", "Write IOPS", "Read Lat (µs)", "Write Lat (µs)", "Runtime (Config)", "NumJobs", "IOEngine", "Filesize", "Test Time"]
    if not no_rack_grouping: headers.insert(4, "Rack Name")
    col_widths = {h: len(h) for h in headers}
    col_widths.update({"Timestamp": 19, "Source File": 28, "Job Name": 25, "Client IP": 15, "Rack Name": 20, "Read BW (MB/s)": 15, "Write BW (MB/s)": 15, "Read IOPS": 15, "Write IOPS": 15, "Read Lat (µs)": 15, "Write Lat (µs)": 15, "Runtime (Config)": 16, "NumJobs": 7, "IOEngine": 10, "Filesize": 10, "Test Time": 18})
    header_line = " | ".join([f"{h:<{col_widths[h]}}" for h in headers])
    print(header_line)
    print('-' * len(header_line))
    sorted_results = sorted(results_list, key=lambda x: (x['timestamp'], x['filename'], x['jobname'], -(x['read_iops'] + x['write_iops'])))
    for data in sorted_results:
        row_data = {"Timestamp": data['timestamp'], "Source File": data['filename'], "Job Name": data['jobname'], "Client IP": data['hostname'], "Rack Name": data['rack_name'], "Runtime (Config)": data['runtime_config'], "NumJobs": data['numjobs'], "IOEngine": data['ioengine'], "Filesize": data['filesize'], "Test Time": data['test_time'], "Read BW (MB/s)": f"{data['read_bw_mbps']:.2f}", "Write BW (MB/s)": f"{data['write_bw_mbps']:.2f}", "Read IOPS": f"{data['read_iops']:.2f}", "Write IOPS": f"{data['write_iops']:.2f}", "Read Lat (µs)": f"{data['read_lat_us']:.2f}", "Write Lat (µs)": f"{data['write_lat_us']:.2f}"}
        row = []
        for h in headers:
            key_to_use = h
            if h == "Node IP": key_to_use = "Client IP"
            row_val = row_data.get(key_to_use, '')
            if h in ["Timestamp", "Source File", "Job Name", "Client IP", "Rack Name", "Node IP", "Runtime (Config)", "NumJobs", "IOEngine", "Filesize", "Test Time"]:
                row.append(f"{row_val:<{col_widths[h]}}")
            else:
                row.append(f"{row_val:>{col_widths[h]}}")
        print(" | ".join(row))
    print("\n")

def write_csv(filename, headers, results_list):
    if not results_list: return
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for data in results_list:
            row = []
            key_map = {
                "Timestamp": "timestamp", "Source File": "filename", "Job Name": "jobname", "Racks": "racks_count", 
                "Nodes": "node_count", "Workers": "workers", "NumJobs": "numjobs", "Read BW (GiB/s)": "read_bw_gib", 
                "Write BW (GiB/s)": "write_bw_gib", "Avg Read/Host (GiB/s)": "avg_read_host_bw", 
                "Avg Write/Host (GiB/s)": "avg_write_host_bw", "Read IOPS (k)": "read_iops_k", 
                "Write IOPS (k)": "write_iops_k", "Avg Read/Host IOPS (k)": "avg_read_host_iops", 
                "Avg Write/Host IOPS (k)": "avg_write_host_iops", "Read Lat (µs)": "read_lat_us", 
                "Write Lat (µs)": "write_lat_us", "Runtime (Config)": "runtime_config", "IOEngine": "ioengine", 
                "Filesize": "filesize", "Test Time": "test_time", "Rack Names": "racks_str", "Node IPs": "racks_str",
                "Client IP": "hostname", "Rack Name": "rack_name", "Read BW (MB/s)": "read_bw_mbps", 
                "Write BW (MB/s)": "write_bw_mbps", "Read IOPS": "read_iops", "Write IOPS": "write_iops", 
                "Read Lat (us)": "read_lat_us", "Write Lat (us)": "write_lat_us"
            }
            for header in headers:
                key = key_map.get(header)
                value = data.get(key)
                if isinstance(value, float):
                    row.append(f"{value:.2f}")
                else:
                    row.append(value)
            writer.writerow(row)
    print(f"Successfully exported to {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process FIO JSON results and generate summary reports.")
    parser.add_argument('files', nargs='*', help='Optional: Specific file(s) or glob patterns to process. Supports comma-separated values.')
    parser.add_argument("--detailed", action="store_true", help="Show detailed per-client performance data.")
    parser.add_argument('--sort-by', type=str, choices=['bw', 'iops', 'latency'], help='Sort the Summary Report by "bw" (desc), "iops" (desc), or "latency" (asc).')
    parser.add_argument("--export-csv", action="store_true", help="Export the reports to CSV files.")
    parser.add_argument("--no-rack-grouping", action="store_true", help="Disable grouping results by RACK names based on IP subnets.")
    parser.add_argument('--filter-job-name', type=str, help='Filter by Job Name (supports wildcards like *)')
    parser.add_argument('--filter-client-ip', type=str, help='Filter by Client IP (for detailed report, supports wildcards)')
    parser.add_argument('--filter-nodes', type=str, help='Filter by Nodes count (for summary report, supports wildcards)')
    parser.add_argument('--filter-workers', type=str, help='Filter by Workers count (for summary report, supports wildcards)')
    args = parser.parse_args()

    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_paths_to_process = []
    if not args.files:
        file_paths_to_process = glob.glob(os.path.join(script_directory, 'results_*.json'))
    else:
        all_files = set()
        for item in args.files:
            patterns = item.split(',')
            for pattern in patterns:
                pattern = pattern.strip()
                matched_files = glob.glob(os.path.join(script_directory, pattern))
                if matched_files:
                    all_files.update(matched_files)
                elif os.path.exists(pattern):
                     all_files.add(pattern)
        file_paths_to_process = sorted(list(all_files))

    summary_results, detailed_results = process_fio_json_files(file_paths_to_process, args.no_rack_grouping)

    # Apply filters
    if args.filter_job_name:
        summary_results = [r for r in summary_results if fnmatch.fnmatch(r['jobname'], args.filter_job_name)]
        detailed_results = [r for r in detailed_results if fnmatch.fnmatch(r['jobname'], args.filter_job_name)]
    if args.filter_client_ip and detailed_results:
        detailed_results = [r for r in detailed_results if fnmatch.fnmatch(r['hostname'], args.filter_client_ip)]
    if args.filter_nodes and summary_results:
        summary_results = [r for r in summary_results if fnmatch.fnmatch(str(r['node_count']), args.filter_nodes)]
    if args.filter_workers and summary_results:
        summary_results = [r for r in summary_results if fnmatch.fnmatch(str(r['workers']), args.filter_workers)]

    if summary_results: 
        print_summary_table("wekatester FIO Summary Report", summary_results, sort_by=args.sort_by, no_rack_grouping=args.no_rack_grouping)
    if args.detailed and detailed_results: 
        print_detailed_table("Detailed Per-Client Performance Report", detailed_results, no_rack_grouping=args.no_rack_grouping)

    if args.export_csv:
        timestamp_str = datetime.now().strftime('%Y%m%d_%H%M%S')
        if summary_results:
            summary_headers = ["Timestamp", "Source File", "Job Name", "Racks" if not args.no_rack_grouping else "Nodes", "Workers", "NumJobs", "Read BW (GiB/s)", "Write BW (GiB/s)", "Avg Read/Host (GiB/s)", "Avg Write/Host (GiB/s)", "Read IOPS (k)", "Write IOPS (k)", "Avg Read/Host IOPS (k)", "Avg Write/Host IOPS (k)", "Read Lat (µs)", "Write Lat (µs)", "Runtime (Config)", "IOEngine", "Filesize", "Test Time", "Rack Names" if not args.no_rack_grouping else "Node IPs"]
            write_csv(f'fio_summary_report_{timestamp_str}.csv', summary_headers, summary_results)
        
        if args.detailed and detailed_results:
            det_headers = ["Timestamp", "Source File", "Job Name", "Client IP", "Rack Name" if not args.no_rack_grouping else "Node IP", "Read BW (MB/s)", "Write BW (MB/s)", "Read IOPS", "Write IOPS", "Read Lat (us)", "Write Lat (us)", "Runtime (Config)", "NumJobs", "IOEngine", "Filesize", "Test Time"]
            write_csv(f'detailed_client_report_{timestamp_str}.csv', det_headers, detailed_results)
