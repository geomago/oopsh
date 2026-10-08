import pytest
from oopsh.rules.brew_cask import match, get_new_command
from oopsh.types import Command


disabled = ('Error: Calling brew cask {0} is disabled!\n'
            'Use brew {0} --cask instead.').format


@pytest.mark.parametrize('script, output', [
    ('brew cask reinstall firefox', disabled('reinstall')),
    ('brew cask install firefox', disabled('install')),
    ('brew cask uninstall firefox', disabled('uninstall')),
])
def test_match(script, output):
    assert match(Command(script, output))


@pytest.mark.parametrize('script, output', [
    ('brew reinstall --cask firefox', ''),
    ('brew install firefox', 'Error: No available formula'),
    ('brew cask reinstall firefox', 'some other output'),
])
def test_not_match(script, output):
    assert not match(Command(script, output))


@pytest.mark.parametrize('script, result', [
    ('brew cask reinstall firefox', 'brew reinstall --cask firefox'),
    ('brew cask install firefox', 'brew install --cask firefox'),
    ('brew cask uninstall firefox', 'brew uninstall --cask firefox'),
])
def test_get_new_command(script, result):
    assert get_new_command(Command(script, disabled('x'))) == result
