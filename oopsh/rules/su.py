import shlex


def match(command):
    output = command.output.lower()
    return (command.script_parts[:1] == ['sudo']
            and ('command not found: sudo' in output
                 or 'sudo: command not found' in output
                 or 'sudo: not found' in output))


def get_new_command(command):
    script = command.script[len('sudo '):]
    # Single quotes: the root shell gets the command exactly as typed (in
    # double quotes, `$(...)` would run first in the user's shell)
    return u'su -c {}'.format(shlex.quote(script))


priority = 1200
