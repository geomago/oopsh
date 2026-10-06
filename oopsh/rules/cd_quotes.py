"""Quotes a directory with spaces: `cd My Documents` -> `cd 'My Documents'`."""
import os
from oopsh.shells import shell
from oopsh.utils import for_app

SHELL_OPERATORS = {'&&', '||', ';', '|', '>', '>>', '<', '&'}


def _directory(command):
    return ' '.join(command.script_parts[1:])


@for_app('cd', at_least=2)
def match(command):
    return (not SHELL_OPERATORS.intersection(command.script_parts)
            and '"' not in command.script and "'" not in command.script
            and os.path.isdir(os.path.expanduser(_directory(command))))


def get_new_command(command):
    return u'cd {}'.format(shell.quote(_directory(command)))


priority = 900
