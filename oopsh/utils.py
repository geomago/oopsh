import atexit
import dbm
import os
import pickle
import re
import shelve
import shlex
import shutil
import sys
from decorator import decorator
from difflib import get_close_matches as difflib_get_close_matches
from functools import wraps
from .logs import warn, exception
from .conf import settings
from .system import Path

DEVNULL = open(os.devnull, 'w')

shelve_open_error = dbm.error


def memoize(fn):
    """Caches previous calls to the function."""
    memo = {}

    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not memoize.disabled:
            key = pickle.dumps((args, kwargs))
            if key not in memo:
                memo[key] = fn(*args, **kwargs)
            value = memo[key]
        else:
            # Memoize is disabled, call the function
            value = fn(*args, **kwargs)

        return value

    return wrapper


memoize.disabled = False


@memoize
def which(program):
    """Returns `program` path or `None`."""
    return shutil.which(program)


def default_settings(params):
    """Adds default values to settings if it not presented.

    Usage:

        @default_settings({'apt': '/usr/bin/apt'})
        def match(command):
            print(settings.apt)

    """
    def _default_settings(fn, command):
        for k, w in params.items():
            settings.setdefault(k, w)
        return fn(command)
    return decorator(_default_settings)


def get_closest(word, possibilities, cutoff=0.6, fallback_to_first=True):
    """Returns closest match or just first from possibilities."""
    possibilities = list(possibilities)
    try:
        return difflib_get_close_matches(word, possibilities, 1, cutoff)[0]
    except IndexError:
        if fallback_to_first:
            return possibilities[0]


def get_close_matches(word, possibilities, n=None, cutoff=0.6):
    """Overrides `difflib.get_close_matches` to control argument `n`."""
    if n is None:
        n = settings.num_close_matches
    return difflib_get_close_matches(word, possibilities, n, cutoff)


def include_path_in_search(path):
    return not any(path.startswith(x) for x in settings.excluded_search_path_prefixes)


@memoize
def get_all_executables():
    from oopsh.shells import shell

    def _safe(fn, fallback):
        try:
            return fn()
        except OSError:
            return fallback

    tf_alias = get_alias()
    tf_entry_points = ['oopsh', 'oops']

    bins = [exe.name
            for path in os.environ.get('PATH', '').split(os.pathsep)
            if include_path_in_search(path)
            for exe in _safe(lambda: list(Path(path).iterdir()), [])
            if not _safe(exe.is_dir, True)]
    if sys.platform == 'win32':
        # `git.exe` is run as `git`, and `PING.EXE` as `ping`: Windows
        # ignores case
        extensions = os.environ.get('PATHEXT', '.COM;.EXE;.BAT;.CMD') \
            .lower().split(';')
        bins += [os.path.splitext(name)[0].lower() for name in bins
                 if os.path.splitext(name)[1].lower() in extensions]
        tf_entry_points += [name + '.exe' for name in tf_entry_points]
    bins = [name for name in bins if name not in tf_entry_points]
    aliases = [alias
               for alias in shell.get_aliases() if alias != tf_alias]

    return bins + aliases


def replace_command_name(script, new_name):
    """Replaces the first word of `script`, keeping the rest of it as typed,
    quotes included. With an empty `new_name`, just drops the first word.

    Rebuilding the script from `script_parts` would turn
    `git commit -m "a b"` into `git commit -m a b`.

    """
    rest = re.sub(r'^\s*\S+\s*', '', script, count=1)
    return u' '.join(part for part in (new_name, rest) if part)


# Characters that make the shell do something other than pass a word along
UNSAFE_CHARACTERS = re.compile(r'[;&|$`<>()\\\n\'"*?!{}]')


def quote_if_unsafe(word):
    """Quotes `word` if the shell would interpret it.

    Rules build fixes from text in commands' output, which whoever controls
    that output (a remote server, a package index...) could fill with shell
    code; the alias evaluates the fix (nvbn/thefuck#1622). Ordinary
    suggestions, even with spaces like `fetch --all`, are left as they are.

    """
    if UNSAFE_CHARACTERS.search(word):
        return shlex.quote(word)
    return word


def replace_argument(script, from_, to, quote=True):
    """Replaces command line argument.

    `to` is quoted if the shell would interpret it, unless `quote` is
    `False`: for replacements a rule builds itself, already safe.

    """
    if quote:
        to = quote_if_unsafe(to)
    replaced_in_the_end = re.sub(u' {}$'.format(re.escape(from_)),
                                 lambda _: u' {}'.format(to),
                                 script, count=1)
    if replaced_in_the_end != script:
        return replaced_in_the_end
    else:
        return script.replace(
            u' {} '.format(from_), u' {} '.format(to), 1)


@decorator
def eager(fn, *args, **kwargs):
    return list(fn(*args, **kwargs))


@eager
def get_all_matched_commands(stderr, separator='Did you mean'):
    if not isinstance(separator, list):
        separator = [separator]
    should_yield = False
    for line in stderr.split('\n'):
        for sep in separator:
            if sep in line:
                should_yield = True
                break
        else:
            if should_yield and line:
                yield line.strip()


def replace_command(command, broken, matched):
    """Helper for *_no_command rules."""
    new_cmds = get_close_matches(broken, matched, cutoff=0.1)
    return [replace_argument(command.script, broken, new_cmd.strip())
            for new_cmd in new_cmds]


@memoize
def is_app(command, *app_names, **kwargs):
    """Returns `True` if command is call to one of passed app names."""

    at_least = kwargs.pop('at_least', 0)
    if kwargs:
        raise TypeError("got an unexpected keyword argument '{}'".format(kwargs.keys()))

    if len(command.script_parts) > at_least:
        return os.path.basename(command.script_parts[0]) in app_names

    return False


def for_app(*app_names, **kwargs):
    """Specifies that matching script is for one of app names."""
    def _for_app(fn, command):
        if is_app(command, *app_names, **kwargs):
            return fn(command)
        else:
            return False

    return decorator(_for_app)


def is_inside(path, directory):
    """Returns `True` when `path` is in `directory`, symlinks resolved.

    A string prefix check isn't enough: `/home/u/proj-evil` starts with
    `/home/u/proj`.

    """
    path = os.path.realpath(path)
    directory = os.path.realpath(directory)
    try:
        return os.path.commonpath([path, directory]) == directory
    except ValueError:  # different drives on Windows
        return False


def get_cache_dir():
    """Returns oopsh's private cache dir, `$XDG_CACHE_HOME/oopsh`, creating
    it readable by the user only."""
    xdg_cache_home = os.getenv('XDG_CACHE_HOME', os.path.expanduser('~/.cache'))
    cache_dir = os.path.join(xdg_cache_home, 'oopsh')
    if os.path.isfile(cache_dir):
        # oopsh 1.0.0 kept its cache in a file with this name
        os.remove(cache_dir)
    os.makedirs(cache_dir, mode=0o700, exist_ok=True)
    return cache_dir


def _is_private_group(gid):
    """`True` for the user's private group: with the user private group
    scheme (Debian, Ubuntu, Fedora...), the default umask 002 makes files
    writable by a group named like the user, that only they belong to."""
    try:
        import grp
        import pwd
        group = grp.getgrgid(gid)
        user = pwd.getpwuid(os.getuid()).pw_name
    except (ImportError, KeyError):
        return False
    return group.gr_name == user and set(group.gr_mem) <= {user}


def is_private(path_or_stat, owners=None):
    """Returns `True` when the file belongs to the user (or to one of
    `owners`) and nobody else can write to it, so others can't plant
    content oopsh would trust."""
    if not hasattr(os, 'getuid'):
        return True
    stat = path_or_stat if isinstance(path_or_stat, os.stat_result) \
        else os.stat(path_or_stat)
    if stat.st_uid not in (owners or (os.getuid(),)):
        return False
    if stat.st_mode & 0o002:
        return False
    return not stat.st_mode & 0o020 or _is_private_group(stat.st_gid)


class Cache(object):
    """Lazy read cache and save changes at exit."""

    def __init__(self):
        self._db = None

    def _init_db(self):
        try:
            self._setup_db()
        except Exception:
            exception("Unable to init cache", sys.exc_info())
            self._db = {}

    def _setup_db(self):
        cache_dir = get_cache_dir()
        # The cache is pickled: loading one someone else wrote runs their code
        if not is_private(cache_dir):
            warn("Not using the cache in {}: other users can write there"
                 .format(cache_dir))
            self._db = {}
            return
        cache_path = Path(cache_dir).joinpath('cache').as_posix()

        try:
            self._db = shelve.open(cache_path)
        except shelve_open_error + (ImportError,):
            # Caused when switching between Python versions
            warn("Removing possibly out-dated cache")
            os.remove(cache_path)
            self._db = shelve.open(cache_path)

        atexit.register(self._db.close)

    def _get_mtime(self, path):
        try:
            return str(os.path.getmtime(path))
        except OSError:
            return '0'

    def _get_key(self, fn, depends_on, args, kwargs):
        parts = (fn.__module__, repr(fn).split('at')[0],
                 depends_on, args, kwargs)
        return str(pickle.dumps(parts))

    def get_value(self, fn, depends_on, args, kwargs):
        if self._db is None:
            self._init_db()

        depends_on = [Path(name).expanduser().absolute().as_posix()
                      for name in depends_on]
        key = self._get_key(fn, depends_on, args, kwargs)
        etag = '.'.join(self._get_mtime(path) for path in depends_on)

        if self._db.get(key, {}).get('etag') == etag:
            return self._db[key]['value']
        else:
            value = fn(*args, **kwargs)
            self._db[key] = {'etag': etag, 'value': value}
            return value


_cache = Cache()


def cache(*depends_on):
    """Caches function result in temporary file.

    Cache will be expired when modification date of files from `depends_on`
    will be changed.

    Only functions should be wrapped in `cache`, not methods.

    """
    def cache_decorator(fn):
        @memoize
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if cache.disabled:
                return fn(*args, **kwargs)
            else:
                return _cache.get_value(fn, depends_on, args, kwargs)

        return wrapper

    return cache_decorator


cache.disabled = False


def get_installation_version():
    from importlib.metadata import version

    return version('oopsh')


# The alias name ends up in generated shell code and in fixes
ALIAS_NAME = re.compile(r'^[A-Za-z_][A-Za-z0-9_-]*$')


def get_alias():
    alias = os.environ.get('TF_ALIAS', 'oops')
    return alias if ALIAS_NAME.match(alias) else 'oops'


@memoize
def get_valid_history_without_current(command):
    def _not_corrected(history, tf_alias):
        """Returns all lines from history except that comes before `oops`."""
        previous = None
        for line in history:
            if previous is not None and line != tf_alias:
                yield previous
            previous = line
        if history:
            yield history[-1]

    from oopsh.shells import shell
    history = shell.get_history()
    tf_alias = get_alias()
    executables = set(get_all_executables())\
        .union(shell.get_builtin_commands())

    return [line for line in _not_corrected(history, tf_alias)
            if not line.startswith(tf_alias) and not line == command.script
            and line.split(' ')[0] in executables]


def format_raw_script(raw_script):
    """Creates single script from a list of script parts.

    :type raw_script: [str]
    :rtype: str

    """
    script = ' '.join(raw_script)

    return script.lstrip()
