(
  to_entries[]
  | .key as $jobfile
  | .value.client_stats
  | map(select(.jobname and (.jobname == "All clients")))
  | group_by(.jobname)
  | map({
      jobfile: $jobfile,
      read_IOPS: ((map(.read.iops | select(. != null)) | add) * 100 | round / 100),
      write_IOPS: ((map(.write.iops | select(. != null)) | add) * 100 | round / 100),
      read_BW_MiBps: ((map(.read.bw_bytes | select(. != null)) | add) / 1024 / 1024 * 100 | round / 100),
      write_BW_MiBps: ((map(.write.bw_bytes | select(. != null)) | add) / 1024 / 1024 * 100 | round / 100),

      read_clat_mean_us: (
        (
          map(.read.clat_ns.mean | select(. != null)) as $rclat
          | if ($rclat | length) > 0
            then ($rclat | add) / ($rclat | length) / 1000
            else 0
            end
        ) * 100 | round / 100
      ),

      write_clat_mean_us: (
        (
          map(.write.clat_ns.mean | select(. != null)) as $wclat
          | if ($wclat | length) > 0
            then ($wclat | add) / ($wclat | length) / 1000
            else 0
            end
        ) * 100 | round / 100
      )
    })
)
