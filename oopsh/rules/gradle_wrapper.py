import os
from oopsh.utils import for_app, replace_command_name, which


@for_app('gradle')
def match(command):
    return (not which(command.script_parts[0])
            and 'not found' in command.output
            and os.path.isfile('gradlew'))


def get_new_command(command):
    return replace_command_name(command.script, './gradlew')
