import pytest
from oopsh.entrypoints.migrate import migrate
from oopsh.shells.generic import ShellConfiguration


@pytest.fixture
def home(tmp_path, os_environ):
    os_environ['HOME'] = str(tmp_path)
    os_environ.pop('XDG_CONFIG_HOME', None)
    return tmp_path


@pytest.fixture
def rc(home, mocker):
    path = home / '.zshrc'
    shell = mocker.patch('oopsh.entrypoints.migrate.shell')
    shell.how_to_configure.return_value = ShellConfiguration(
        content='eval $(oopsh --alias)',
        path=str(path),
        reload='source ~/.zshrc',
        can_configure_automatically=True)
    return path


def _thefuck_config(home):
    config = home / '.config' / 'thefuck'
    (config / 'rules' / '__pycache__').mkdir(parents=True)
    (config / 'settings.py').write_text('require_confirmation = False\n')
    (config / 'rules' / 'my_rule.py').write_text('# rule\n')
    (config / 'rules' / '__pycache__' / 'my_rule.pyc').write_text('')
    return config


@pytest.mark.usefixtures('rc', 'no_colors')
def test_copies_thefuck_config(home, capsys):
    _thefuck_config(home)
    migrate()
    oopsh = home / '.config' / 'oopsh'
    assert (oopsh / 'settings.py').read_text() == 'require_confirmation = False\n'
    assert (oopsh / 'rules' / 'my_rule.py').read_text() == '# rule\n'
    assert not (oopsh / 'rules' / '__pycache__').exists()
    assert 'Copied 2 file(s)' in capsys.readouterr().out


@pytest.mark.usefixtures('rc', 'no_colors')
def test_never_overwrites(home, capsys):
    _thefuck_config(home)
    oopsh = home / '.config' / 'oopsh'
    (oopsh / 'rules').mkdir(parents=True)
    (oopsh / 'rules' / 'my_rule.py').write_text('# mine\n')
    migrate()
    assert (oopsh / 'rules' / 'my_rule.py').read_text() == '# mine\n'
    out = capsys.readouterr().out
    assert 'Copied 1 file(s)' in out
    assert 'Skipped rules/my_rule.py' in out


@pytest.mark.usefixtures('rc', 'no_colors')
def test_replaces_default_settings(home):
    _thefuck_config(home)
    oopsh = home / '.config' / 'oopsh'
    oopsh.mkdir(parents=True)
    (oopsh / 'settings.py').write_text('# oopsh settings file\n\n# debug = False\n')
    migrate()
    assert (oopsh / 'settings.py').read_text() == 'require_confirmation = False\n'


@pytest.mark.usefixtures('rc', 'no_colors')
def test_without_thefuck_config(home, capsys):
    migrate()
    assert 'No thefuck config found' in capsys.readouterr().out
    assert not (home / '.config' / 'oopsh').exists()


@pytest.mark.usefixtures('no_colors')
@pytest.mark.parametrize('rc_content, expected', [
    ('eval $(thefuck --alias)\n', 'replace the line with thefuck --alias'),
    ('eval $(oopsh --alias)\n', 'already sets up oopsh'),
    ('', 'Add this line to')])
def test_shell_config_advice(rc, capsys, rc_content, expected):
    rc.write_text(rc_content)
    migrate()
    assert expected in capsys.readouterr().out


@pytest.mark.usefixtures('rc', 'no_colors')
def test_env_advice(os_environ, capsys):
    os_environ['THEFUCK_RULES'] = 'sudo'
    os_environ['THEFUCK_OVERRIDDEN_ALIASES'] = 'ls'
    migrate()
    assert 'THEFUCK_OVERRIDDEN_ALIASES, THEFUCK_RULES' in capsys.readouterr().out
