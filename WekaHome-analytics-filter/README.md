# Weka Home analytics filter

---

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

---

## ⚙️ Configuration

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

---

## 📊 Export Analytics Data

### 6. Dump all analytics into a file
```bash
homecli analytics -a > all-analytics.json
```

This exports all available analytics data to `all-analytics.json`.

---

## 🔍 Filter Analytics with `analytics-filter.py`

This is a helper script `analytics-filter.py`, requires Python 3.7+, to filter the exported analytics JSON by:

- Kernel version pattern
- OS name pattern
- Release version pattern

### Usage
```bash
python3 analytics-filter.py all-analytics.json --kernel "4.18.*" --os "CentOS*" --release "4.2.*"

python3 analytics-filter.py all-analytics.json
```

This will print:

- Matched host count
- Top kernel versions
- Top OS names
- Top release versions
- Combination statistics

> Wildcards are supported using Unix-style `*` matching.

