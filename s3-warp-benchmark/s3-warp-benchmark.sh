#!/bin/bash

### Comma seperated list
warp_client="10.220.104.2,10.220.104.4,10.220.104.6"
warp_host="10.220.104.44:9000,10.220.104.42:9000,10.220.104.40:9000"
object_size="1KiB,16MiB"
###

access_key="access_key"
secret_key="secret_key"
bucket="warp-benchmark-bucket"
duation="1m"
concurrent="20"
param="--insecure --tls"

### Main ###

date_time=$(date "+%Y%m%d-%H%m%S")

PDSH_SSH_ARGS_APPEND="-o StrictHostKeyChecking=no" \
pdsh -w "$warp_client" \
'bash -c '\''if ! tmux has-session -t warp 2>/dev/null; then
  echo "$(hostname): Starting warp client...";
  cd /tmp ; tmux new-session -d -s warp "warp client"
else
  echo "$(hostname): warp client already running"
fi'\'''

sleep 3

for size in $(sed 's/,/ /g' <<< "$object_size")
do
  action=put
  date
  echo "Action: $action , Object Size: $size, Duration: $duation, Concurrent: $concurrent" | tee -a $date_time-warp-benchmark.log
  warp $action \
    --warp-client $warp_client \
    --host  $warp_host\
    --access-key $access_key \
    --secret-key $secret_key \
    --bucket $bucket \
    --duration $duation \
    --obj.size $size \
    --concurrent $concurrent \
    --disable-multipart \
    --prefix warp_${size}/ \
    --noclear $param |  grep -A 100 "Throughput" | sed 's|^|\t|g' | tee -a $date_time-warp-benchmark.log
done

for size in $(sed 's/,/ /g' <<< "$object_size")
do
  action=get
  date
  echo "Action: $action , Object Size: $size, Duration: $duation, Concurrent: $concurrent" | tee -a $date_time-warp-benchmark.log
  warp $action \
    --warp-client $warp_client \
    --host  $warp_host\
    --access-key $access_key \
    --secret-key $secret_key \
    --bucket $bucket \
    --duration $duation \
    --concurrent $concurrent \
    --list-existing \
    --prefix warp_${size}/ \
    --noclear $param |  grep -A 100 "Throughput" | sed 's|^|\t|g' | tee -a $date_time-warp-benchmark.log
done

for size in $(cut -d',' -f1 <<< "$object_size")
do
  action=stat
  date
  echo "Action: $action , Object Size: $size, Duration: $duation, Concurrent: $concurrent" | tee -a $date_time-warp-benchmark.log
  warp $action \
    --warp-client $warp_client \
    --host  $warp_host\
    --access-key $access_key \
    --secret-key $secret_key \
    --bucket $bucket \
    --duration $duation \
    --concurrent $concurrent \
    --list-existing \
    --prefix warp_${size}/ \
    --noclear $param |  grep -A 100 "Throughput" | sed 's|^|\t|g' | tee -a $date_time-warp-benchmark.log
done

### This action will clean up objects that start with warp in the bucket.
for size in $(cut -d',' -f1 <<< "$object_size")
do
  action=list
  date
  echo "Action: $action , Object Size: $size, Duration: $duation, Concurrent: $concurrent" | tee -a $date_time-warp-benchmark.log
  warp $action \
    --warp-client $warp_client \
    --host  $warp_host\
    --access-key $access_key \
    --secret-key $secret_key \
    --bucket $bucket \
    --obj.size $size \
    --duration $duation \
    --concurrent $concurrent \
    --prefix warp/ $param |  grep -A 100 "Throughput" | sed 's|^|\t|g' | tee -a $date_time-warp-benchmark.log
done

PDSH_SSH_ARGS_APPEND="-o StrictHostKeyChecking=no" \
pdsh -w $warp_client \
'bash -c '\''if tmux has-session -t warp 2>/dev/null; then echo "Stopping warp client..."; tmux kill-session -t warp; fi'\'''


sed -i '/^\tCleanup/,$d' $date_time-warp-benchmark.log

echo ""

echo ">>> Benchmark output file: $date_time-warp-benchmark.log"
