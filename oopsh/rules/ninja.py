import re
from oopsh.utils import for_app, replace_argument

UNKNOWN_TARGET = re.compile(r"unknown target '([^']*)', did you mean '([^']*)'\?")


@for_app('ninja')
def match(command):
    return UNKNOWN_TARGET.search(command.output) is not None


def get_new_command(command):
    broken, fixed = UNKNOWN_TARGET.search(command.output).groups()
    return replace_argument(command.script, broken, fixed)
