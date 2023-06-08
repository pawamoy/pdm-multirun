"""PDM Multirun plugin."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

from pdm import termui
from pdm.cli import actions
from pdm.cli.commands.run import Command as RunCommand
from pdm.cli.commands.run import Project
from pdm.cli.hooks import HookManager

if TYPE_CHECKING:
    import argparse

    from pdm.core import Core

PYTHON_VERSIONS = os.getenv("PDM_MULTIRUN_VERSIONS", "").split()
PYTHON_VERSIONS = PYTHON_VERSIONS or [f"python3.{minor}" for minor in range(7, 12)]


def _interpreters(versions: str) -> list[str]:
    return [f"python{version.strip()}" for version in versions.split(",")]


class MultirunCommand(RunCommand):
    """Run a command under multiple Python versions."""

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:  # noqa: D102
        super().add_arguments(parser)
        parser.add_argument(
            "-f",
            "--fail-fast",
            help="Exit as soon as an interpreter cannot be found or used",
            action="store_true",
            default=False,
        )
        parser.add_argument(
            "-i",
            "--interpreters",
            "--versions",
            help="Comma-separated list of Python versions to run the command with",
            type=_interpreters,
        )

    def handle(self, project: Project, options: argparse.Namespace) -> None:  # noqa: D102
        os.environ["PDM_MULTIRUN"] = "1"
        old_python = str(project.environment.interpreter.path)
        project.core.ui.echo(f"Current interpreter: {old_python}", verbosity=termui.Verbosity.DETAIL)
        for python_version in options.interpreters or PYTHON_VERSIONS:
            try:
                self._use(project, options, python_version)
            except Exception:  # noqa: BLE001
                if options.fail_fast:
                    raise
                project.core.ui.echo(f"Skipped interpreter: {python_version}", verbosity=termui.Verbosity.DETAIL)
                continue
            try:
                super().handle(project, options)
            except SystemExit as exit:
                if exit.code:
                    self._use(project, options, old_python)
                    raise
        project.core.ui.echo(f"Restoring interpreter: {old_python}", verbosity=termui.Verbosity.DETAIL)
        self._use(project, options, old_python)
        os.environ.pop("PDM_MULTIRUN", None)

    def _use(self, project: Project, options: argparse.Namespace, python: str) -> None:
        old_echo = project.core.ui.echo
        if not options.verbose:
            project.core.ui.echo = lambda *args, **kwargs: None  # type: ignore[method-assign]
        # unset cached environment
        project.environment = None  # type: ignore[assignment]
        try:
            actions.do_use(
                project,
                python=python,
                first=True,
                ignore_remembered=False,
                hooks=HookManager(project, skip=options.skip),
            )
        finally:
            project.core.ui.echo = old_echo  # type: ignore[method-assign]


def multirun(core: Core) -> None:  # noqa: D103
    core.register_command(MultirunCommand, "multirun")
