# SPDX-License-Identifier: Unlicense
"""PICO 4 Enterprise's settings in .env (PHOENIX_ENTERPRISE_ keys; env.example lists them).

What every Qualcomm Android headset names (serials, the EDL backup, the Firehose loader, the tools) is
overpressure's DeviceSettings; the headset adds only its own fields here.
"""

from __future__ import annotations

from dataclasses import dataclass

from overpressure.api.v1 import localconfig as _base


@dataclass
class Settings(_base.DeviceSettings):
    """One headset's settings: its serials, its backup and the private files its workflow uses."""

    PREFIX = "PHOENIX_ENTERPRISE_"


def load() -> Settings:
    """Return the settings from .env and the environment."""
    return _base.load(Settings)
