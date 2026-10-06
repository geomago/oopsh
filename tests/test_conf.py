import pytest
from io import StringIO
from unittest.mock import Mock
from oopsh import const


@pytest.fixture
def load_source(mocker):
    return mocker.patch('oopsh.conf.load_source')


def test_settings_defaults(load_source, settings):
    load_source.return_value = object()
    settings.init()
    for key, val in const.DEFAULT_SETTINGS.items():
        assert getattr(settings, key) == val


class TestSettingsFromFile(object):
    def test_from_file(self, load_source, settings):
        load_source.return_value = Mock(rules=['test'],
                                        wait_command=10,
                                        require_confirmation=True,
                                        no_colors=True,
                                        priority={'vim': 100},
                                        exclude_rules=['git'])
        settings.init()
        assert settings.rules == ['test']
        assert settings.wait_command == 10
        assert settings.require_confirmation is True
        assert settings.no_colors is True
        assert settings.priority == {'vim': 100}
        assert settings.exclude_rules == ['git']

    def test_from_file_with_DEFAULT(self, load_source, settings):
        load_source.return_value = Mock(rules=const.DEFAULT_RULES + ['test'],
                                        wait_command=10,
                                        exclude_rules=[],
                                        require_confirmation=True,
                                        no_colors=True)
        settings.init()
        assert settings.rules == const.DEFAULT_RULES + ['test']


@pytest.mark.usefixtures('load_source')
class TestSettingsFromEnv(object):
    def test_from_env(self, os_environ, settings):
        os_environ.update({'OOPSH_RULES': 'bash:lisp',
                           'OOPSH_EXCLUDE_RULES': 'git:vim',
                           'OOPSH_WAIT_COMMAND': '55',
                           'OOPSH_REQUIRE_CONFIRMATION': 'true',
                           'OOPSH_NO_COLORS': 'false',
                           'OOPSH_PRIORITY': 'bash=10:lisp=wrong:vim=15',
                           'OOPSH_WAIT_SLOW_COMMAND': '999',
                           'OOPSH_SLOW_COMMANDS': 'lein:react-native:./gradlew',
                           'OOPSH_NUM_CLOSE_MATCHES': '359',
                           'OOPSH_EXCLUDED_SEARCH_PATH_PREFIXES': '/media/:/mnt/'})
        settings.init()
        assert settings.rules == ['bash', 'lisp']
        assert settings.exclude_rules == ['git', 'vim']
        assert settings.wait_command == 55
        assert settings.require_confirmation is True
        assert settings.no_colors is False
        assert settings.priority == {'bash': 10, 'vim': 15}
        assert settings.wait_slow_command == 999
        assert settings.slow_commands == ['lein', 'react-native', './gradlew']
        assert settings.num_close_matches == 359
        assert settings.excluded_search_path_prefixes == ['/media/', '/mnt/']

    def test_from_env_with_DEFAULT(self, os_environ, settings):
        os_environ.update({'OOPSH_RULES': 'DEFAULT_RULES:bash:lisp'})
        settings.init()
        assert settings.rules == const.DEFAULT_RULES + ['bash', 'lisp']

    def test_from_thefuck_env(self, os_environ, settings):
        os_environ.update({'THEFUCK_RULES': 'bash:lisp',
                           'THEFUCK_WAIT_COMMAND': '55',
                           'THEFUCK_REQUIRE_CONFIRMATION': 'false'})
        settings.init()
        assert settings.rules == ['bash', 'lisp']
        assert settings.wait_command == 55
        assert settings.require_confirmation is False

    def test_oopsh_env_wins_over_thefuck_env(self, os_environ, settings):
        os_environ.update({'THEFUCK_WAIT_COMMAND': '55',
                           'OOPSH_WAIT_COMMAND': '10'})
        settings.init()
        assert settings.wait_command == 10


def test_settings_from_args(settings):
    settings.init(Mock(yes=True, debug=True, repeat=True))
    assert not settings.require_confirmation
    assert settings.debug
    assert settings.repeat


class TestInitializeSettingsFile(object):
    def test_ignore_if_exists(self, settings):
        settings_path_mock = Mock(is_file=Mock(return_value=True), open=Mock())
        settings.user_dir = Mock(joinpath=Mock(return_value=settings_path_mock))
        settings._init_settings_file()
        assert settings_path_mock.is_file.call_count == 1
        assert not settings_path_mock.open.called

    def test_create_if_doesnt_exists(self, settings):
        settings_file = StringIO()
        settings_path_mock = Mock(
            is_file=Mock(return_value=False),
            open=Mock(return_value=Mock(
                __exit__=lambda *args: None, __enter__=lambda *args: settings_file)))
        settings.user_dir = Mock(joinpath=Mock(return_value=settings_path_mock))
        settings._init_settings_file()
        settings_file_contents = settings_file.getvalue()
        assert settings_path_mock.is_file.call_count == 1
        assert settings_path_mock.open.call_count == 1
        assert const.SETTINGS_HEADER in settings_file_contents
        for setting in const.DEFAULT_SETTINGS.items():
            assert '# {} = {}\n'.format(*setting) in settings_file_contents
        settings_file.close()


@pytest.mark.parametrize('existing, xdg_config_home, result, warns', [
    ([], None, 'home/.config/oopsh', False),
    ([], 'xdg', 'xdg/oopsh', False),
    (['xdg/thefuck'], 'xdg', 'xdg/thefuck', False),
    (['home/.config/thefuck'], None, 'home/.config/thefuck', False),
    (['home/.thefuck'], 'xdg', 'home/.thefuck', True),
    (['xdg/oopsh', 'xdg/thefuck'], 'xdg', 'xdg/oopsh', False),
    (['xdg/oopsh', 'home/.thefuck'], 'xdg', 'xdg/oopsh', False),
    (['xdg/thefuck', 'home/.thefuck'], 'xdg', 'xdg/thefuck', False)])
def test_get_user_dir_path(tmp_path, os_environ, settings, existing,
                           xdg_config_home, result, warns):
    os_environ['HOME'] = str(tmp_path / 'home')
    if xdg_config_home is not None:
        os_environ['XDG_CONFIG_HOME'] = str(tmp_path / xdg_config_home)
    for path in existing:
        (tmp_path / path).mkdir(parents=True)

    if warns:
        with pytest.warns(UserWarning, match='is deprecated'):
            path = settings._get_user_dir_path()
    else:
        path = settings._get_user_dir_path()
    assert path == tmp_path / result
