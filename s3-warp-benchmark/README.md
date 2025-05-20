# S3 Warp Benchmark

This repository provides a benchmarking script for evaluating S3-compatible object storage performance using [Warp](https://github.com/minio/warp). It performs PUT, GET, and STAT tests with multiple clients, leveraging `tmux` and `pdsh` for remote session control and coordination.

## ⚠️ WARNING

> **⚠️ SEVERE WARNING: DO NOT use this script on a production or in-use S3 bucket!**
>
> The final `warp list` cleanup stage will remove all the objects on the test bucket.
>
> If run against a bucket that contains production or important data, **you risk losing all objects under that bucket**.
>
> **DO NOT use this script on buckets actively used for storing critical data.**

## Prerequisites

- [Warp](https://github.com/minio/warp) v1.1.4 or later
  - Download latest version from [warp release](https://github.com/minio/warp/releases) 
- `pdsh` (for parallel SSH)
- `tmux` (must be installed on all remote clients)

## Script Overview

The `s3-warp-benchmark.sh` script does the following:
1. Starts Warp clients on a list of remote nodes using `tmux`
2. Runs `put`, `get`, and `stat` operations across a defined object size set
3. Logs results into a timestamped log file
4. Optionally performs a list operation to verify contents
5. Stops all remote Warp clients after benchmarking

## Configuration

Modify the top section of the script:

```bash
warp_client="10.220.104.2,10.220.104.4,..."
warp_host="10.220.104.44:9000,10.220.104.42:9000,..."
object_size="4KiB,16MiB"
access_key="access_key"
secret_key="secret_key"
bucket="warp-benchmark-bucket"
duation="1m"
concurrent="20"
```

## Usage

```bash
bash s3-warp-benchmark.sh
```

After execution, a log file will be generated in the format:

```
YYYYMMDD-HHMMSS-warp-benchmark.log
```

This file contains the benchmark results with throughput and latency metrics for each test.

