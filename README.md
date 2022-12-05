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
