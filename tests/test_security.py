"""Regression tests for the security reports filed on thefuck."""
import importlib
import os
import shlex
import stat
import sys
import types
import pytest
from oopsh.types import Command


EVIL_URL = 'https://example.com;touch${IFS}/tmp/poc_yarn'


@pytest.mark.skipif(sys.platform == 'win32', reason='unix module')
def test_yarn_help_url_cannot_inject_commands(mocker):
    """nvbn/thefuck#1531"""
    from oopsh.rules import yarn_help
    mocker.patch('oopsh.system.unix.which', return_value='/usr/bin/xdg-open')
    mocker.patch.object(yarn_help, 'open_command',
                        importlib.import_module('oopsh.system.unix').open_command)
    output = 'Visit {} for documentation about this command.'.format(EVIL_URL)
    new_command = yarn_help.get_new_command(Command('yarn help foo', output))
    assert shlex.split(new_command) == ['xdg-open', EVIL_URL]


@pytest.mark.skipif(sys.platform == 'win32', reason='unix module')
@pytest.mark.parametrize('opener', ['/usr/bin/xdg-open', None])
def test_unix_open_command_quotes(mocker, opener):
    from oopsh.system import unix
    mocker.patch('oopsh.system.unix.which', return_value=opener)
    assert shlex.split(unix.open_command(EVIL_URL))[1] == EVIL_URL


def test_win32_open_command_strips_cmd_metacharacters(monkeypatch):
    monkeypatch.setitem(sys.modules, 'msvcrt', types.ModuleType('msvcrt'))
    win32 = importlib.import_module('oopsh.system.win32')
    assert (win32.open_command('https://example.com/a&calc.exe|x"y')
            == 'cmd /c start "" "https://example.com/acalc.exexy"')


@pytest.mark.skipif(sys.platform == 'win32', reason='no shell logger on Windows')
def test_shell_logger_log_is_private(tmp_path, mocker, monkeypatch):
    """nvbn/thefuck#1621"""
    from oopsh.entrypoints import shell_logger
    log = tmp_path / 'log'
    log.write_bytes(b'')
    log.chmod(0o666)
    monkeypatch.setenv('SHELL', '/bin/sh')
    mocker.patch.object(shell_logger, '_spawn', return_value=0)
    with pytest.raises(SystemExit):
        shell_logger.shell_logger(str(log))
    assert stat.S_IMODE(log.stat().st_mode) == 0o600


@pytest.mark.skipif(not hasattr(os, 'getuid'), reason='unix permissions')
@pytest.mark.parametrize('mode, trusted', [
    (0o600, True), (0o644, True), (0o620, False), (0o666, False)])
def test_read_log_ignores_logs_others_can_write(tmp_path, mode, trusted):
    """nvbn/thefuck#1622"""
    from oopsh.output_readers.read_log import _is_trusted_log
    log = tmp_path / 'log'
    log.write_bytes(b'')
    log.chmod(mode)
    fd = os.open(str(log), os.O_RDONLY)
    try:
        assert _is_trusted_log(fd) is trusted
    finally:
        os.close(fd)


@pytest.mark.parametrize('rule, script, output, expected', [
    ('python_module_error', 'python app.py',
     "ModuleNotFoundError: No module named 'x;touch /tmp/pwned'",
     "pip install 'x;touch /tmp/pwned' && python app.py"),
    ('heroku_multiple_apps', 'heroku pg',
     'Multiple apps in git remotes\n Usage: --remote heroku-dev\n Your apps:\n'
     '  $(id) (heroku-dev)\n',
     "heroku pg --app '$(id)'")])
def test_output_text_is_quoted(rule, script, output, expected):
    """nvbn/thefuck#1622: rules quote what they copy from the output."""
    module = importlib.import_module('oopsh.rules.' + rule)
    new_command = module.get_new_command(Command(script, output))
    if isinstance(new_command, list):
        new_command = new_command[0]
    assert new_command == expected
