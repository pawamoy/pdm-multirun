"""Tests for the `cli` module."""

from pdm.core import main


def test_multirun():
    """Basic run."""
    main(["multirun", "python", "-V"])
