import sys
from oopsh import conf, utils
from oopsh.compat import ThefuckImportAlias, install_thefuck_import_alias
from oopsh.conf import load_source


def test_install_is_idempotent():
    install_thefuck_import_alias()
    install_thefuck_import_alias()
    assert isinstance(sys.meta_path[0], ThefuckImportAlias)
    assert sum(isinstance(finder, ThefuckImportAlias)
               for finder in sys.meta_path) == 1


def test_thefuck_modules_are_oopsh_modules():
    install_thefuck_import_alias()
    import thefuck.utils
    from thefuck.conf import settings
    from thefuck.specific.git import git_support  # noqa: F401
    assert thefuck.utils is utils
    assert settings is conf.settings


def test_load_rule_written_for_thefuck(tmp_path):
    rule = tmp_path / 'my_rule.py'
    rule.write_text(
        'from thefuck.utils import for_app\n'
        'from thefuck.specific.sudo import sudo_support\n'
        'from thefuck.conf import settings\n'
        '\n'
        '@sudo_support\n'
        '@for_app("ehco")\n'
        'def match(command):\n'
        '    return True\n'
        '\n'
        'def get_new_command(command):\n'
        '    return command.script.replace("ehco", "echo")\n')
    module = load_source('my_rule', str(rule))
    assert module.settings is conf.settings
    assert module.match.__module__ == 'my_rule'


def test_oopsh_modules_keep_their_spec():
    install_thefuck_import_alias()
    import thefuck.logs  # noqa: F401
    from oopsh import logs
    assert logs.__spec__.name == 'oopsh.logs'
