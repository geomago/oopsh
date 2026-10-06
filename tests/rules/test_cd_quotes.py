import pytest
from oopsh.rules.cd_quotes import match, get_new_command
from oopsh.types import Command


@pytest.fixture(autouse=True)
def directory(tmp_path, monkeypatch):
    (tmp_path / 'My Documents').mkdir()
    (tmp_path / 'a b c').mkdir()
    monkeypatch.chdir(tmp_path)


@pytest.mark.parametrize('script', ['cd My Documents', 'cd a b c'])
def test_match(script):
    assert match(Command(script, 'cd: too many arguments'))


@pytest.mark.parametrize('script', [
    'cd My',
    'cd Missing Folder',
    'cd "My Documents"',
    'cd My Documents && ls',
    'ls My Documents'])
def test_not_match(script):
    assert not match(Command(script, 'cd: too many arguments'))


@pytest.mark.parametrize('script, new_command', [
    ('cd My Documents', "cd 'My Documents'"),
    ('cd a b c', "cd 'a b c'")])
def test_get_new_command(script, new_command):
    assert get_new_command(Command(script, '')) == new_command
