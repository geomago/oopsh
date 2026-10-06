import pytest

from oopsh.rules.restic_typo import match, get_new_command
from oopsh.types import Command


@pytest.fixture
def mistype_suggestion():
    return """Error: unknown command "snapshot" for "restic"

Did you mean this?
\tsnapshots

Run 'restic --help' for usage.
"""


def test_match(mistype_suggestion):
    assert match(Command('restic snapshot', mistype_suggestion))


def test_get_new_command(mistype_suggestion):
    assert (get_new_command(Command('restic snapshot', mistype_suggestion)) == ['restic snapshots'])
