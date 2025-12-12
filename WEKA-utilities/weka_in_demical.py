#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import signal
import subprocess

signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# --- SI / decimal (1000-based) ---
UNITS = ["B", "KB", "MB", "GB", "TB", "PB", "EB"]
BASE = 1000.0

def human_si(n):
    n = float(n)
    i = 0
    while abs(n) >= BASE and i < len(UNITS) - 1:
        n /= BASE
        i += 1
    return "{:.2f} {}".format(n, UNITS[i])

def is_target_line(line):
    s = line.lstrip()
    return s.startswith(("hot spare:", "drive storage:", "reads:", "writes:"))

# Match numbers including scientific notation:
NUM = r'\d+(?:\.\d+)?(?:e[+-]?\d+)?'

# 123 bytes or (123 bytes)
BYTES_RE = re.compile(r'(?P<lpar>\()?(?P<num>%s)\s+bytes(?P<rpar>\))?' % NUM, re.IGNORECASE)
# 1.23e+06 bytes/s
BPS_RE   = re.compile(r'(?P<num>%s)\s+bytes/s' % NUM, re.IGNORECASE)

def convert_line(line):
    # bytes/s -> <unit>/s  (remove "bytes/s")
    line = BPS_RE.sub(lambda m: human_si(m.group("num")) + "/s", line)

    # bytes -> <unit> (remove "bytes", keep parentheses)
    def repl(m):
        lpar = m.group("lpar") or ""
        rpar = m.group("rpar") or ""
        return lpar + human_si(m.group("num")) + rpar
    line = BYTES_RE.sub(repl, line)

    return line

def find_real_weka():
    wrapper_path = os.path.realpath(sys.argv[0])
    for d in os.environ.get("PATH", "").split(os.pathsep):
        p = os.path.realpath(os.path.join(d, "weka"))
        if os.path.isfile(p) and os.access(p, os.X_OK) and p != wrapper_path:
            return p
    for p in ["/usr/bin/weka", "/usr/local/bin/weka", "/bin/weka"]:
        if os.path.isfile(p) and os.access(p, os.X_OK) and os.path.realpath(p) != wrapper_path:
            return p
    return None

def exec_passthrough(real_weka, argv):
    os.execv(real_weka, [real_weka] + argv[1:])

def run_status_decimal(real_weka):
    # user typed: weka status
    # we run: weka status -R
    proc = subprocess.Popen(
        [real_weka, "status", "-R"],
        stdout=subprocess.PIPE,
        stderr=None,  # keep original stderr behaviour
        universal_newlines=True
    )

    try:
        for line in proc.stdout:
            if is_target_line(line):
                line = convert_line(line)
            sys.stdout.write(line)
    except BrokenPipeError:
        pass

    proc.wait()
    sys.exit(proc.returncode)

def main():
    real_weka = find_real_weka()
    if not real_weka:
        sys.stderr.write("ERROR: cannot locate real weka binary in PATH\n")
        sys.exit(127)

    argv = sys.argv

    # Rule:
    # - if exactly `weka status` (no extra args) => run `weka status -R` + convert
    # - else passthrough (including `weka status -R`)
    if len(argv) == 2 and argv[1] == "status":
        run_status_decimal(real_weka)
    else:
        exec_passthrough(real_weka, argv)

if __name__ == "__main__":
    main()
