import re

from oopsh.utils import for_app, replace_command

INVALID_CHOICE = re.compile(r"Invalid choice: '([^']*)'")


@for_app('gcloud')
def match(command):
    return (INVALID_CHOICE.search(command.output) is not None
            and 'Maybe you meant:' in command.output)


def _suggested_words(output):
    suggestions = output.split('Maybe you meant:', 1)[1]
    for line in suggestions.splitlines():
        line = line.strip()
        if line.startswith('gcloud '):
            yield line.split()[-1]
        elif line:
            break


def get_new_command(command):
    broken = INVALID_CHOICE.search(command.output).group(1)
    return replace_command(command, broken,
                           list(_suggested_words(command.output)))
