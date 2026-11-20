## What and why

<!-- One or two sentences. The title is a conventional commit: feat:, fix:, docs:, ... -->

Closes #

## Checks

- [ ] Its tests and `make lint` pass, in an overpressure checkout with this repository in `devices/phoenix_enterprise`
- [ ] New behaviour has tests; documents state the new facts
- [ ] No serials, vendor files or private data (`python scripts/check-private.py --repo devices/phoenix_enterprise`)
- [ ] Changes that write to a headset keep a recoverable path; hardware results are below

## Hardware

<!-- What ran on which headset, or "not needed". -->
