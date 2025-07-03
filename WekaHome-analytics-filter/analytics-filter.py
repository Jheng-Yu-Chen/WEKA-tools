#!/usr/bin/env python3
import json
import fnmatch
import argparse
import sys
from collections import Counter
from pathlib import Path

def match(val: str, pattern: str) -> bool:
    return fnmatch.fnmatch((val or "").lower(), pattern.lower())

def parse_args():
    parser = argparse.ArgumentParser(description="Filter and summarize hosts from JSONL")
    parser.add_argument("file", type=Path, help="Path to JSON Lines file")
    parser.add_argument("--release", default="*", help="Release version pattern (e.g., 4.2.*)")
    parser.add_argument("--kernel", default="*", help="Kernel pattern (e.g., 4.18.*)")
    parser.add_argument("--os", default="*", help="OS name pattern (e.g., Rocky*)")
    parser.add_argument("--ofed", default="*", help="OFED version pattern (e.g., 5.1*)")
    parser.add_argument("--platform", default="*", help="Platform pattern (e.g., x86_64, aarch64)")
    parser.add_argument("--mode", default="*", help="Mode pattern (e.g., client, backend)")
    parser.add_argument("--customer", default="*", help="Customer Name")
    parser.add_argument("--cluster", default="*", help="Cluster Name")
    parser.add_argument("--cpu_is_dedicated", type=str, choices=['true', 'false', 'udp'], help="Filter by CPU dedicated status of nodes (true/false/udp)")
    return parser.parse_args(), sys.argv

def main():
    args, raw_args = parse_args()

    # Determine which filters were explicitly provided in the command line
    show_kernel = "--kernel" in raw_args
    show_os = "--os" in raw_args
    show_release = "--release" in raw_args
    show_ofed = "--ofed" in raw_args
    show_platform = "--platform" in raw_args
    show_mode = "--mode" in raw_args
    show_customer = "--customer" in raw_args
    show_cluster = "--cluster" in raw_args
    show_cpu_is_dedicated = "--cpu_is_dedicated" in raw_args

    flag_map = {
        "--kernel": "kernel",
        "--os": "os",
        "--release": "release",
        "--ofed": "ofed",
        "--platform": "platform",
        "--mode": "mode",
        "--customer": "customer",
        "--cluster": "cluster",
        "--cpu_is_dedicated": "cpu_is_dedicated_status"
    }

    # Define display labels for output
    display_label_map = {
        "kernel": "Kernel",
        "os": "OS",
        "release": "Cluster Release",
        "ofed": "OFED",
        "platform": "Platform",
        "mode": "Mode",
        "customer": "Customer",
        "cluster": "Cluster Name",
        "cpu_is_dedicated_status": "CPU Dedicated"
    }
    
    # Define mapping for 'true'/'false'/'udp' values for display
    cpu_dedicated_display_map = {
        'true': 'dpdk_cpu_is_dedicated',
        'false': 'dpdk_cpu_is_non-dedicated',
        'udp': 'udp_mode'
    }

    # Determine the order of combination fields based on user input
    combo_order = [flag_map[arg] for arg in raw_args if arg in flag_map]

    matched = []
    total = 0

    with args.file.open() as f:
        for line in f:
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            customer = obj.get("_meta", {}).get("customer_name", "")
            cluster = obj.get("cluster", {}).get("name", "")

            # Store hosts and nodes in lookup dictionaries for easier access
            hosts_by_id = {h['id']: h for h in obj.get("host", {}).get("hosts", [])}
            nodes_by_host_id = {}
            for node in obj.get("node", {}).get("nodes", []):
                host_id = node.get('host_id')
                if host_id not in nodes_by_host_id:
                    nodes_by_host_id[host_id] = []
                nodes_by_host_id[host_id].append(node)

            for host_id, host_data in hosts_by_id.items():
                total += 1
                os_info = host_data.get("os_info", {})
                kernel = os_info.get("kernel_release", "")
                os_name = os_info.get("os_name", "")
                platform = os_info.get("platform", "")
                release = host_data.get("software_version", "")
                ofed = host_data.get("host_ofed_version", "")
                mode = host_data.get("mode", "")

                # Apply existing filters to host data
                if not (
                    match(kernel, args.kernel) and
                    match(os_name, args.os) and
                    match(release, args.release) and
                    match(ofed, args.ofed) and
                    match(platform, args.platform) and
                    match(mode, args.mode) and
                    match(customer, args.customer) and
                    match(cluster, args.cluster)
                ):
                    continue

                # Apply new cpu_is_dedicated filter logic if specified
                passed_cpu_dedicated_filter = True
                if args.cpu_is_dedicated is not None:
                    filter_type = args.cpu_is_dedicated.lower()
                    host_has_matching_node = False
                    
                    associated_nodes = nodes_by_host_id.get(host_id, [])
                    for node_data in associated_nodes:
                        node_roles = node_data.get('roles', [])
                        # Exclude nodes with 'MANAGEMENT' role
                        if "MANAGEMENT" in node_roles:
                            continue

                        node_is_dpdk = node_data.get('is_dpdk') # Get is_dpdk attribute for all cases
                        
                        if filter_type == 'true':
                            target_cpu_dedicated_bool = True
                            node_cpu_dedicated_val = node_data.get('cpu_is_dedicated')
                            if (node_cpu_dedicated_val is not None and node_cpu_dedicated_val == target_cpu_dedicated_bool) and \
                                (node_is_dpdk is not None and node_is_dpdk == True): # is_dpdk must be true for 'true'
                                host_has_matching_node = True
                                break
                        elif filter_type == 'false':
                            target_cpu_dedicated_bool = False
                            node_cpu_dedicated_val = node_data.get('cpu_is_dedicated')
                            if (node_cpu_dedicated_val is not None and node_cpu_dedicated_val == target_cpu_dedicated_bool) and \
                                (node_is_dpdk is not None and node_is_dpdk == True): # is_dpdk must be true for 'false'
                                host_has_matching_node = True
                                break
                        elif filter_type == 'udp':
                            # For 'udp', filter condition is roles without MANAGEMENT AND is_dpdk is false
                            if node_is_dpdk is not None and node_is_dpdk == False:
                                host_has_matching_node = True
                                break
                    
                    if not host_has_matching_node:
                        passed_cpu_dedicated_filter = False
                
                if not passed_cpu_dedicated_filter:
                    continue

                matched_entry = {
                    "kernel": kernel,
                    "os": os_name,
                    "release": release,
                    "ofed": ofed,
                    "platform": platform,
                    "mode": mode,
                    "customer": customer,
                    "cluster": cluster
                }
                
                # Store the displayed string for cpu_is_dedicated_status if filter was applied
                if args.cpu_is_dedicated is not None:
                    matched_entry["cpu_is_dedicated_status"] = cpu_dedicated_display_map.get(args.cpu_is_dedicated.lower(), args.cpu_is_dedicated.lower())
                
                matched.append(matched_entry)

    print(f"\U0001F50D Filtering:")
    if show_kernel:
        print(f"  - Kernel release   : {args.kernel}")
    if show_os:
        print(f"  - OS name          : {args.os}")
    if show_release:
        print(f"  - Cluster release  : {args.release}")
    if show_ofed:
        print(f"  - OFED version     : {args.ofed}")
    if show_platform:
        print(f"  - Platform         : {args.platform}")
    if show_mode:
        print(f"  - Mode             : {args.mode}")
    if show_customer:
        print(f"  - Customer         : {args.customer}")
    if show_cluster:
        print(f"  - Cluster name     : {args.cluster}")
    if show_cpu_is_dedicated:
        print(f"  - CPU Dedicated    : {cpu_dedicated_display_map.get(args.cpu_is_dedicated.lower(), args.cpu_is_dedicated.lower())}")

    print(f"\n\U0001F4CA Matched: {len(matched)} / {total} hosts")

    for key in combo_order:
        counter = Counter(m.get(key, '') for m in matched)
        if counter:
            label_to_print = display_label_map.get(key, key.capitalize())
            if key in ["kernel", "ofed", "platform", "release"]:
                print(f"\n\U0001F4CE Top {label_to_print} Versions:")
            elif key == "cpu_is_dedicated_status":
                print(f"\n\U0001F4CE Top {label_to_print} Status:")
            else:
                print(f"\n\U0001F4CE Top {label_to_print}s:")
            
            for val, count in counter.most_common():
                print(f"    {count} × {val}")

    if len(combo_order) >= 2:
        combo = Counter(" | ".join(str(m.get(key, '')) for key in combo_order) for m in matched)
        if combo:
            title = " + ".join(display_label_map[key] for key in combo_order)
            print(f"\n\U0001F4CE {title} combinations:")
            for item, c in combo.most_common():
                print(f"    {c} × {item}")

if __name__ == "__main__":
    main()
