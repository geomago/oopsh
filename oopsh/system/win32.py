import os
import msvcrt
from pathlib import Path
from .. import const


def init_output():
    import colorama
    colorama.init()


def get_key():
    ch = msvcrt.getwch()
    if ch in ('\x00', '\xe0'):  # arrow or function key prefix?
        ch = msvcrt.getwch()  # second call returns the actual key code

    if ch in const.KEY_MAPPING:
        return const.KEY_MAPPING[ch]
    if ch == 'H':
        return const.KEY_UP
    if ch == 'P':
        return const.KEY_DOWN

    return ch


def open_command(arg):
    # `arg` can come from a command's output: drop the characters cmd.exe
    # treats specially, and quote it (the empty title keeps `start` from
    # taking the quoted argument as the window title)
    arg = ''.join(char for char in arg if char not in '"&|<>^%!')
    return 'cmd /c start "" "{}"'.format(arg)


def _expanduser(self):
    return self.__class__(os.path.expanduser(str(self)))


# pathlib's expanduser fails on windows, see http://bugs.python.org/issue19776
Path.expanduser = _expanduser
