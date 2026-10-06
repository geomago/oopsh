import pytest
from oopsh.argument_parser import Parser
from oopsh.const import ARGUMENT_PLACEHOLDER


def _args(**override):
    args = {'alias': None, 'command': [], 'yes': False,
            'help': False, 'version': False, 'debug': False,
            'force_command': None, 'repeat': False,
            'enable_experimental_instant_mode': False,
            'shell_logger': None, 'migrate': False}
    args.update(override)
    return args


@pytest.mark.parametrize('argv, result', [
    (['oopsh', '--migrate'], _args(migrate=True)),
    (['oopsh'], _args()),
    (['oopsh', '-a'], _args(alias='oops')),
    (['oopsh', '--alias', '--enable-experimental-instant-mode'],
     _args(alias='oops', enable_experimental_instant_mode=True)),
    (['oopsh', '-a', 'fix'], _args(alias='fix')),
    (['oopsh', 'git', 'branch', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch'], yes=True)),
    (['oopsh', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch', '-a'], yes=True)),
    (['oopsh', ARGUMENT_PLACEHOLDER, '-v'], _args(version=True)),
    (['oopsh', ARGUMENT_PLACEHOLDER, '--help'], _args(help=True)),
    (['oopsh', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y', '-d'],
     _args(command=['git', 'branch', '-a'], yes=True, debug=True)),
    (['oopsh', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-r', '-d'],
     _args(command=['git', 'branch', '-a'], repeat=True, debug=True)),
    (['oopsh', '-l', '/tmp/log'], _args(shell_logger='/tmp/log')),
    (['oopsh', '--shell-logger', '/tmp/log'],
     _args(shell_logger='/tmp/log'))])
def test_parse(argv, result):
    assert vars(Parser().parse(argv)) == result
