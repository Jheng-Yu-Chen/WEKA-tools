# bios\_tool

## Project Origin
This tool is a fork of the Weka bios_tools repository, based on commit:

```
commit 9c1034b9888c9d1680d553fb0d723ba49ff62bec
Merge: 85e98e8 478ec1e
Author: Vince Fleming <46109871+vince-weka@users.noreply.github.com>
Date:   Thu Mar 27 08:50:02 2025 -0400
```

A tool for viewing/setting BIOS settings for Weka servers

```text
usage: bios_tool [-h] [-c [HOSTCONFIGFILE]] [-b [BIOS]] [--bmc_config] [--fix] [--reboot] [--dump] [--reset_bios] [--diff DIFF DIFF]
                 [--bmc_ips [BMC_IPS ...]] [--bmc_username BMC_USERNAME] [--bmc_password BMC_PASSWORD] [--arch {AMD,Intel}] [-v] [--version]

View/Change BIOS Settings on servers

optional arguments:
  -h, --help            show this help message and exit
  -c [HOSTCONFIGFILE], --hostconfigfile [HOSTCONFIGFILE]
                        filename of host config file
  -b [BIOS], --bios [BIOS]
                        BIOS configuration filename
  --bmc_config          Configure the BMCs to allow RedFish access
  --fix                 Correct any BIOS settings that do not match the definition
  --reboot              Reboot server if changes have been made
  --dump                Print out BIOS settings only
  --reset_bios          Reset BIOS to default settings. To also reboot, add the --reboot option
  --diff DIFF DIFF      Compare 2 hosts' BIOS settings
  --bmc_ips [BMC_IPS ...]
                        A list of hosts to configure, or none to use cluster beacons
  --bmc_username BMC_USERNAME
                        A username to use on all hosts in --bmc_ips
  --bmc_password BMC_PASSWORD
                        A password to use on all hosts in --bmc_ips
  --arch {AMD,Intel}    Optional. Limit BIOS setting checks/fixes to a specific CPU architecture (DEFAULT: AMD)
  -v, --verbose         Enable verbose mode
  --version             Report program version and exit
```

## Getting Started

There are 2 configuration files for bios\_tool: a host configuration file ("host\_config.yml" or host\_config.csv) and a BIOS settings configuration file ("bios\_config.yml").
You can either use these default names or override the configuration file names using the provided command-line switches `-c/--hostconfigfile`, `-b/--bios`, or `--bmc_ips`.

### host\_config.yml or csv

The `host_config.yml` or `.csv` file defines the list of hosts and their login credentials for the BMC (IPMI, iLO, iDRAC). It can be in YAML or CSV format. The file extension `.yml` or `.csv` determines the format.

**CSV example:**

```csv
name,user,password
172.29.3.164,ADMIN,_PASSWORD_1!
172.29.3.1,Administrator,Administrator
172.29.1.74,root,Administrator
172.29.1.75,root,Administrator
```

**YAML example:**

```yaml
hosts:
  - name: 172.29.3.1
    user: Administrator
    password: Administrator
  - name: 172.29.3.2
    user: Administrator
    password: Administrator
```

### bios\_config.yml (and others)

The `bios_config.yml` file defines general BIOS settings you want to set on the servers defined in the host config file.

The format is standard YAML:

```yaml
Dell:
  AMD:
    LogicalProc: Disabled
    NumaNodesPerSocket: "1"
    PcieAspmL1: Disabled
    ProcCStates: Disabled
    ProcPwrPerf: MaxPerf
```

Supported manufacturers: `Dell`, `Hpe`, `Lenovo`, `Supermicro` (matched via RedFish OEM field).
Supported architectures: `AMD` and `Intel`.

## Default Behavior

With no overrides, `bios_tool` scans the hosts in `host_config.csv` and checks whether BIOS settings match the definitions in `bios_config.yml`. No changes are made (read-only mode).

**Example output:**

```
Fetching BIOS settings of host 172.29.3.1
No changes are needed on 172.29.3.1
...
172.29.3.4: BIOS setting CStateEfficiencyMode is Enabled, but should be Disabled
```

## Optional Behaviors

### BMC Configuration mode

Use `--bmc_config` to SSH into each server and enable RedFish + IPMI Over LAN.

### Fix Mode

Use `--fix` to apply settings from the BIOS config file.
Requires `--reboot` if you want changes to take effect.

### Reboot Option

Use `--reboot` with `--fix` to reboot only modified hosts.

### Dump Option

Use `--dump` to output the current BIOS settings of each server (read-only).

### Diff Option

Use `--diff` to compare BIOS settings between two servers.

**Example diff output:**

```
Setting                     172.29.3.1                 172.29.3.6
--------------------------  -------------------------  ----------------------------
ApplicationPowerBoost       Disabled                   Enabled
CStateEfficiencyMode        Disabled                   Enabled
```

### Architecture Specification

Use `--arch {AMD,Intel}` to restrict checks and fixes to systems with the specified CPU architecture.

**Example:**

```bash
bios_tool --fix --arch AMD
```

### Command-line Host Specification

Use `--bmc_ips` with IP list, `--bmc_username`, and `--bmc_password` to bypass the config file.

**Example:**

```bash
bios_tool --bmc_ips 10.1.1.1 10.1.1.2 --bmc_username root --bmc_password secret
```

### Version Option

Use `--version` to print the current version and exit.

