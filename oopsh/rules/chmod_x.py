import os
from oopsh.shells import shell


def _path(command):
    return os.path.expanduser(command.script_parts[0])


def match(command):
    # Only paths: a bare name is looked up in $PATH, not in the current dir
    return ('/' in command.script_parts[0]
            and 'permission denied' in command.output.lower()
            and os.path.exists(_path(command))
            and not os.access(_path(command), os.X_OK))


def get_new_command(command):
    path = command.script_parts[0]
    if path.startswith('./'):
        path = shell.quote(path[2:])
    elif path.startswith('~/'):
        # Keep the tilde outside the quotes, so the shell still expands it
        path = '~/' + shell.quote(path[2:])
    else:
        path = shell.quote(path)
    return shell.and_('chmod +x {}'.format(path), command.script)
