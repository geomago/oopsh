import pytest
from oopsh.rules.git_safe_directory import match, get_new_command
from oopsh.types import Command

output = """fatal: detected dubious ownership in repository at '/srv/my repo'
To add an exception for this directory, call:

\tgit config --global --add safe.directory '/srv/my repo'
"""


@pytest.mark.parametrize('script', ['git status', 'git add .'])
def test_match(script):
    assert match(Command(script, output))


@pytest.mark.parametrize('script, output', [
    ('git status', ''),
    ('git status', 'fatal: not a git repository'),
    ('hg status', output)])
def test_not_match(script, output):
    assert not match(Command(script, output))


def test_get_new_command():
    assert (get_new_command(Command('git add .', output))
            == "git config --global --add safe.directory '/srv/my repo' && git add .")
