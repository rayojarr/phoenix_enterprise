# CLAUDE.md: PICO 4 Enterprise (phoenix_enterprise)

Guidance for working on PICO 4 Enterprise's module for overpressure, this repository, with its own releases
(overpressure's [CLAUDE.md](https://github.com/overpressure/overpressure/blob/main/CLAUDE.md) has the general
rules, [GOVERNANCE.md](https://github.com/overpressure/.github/blob/main/GOVERNANCE.md) who reviews and releases
what). This repository is dropped into `devices/phoenix_enterprise/` of an overpressure checkout (for development a clone:
`git clone https://github.com/overpressure/phoenix_enterprise devices/phoenix_enterprise`). Paths are relative to this repository;
commands run from the overpressure checkout's root. The tooling and its tests import overpressure only through
`overpressure.api.v1`, and never its window or command line. CI runs this repository against overpressure's
`main`.

## Where things stand

The status of each feature is in [README.md](README.md); what comes next is this repository's GitHub issues.
Keep the README current: when a result changes, change its row.

## Backlog

This repository's GitHub issues; the rules are in overpressure's CLAUDE.md.

## Documentation

The headset's documents are in `docs/` here ([docs/README.md](docs/README.md) lists them), its overview for
owners in `README.md`, which follows overpressure's headset README template. `python scripts/check-docs.py --repo
devices/phoenix_enterprise` checks the links and the README; a link may not leave this repository, so links to
overpressure are GitHub URLs. Releasing: [docs/releasing.md](docs/releasing.md).

## Layout

- `headset.json`: codename, name, version, the headset interface it was made for (`api`); a release zip carries its
  commit and date.
- `tooling/`: the host tooling, reached as `python -m overpressure --device phoenix_enterprise COMMAND`. `__init__.py` holds
  `HEADSET` (its commands, the window's steps, its doctor checks); `localconfig.py` its `.env` settings
  (`PHOENIX_ENTERPRISE_` keys, `env.example`); `doctor.py` its checks; `dev.py` the development commands.
- `tests/`: host tests, no hardware. `docs/`: its documents. `.github/`: CI and the release workflow.
- Private and generated, ignored, at the overpressure checkout's root: `backup/`, `assets/`, `cache/`, `out/`,
  `.env`.

## Commands

From the overpressure checkout's root:

```sh
python -m unittest discover -t . -s devices/phoenix_enterprise/tests   # host tests, seconds, no hardware
uv run ruff format --check devices/phoenix_enterprise && uv run ruff check devices/phoenix_enterprise && uv run ty check devices/phoenix_enterprise
python -m overpressure devices                                # it loads, or why not
python -m overpressure --device phoenix_enterprise steps               # its steps and their command lines
python -m overpressure --device phoenix_enterprise dev status          # what this computer sees of the headset
```

## Hard rules

- **Private data.** Never commit or redistribute device data or vendor files: `backup/`, `assets/`, `out/`,
  `cache/` and `.env` are ignored on purpose. Docs and code must not contain device serials or similar
  identifiers; they belong in `.env`.
- **Hardware actions need a recoverable path.** Before anything writes to the headset, a verified backup exists
  and the way back to stock is known to work. Ask before the first flash or low-level action in a new
  conversation. Name here what must never be written on this headset, and what crashes its kernel.

## Hardware workflow

How the headset is put into development mode, flashed, reached and brought back to stock, as it is found.
