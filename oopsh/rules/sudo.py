import re
import shlex

patterns = ['permission denied',
            'eacces',
            'pkg: insufficient privileges',
            'you cannot perform this operation unless you are root',
            'non-root users cannot',
            'operation not permitted',
            'not super-user',
            'superuser privilege',
            'root privilege',
            'this command has to be run under the root user.',
            'this operation requires root.',
            'requested operation requires superuser privilege',
            'must be run as root',
            'must run as root',
            'must be superuser',
            'must be root',
            'need to be root',
            'need root',
            'needs to be run as root',
            'only root can ',
            'you don\'t have access to the history db.',
            'authentication is required',
            'edspermissionerror',
            'you don\'t have write permissions',
            'use `sudo`',
            'sudorequirederror',
            'error: insufficient privileges',
            'updatedb: can not open a temporary file']


def match(command):
    if command.script_parts and '&&' not in command.script_parts and command.script_parts[0] == 'sudo':
        return False

    for pattern in patterns:
        if pattern in command.output.lower():
            return True
    return False


def get_new_command(command):
    if '&&' in command.script or '>' in command.script:
        # sudo must cover the whole command line. Single quotes pass it to
        # the root shell exactly as typed: in double quotes, `$(...)` and
        # backticks would run first in the user's shell, and text the user
        # had quoted could run as code, as root
        script = re.sub(r'^\s*sudo\s+', '', command.script)
        return u'sudo sh -c {}'.format(shlex.quote(script))
    else:
        return u'sudo {}'.format(command.script)
