import re
from oopsh.utils import for_app, replace_command


@for_app('restic')
def match(command):
    return (re.search('unknown command ".*" for "restic"', command.output)
            and 'Did you mean this' in command.output)


def get_new_command(command):
    broken_cmd = re.findall(r'unknown command "([^"]+)"', command.output)[0]
    suggestions = command.output.split('Did you mean this?', 1)[1]
    matched = []
    for line in suggestions.strip('\n').splitlines():
        if not line.strip():
            break
        matched.append(line.strip())
    return replace_command(command, broken_cmd, matched)
