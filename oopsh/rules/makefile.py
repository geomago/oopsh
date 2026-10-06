"""Fixes misspelled `make` and make targets: `maek biuld` -> `make build`."""
import os
from oopsh.utils import get_closest

MAKEFILES = ('GNUmakefile', 'makefile', 'Makefile')
MISSPELLINGS = ['mke', 'maek', 'amke', 'meak', 'mkae', 'ake', 'mae', 'mak',
                'makee', 'mmake', 'nake', 'makr', 'mske']
TOLERANCE = 0.6


def _makefile():
    for name in MAKEFILES:
        if os.path.isfile(name):
            return name
    return None


def _targets(makefile):
    """Explicit targets: `name:` at the start of a line, not variables or
    pattern rules."""
    targets = []
    with open(makefile) as lines:
        for line in lines:
            if not line.strip() or line[0].isspace() or line.startswith(('.', '#')):
                continue
            head, colon, rest = line.partition(':')
            if not colon or '=' in head or rest.startswith('='):
                continue
            targets.extend(target for target in head.split()
                           if '%' not in target and '$' not in target)
    return targets


def match(command):
    if not command.script_parts or _makefile() is None:
        return False
    if command.script_parts[0] in MISSPELLINGS:
        return True
    return (command.script_parts[0] == 'make'
            and 'no rule to make target' in command.output.lower())


def get_new_command(command):
    targets = _targets(_makefile())
    parts = ['make']
    for part in command.script_parts[1:]:
        if targets and not part.startswith('-') and '=' not in part \
                and part not in targets:
            part = get_closest(part, targets, cutoff=TOLERANCE)
        parts.append(part)
    return ' '.join(parts)
