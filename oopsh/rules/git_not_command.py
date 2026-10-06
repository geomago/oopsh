import re
from oopsh.utils import get_all_matched_commands, replace_argument, replace_command
from oopsh.specific.git import git_support


# Typos git doesn't suggest a fix for, or suggests the wrong one
COMMON_TYPOS = {
    'copy': ['branch'],
    'list': ['branch'],
    'lock': ['log'],
    'update': ['fetch', 'fetch --all', 'fetch --all --tags', 'remote update'],
}


def _broken_command(command):
    return re.findall(r"git: '([^']*)' is not a git command",
                      command.output)[0]


@git_support
def match(command):
    return (" is not a git command. See 'git --help'." in command.output
            and ('The most similar command' in command.output
                 or 'Did you mean' in command.output
                 or _broken_command(command) in COMMON_TYPOS))


@git_support
def get_new_command(command):
    broken_cmd = _broken_command(command)
    common = [replace_argument(command.script, broken_cmd, fix)
              for fix in COMMON_TYPOS.get(broken_cmd, [])]
    suggested = replace_command(command, broken_cmd, list(get_all_matched_commands(
        command.output, ['The most similar command', 'Did you mean'])))
    return common + [new_command for new_command in suggested
                     if new_command not in common]
