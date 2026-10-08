import re
from oopsh.utils import for_app
from oopsh.specific.brew import brew_available


@for_app('brew', at_least=2)
def match(command):
    # Modern Homebrew removed the `brew cask <cmd>` syntax:
    #   Error: Calling brew cask reinstall is disabled!
    #   Use brew reinstall --cask instead.
    return ('cask' in command.script_parts
            and 'is disabled' in command.output
            and '--cask' in command.output)


def get_new_command(command):
    # `brew cask reinstall firefox` -> `brew reinstall --cask firefox`
    return re.sub(r'\bcask\s+(\S+)', r'\1 --cask', command.script, count=1)


enabled_by_default = brew_available
