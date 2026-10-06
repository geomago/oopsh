import re
from oopsh.utils import for_app, replace_command
from oopsh.specific.npm import get_scripts, npm_available

enabled_by_default = npm_available

# npm 6: `npm ERR! missing script: x`, npm 7+: `npm ERR! Missing script: "x"`,
# npm 10: `npm error Missing script: "x"`
MISSING_SCRIPT = re.compile(r'missing script: "?([^"\n]+)"?', re.IGNORECASE)


@for_app('npm')
def match(command):
    return (any(part.startswith('ru') for part in command.script_parts)
            and MISSING_SCRIPT.search(command.output) is not None)


def get_new_command(command):
    misspelled_script = MISSING_SCRIPT.search(command.output).group(1)
    return replace_command(command, misspelled_script, get_scripts())
