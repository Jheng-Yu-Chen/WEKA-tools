#!/bin/bash

total_mem_bytes=$(free -b | awk '/^Mem:/ {print $2}')
total_mem_gb=$(echo "$total_mem_bytes / 1024 / 1024 / 1024" | bc -l)
total_online_cpu_cores=$(lscpu  -p=CPU --online | grep -v '\#' | wc -l)
total_offline_cpu_cores=$(lscpu  -p=CPU --offline | grep -v '\#' | wc -l)

echo "Total host Online/Offline CPU cores: $total_online_cpu_cores/$total_offline_cpu_cores"
echo "Total host memory: $(printf "%.2f" "$total_mem_gb") GB"

echo ""

free -g --wide

echo ""

printf "%-12s %-12s %-12s %-14s %-14s %-8s %-16s %-14s %-14s %-14s\n" \
  "CONTAINER" "ALLOC(GB)" "ALLOC(%)" "VM_USED(GB)" "RSS_USED(GB)" "CORES" "AVG_ALLOC/CORE" "AVG_VM/CORE" "AVG_RSS/CORE" "NON-WEKA(%)"

total_alloc_gb=0
total_vm_gb=0
total_rss_gb=0
total_cores=0

containers=$(weka local ps | awk 'NR>1 {print $1}')

for container in $containers; do
    res_json=$(weka local resources -C "$container" -J)
    mem_bytes=$(echo "$res_json" | jq '.memory')
    mem_gb=$(echo "$mem_bytes / 1024 / 1024 / 1024" | bc -l)
    percent=$(echo "$mem_gb / $total_mem_gb * 100" | bc -l)
    non_weka_percent=$(echo "$res_json" | jq '.non_weka_memory_percentage')
    total_alloc_gb=$(echo "$total_alloc_gb + $mem_gb" | bc -l)

    core_ids=$(echo "$res_json" | jq '[.nodes[] | select(.roles[] != "MANAGEMENT") | .core_id] | join(",")')
    IFS=',' read -r -a core_array <<< "$(echo "$core_ids" | tr -d '"')"

    vm_kb=0
    rss_kb=0

    for pid in $(ls -1 /proc | grep -E '^[0-9]+$'); do
        if [[ -r "/proc/$pid/status" ]]; then
            cpu_line=$(awk '/Cpus_allowed_list/ {print $2}' /proc/$pid/status)
            for core in "${core_array[@]}"; do
                if [[ "$cpu_line" == "$core" || "$cpu_line" == *",$core"* || "$cpu_line" == *"-$core"* ]]; then
                    vm=$(awk '/VmSize:/ {print $2}' /proc/$pid/status)
                    rss=$(awk '/VmRSS:/ {print $2}' /proc/$pid/status)
                    [[ -n "$vm" ]] && vm_kb=$((vm_kb + vm))
                    [[ -n "$rss" ]] && rss_kb=$((rss_kb + rss))
                    break
                fi
            done
        fi
    done

    vm_gb=$(echo "$vm_kb / 1024 / 1024" | bc -l)
    rss_gb=$(echo "$rss_kb / 1024 / 1024" | bc -l)

    total_vm_gb=$(echo "$total_vm_gb + $vm_gb" | bc -l)
    total_rss_gb=$(echo "$total_rss_gb + $rss_gb" | bc -l)
    core_count=${#core_array[@]}
    total_cores=$((total_cores + core_count))

    if [[ "$core_count" -gt 0 ]]; then
        avg_alloc_core=$(echo "$mem_gb / $core_count" | bc -l)
        avg_vm_core=$(echo "$vm_gb / $core_count" | bc -l)
        avg_rss_core=$(echo "$rss_gb / $core_count" | bc -l)
    else
        avg_alloc_core=0
        avg_vm_core=0
        avg_rss_core=0
    fi

    printf "%-12s %-12.2f %-12.2f %-14.2f %-14.2f %-8d %-16.2f %-14.2f %-14.2f %-14s\n" \
        "$container" "$mem_gb" "$percent" "$vm_gb" "$rss_gb" "$core_count" "$avg_alloc_core" "$avg_vm_core" "$avg_rss_core" "$non_weka_percent"
done

total_percent=$(echo "$total_alloc_gb / $total_mem_gb * 100" | bc -l)

printf "\n%-12s %-12.2f %-12.2f %-14.2f %-14.2f %-8d\n" \
    "TOTAL" "$total_alloc_gb" "$total_percent" "$total_vm_gb" "$total_rss_gb" "$total_cores"
