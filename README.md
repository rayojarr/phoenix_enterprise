# PICO 4 Enterprise

[![Newest release](https://img.shields.io/github/v/release/overpressure/phoenix_enterprise?include_prereleases&label=release&color=2a66ec)](https://github.com/overpressure/phoenix_enterprise/releases)
[![CI on main](https://github.com/overpressure/phoenix_enterprise/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/overpressure/phoenix_enterprise/actions/workflows/ci.yml?query=branch%3Amain)
[![Chat: the PICO 4 Enterprise room on Matrix](https://img.shields.io/badge/chat-PICO%204%20Enterprise%20room-2a66ec?logo=matrix&logoColor=white)](https://matrix.to/#/#overpressure-phoenix_enterprise:matrix.org)

**Linux and Valve's SteamVR on PICO 4 Enterprise, installed with
[overpressure](https://github.com/overpressure/overpressure).** It replaces the headset's stock system with a
system built on Valve's Steam Frame software: SteamVR, the Steam client and its games run on the headset itself,
without a PC. The way back to the stock system is part of it.

| | |
| --- | --- |
| **Status** | In development: nothing to install yet |
| **Newest release** | none yet |
| **Your headset** | PICO 4 Enterprise; the stock system versions it needs follow with the first release |
| **Your computer** | Windows ❔ · Linux ❔ · macOS ❔ |
| **Tested on** | no headset yet |

> [!WARNING]
> Installing will erase the stock system's apps and data. The installer makes a full backup first: it is your
> way back, so keep it safe.

## What works

✅ Works · 🟡 Works, with limits · ❌ Doesn't work yet · ❔ Not tested yet · ➖ Not on this headset

### Display and comfort

| Feature | | Notes |
| --- | --- | --- |
| Both displays | ❔ | |
| Lens distance (IPD) | ❔ | |
| Standby when taken off | ❔ | |
| Cooling | ❔ | |

### Tracking

| Feature | | Notes |
| --- | --- | --- |
| Head tracking (6DoF) | ❔ | |
| Controller tracking | ❔ | |
| Hand tracking | ❔ | |
| Eye tracking | ❔ | |
| Room setup and boundary | ❔ | |
| Passthrough (room view) | ❔ | |

### Controllers

| Feature | | Notes |
| --- | --- | --- |
| Buttons, sticks and triggers | ❔ | |
| Vibration | ❔ | |
| Battery level | ❔ | |
| Pairing | ❔ | |

### Sound

| Feature | | Notes |
| --- | --- | --- |
| Speakers and volume | ❔ | |
| Microphone | ❔ | |
| Headphone jack | ❔ | |

### Connections and power

| Feature | | Notes |
| --- | --- | --- |
| Wi-Fi | ❔ | |
| Bluetooth | ❔ | |
| Battery and charging | ❔ | |
| Sleep | ❔ | |
| Battery life | ❔ | |

### Games and apps

| Feature | | Notes |
| --- | --- | --- |
| Steam store and library | ❔ | |
| Linux games | ❔ | |
| Windows games (Proton) | ❔ | |
| Android apps | ❔ | |
| PC VR over Steam Link | ❔ | |
| Video playback | ❔ | |

### Installing

| Feature | | Notes |
| --- | --- | --- |
| Install | ❔ | |
| Upgrade to a new release | ❔ | |
| Back to the stock system | ❔ | |

Everything that is still open: [the issues](https://github.com/overpressure/phoenix_enterprise/issues).

## What you need

- PICO 4 Enterprise, charged.
- A USB-C cable that carries data, not only power.
- A computer with Windows, Linux or macOS and an internet connection.

## Install

There is no release to install yet. Once there is:

1. Download [overpressure](https://github.com/overpressure/overpressure/releases) and unpack it.
2. Start it: double-click `Install.cmd` on Windows or `Install.command` on macOS, or run `sh install.sh` on Linux.
3. Accept the disclaimer, choose PICO 4 Enterprise and click **Download**.
4. Click **Install** and follow the window. It checks your computer and the headset, backs the headset up, then
   installs.
5. When the window says so, unplug the headset and put it on.

**Upgrade** installs a newer release and keeps your data. **Restore to stock** brings the stock system back from
the backup.

## If something goes wrong

The window says what state the headset is in and what to do next; starting it again goes on where it stopped. To
report a problem, click **Save logs…** on PICO 4 Enterprise's page in the window and attach the file to
[an issue](https://github.com/overpressure/phoenix_enterprise/issues/new/choose); it leaves out your headset's serial
numbers.

Questions and quick help: the [PICO 4 Enterprise room](https://matrix.to/#/#overpressure-phoenix_enterprise:matrix.org) and the
[Help room](https://matrix.to/#/#overpressure-help:matrix.org) of the project's Matrix space.

## For developers

How it works, how it is built and how it is tested: [docs/](docs/), starting with
[CLAUDE.md](CLAUDE.md) and [docs/releasing.md](docs/releasing.md).
