# SPDX-License-Identifier: Unlicense
"""PICO 4 Enterprise's host tooling: HEADSET, its commands, the window's steps and its doctor checks.

overpressure loads HEADSET from here (docs/adding-a-headset.md in overpressure). The template's one command,
dev status, shows how a command and a window step reach the headset; the headset's own workflow replaces it:
its images, its installer (install_plan, workflows), its backup (backup_set) and its logs (support_files).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from overpressure.api.v1.headset import Command, Headset, Info, Step, tools_step

if TYPE_CHECKING:
    from collections.abc import Sequence

    from overpressure.api.v1.doctor import Check, Host


class PhoenixEnterprise(Headset):
    """PICO 4 Enterprise: what overpressure's command line and window know of it."""

    info = Info("phoenix_enterprise", "PICO 4 Enterprise", "Qualcomm SM8250 / Snapdragon XR2", "the approach in one line, for Advanced mode's header")

    def commands(self) -> dict[str, Command]:
        """Return the command line: python -m overpressure --device phoenix_enterprise dev status."""
        return {"dev": Command("dev", "the development commands: dev status")}

    def steps(self) -> Sequence[Step]:
        """Return the window's steps, in order: the host tools, then what reaches the headset."""
        return (
            tools_step(),
            Step("status", "Status", "Headset", ("dev", "status"), "What this computer sees of the headset on USB."),
        )

    def dependencies(self) -> Sequence[Callable[[Host], list[Check]]]:
        """Return the doctor's checks: .env and the host tools (tooling/doctor.py)."""
        from .doctor import probes  # noqa: PLC0415  # doctor imports this package: a top-level import is circular

        return probes()


HEADSET = PhoenixEnterprise()
