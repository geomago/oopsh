import os
import shlex
import sys
import tty
import termios
import colorama
from pathlib import Path
from shutil import which
from .. import const

init_output = colorama.init


def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def get_key():
    ch = getch()

    if ch in const.KEY_MAPPING:
        return const.KEY_MAPPING[ch]
    elif ch == '\x1b':
        next_ch = getch()
        if next_ch == '[':
            last_ch = getch()

            if last_ch == 'A':
                return const.KEY_UP
            elif last_ch == 'B':
                return const.KEY_DOWN

    return ch


def open_command(arg):
    # `arg` can come from a command's output: never let it run as shell code
    if which('xdg-open'):
        return 'xdg-open ' + shlex.quote(arg)
    return 'open ' + shlex.quote(arg)


def _expanduser(self):
    return self.__class__(os.path.expanduser(str(self)))


if not hasattr(Path, 'expanduser'):
    Path.expanduser = _expanduser
