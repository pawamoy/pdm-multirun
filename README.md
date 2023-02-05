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

By default, PDM Multirun reads Python versions from the
`PDM_MULTIRUN_VERSIONS` environment variable.
It is a string of `{major}.{minor}` versions,
separated by spaces, that can be found and called by PDM.

```bash
export PDM_MULTIRUN_VERSIONS="3.7 3.8 3.9 3.10 3.11"
pdm multirun pytest tests/
```

PDM Multirun sets the `PDM_MULTIRUN=1` environment variable
when running the specified command.
You can use it to decide if you should, for example,
print the current Python version in the output
of the command:

```python
import os
import sys

MULTIRUN = os.getenv("PDM_MULTIRUN", "0") == "1"

if MULTIRUN:
    py = f"{sys.version_info[0]}.{sys.version_info[1]}"  # 3.8, 3.9, etc.
    ...  # use `py` string accordingly
```

---

PDM Multirun successively runs the `pdm use` then `pdm run` internal actions.
If the command fails on a Python version, PDM Multirun stops there.
It any case, PDM Multirun will restore the Python version
saved in `.pdm.toml` (through the `pdm use` command) before exiting.
