# Weka Tools - Install Scripts

This directory contains diagnostic and configuration scripts to help verify Weka environment settings.

---

## 🔍 checkmemory.sh

This script collects and displays per-container memory allocation and usage information on a Weka host.

### ✔ Features
- Displays host total memory and CPU core count (online/offline).
- Lists memory statistics per Weka container:
  - Allocated memory (GB and %)
  - Virtual memory used (VM)
  - Resident Set Size (RSS)
  - Number of assigned compute cores
  - Average memory usage per core
  - Non-Weka memory reservation percentage

### 🛠 Dependencies
- `jq`
- `weka` CLI tools
- Run as root or with access to `/proc` and Weka environment

### 📦 Output Example
```
CONTAINER    ALLOC(GB)  ALLOC(%)  VM_USED(GB)  RSS_USED(GB)  CORES  AVG_ALLOC/CORE  AVG_VM/CORE  AVG_RSS/CORE  NON-WEKA(%)
compute0     123.88     32.84     352.67       72.67         19     6.52            18.56        3.83          20
...
TOTAL        169.52     44.94     785.21       154.56        40
```

---

## 🧪 scripts.d/default/901_checkcpupowerstats.sh

This script verifies CPU power-saving and boost configurations via `cpupower`.

### ✔ Checks Performed
- **P-state check**:
  - Ensures only limited P-states (e.g., P0–P1) are enabled
  - Checks if CPU Boost is disabled
- **C-state check**:
  - Ensures only basic idle states (e.g., POLL, C1) are available

### 🛠 Requirements
- `cpupower` installed and executable as root
- System BIOS settings aligned with performance tuning (disable deep C-states and boost)

### 📦 Output Example
```
✅ Limited P-states (P0–P2) → Likely BIOS setting: P-state 1 & 2 Disabled
✅ Boost state disabled
✅ Only C1 state available → Likely BIOS setting: GlobalC_stateControl & DFCstates Disabled
```

---
