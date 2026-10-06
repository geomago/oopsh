from oopsh.utils import replace_command_name

patterns = ['you cannot perform this operation as root']


def match(command):
    if command.script_parts and command.script_parts[0] != 'sudo':
        return False

    for pattern in patterns:
        if pattern in command.output.lower():
            return True
    return False


def get_new_command(command):
    return replace_command_name(command.script, '')
