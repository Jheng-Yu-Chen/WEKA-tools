import subprocess
import re
import json

visited = set()

def run_help(command):
    try:
        output = subprocess.check_output(command + " --help", stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output

def parse_usage(output):
    match = re.search(r"Usage:\n((?:\s{4,}.*\n?)+)", output)
    if match:
        return [line.strip() for line in match.group(1).splitlines() if line.strip()]
    return []

def parse_arguments(output):
    args = {}
    arg_section = False
    for line in output.splitlines():
        if line.strip().lower().startswith("arguments"):
            arg_section = True
            continue
        if arg_section:
            match = re.match(r"^\s{3,}([a-zA-Z0-9\-_<>]+)\s{2,}(.*)", line)
            if match:
                name = match.group(1).strip()
                desc = match.group(2).strip()
                args[name] = desc
            elif line.strip() == "":
                break
    return args

def parse_subcommands(output):
    subcommands = {}
    subcmd_section = False
    for line in output.splitlines():
        if line.strip().lower().startswith("subcommands"):
            subcmd_section = True
            continue
        if subcmd_section and re.match(r"^\s{3,}[a-zA-Z0-9\-_]+\s{2,}", line):
            parts = re.split(r"\s{2,}", line.strip(), maxsplit=1)
            if len(parts) == 2:
                subcommands[parts[0]] = parts[1]
        elif subcmd_section and line.strip() == "":
            break
    return subcommands

def parse_options(output):
    options = {}
    opt_section = False
    last_flag = None
    for line in output.splitlines():
        if line.strip().lower().startswith("options"):
            opt_section = True
            continue
        if opt_section:
            # Check for new option line
            match = re.match(r"^\s{3,}(-{1,2}[\w,\-]+(?:,\s*-{1,2}[\w\-]+)*)\s{2,}(.*)", line)
            if match:
                flag = match.group(1).strip()
                desc = match.group(2).strip()
                options[flag] = desc
                last_flag = flag
            elif re.match(r"^\s{20,}.*", line) and last_flag:
                # Likely a continuation line (indented)
                options[last_flag] += " " + line.strip()
            elif line.strip() == "":
                break
    return options

def parse_description(output):
    lines = output.splitlines()
    desc_lines = []
    capture = False
    for line in lines:
        if line.strip().lower().startswith("description"):
            capture = True
            continue
        if capture:
            if re.match(r"^\s{4,}\S", line):
                desc_lines.append(line.strip())
            else:
                break
    return " ".join(desc_lines)

def explore_command_tree(base_command, depth=0, max_depth=4):
    if depth > max_depth or base_command in visited:
        return {}

    visited.add(base_command)

    output = run_help(base_command)
    description = parse_description(output)
    usage = parse_usage(output)
    arguments = parse_arguments(output)
    subcommands = parse_subcommands(output)
    options = parse_options(output)

    # 建立結果物件
    result = {
        "description": description
    }

    if usage:
        result["usage"] = usage
    if arguments:
        result["arguments"] = arguments
    if options:
        result["options"] = options

    if subcommands:
        structured_subcommands = {}
        for subcmd, desc in subcommands.items():
            full_cmd = f"{base_command} {subcmd}"
            print("  " * depth + f"↳ {full_cmd}")
            sub_result = explore_command_tree(full_cmd, depth + 1, max_depth)

            entry = {"description": desc}
            if sub_result.get("usage"):
                entry["usage"] = sub_result["usage"]
            if sub_result.get("arguments"):
                entry["arguments"] = sub_result["arguments"]
            if sub_result.get("options"):
                entry["options"] = sub_result["options"]
            if sub_result.get("subcommands"):
                entry["subcommands"] = sub_result["subcommands"]
            structured_subcommands[subcmd] = entry

        result["subcommands"] = structured_subcommands

    return result

# ==== 主流程 ====
all_data = {}

print("Exploring: weka")
all_data["weka"] = explore_command_tree("weka")

# 探索 hidden subcommand: weka debug
print("↳ (manual) weka debug")
debug_result = explore_command_tree("weka debug")
if debug_result:
    if "subcommands" not in all_data["weka"]:
        all_data["weka"]["subcommands"] = {}
    all_data["weka"]["subcommands"]["debug"] = debug_result

# 版本與 build
try:
    version_out = subprocess.check_output("weka --version", shell=True, universal_newlines=True).strip()
except Exception as e:
    version_out = f"Error: {e}"

try:
    build_out = subprocess.check_output("weka --build", shell=True, text=True).strip()
except Exception as e:
    build_out = f"Error: {e}"

final_output = {
    "version": version_out,
    "build": build_out,
    **all_data
}

# 從 version 字串中擷取版本號並建立檔名
version_tag = version_out.strip().split()[-1]  # 例如 "Weka CLI build 4.2.17.77" -> "4.2.17.77"
output_filename = f"weka_cli_{version_tag}.json"

with open(output_filename, "w") as f:
    json.dump(final_output, f, indent=4)

print(f"✅ Done. Saved to {output_filename}")
