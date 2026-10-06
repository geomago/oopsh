import re
from oopsh.shells import shell
from oopsh.specific.git import git_support

SET_UPSTREAM = re.compile(
    r'^\s*(git branch --set-upstream-to=<remote>/<branch> (\S+))\s*$',
    re.MULTILINE)


@git_support
def match(command):
    return ('pull' in command.script
            and SET_UPSTREAM.search(command.output) is not None)


@git_support
def get_new_command(command):
    line, branch = SET_UPSTREAM.search(command.output).groups()
    set_upstream = line.replace('<remote>', 'origin')\
                       .replace('<branch>', branch)
    return shell.and_(set_upstream, command.script)
