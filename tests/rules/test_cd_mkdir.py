import pytest
from oopsh.rules.cd_mkdir import match, get_new_command
from oopsh.types import Command


@pytest.mark.parametrize('command', [
    Command('cd foo', 'cd: foo: No such file or directory'),
    Command('cd foo/bar/baz',
            'cd: foo: No such file or directory'),
    Command('cd foo/bar/baz', 'cd: can\'t cd to foo/bar/baz'),
    Command('cd /foo/bar/', 'cd: The directory "/foo/bar/" does not exist'),
    Command('cd foo', "Set-Location: Cannot find path 'C:\\foo' because it does not exist."),
    Command('cd foo', 'The system cannot find the path specified.')])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command', [
    Command('cd foo', ''), Command('', '')])
def test_not_match(command):
    assert not match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('cd foo', ''), 'mkdir -p foo && cd foo'),
    (Command('cd foo/bar/baz', ''), 'mkdir -p foo/bar/baz && cd foo/bar/baz')])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
