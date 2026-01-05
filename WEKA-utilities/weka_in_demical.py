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

def get_scale(name, default=1.0):
    v = os.environ.get(name, "")
    if not v:
        return float(default)
    try:
        return float(v)
    except ValueError:
        return float(default)

# Scales
# - WEKA_IO_SCALE: scales reads/writes bytes/s
# - WEKA_OPS_SCALE: scales operations ops/s
IO_SCALE  = get_scale("WEKA_IO_SCALE", 1.0)
OPS_SCALE = get_scale("WEKA_OPS_SCALE", 1.0)

def is_target_line(line):
    s = line.lstrip()
    return s.startswith(("hot spare:", "drive storage:", "reads:", "writes:", "operations:"))

NUM = r'\d+(?:\.\d+)?(?:e[+-]?\d+)?'

# (123 bytes) / 123 bytes
BYTES_RE = re.compile(r'(?P<lpar>\()?(?P<num>%s)\s+bytes(?P<rpar>\))?' % NUM, re.IGNORECASE)

# reads/writes: <num> bytes/s
BPS_RE = re.compile(r'(?P<num>%s)\s+bytes/s' % NUM, re.IGNORECASE)

# operations: <num> ops/s
OPS_RE = re.compile(r'(?P<num>%s)\s+ops/s' % NUM, re.IGNORECASE)

def convert_line(line):
    s = line.lstrip()

    # 1) Scale + convert bytes/s (only for reads/writes lines)
    if s.startswith(("reads:", "writes:")):
        def repl_bps(m):
            scaled = float(m.group("num")) * IO_SCALE
            return human_si(scaled) + "/s"
        line = BPS_RE.sub(repl_bps, line)

    # 2) Convert bytes -> SI unit (keep parentheses) (hot spare / drive storage)
    if s.startswith(("hot spare:", "drive storage:")):
        def repl_bytes(m):
            lpar = m.group("lpar") or ""
            rpar = m.group("rpar") or ""
            return lpar + human_si(m.group("num")) + rpar
        line = BYTES_RE.sub(repl_bytes, line)

    # 3) Scale operations ops/s
    if s.startswith("operations:"):
        def repl_ops(m):
            scaled = float(m.group("num")) * OPS_SCALE
            # Keep it clean: integer if it is effectively an int
            if abs(scaled - round(scaled)) < 1e-9:
                return "{} ops/s".format(int(round(scaled)))
            return "{:.2f} ops/s".format(scaled)
        line = OPS_RE.sub(repl_ops, line)

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
    proc = subprocess.Popen(
        [real_weka, "status", "-R"],
        stdout=subprocess.PIPE,
        stderr=None,
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

    # Only intercept exactly: `weka status`
    if len(sys.argv) == 2 and sys.argv[1] == "status":
        run_status_decimal(real_weka)
    else:
        exec_passthrough(real_weka, sys.argv)

if __name__ == "__main__":
    main()
