"""Moves an existing thefuck setup over to oopsh."""
import os
import shutil
import colorama
from .. import const
from ..conf import get_thefuck_env_name, get_thefuck_user_dir, get_user_dir
from ..logs import color
from ..shells import shell
from ..system import Path


def _bold(text):
    return u'{}{}{}'.format(color(colorama.Style.BRIGHT), text,
                            color(colorama.Style.RESET_ALL))


def _is_default_settings(path):
    """Returns `True` when `settings.py` only has the comments that oopsh
    writes on the first run."""
    with path.open() as settings_file:
        return all(not line.strip() or line.lstrip().startswith('#')
                   for line in settings_file)


def _copy_config(source, destination):
    """Copies the files of `source` that aren't in `destination` yet.

    :rtype: ([Path], [Path]) relative paths of copied and skipped files

    """
    copied, skipped = [], []
    for path in sorted(source.rglob('*')):
        relative = path.relative_to(source)
        if path.is_dir() or '__pycache__' in relative.parts:
            continue

        target = destination.joinpath(relative)
        if target.exists() and not (relative == Path('settings.py')
                                    and _is_default_settings(target)):
            skipped.append(relative)
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(path), str(target))
        copied.append(relative)
    return copied, skipped


def _migrate_config():
    source = get_thefuck_user_dir()
    destination = get_user_dir()
    if source is None:
        print(u'No thefuck config found, nothing to copy.')
        return

    copied, skipped = _copy_config(source, destination)
    print(u'Copied {} file(s) from {} to {}.'.format(
        len(copied), _bold(source), _bold(destination)))
    for relative in skipped:
        print(u'  Skipped {}: it already exists in {}.'.format(
            relative.as_posix(), destination))
    print(u'Custom rules importing from {} keep working as they are.'.format(
        _bold('thefuck')))
    print(u'You can delete {} once oopsh works for you.'.format(source))


def _migrate_shell_config():
    configuration = shell.how_to_configure()
    if not configuration:
        print(u'\nSet up the alias as described at '
              u'https://github.com/geomago/oopsh#manual-installation')
        return

    path = Path(configuration.path).expanduser()
    content = path.read_text(errors='replace') if path.is_file() else ''
    if 'thefuck --alias' in content:
        print(u'\nIn {}, replace the line with {} with:\n\n    {}\n'.format(
            _bold(configuration.path), _bold('thefuck --alias'),
            configuration.content))
    elif 'oopsh --alias' in content:
        print(u'\n{} already sets up oopsh.'.format(configuration.path))
        return
    else:
        print(u'\nAdd this line to {}:\n\n    {}\n'.format(
            _bold(configuration.path), configuration.content))
    print(u'Then run {} or restart your shell, and type {} instead of {}.'.format(
        _bold(configuration.reload), _bold('oops'), _bold('fuck')))
    print(u'To keep typing fuck, use {} instead.'.format(
        _bold(configuration.content.replace('--alias', '--alias fuck'))))


def _migrate_env():
    names = [get_thefuck_env_name(env) for env in const.ENV_TO_ATTR]
    names.append('THEFUCK_OVERRIDDEN_ALIASES')
    found = sorted(name for name in names if name in os.environ)
    if found:
        print(u'\nThese env vars still work, but you can rename them to '
              u'OOPSH_*: {}'.format(', '.join(found)))


def migrate():
    """Copies thefuck's config to oopsh's config dir and explains what else
    to change. Never overwrites existing files."""
    _migrate_config()
    _migrate_shell_config()
    _migrate_env()
