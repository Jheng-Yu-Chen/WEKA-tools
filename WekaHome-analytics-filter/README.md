# Weka Home analytics filter

---

## 🛠️ Requirements

- Python 3.6+


## 🔧 Prerequisites and Setup (macOS)

### 1. Install Go
```bash
brew install go
```

### 2. Download and compile the CLI tool
```bash
git clone https://github.com/weka/gohomecli.git
cd gohomecli
go build -o gohomecli ./cmd/homecli
```

### 3. Move the binary to your system path
```bash
cp gohomecli /usr/local/bin/homecli
```

### 4. List configured sites
This will create or reference your config at `~/.config/home-cli/config.toml`:

```bash
homecli config site list
```

### 5. Setup your API key
Replace `<token>` with your actual API key:
```bash
sed -i '' 's/api_key = """"/api_key = ""<token>""/g' ~/.config/home-cli/config.toml
```

### 6. Dump all analytics into a file
```bash
homecli analytics -a > all-analytics.json
```

This exports all available analytics data to `all-analytics.json`.

---

## 🔍 Filter Analytics with `analytics-filter.py`

This script parses a JSON file exported from WEKA analytics and provides filtering and summary reports for host information such as kernel version, OS name, OFED version, platform type, and mode.

## ✅ Features

- Pattern-based filtering (wildcard `*` support)
- Case-insensitive matching
- Dynamically ordered summary and combination statistics
- Multiple metadata fields supported

## 🧾 Usage

```bash
python3 filter_json.py <json_file> [--kernel <pattern>] [--os <pattern>] [--release <pattern>] [--ofed <pattern>] [--platform <pattern>] [--mode <pattern>]
```

### Example

```bash
python3 filter_json.py 20250515-analytics.json --os "SUSE*" --kernel "5.*" --release "4.2.*"
```

### Supported Options

| Option       | Description                            | Example                 |
|--------------|----------------------------------------|-------------------------|
| `--kernel`   | Match kernel release (wildcard allowed) | `--kernel "4.18.*"`    |
| `--os`       | Match OS name                          | `--os "rocky*"`       |
| `--release`  | Match software version                 | `--release "4.2.*"`    |
| `--ofed`     | Match OFED version                     | `--ofed "5.1*"`        |
| `--platform` | Match hardware platform type           | `--platform "x86_64"`  |
| `--mode`     | Match host mode                        | `--mode "backend"`     |

> All filters are optional. Default value for each is `*`.

