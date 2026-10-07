import os
import sys
from .conf import settings
from .types import Rule
from .system import Path
from .utils import is_private
from . import logs


def get_loaded_rules(rules_paths):
    """Yields all available rules.

    :type rules_paths: [Path]
    :rtype: Iterable[Rule]

    """
    for path in rules_paths:
        if path.name != '__init__.py':
            rule = Rule.from_path(path)
            if rule and rule.is_enabled:
                yield rule


def _is_trusted_dir(path):
    """Third-party rules run as soon as they're found: only take them from
    directories owned by the user or root and not writable by others, so
    another user of a shared machine can't plant some (nvbn/thefuck#1623)."""
    if not hasattr(os, 'getuid'):
        return True
    for directory in (path, path.parent):
        try:
            if not is_private(directory.stat(), owners=(0, os.getuid())):
                return False
        except OSError:
            return False
    return True


def get_rules_import_paths():
    """Yields all rules import paths.

    :rtype: Iterable[Path]

    """
    # Bundled rules:
    yield Path(__file__).parent.joinpath('rules')
    # Rules defined by user:
    yield settings.user_dir.joinpath('rules')
    # Packages with third-party rules:
    for path in sys.path:
        for pattern in ('oopsh_contrib_*', 'thefuck_contrib_*'):
            for contrib_module in Path(path).glob(pattern):
                contrib_rules = contrib_module.joinpath('rules')
                if not contrib_rules.is_dir():
                    continue
                if _is_trusted_dir(contrib_rules):
                    yield contrib_rules
                else:
                    logs.warn(u'Ignoring rules in {}: other users can write '
                              u'there'.format(contrib_rules))


def get_rules():
    """Returns all enabled rules.

    :rtype: [Rule]

    """
    paths = [rule_path for path in get_rules_import_paths()
             for rule_path in sorted(path.glob('*.py'))]
    return sorted(get_loaded_rules(paths),
                  key=lambda rule: rule.priority)


def organize_commands(corrected_commands):
    """Yields sorted commands without duplicates.

    :type corrected_commands: Iterable[oopsh.types.CorrectedCommand]
    :rtype: Iterable[oopsh.types.CorrectedCommand]

    """
    try:
        first_command = next(corrected_commands)
        yield first_command
    except StopIteration:
        return

    without_duplicates = {
        command for command in sorted(
            corrected_commands, key=lambda command: command.priority)
        if command != first_command}

    sorted_commands = sorted(
        without_duplicates,
        key=lambda corrected_command: corrected_command.priority)

    logs.debug(u'Corrected commands: {}'.format(
        ', '.join(u'{}'.format(cmd) for cmd in [first_command] + sorted_commands)))

    yield from sorted_commands


def get_corrected_commands(command):
    """Returns generator with sorted and unique corrected commands.

    :type command: oopsh.types.Command
    :rtype: Iterable[oopsh.types.CorrectedCommand]

    """
    corrected_commands = (
        corrected for rule in get_rules()
        if rule.is_match(command)
        for corrected in rule.get_corrected_commands(command))
    return organize_commands(corrected_commands)
