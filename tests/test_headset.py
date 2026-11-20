# SPDX-License-Identifier: Unlicense
"""The headset as overpressure sees it: its identity, its commands and steps, the dev status command."""

from __future__ import annotations

import io
import json
import subprocess
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

from devices.phoenix_enterprise.tooling import HEADSET, dev

ROOT = Path(__file__).resolve().parents[1]


class HeadsetTests(unittest.TestCase):
    def test_it_is_the_headset_its_headset_json_names(self):
        manifest = json.loads((ROOT / "headset.json").read_text(encoding="utf-8"))
        self.assertEqual(HEADSET.info.codename, manifest["codename"])
        self.assertEqual(HEADSET.info.name, manifest["name"])

    def test_every_command_and_step_has_its_module(self):
        commands = HEADSET.commands()
        for word, command in commands.items():
            self.assertTrue((ROOT / "tooling" / f"{command.module}.py").is_file(), word)
        for step in HEADSET.steps():
            if not step.script:
                self.assertIn(step.argv[0], [*commands, "tools"], step.key)

    def test_status_lists_what_adb_sees(self):
        seen = subprocess.CompletedProcess(["adb", "devices"], 0, "List of devices attached\nSERIAL1\tdevice\n", "")
        out = io.StringIO()
        with mock.patch.object(dev.subprocess, "run", return_value=seen) as run, redirect_stdout(out):
            self.assertEqual(dev.main(["status"]), 0)
        self.assertEqual(run.call_args.args[0][-1], "devices")
        self.assertIn("SERIAL1\tdevice", out.getvalue())

    def test_status_says_when_adb_is_missing(self):
        with mock.patch.object(dev.subprocess, "run", side_effect=FileNotFoundError("adb")):
            self.assertEqual(dev.main(["status"]), 1)


if __name__ == "__main__":
    unittest.main()
