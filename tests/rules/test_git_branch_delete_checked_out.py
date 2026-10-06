import pytest
from oopsh.rules.git_branch_delete_checked_out import match, get_new_command
from oopsh.types import Command


@pytest.fixture
def output():
    return "error: Cannot delete branch 'foo' checked out at '/bar/foo'"


@pytest.mark.parametrize("script", ["git branch -d foo", "git branch -D foo"])
def test_match(script, output):
    assert match(Command(script, output))


@pytest.mark.parametrize("script", ["git branch -d foo", "git branch -D foo"])
def test_not_match(script):
    assert not match(Command(script, "Deleted branch foo (was a1b2c3d)."))


@pytest.mark.parametrize(
    "script, new_command",
    [
        ("git branch -d foo", "git checkout master && git branch -D foo"),
        ("git branch -D foo", "git checkout master && git branch -D foo"),
    ],
)
def test_get_new_command(script, new_command, output, mocker):
    mocker.patch('oopsh.rules.git_branch_delete_checked_out._git', return_value='')
    assert get_new_command(Command(script, output)) == new_command


@pytest.mark.parametrize("git_outputs, default_branch", [
    ({'symbolic-ref': 'origin/main'}, 'main'),
    ({'symbolic-ref': 'upstream/develop'}, 'develop'),
    ({'rev-parse': 'a1b2c3d'}, 'main'),
    ({}, 'master'),
])
def test_get_new_command_default_branch(output, mocker, git_outputs, default_branch):
    mocker.patch('oopsh.rules.git_branch_delete_checked_out._git',
                 side_effect=lambda *args: git_outputs.get(args[0], ''))
    assert (get_new_command(Command('git branch -d foo', output))
            == 'git checkout {} && git branch -D foo'.format(default_branch))
