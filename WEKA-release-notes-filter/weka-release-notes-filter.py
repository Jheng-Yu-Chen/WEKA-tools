#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import fnmatch
import os
import re
import requests
from datetime import datetime
from html import unescape

# ANSI color codes
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'


def match_pattern(pattern, text):
    return fnmatch.fnmatchcase(text.lower(), pattern.lower())


def highlight_keyword(text, pattern):
    if pattern == "*":
        return text
    try:
        # 將 pattern 拆成多個關鍵字進行 highlight，例如 "*abc*xyz*" => ["abc", "xyz"]
        keywords = [k for k in pattern.strip("*").split("*") if k]
        for kw in keywords:
            text = re.sub(f"(?i)({re.escape(kw)})", RED + r"\1" + RESET, text)
        return text
    except Exception:
        return text


def format_inline_code(text):
    return re.sub(r"`([^`]+)`", r"\033[96m`\1`\033[0m", text)


def filter_releases(data, version_pattern="*", keyword_pattern="*", field_choice="both"):
    results = []
    for obj in data.get("objects", []):
        release_id = obj.get("id", "")
        created_at = obj.get("created_at", "")
        notes = obj.get("notes", "")
        internal_notes = obj.get("internal_notes", "")

        if match_pattern(version_pattern, release_id):
            fields_to_check = []
            if field_choice == "notes":
                fields_to_check.append(("notes", notes))
            elif field_choice == "internal_notes":
                fields_to_check.append(("internal_notes", internal_notes))
            else:  # both
                fields_to_check = [("notes", notes), ("internal_notes", internal_notes)]

            for field_name, text in fields_to_check:
                if text:
                    if keyword_pattern == "*":
                        results.append((release_id, created_at, field_name, text.strip()))
                    else:
                        for line in text.splitlines():
                            if match_pattern(keyword_pattern, line):
                                highlighted = highlight_keyword(line.strip(), keyword_pattern)
                                formatted = format_inline_code(highlighted)
                                results.append((release_id, created_at, field_name, formatted))

    results.sort(key=lambda x: datetime.strptime(x[1], "%Y-%m-%dT%H:%M:%S.%fZ"), reverse=True)
    return results


def main():
    parser = argparse.ArgumentParser(description="Search Weka release notes/internal_notes for specific patterns.")
    parser.add_argument("--token", help="API token for authentication with get.weka.io")
    parser.add_argument("--version", default="*", help="Version pattern to match (wildcard supported, e.g., '4.4.2*')")
    parser.add_argument("--keyword", default="*", help="Keyword pattern to search in notes/internal_notes (wildcard supported, e.g., '*nfs*')")
    parser.add_argument("--field", choices=["notes", "internal_notes", "both"], default="both",
                        help="Which field to search in: 'notes', 'internal_notes', or 'both' (default: both)")
    parser.add_argument("--json_file", help="Optional path to local releases.json file")

    args = parser.parse_args()

    if args.json_file:
        if not os.path.isfile(args.json_file):
            print(RED + "[Error] File not found:" + RESET, args.json_file)
            return
        with open(args.json_file, 'r') as f:
            data = json.load(f)
    elif args.token:
        try:
            resp = requests.get(
                "https://get.weka.io/dist/v1/release",
                auth=(args.token, "")
            )
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            print(RED + f"[Error] Failed to fetch data from API: {e}" + RESET)
            return
    else:
        print(RED + "[Error] Please specify either --json_file or --token" + RESET)
        return

    matches = filter_releases(
        data,
        version_pattern=args.version,
        keyword_pattern=args.keyword,
        field_choice=args.field
    )

    if not matches:
        print(YELLOW + "No matches found." + RESET)
        return

    if args.keyword == "*":
        grouped = {}
        for version, created_at, field, content in matches:
            key = (version, created_at)
            grouped.setdefault(key, {}).setdefault(field, content)

        for (version, created_at), fields in sorted(grouped.items(), key=lambda x: x[0][1], reverse=True):
            print(f"{CYAN}## Version: {version} ({created_at}){RESET}\n")
            for field in ["notes", "internal_notes"]:
                if field in fields:
                    print(f"{YELLOW}### {field}{RESET}\n\n{fields[field]}\n")
    else:
        for version, created_at, field, line in matches:
            print(f"{CYAN}[{created_at}] ({version}, {field}):{RESET} {line}")


if __name__ == "__main__":
    main()

