# -*- coding: utf-8 -*-

import pytest
from oopsh.shells import Nushell


@pytest.mark.usefixtures('isfile', 'no_memoize', 'no_cache')
class TestNushell(object):
    @pytest.fixture
    def shell(self):
        return Nushell()

    @pytest.fixture(autouse=True)
    def Popen(self, mocker):
        mock = mocker.patch('oopsh.shells.nushell.Popen')
        return mock

    def test_and_(self, shell):
        # The fix runs with `sh`
        assert shell.and_('ls', 'cd') == 'ls && cd'

    def test_app_alias(self, shell):
        assert 'def --env --wrapped fuck [...args]' in shell.app_alias('fuck')
        assert 'def --env --wrapped FUCK [...args]' in shell.app_alias('FUCK')
        assert 'TF_ALIAS: fuck' in shell.app_alias('fuck')

    def test_app_alias_calls_executable(self, shell):
        alias = shell.app_alias('oops')
        assert '^oopsh $previous OOPSH_ARGUMENT_PLACEHOLDER ...$args' in alias
        assert 'TF_SHELL: nu' in alias

    def test_app_alias_runs_fix_and_follows_cd(self, shell):
        alias = shell.app_alias('oops')
        assert '^sh -c ($fixed + \' && pwd > "$OOPSH_PWD_FILE"\')' in alias
        assert 'cd $directory' in alias

    def test_executable_alias(self, shell):
        alias = shell.app_alias('oops')
        assert 'def --env --wrapped oopsh [...args]' in alias
        assert "=~ '^(-a|--alias|" in alias
        assert '        ^oopsh ...$args\n' in alias
        assert '        oops ...$args\n' in alias

    def test_no_executable_alias_when_alias_is_oopsh(self, shell):
        alias = shell.app_alias('oopsh')
        assert 'def --env --wrapped oopsh [...args]' in alias
        assert '=~ \'^(-a' not in alias

    def test_get_aliases(self, shell, monkeypatch):
        monkeypatch.setenv('TF_SHELL_ALIASES', 'g\tgit\nll\tls -l\nbroken')
        assert shell.get_aliases() == {'g': 'git', 'll': 'ls -l'}

    def test_from_shell(self, shell, monkeypatch):
        monkeypatch.setenv('TF_SHELL_ALIASES', 'g\tgit')
        assert shell.from_shell('g sttaus') == 'git sttaus'
        assert shell.from_shell('ls') == 'ls'

    def test_get_history(self, history_lines, shell, monkeypatch):
        monkeypatch.setenv('OOPSH_NU_HISTORY', '/home/me/.config/nushell/history.txt')
        history_lines(['ls', 'rm'])
        assert list(shell.get_history()) == ['ls', 'rm']

    def test_get_history_sqlite(self, shell, monkeypatch):
        monkeypatch.setenv('OOPSH_NU_HISTORY', '/home/me/.config/nushell/history.sqlite3')
        assert shell._get_history_file_name() == ''

    def test_how_to_configure(self, shell, Popen):
        Popen.return_value.stdout.read.return_value = \
            b'/home/me/.config/nushell/config.nu\n'
        configuration = shell.how_to_configure()
        assert configuration.path == '/home/me/.config/nushell/config.nu'
        assert 'oopsh --alias | save -f' in configuration.content
        assert configuration.can_configure_automatically

    def test_how_to_configure_without_nu(self, shell, Popen):
        Popen.side_effect = OSError
        configuration = shell.how_to_configure()
        assert configuration.path == '$nu.config-path'
        assert not configuration.can_configure_automatically

    def test_info(self, shell, Popen):
        Popen.return_value.stdout.read.side_effect = [b'0.116.1\n']
        assert shell.info() == 'Nushell 0.116.1'
        assert Popen.call_args[0][0] == ['nu', '--version']
