#!/usr/bin/env bash
# ib_write_bw full-mesh tester
#
# Usage:
#   ./ib_write_bw.sh 192.168.0.{1..12}
#
set -euo pipefail

IPS=("$@")
if [[ ${#IPS[@]} -lt 2 ]]; then
  echo "Usage: $0 ip1 ip2 [ip3 ...]"
  exit 1
fi

DURATION=5
PROCS=8
SIZE=65535
EXPECTED_GBPS=$(ssh "${IPS[0]}" "ip -o addr show | awk -v ip=\"${IPS[0]}\" '\$0 ~ (\"inet \" ip\"/\") {print \$2; exit}' | xargs -I {} cat /sys/class/net/{}/speed | awk '{print \$1 / 1000}'")

if [[ -n "${EXPECTED_GBPS:-}" ]]; then
  echo "Expected target = ${EXPECTED_GBPS} Gb/s"
fi

for src in "${IPS[@]}"; do
  for dst in "${IPS[@]}"; do
    if [[ "$src" == "$dst" ]]; then
      continue
    fi
    dst_iface=$(ssh "$dst" "ip -o addr show | awk -v ip=\"$dst\" '\$0 ~ (\"inet \" ip\"/\") {print \$2; exit}'")
    dst_mlx=$(ssh "$dst" "ibdev2netdev | awk -v ifc=\"$dst_iface\" '\$0 ~ (\"==> \" ifc \" \") {print \$1; exit}'")
    ssh "$dst" "nohup ib_write_bw -F -s $SIZE -q $PROCS -d $dst_mlx &>/dev/null &" || { echo "Failed to start server on $ip"; exit 1; }

    src_iface=$(ssh "$src" "ip -o addr show | awk -v ip=\"$src\" '\$0 ~ (\"inet \" ip\"/\") {print \$2; exit}'")
    src_mlx=$(ssh "$dst" "ibdev2netdev | awk -v ifc=\"$src_iface\" '\$0 ~ (\"==> \" ifc \" \") {print \$1; exit}'")
    BW=$(ssh "$src" "ib_write_bw --report_gbits $dst -F -D $DURATION -s $SIZE -q $PROCS --output=bandwidth -d $src_mlx 2>&1")

    if [[ -n "$BW" ]]; then
      line="Result: $src ($src_mlx - $src_iface) -> $dst ($dst_mlx - $dst_iface) : $BW Gb/s"
      if [[ -n "${EXPECTED_GBPS:-}" ]]; then
        THRESH=$(echo "$EXPECTED_GBPS * 0.9" | bc -l)
        comp=$(echo "$BW < $THRESH" | bc -l)
        if [[ "$comp" -eq 1 ]]; then
          line="$line  ****** Below expected performance"
        fi
      fi
      echo "$line"
    else
      echo "WARNING: Could not parse BW average"
    fi
  done
done

for ip in "${IPS[@]}"; do
  ssh "$ip" "pkill -f '^ib_write_bw -F'" || true
done
