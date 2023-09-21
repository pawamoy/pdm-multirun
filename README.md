# PDM Multirun

[![ci](https://github.com/pawamoy/pdm-multirun/workflows/ci/badge.svg)](https://github.com/pawamoy/pdm-multirun/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://pawamoy.github.io/pdm-multirun/)
[![pypi version](https://img.shields.io/pypi/v/pdm-multirun.svg)](https://pypi.org/project/pdm-multirun/)
[![gitpod](https://img.shields.io/badge/gitpod-workspace-blue.svg?style=flat)](https://gitpod.io/#https://github.com/pawamoy/pdm-multirun)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://gitter.im/pdm-multirun/community)

A [PDM](https://github.com/pdm-project/pdm) plugin to run a command on multiple Python versions.

## Installation

With [`pipx`](https://github.com/pipxproject/pipx):

```bash
pipx install pdm
pipx inject pdm pdm-multirun
```

With [PDM](https://github.com/pdm-project/pdm):

```bash
pdm self add pdm-multirun
```

As a local-only plugin:

```toml
# pyproject.toml
[tool.pdm]
plugins = [
    "pdm-multirun",
]
```

```bash
pdm install --plugins
```

## Usage

This plugin adds a `multirun` command to PDM.
The command accepts the same parameters as the `run` command,
with an additional `-i`, `--interpreters`, `--versions` parameter
that allows to specify the interpreters to use.

```bash
pdm multirun pytest tests/
```

To specify interpreters, pass a comma-separated string
of Python versions:

```bash
pdm multirun -i 3.10,3.11 pytest tests/
```

If you use virtual environments instead,
pass their names to the `--interpreters` option
and add the `-e`, `--venvs` flag:

```bash
pdm multirun -ei 3.10,3.11 pytest tests/
```

```bash
pdm multirun -ei tests38,tests39 pytest tests/
```

You can set PDM Multirun to use virtual environments by default by
setting the `PDM_MULTIRUN_USE_VENVS` environment variable to `1`.

By default, PDM Multirun reads Python versions (or venv names)
from the `PDM_MULTIRUN_VERSIONS` environment variable.
It is a string of `{major}.{minor}` versions (or venv names),
separated by spaces, that can be found and called by PDM.

```bash
export PDM_MULTIRUN_VERSIONS="3.8 3.9 3.10 3.11 3.12"
pdm multirun pytest tests/
```

```bash
export PDM_MULTIRUN_VERSIONS="tests38 tests39 tests310"
pdm multirun pytest tests/
```

PDM Multirun sets a number of environment variables that can be used by code run
in each version.

* `PDM_MULTIRUN` set to `1` whenever PDM Multirun is being used.
* `PDM_MULTIRUN_CURRENT` is set to the name of the current interpreter or
  virtual environment (such as that passed using `-i` or
  `PDM_MULTIRUN_VERSIONS`).

You can use these variables, for example, to output metadata about the current
Python version or interpreter, like in the example below, which if invoked by
PDM Multirun, would start by printing the name of the virtual environment or
interpeter, and the version of Python being used.

**script.py**
```python
import os
import sys

MULTIRUN = os.getenv("PDM_MULTIRUN", "0") == "1"

if MULTIRUN:
    int_name = os.getenv('PDM_MULTIRUN_CURRENT', '')
    py = f"{int_name}: {sys.version_info[0]}.{sys.version_info[1]}"

    print(f"{py} - Hello from python! 👋")

# continue script as required...
```

In a scenario where you had two virtual environments, `tests38` and `tests39`,
and saved this script in a file named `example.py`, running the command:

    pdm multirun -e tests38,tests39 python example.py

Would output the text below.

```
tests38: 3.8 - Hello from python! 👋
tests39: 3.9 - Hello from python! 👋
```

---

PDM Multirun successively runs the `pdm use` then `pdm run` internal actions.
By default, if PDM cannot "use" an interpreter/venv, it continues with the next.

```bash
# will continue with 3.8 even if 3.7 is not available
pdm multirun -i 3.7,3.8 pytest tests/
```

You can tell it to fail instead with the `-f`, `--fail-fast` flag:

```bash
# will stop at 3.7 if it's not available
pdm multirun -fi 3.7,3.8 pytest tests/
```

If the command you run fails on a Python version, PDM Multirun stops there.
In any case, PDM Multirun will restore the Python interpreter
saved in `.pdm-python` (through the `pdm use` command) before exiting.
