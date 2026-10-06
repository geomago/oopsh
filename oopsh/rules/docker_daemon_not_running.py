from oopsh.shells import shell
from oopsh.specific.sudo import sudo_support
from oopsh.utils import for_app, which

enabled_by_default = bool(which('systemctl'))


@sudo_support
@for_app('docker')
def match(command):
    return ('Cannot connect to the Docker daemon' in command.output
            and 'Is the docker daemon running?' in command.output)


def get_new_command(command):
    start = 'systemctl start docker'
    if command.script_parts[0] == 'sudo':
        start = 'sudo ' + start
    return shell.and_(start, command.script)
