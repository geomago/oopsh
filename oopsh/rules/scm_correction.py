import os
from oopsh.utils import for_app, memoize, replace_command_name
from oopsh.system import Path

path_to_scm = {
    '.git': 'git',
    '.hg': 'hg',
}

wrong_scm_patterns = {
    'git': 'fatal: Not a git repository',
    'hg': 'abort: no repository found',
}


@memoize
def _get_actual_scm():
    for path, scm in path_to_scm.items():
        if Path(path).is_dir():
            return scm


@for_app(*wrong_scm_patterns.keys())
def match(command):
    scm = next((os.path.basename(part) for part in command.script_parts
                if os.path.basename(part) in wrong_scm_patterns), None)
    if scm is None:
        return False

    return wrong_scm_patterns[scm] in command.output and _get_actual_scm()


def get_new_command(command):
    scm = _get_actual_scm()
    return replace_command_name(command.script, scm)
