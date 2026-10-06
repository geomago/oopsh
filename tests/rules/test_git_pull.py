import pytest
from oopsh.rules.git_pull import match, get_new_command
from oopsh.types import Command


@pytest.fixture
def output():
    return '''There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=<remote>/<branch> master

'''


def test_match(output):
    assert match(Command('git pull', output))
    assert not match(Command('git pull', ''))
    assert not match(Command('ls', output))


def test_get_new_command(output):
    assert (get_new_command(Command('git pull', output))
            == "git branch --set-upstream-to=origin/master master && git pull")


def test_get_new_command_with_fetch_output():
    """nvbn/thefuck#1406: the hint isn't always the third line from the end."""
    output = """From github.com:corp/xxx
   324b9f9..3a6a1c4  stg        -> origin/stg
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=<remote>/<branch> feature/ONEPOR-70-local-connection
"""
    assert (get_new_command(Command('git pull', output))
            == 'git branch --set-upstream-to=origin/feature/ONEPOR-70-local-connection '
               'feature/ONEPOR-70-local-connection && git pull')
