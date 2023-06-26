"""PDM Multirun plugin."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

from pdm import termui
from pdm.cli.commands.run import Command as RunCommand
from pdm.cli.commands.run import Project
from pdm.cli.commands.use import Command as UseCommand
from pdm.cli.hooks import HookManager

if TYPE_CHECKING:
    import argparse

    from pdm.core import Core

PYTHON_VERSIONS = os.getenv("PDM_MULTIRUN_VERSIONS", "").split() or [f"3.{minor}" for minor in range(8, 13)]


def _comma_separated_list(value: str) -> list[str]:
    return value.split(",")


class MultirunCommand(RunCommand):
    """Run a command under multiple Python versions."""

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:  # noqa: D102
        super().add_arguments(parser)
        parser.add_argument(
            "-f",
            "--fail-fast",
            help="Exit as soon as an interpreter/venv cannot be found or used",
            action="store_true",
            default=False,
        )
        parser.add_argument(
            "-i",
            "--interpreters",
            "--versions",
            "--names",
            help="Comma-separated list of Python versions or virtual environment names to run the command with",
            type=_comma_separated_list,
        )
        parser.add_argument(
            "-e",
            "--venvs",
            action="store_true",
            default=False,
            help="Use virtual environments",
        )

    def handle(self, project: Project, options: argparse.Namespace) -> None:  # noqa: D102
        os.environ["PDM_MULTIRUN"] = "1"
        old_python = str(project.environment.interpreter.path)
        project.core.ui.echo(f"Current interpreter: {old_python}", verbosity=termui.Verbosity.DETAIL)
        for selected in options.interpreters or PYTHON_VERSIONS:
            use_kwargs = {"venv" if options.venvs else "python": selected}
            try:
                self._use(project, options, **use_kwargs)
            except Exception:  # noqa: BLE001
                if options.fail_fast:
                    raise
                project.core.ui.echo(f"Skipped interpreter/venv: {selected}", verbosity=termui.Verbosity.DETAIL)
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

    def _use(self, project: Project, options: argparse.Namespace, python: str = "", venv: str | None = None) -> None:
        old_echo = project.core.ui.echo
        if not options.verbose:
            project.core.ui.echo = lambda *args, **kwargs: None  # type: ignore[method-assign]
        # unset cached environment
        project.environment = None  # type: ignore[assignment]
        try:
            UseCommand().do_use(
                project,
                python=python,
                venv=venv,
                first=True,
                ignore_remembered=False,
                hooks=HookManager(project, skip=options.skip),
            )
        finally:
            project.core.ui.echo = old_echo  # type: ignore[method-assign]


def multirun(core: Core) -> None:  # noqa: D103
    core.register_command(MultirunCommand, "multirun")
