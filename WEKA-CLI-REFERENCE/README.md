# WEKA-CLI-REFERENCE

📘 A structured reference of the `weka` CLI command tree with descriptions, usage, arguments, and options.

This repository automatically generates a fully structured JSON representation of the Weka CLI using `weka --help` and recursive subcommand parsing.

- Recursively explores all `weka` subcommands
- Parses:
  - Command descriptions
  - `Usage:` blocks
  - `Arguments:` blocks
  - `Options:` blocks
- Supports hidden subcommands (e.g. `weka debug`)

---

## 🧰 Files

| File | Description |
|------|-------------|
| `weka-cli-json-generator.py` | Python script to recursively collect and parse `weka` CLI structure |
| `weka_cli_{version}.json` | Generated command tree from `weka --help` command  |

---

## 🛠️ How to use

### 1. Install requirements (Python 3.6+)
- WEKA CLI

### 2. Run the generator script

- Outputs version-specific JSON files like: `weka_cli_4.2.17.77.json`
  
```bash
python3 weka-cli-json-generator.py
```


