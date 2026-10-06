import pytest

from oopsh.rules.upper_to_lower_case import match, get_new_command
from oopsh.types import Command


@pytest.fixture(autouse=True)
def executables(mocker):
    return mocker.patch('oopsh.rules.upper_to_lower_case.get_all_executables',
                        return_value=['ls', 'cat', 'git', 'mv'])


@pytest.mark.parametrize(
    "script, output",
    [
        ("LS", "command not found"),
        ("LS -A", "command not found"),
    ],
)
def test_match(script, output):
    assert match(Command(script, output))


@pytest.mark.parametrize(
    "script, output",
    [
        ("ls", ""),
        ("cd thefuck", ""),
        ("mv tests testing", ""),
        ("git add .", ""),
        ("FOO", "command not found"),
    ],
)
def test_not_match(script, output):
    assert not match(Command(script, output))


@pytest.mark.parametrize(
    "script, output, new_command",
    [
        ("LS", "command not found", "ls"),
        ("CD TESTS", "command not found", "cd tests"),
        ("CAT README.MD", "command not found", "cat readme.md"),
        ("GIT ADD .", "command not found", "git add ."),
        ("GIT ADD .", "command not found", "git add ."),
        ("MV TESTS TESTING", "command not found", "mv tests testing"),
    ],
)
def test_get_new_command(script, output, new_command):
    assert get_new_command(Command(script, output)) == new_command
