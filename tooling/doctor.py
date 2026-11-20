# SPDX-License-Identifier: Unlicense
"""PICO 4 Enterprise's checks for python -m overpressure doctor: .env and the host tools, from overpressure's shared ones."""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from overpressure.api.v1 import doctor

from . import localconfig

if TYPE_CHECKING:
    from overpressure.api.v1.doctor import Check, Host

NEEDED_FOR = "PICO 4 Enterprise's commands"


def env(_host: Host) -> list[Check]:
    """Return whether .env is there."""
    return [doctor.env_check(needed_for=NEEDED_FOR)]


def tools(host: Host) -> list[Check]:
    """Return whether adb and fastboot are there."""
    return doctor.tool_checks(host, localconfig.load(), needed_for=NEEDED_FOR)


def probes() -> list[Callable[[Host], list[Check]]]:
    """Return the checks, in the order the doctor shows them."""
    return [env, tools]
