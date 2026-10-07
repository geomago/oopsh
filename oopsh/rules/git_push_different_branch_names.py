import re
from oopsh.specific.git import git_support
from oopsh.utils import quote_if_unsafe


@git_support
def match(command):
    return "push" in command.script and "The upstream branch of your current branch does not match" in command.output


@git_support
def get_new_command(command):
    remote, refspec = re.findall(r'^ +git push ([^\s]+) ([^\s]+)', command.output,
                                 re.MULTILINE)[0]
    # The refspec holds branch names, which can contain shell characters
    return 'git push {} {}'.format(quote_if_unsafe(remote), quote_if_unsafe(refspec))
