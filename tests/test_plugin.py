"""Tests for the `plugin` module."""

from pdm.core import main


def test_multirun() -> None:
    """Basic run."""
    main(["multirun", "python", "-V"])
