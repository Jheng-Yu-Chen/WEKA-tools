(
  to_entries[]
  | .key as $jobfile
  | .value.client_stats
  | map(select(.jobname and (.jobname == "All clients")))
  | group_by(.jobname)
  | map({
      "jobfile": $jobfile,
      "read_IOPS": ((map(.read.iops | select(. != null)) | add) * 100 | round / 100),
      "write_IOPS": ((map(.write.iops | select(. != null)) | add) * 100 | round / 100),
      "read_GiB/s": ((map(.read.bw_bytes | select(. != null)) | add) / 1024 / 1024 / 1024 * 100 | round / 100),
      "write_GiB/s": ((map(.write.bw_bytes | select(. != null)) | add) / 1024 /1024 / 1024 * 100 | round / 100),

      read_lat_mean_us: (
        (
          map(.read.lat_ns.mean | select(. != null)) as $rclat
          | if ($rclat | length) > 0 then ($rclat | add) / ($rclat | length) / 1000 else 0 end
        ) * 100 | round / 100
      ),

      write_lat_mean_us: (
        (
          map(.write.lat_ns.mean | select(. != null)) as $wclat
          | if ($wclat | length) > 0 then ($wclat | add) / ($wclat | length) / 1000 else 0 end
        ) * 100 | round / 100
      )
    })
)
| map(
    with_entries(
      select((.value|type) != "number" or (.value != 0))
    )
  )
