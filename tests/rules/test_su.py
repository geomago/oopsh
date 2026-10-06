import pytest
from oopsh.rules.su import match, get_new_command
from oopsh.types import Command


@pytest.mark.parametrize('output', [
    'zsh: command not found: sudo',
    'bash: sudo: command not found',
    'sh: 1: sudo: not found'])
def test_match(output):
    assert match(Command('sudo ls', output))


@pytest.mark.parametrize('script, output', [
    ('sudo ls', ''),
    ('sudo ls', 'Permission denied'),
    ('su -c ls', 'Permission denied'),
    ('ls', 'command not found: ls'),
    ('ls', 'command not found: sudo')])
def test_not_match(script, output):
    assert not match(Command(script, output))


@pytest.mark.parametrize('before, after', [
    ('sudo ls', 'su -c "ls"'),
    ('sudo echo a > b', 'su -c "echo a > b"'),
    ('sudo echo "a" >> b', 'su -c "echo \\"a\\" >> b"'),
    ('sudo mkdir && touch a', 'su -c "mkdir && touch a"')])
def test_get_new_command(before, after):
    assert get_new_command(Command(before, '')) == after
