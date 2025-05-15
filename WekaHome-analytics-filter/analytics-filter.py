#!/usr/bin/env python3
import json
import fnmatch
import argparse
from collections import Counter
from pathlib import Path

def match(val: str, pattern: str) -> bool:
    return fnmatch.fnmatch(val or "", pattern)

def parse_args():
    parser = argparse.ArgumentParser(description="Filter and summarize hosts from JSONL")
    parser.add_argument("file", type=Path, help="Path to JSON Lines file")
    parser.add_argument("--kernel", default="*", help="Kernel pattern (e.g., 4.18.*)")
    parser.add_argument("--os", default="*", help="OS name pattern (e.g., CentOS*)")
    parser.add_argument("--release", default="*", help="Release version pattern (e.g., 4.2.*)")
    return parser.parse_args()

def main():
    args = parse_args()

    matched = []
    total = 0

    with args.file.open() as f:
        for line in f:
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            hosts = obj.get("host", {}).get("hosts", [])
            for h in hosts:
                os_info = h.get("os_info", {})
                kernel = os_info.get("kernel_release", "UNKNOWN_KERNEL")
                os_name = os_info.get("os_name", "UNKNOWN_OS")
                release = h.get("release_version", obj.get("cluster", {}).get("release_version", "UNKNOWN_RELEASE"))

                total += 1
                if (
                    match(kernel, args.kernel)
                    and match(os_name, args.os)
                    and match(release, args.release)
                ):
                    matched.append((kernel, os_name, release))

    print(f"🔍 Filtering:")
    print(f"  - Kernel release : {args.kernel}")
    print(f"  - OS name        : {args.os}")
    print(f"  - Cluster release: {args.release}\n")

    print(f"📊 Matched: {len(matched)} / {total} hosts\n")

    def show_top(title, values, index):
        print(f"📎 Top {title}:")
        counter = Counter([v[index] for v in values])
        for val, count in counter.most_common():
            print(f"{count:>6} × {val}")
        print()

    show_top("Kernel Versions", matched, 0)
    show_top("OS Names", matched, 1)
    show_top("Cluster Releases", matched, 2)

    print("📎 Release + Kernel + OS combinations:")
    combo_counter = Counter(matched)
    for (k, o, r), count in combo_counter.most_common():
        print(f"{count:>6} × {r:<12} | {k:<25} | {o:<30}")

if __name__ == "__main__":
    main()

