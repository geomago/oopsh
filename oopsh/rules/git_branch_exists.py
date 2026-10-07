import re
from oopsh.shells import shell
from oopsh.specific.git import git_support
from oopsh.utils import eager, quote_if_unsafe


@git_support
def match(command):
    return ("fatal: A branch named '" in command.output
            and "' already exists." in command.output)


@git_support
@eager
def get_new_command(command):
    branch_name = re.findall(
        r"fatal: A branch named '(.+)' already exists.", command.output)[0]
    branch_name = quote_if_unsafe(branch_name)
    new_command_templates = [['git branch -d {0}', 'git branch {0}'],
                             ['git branch -d {0}', 'git checkout -b {0}'],
                             ['git branch -D {0}', 'git branch {0}'],
                             ['git branch -D {0}', 'git checkout -b {0}'],
                             ['git checkout {0}']]
    for new_command_template in new_command_templates:
        yield shell.and_(*new_command_template).format(branch_name)
