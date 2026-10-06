import pytest
from oopsh.rules.makefile import match, get_new_command
from oopsh.types import Command

MAKEFILE = '''CC := gcc
.PHONY: foo bar

foo:
\tg++ testfoo.cpp
bar: foo
\techo "build: done"
food:
\tg++ testfood.cpp
%.o: %.c
\t$(CC) -c $<
'''


@pytest.fixture(params=['Makefile', 'makefile', 'GNUmakefile'])
def makefile(request, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / request.param).write_text(MAKEFILE)


def no_rule(target):
    return "make: *** No rule to make target '{}'.  Stop.".format(target)


@pytest.mark.usefixtures('makefile')
@pytest.mark.parametrize('command', [
    Command('make fo', no_rule('fo')),
    Command('make ba', "make: *** No rule to make target `ba'.  Stop."),
    Command('mak foo', 'mak: command not found'),
    Command('maek bar', 'maek: command not found'),
    Command('amke foo', 'amke: command not found')])
def test_match(command):
    assert match(command)


@pytest.mark.usefixtures('makefile')
@pytest.mark.parametrize('command', [
    Command('make foo', 'make: command not found'),
    Command('cd foo', 'cd: foo: No such file or directory'),
    Command('java foo.java', 'error message')])
def test_not_match(command):
    assert not match(command)


@pytest.mark.parametrize('command', [
    Command('make fo', no_rule('fo')),
    Command('maek bar', 'maek: command not found')])
def test_not_match_without_makefile(command, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert not match(command)


@pytest.mark.usefixtures('makefile')
@pytest.mark.parametrize('command, new_command', [
    (Command('make fo', no_rule('fo')), 'make foo'),
    (Command('make ba', no_rule('ba')), 'make bar'),
    (Command('make foodo', no_rule('foodo')), 'make food'),
    (Command('make -j4 dfoo', no_rule('dfoo')), 'make -j4 foo'),
    (Command('make CC=clang fo', no_rule('fo')), 'make CC=clang foo'),
    (Command('mak foo', 'mak: command not found'), 'make foo'),
    (Command('maek br', 'maek: command not found'), 'make bar'),
    (Command('amke', 'amke: command not found'), 'make')])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
