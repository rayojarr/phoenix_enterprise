# SPDX-License-Identifier: Unlicense
"""PICO 4 Enterprise's development commands.

    python -m overpressure --device phoenix_enterprise dev status   what this computer sees of the headset on USB

A starting point: it reads nothing but adb's list. The headset's own commands (images, flashing, a
development loop) go here or into modules of their own, each named in HEADSET.commands().
"""

from __future__ import annotations

import argparse
import subprocess
import sys

from . import localconfig


def status() -> int:
    """Print adb's devices, with the adb .env names (or the one python -m overpressure tools fetched)."""
    adb = localconfig.load().tool("adb")
    try:
        done = subprocess.run([adb, "devices"], capture_output=True, text=True, timeout=30, check=False)  # noqa: S603  # adb, no shell
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(f"error: {adb}: {exc}", file=sys.stderr)
        return 1
    print(done.stdout.strip() or done.stderr.strip())
    return done.returncode


def main(argv: list[str]) -> int:
    """Run a development command."""
    parser = argparse.ArgumentParser(prog="python -m overpressure --device phoenix_enterprise dev")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="what this computer sees of the headset on USB")
    args = parser.parse_args(argv)
    if args.command == "status":
        return status()
    return 2
