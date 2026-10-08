import pytest
from oopsh.rules.brew_cask_dependency import match, get_new_command
from oopsh.types import Command


output = '''sshfs: OsxfuseRequirement unsatisfied!

You can install with Homebrew-Cask:
  brew cask install osxfuse

You can download from:
  https://osxfuse.github.io/
Error: An unsatisfied requirement failed this build.'''


def test_match():
    command = Command('brew install sshfs', output)
    assert match(command)


# Modern brew phrases a "this is itself a cask" hint inside a sentence rather
# than as a standalone `brew cask install` line; the rule must not match it
# (previously this raised IndexError, nvbn/thefuck#936).
did_you_mean = ('Error: No available formula with the name "sublime-merge".\n'
                'Did you mean to type "brew cask install sublime-merge"?')


@pytest.mark.parametrize('script, output', [
    ('brew link sshfs', output),
    ('cat output', output),
    ('brew install sublime-merge', did_you_mean),
    ('brew install sshfs', '')])
def test_not_match(script, output):
    command = Command(script, output)
    assert not match(command)


@pytest.mark.parametrize('before, after', [
    ('brew install sshfs',
     'brew cask install osxfuse && brew install sshfs')])
def test_get_new_command(before, after):
    command = Command(before, output)
    assert get_new_command(command) == after
