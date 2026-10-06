# -*- encoding: utf-8 -*-

import os
import sys
from .conf import settings
from .exceptions import NoRuleMatched
from .system import get_key
from .utils import get_alias
from . import logs, const


def _is_interactive():
    """Returns `True` when stdin is a terminal we can read keys from."""
    try:
        return os.isatty(sys.stdin.fileno())
    except (AttributeError, ValueError, OSError):
        return False


def read_actions():
    """Yields actions for pressed keys."""
    while True:
        key = get_key()

        # Handle arrows, j/k (qwerty), and n/e (colemak)
        if key in (const.KEY_UP, const.KEY_CTRL_N, 'k', 'e'):
            yield const.ACTION_PREVIOUS
        elif key in (const.KEY_DOWN, const.KEY_CTRL_P, 'j', 'n'):
            yield const.ACTION_NEXT
        elif key in (const.KEY_CTRL_C, 'q'):
            yield const.ACTION_ABORT
        elif key == '':
            # End of input: the terminal was closed. Without this we would
            # spin forever at full CPU (nvbn/thefuck#806)
            yield const.ACTION_ABORT
            return
        elif key in ('\n', '\r'):
            yield const.ACTION_SELECT


class CommandSelector(object):
    """Helper for selecting rule from rules list."""

    def __init__(self, commands):
        """:type commands: Iterable[oopsh.types.CorrectedCommand]"""
        self._commands_gen = commands
        try:
            self._commands = [next(self._commands_gen)]
        except StopIteration:
            raise NoRuleMatched
        self._realised = False
        self._index = 0

    def _realise(self):
        if not self._realised:
            self._commands += list(self._commands_gen)
            self._realised = True

    def next(self):
        self._realise()
        self._index = (self._index + 1) % len(self._commands)

    def previous(self):
        self._realise()
        self._index = (self._index - 1) % len(self._commands)

    @property
    def value(self):
        """:rtype oopsh.types.CorrectedCommand"""
        return self._commands[self._index]


def select_command(corrected_commands):
    """Returns:

     - the first command when confirmation disabled;
     - None when ctrl+c pressed;
     - selected command.

    :type corrected_commands: Iterable[oopsh.types.CorrectedCommand]
    :rtype: oopsh.types.CorrectedCommand | None

    """
    try:
        selector = CommandSelector(corrected_commands)
    except NoRuleMatched:
        logs.failed('No fucks given' if get_alias() == 'fuck'
                    else 'Nothing found')
        return

    if not settings.require_confirmation:
        logs.show_corrected_command(selector.value)
        return selector.value

    if not _is_interactive():
        # Never run a fix the user couldn't confirm
        logs.show_corrected_command(selector.value)
        logs.failed("Can't ask for confirmation: stdin is not a terminal. "
                    "Run with --yes to execute the fix.")
        return

    logs.confirm_text(selector.value)

    for action in read_actions():
        if action == const.ACTION_SELECT:
            sys.stderr.write('\n')
            return selector.value
        elif action == const.ACTION_ABORT:
            logs.failed('\nAborted')
            return
        elif action == const.ACTION_PREVIOUS:
            selector.previous()
            logs.confirm_text(selector.value)
        elif action == const.ACTION_NEXT:
            selector.next()
            logs.confirm_text(selector.value)
