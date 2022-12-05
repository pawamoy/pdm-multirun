"""PDM Multirun plugin."""

from __future__ import annotations

import argparse
import os

from pdm import termui
from pdm.cli import actions
from pdm.cli.commands.run import Command as RunCommand
from pdm.cli.commands.run import Project
from pdm.cli.hooks import HookManager

PYTHON_VERSIONS = os.getenv("PDM_MULTIRUN_VERSIONS", "").split()
PYTHON_VERSIONS = PYTHON_VERSIONS or [f"python3.{minor}" for minor in range(7, 12)]  # noqa: WPS432


def _interpreters(versions: str) -> list[str]:
    return [f"python{version.strip()}" for version in versions.split(",")]


class MultirunCommand(RunCommand):
    """Run a command under multiple Python versions."""

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:  # noqa: D102
        super().add_arguments(parser)
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
            self._use(project, options, python_version)
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
            project.core.ui.echo = lambda *args, **kwargs: None  # type: ignore[assignment]
        # unset cached environment
        project.environment = None  # type: ignore[assignment]
        try:  # noqa: WPS501
            actions.do_use(
                project,
                python=python,
                first=True,
                ignore_remembered=False,
                hooks=HookManager(project, skip=options.skip),
            )
        finally:
            project.core.ui.echo = old_echo  # type: ignore[assignment]


def multirun(core):  # noqa: D103
    core.register_command(MultirunCommand, "multirun")
