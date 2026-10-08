import re
from oopsh.utils import for_app, quote_if_unsafe
from oopsh.specific.brew import brew_available

enabled_by_default = brew_available

# The real "formula typo" suggestion looks like:
#   Warning: No available formula with the name "pythonn". Did you mean python?
# The negative lookahead skips the cask hint ("Did you mean to type
# ...brew cask install..."), which has a different shape and used to make
# get_new_command crash (nvbn/thefuck#936).
suggestion_regex = re.compile(
    r'No available formula with the name "(?:[^"]+)"\. '
    r'Did you mean ((?!to type)[^?]+)\?')


def _get_suggestions(str):
    suggestions = str.replace(" or ", ", ").split(", ")
    return suggestions


@for_app('brew', at_least=2)
def match(command):
    return 'install' in command.script and \
        bool(suggestion_regex.search(command.output))


def get_new_command(command):
    matcher = suggestion_regex.search(command.output)
    suggestions = _get_suggestions(matcher.group(1))
    return ["brew install " + quote_if_unsafe(formula) for formula in suggestions]
