from oopsh.rules.ninja import get_new_command, match
from oopsh.types import Command

match_output = "ninja: error: unknown target 'clong', did you mean 'clang'?"
no_match_output = "ninja: error: unknown target 'foobar'"


def test_match():
    assert match(Command('ninja clong', match_output))
    assert match(Command('ninja -C out clong', match_output))
    assert not match(Command('ninja foobar', no_match_output))


def test_get_new_command():
    assert get_new_command(Command('ninja clong', match_output)) == 'ninja clang'
    assert (get_new_command(Command('ninja -C out clong', match_output))
            == 'ninja -C out clang')
