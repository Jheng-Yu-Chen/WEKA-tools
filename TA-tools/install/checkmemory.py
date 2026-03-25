#!/usr/bin/env python3
import csv
import json
import re
import socket
import subprocess
import sys
from collections import defaultdict

HOST = socket.gethostname()


def run(cmd):
    try:
        return subprocess.check_output(
            cmd,
            universal_newlines=True,
            stderr=subprocess.DEVNULL
        )
    except Exception:
        return ""


def run_json(cmd):
    out = run(cmd)
    if not out.strip():
        return {}
    try:
        return json.loads(out)
    except Exception:
        return {}


def to_gib_bytes(v):
    try:
        return float(v) / 1024 / 1024 / 1024
    except Exception:
        return 0.0


def to_gib_kb(v):
    try:
        return float(v) / 1024 / 1024
    except Exception:
        return 0.0


def get_mem_info():
    out = run(["free", "-b"])
    for line in out.splitlines():
        if line.startswith("Mem:"):
            parts = line.split()
            if len(parts) >= 7:
                return {
                    "total": to_gib_bytes(parts[1]),
                    "used": to_gib_bytes(parts[2]),
                    "free": to_gib_bytes(parts[3]),
                    "buff_cache": to_gib_bytes(parts[5]),
                    "available": to_gib_bytes(parts[6]),
                }
    return {
        "total": 0.0,
        "used": 0.0,
        "free": 0.0,
        "buff_cache": 0.0,
        "available": 0.0,
    }


def get_container_names():
    out = run(["ps", "-eo", "args="])
    seen = set()
    for line in out.splitlines():
        m = re.search(r"--container-name\s+(\S+)", line)
        if m:
            seen.add(m.group(1))
    return sorted(seen)


def get_ps_stats():
    out = run(["ps", "-eo", "rss=,vsz=,args="])

    stats = defaultdict(lambda: {
        "mgmt_rss": 0.0,
        "node_rss": 0.0,
        "mgmt_virt": 0.0,
        "node_virt": 0.0,
        "node_count": 0,
    })

    for line in out.splitlines():
        parts = line.split()
        if len(parts) < 3:
            continue

        try:
            rss_kb = float(parts[0])
            virt_kb = float(parts[1])
        except Exception:
            continue

        args = parts[2:]
        container = None
        slot = None

        i = 0
        while i < len(args):
            if args[i] == "--container-name" and i + 1 < len(args):
                container = args[i + 1]
                i += 2
                continue
            if args[i] == "--slot" and i + 1 < len(args):
                slot = args[i + 1]
                i += 2
                continue
            i += 1

        if not container or slot is None:
            continue

        if slot == "0":
            stats[container]["mgmt_rss"] += to_gib_kb(rss_kb)
            stats[container]["mgmt_virt"] += to_gib_kb(virt_kb)
        else:
            stats[container]["node_rss"] += to_gib_kb(rss_kb)
            stats[container]["node_virt"] += to_gib_kb(virt_kb)
            stats[container]["node_count"] += 1

    return stats


def get_container_memory_gib(container):
    data = run_json(["weka", "local", "resources", "-C", container, "-J"])
    return to_gib_bytes(data.get("memory", 0))


def get_leadership_state(containers):
    states = {}

    process_out = run(["weka", "cluster", "process", "-l"])
    leader_out = run(["weka", "cluster", "process", "-L"])

    mgmt_containers_on_host = set()

    for line in process_out.splitlines()[1:]:
        parts = line.split()
        if len(parts) < 9:
            continue

        hostname = parts[3]
        container = parts[4]
        roles = parts[8]

        if hostname == HOST and roles == "MANAGEMENT":
            mgmt_containers_on_host.add(container)

    leader_host = None
    leader_container = None

    leader_lines = leader_out.splitlines()
    if len(leader_lines) >= 2:
        parts = leader_lines[1].split()
        if len(parts) >= 5:
            leader_host = parts[3]
            leader_container = parts[4]

    for c in containers:
        if c in mgmt_containers_on_host:
            if HOST == leader_host and c == leader_container:
                states[c] = "Leader"
            else:
                states[c] = "council"
        else:
            states[c] = "-"

    return states


def sort_key(container):
    m = re.match(r"([a-zA-Z_]+)(\d+)$", container)
    if m:
        return (m.group(1), int(m.group(2)))
    return (container, -1)


def main():
    mem = get_mem_info()
    stats = get_ps_stats()
    containers = sorted(stats.keys(), key=sort_key)
    leadership = get_leadership_state(containers)

    writer = csv.writer(sys.stdout)
    writer.writerow([
        "host",
        "container",
        "mgmt_rss_GiB",
        "node_rss_GiB",
        "mgmt_virt_GiB",
        "node_virt_GiB",
        "node_count",
        "container_memory_GiB",
        "leadership_state",
        "mem_used_GiB",
        "mem_free_GiB",
        "mem_available_GiB",
        "mem_buff_cache_GiB",
        "mem_total_GiB",
    ])

    sum_mgmt_rss = 0.0
    sum_node_rss = 0.0
    sum_mgmt_virt = 0.0
    sum_node_virt = 0.0
    sum_node_count = 0
    sum_container_memory = 0.0

    for c in containers:
        s = stats[c]
        container_memory_gib = get_container_memory_gib(c)

        writer.writerow([
            HOST,
            c,
            "{:.2f}".format(s["mgmt_rss"]),
            "{:.2f}".format(s["node_rss"]),
            "{:.2f}".format(s["mgmt_virt"]),
            "{:.2f}".format(s["node_virt"]),
            s["node_count"],
            "{:.2f}".format(container_memory_gib),
            leadership.get(c, "-"),
            "-",
            "-",
            "-",
            "-",
            "-",
        ])

        sum_mgmt_rss += s["mgmt_rss"]
        sum_node_rss += s["node_rss"]
        sum_mgmt_virt += s["mgmt_virt"]
        sum_node_virt += s["node_virt"]
        sum_node_count += s["node_count"]
        sum_container_memory += container_memory_gib

    writer.writerow([
        HOST,
        "SUM",
        "{:.2f}".format(sum_mgmt_rss),
        "{:.2f}".format(sum_node_rss),
        "{:.2f}".format(sum_mgmt_virt),
        "{:.2f}".format(sum_node_virt),
        sum_node_count,
        "{:.2f}".format(sum_container_memory),
        "-",
        "{:.2f}".format(mem["used"]),
        "{:.2f}".format(mem["free"]),
        "{:.2f}".format(mem["available"]),
        "{:.2f}".format(mem["buff_cache"]),
        "{:.2f}".format(mem["total"]),
    ])


if __name__ == "__main__":
    main()
