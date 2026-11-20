# SPDX-License-Identifier: Unlicense
"""Host tests of PICO 4 Enterprise's tooling."""

# Tools fetched into this checkout (python -m overpressure tools) must not stand in for the tests'
# fakes: every test sees an empty tools cache.
import atexit as _atexit
import shutil as _shutil
import tempfile as _tempfile
from pathlib import Path as _Path

from overpressure.api.v1 import tools as _tools

_tools.CACHE = _Path(_tempfile.mkdtemp(prefix="overpressure-tools-"))
_atexit.register(_shutil.rmtree, _tools.CACHE, ignore_errors=True)
