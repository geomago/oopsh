"""Trusts a repository git refuses to use because someone else owns it, with
the command git itself suggests:

    fatal: detected dubious ownership in repository at '/srv/repo'
    To add an exception for this directory, call:

            git config --global --add safe.directory /srv/repo
"""
import re
from oopsh.shells import shell
from oopsh.specific.git import git_support

SUGGESTION = re.compile(r'^\s*(git config --global --add safe\.directory .+?)\s*$',
                        re.MULTILINE)


@git_support
def match(command):
    return ('detected dubious ownership' in command.output
            and SUGGESTION.search(command.output) is not None)


@git_support
def get_new_command(command):
    return shell.and_(SUGGESTION.search(command.output).group(1),
                      command.script)
