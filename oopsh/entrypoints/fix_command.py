from contextlib import contextmanager
from pprint import pformat
import io
import os
import sys
from difflib import SequenceMatcher
from .. import logs, types, const
from ..conf import settings
from ..corrector import get_corrected_commands
from ..exceptions import EmptyCommand
from ..ui import select_command
from ..utils import get_alias, get_all_executables


def _get_raw_command(known_args):
    if known_args.force_command:
        return [known_args.force_command]
    elif not os.environ.get('TF_HISTORY'):
        return known_args.command
    else:
        history = os.environ['TF_HISTORY'].split('\n')[::-1]
        alias = get_alias()
        executables = get_all_executables()
        for command in history:
            diff = SequenceMatcher(a=alias, b=command).ratio()
            if diff < const.DIFF_WITH_ALIAS or command in executables:
                return [command]
    return []


@contextmanager
def _only_the_fix_on_stdout():
    """The shell alias evaluates whatever oopsh writes to stdout, so nothing
    but the fix may get there: while rules run, stdout (the file descriptor,
    which subprocesses inherit, and `sys.stdout`) goes to stderr. Yields a
    stream on the real stdout, for the fix.

    """
    sys.stdout.flush()
    real_stdout_fd = os.dup(1)
    os.dup2(2, 1)
    original_stdout = sys.stdout
    sys.stdout = sys.stderr
    real_stdout = io.TextIOWrapper(
        io.FileIO(real_stdout_fd, 'w', closefd=False),
        encoding=original_stdout.encoding or 'utf-8',
        errors=getattr(original_stdout, 'errors', None) or 'strict')
    try:
        yield real_stdout
    finally:
        real_stdout.flush()
        sys.stdout = original_stdout
        os.dup2(real_stdout_fd, 1)
        os.close(real_stdout_fd)


def fix_command(known_args):
    """Fixes previous command. Used when `oopsh` called without arguments."""
    settings.init(known_args)
    with _only_the_fix_on_stdout() as real_stdout, logs.debug_time('Total'):
        logs.debug(u'Run with settings: {}'.format(pformat(settings)))
        raw_command = _get_raw_command(known_args)

        try:
            command = types.Command.from_raw_script(raw_command)
        except EmptyCommand:
            logs.debug('Empty command, nothing to do')
            return

        corrected_commands = get_corrected_commands(command)
        selected_command = select_command(corrected_commands)

        if selected_command:
            selected_command.run(command, out=real_stdout)
        else:
            sys.exit(1)
