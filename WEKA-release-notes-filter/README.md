# 🔍 Weka Release Notes Filter

A Python script for filtering and highlighting specific keywords in Weka release notes or internal notes.

This tool supports:
- Wildcard pattern search (e.g., `*nfs*`)
- Version-based filtering (e.g., `4.4.*`)
- Highlighted keyword output
- Selective search in `notes`, `internal_notes`, or both

---

## 📦 Requirements

- Python 3.6+
- Internet access (for API access to `get.weka.io`) or a local `releases.json` file

---

## 🚀 Usage

```bash
python3 weka-release-notes-filter.py [--token <API_TOKEN>] [--json_file <releases.json>] \
       [--version <pattern>] [--keyword <pattern>] [--field notes|internal_notes|both]
```

---

## 🔧 Options

| Option        | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `--token`     | API token for authentication with `get.weka.io`. Required if not using `--json_file`. |
| `--json_file` | Path to a local `releases.json` file instead of fetching from the API.      |
| `--version`   | Version pattern to match (wildcard supported). Default: `*`.                |
| `--keyword`   | Keyword pattern to match within release notes. Wildcards supported (e.g., `*nfs*`). Default: `*`. |
| `--field`     | Search target: `notes`, `internal_notes`, or `both` (default).              |

---

## ✨ Examples

```bash
# Search all 4.4.x versions for the keyword 'nfs' in both notes and internal_notes
python3 weka-release-notes-filter.py --token <API_TOKEN> --version "4.4.*" --keyword "*nfs*"

# Search internal_notes only
python3 weka-release-notes-filter.py --token <API_TOKEN> --version "4.4.*" --keyword "*WEKAPP*" --field internal_notes

# Use a local release file
python3 weka-release-notes-filter.py --json_file releases.json --version "4.4.*" --keyword "*nfs*"
```

---

## 📌 Notes

- Keywords support wildcards like `*nfs*` or `*WEKAPP*nfs*`
- Keywords will be highlighted in red in the outputs
