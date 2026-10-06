from oopsh.utils import for_app, replace_command_name


@for_app('ls')
def match(command):
    return command.output.strip() == ''


def get_new_command(command):
    return replace_command_name(command.script, 'ls -A')
