"""Fixes commands typed with caps lock on: `LS -A` -> `ls -a`."""
from oopsh.utils import get_all_executables


def match(command):
    return (command.script.isupper()
            and ('not found' in command.output
                 or 'is not recognized as' in command.output)
            and command.script_parts[0].lower() in get_all_executables())


def get_new_command(command):
    return command.script.lower()


priority = 100
