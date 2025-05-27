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
    return parser.parse_args(), sys.argv

def main():
    args, raw_args = parse_args()

    show_kernel = "--kernel" in raw_args
    show_os = "--os" in raw_args
    show_release = "--release" in raw_args
    show_ofed = "--ofed" in raw_args
    show_platform = "--platform" in raw_args
    show_mode = "--mode" in raw_args
    show_customer = "--customer" in raw_args

    flag_map = {
        "--kernel": "kernel",
        "--os": "os",
        "--release": "release",
        "--ofed": "ofed",
        "--platform": "platform",
        "--mode": "mode",
        "--customer": "customer"
    }
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

            hosts = obj.get("host", {}).get("hosts", [])
            for host in hosts:
                total += 1
                os_info = host.get("os_info", {})
                kernel = os_info.get("kernel_release", "")
                os_name = os_info.get("os_name", "")
                platform = os_info.get("platform", "")
                release = host.get("software_version", "")
                ofed = host.get("host_ofed_version", "")
                mode = host.get("mode", "")

                if (
                    match(kernel, args.kernel) and
                    match(os_name, args.os) and
                    match(release, args.release) and
                    match(ofed, args.ofed) and
                    match(platform, args.platform) and
                    match(mode, args.mode) and
                    match(customer, args.customer)
                ):
                    matched.append({
                        "kernel": kernel,
                        "os": os_name,
                        "release": release,
                        "ofed": ofed,
                        "platform": platform,
                        "mode": mode,
                        "customer": customer
                    })

    print(f"\U0001F50D Filtering:")
    if show_kernel:
        print(f"  - Kernel release : {args.kernel}")
    if show_os:
        print(f"  - OS name        : {args.os}")
    if show_release:
        print(f"  - Cluster release: {args.release}")
    if show_ofed:
        print(f"  - OFED version   : {args.ofed}")
    if show_platform:
        print(f"  - Platform       : {args.platform}")
    if show_mode:
        print(f"  - Mode           : {args.mode}")
    if show_customer:
        print(f"  - Customer       : {args.customer}")

    print(f"\n\U0001F4CA Matched: {len(matched)} / {total} hosts")

    for key in combo_order:
        counter = Counter(m[key] for m in matched)
        if counter:
            label = key.upper() if key in ["os", "ofed"] else key.capitalize()
            print(f"\n\U0001F4CE Top {label} Versions:" if key in ["kernel", "ofed", "platform"] else f"\n\U0001F4CE Top {label}s:")
            for val, count in counter.most_common():
                print(f"    {count} × {val}")

    if len(combo_order) >= 2:
        combo = Counter(" | ".join(m[key] for key in combo_order) for m in matched)
        if combo:
            title = " + ".join(label.capitalize() for label in combo_order)
            print(f"\n\U0001F4CE {title} combinations:")
            for item, c in combo.most_common():
                print(f"    {c} × {item}")

if __name__ == "__main__":
    main()
