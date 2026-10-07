import re
from oopsh.shells import shell
from oopsh.specific.git import git_support
from oopsh.utils import quote_if_unsafe

SET_UPSTREAM = re.compile(
    r'^\s*git branch --set-upstream-to=<remote>/<branch> (\S+)\s*$',
    re.MULTILINE)


@git_support
def match(command):
    return ('pull' in command.script
            and SET_UPSTREAM.search(command.output) is not None)


@git_support
def get_new_command(command):
    # Branch names can hold characters the shell would interpret
    branch = quote_if_unsafe(SET_UPSTREAM.search(command.output).group(1))
    set_upstream = 'git branch --set-upstream-to=origin/{0} {0}'.format(branch)
    return shell.and_(set_upstream, command.script)
