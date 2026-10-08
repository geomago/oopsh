from subprocess import Popen, PIPE
import os
import sqlite3
from ..conf import settings
from ..const import ARGUMENT_PLACEHOLDER, EXECUTABLE, EXECUTABLE_ARGUMENTS
from ..logs import warn
from ..system import Path
from ..utils import DEVNULL
from .generic import Generic, ShellConfiguration


class Nushell(Generic):
    """Nushell has no `eval`: code is parsed before it runs, so the alias
    can't run the fix inside the shell like the other shells do.

    oopsh reruns the failed command with `sh` and its rules build POSIX
    commands, so the alias runs the fix with `sh -c` too (`nu -c` where
    there's no `sh`, on Windows). The fix can't change the shell's state
    from a subprocess, so the alias does the part that matters most: when
    the fix ends in another directory (`mkdir -p foo && cd foo`), it `cd`s
    there. Environment variables set by a fix are lost.

    """
    friendly_name = 'Nushell'

    def app_alias(self, alias_name):
        # `^oopsh` is the executable, even where the `oopsh` command below
        # shadows it
        return '''def --env --wrapped {name} [...args] {{
    let last = (history | last 2 | get command)
    # Depending on its settings, nushell has already saved this command
    let previous = if ($last | is-not-empty) and (($last | last) =~ '^{name}( |$)') {{
        $last | first
    }} else {{
        $last | last
    }}
    if ($previous | is-empty) or ($previous =~ '^{name}( |$)') {{ return }}
    let aliases = (scope aliases | each {{|a| $"($a.name)\\t($a.expansion)" }} | str join "\\n")
    let fixed = (try {{
        with-env {{
            TF_SHELL: nu
            TF_ALIAS: {name}
            TF_SHELL_ALIASES: $aliases
            OOPSH_NU_HISTORY: $nu.history-path
            PYTHONIOENCODING: utf-8
        }} {{
            ^{executable} $previous {placeholder} ...$args
        }}
    }} catch {{ "" }} | str trim)
    if ($fixed | is-empty) {{ return }}
    let pwd_file = (mktemp --tmpdir oopsh-pwd.XXXXXX)
    try {{
        with-env {{OOPSH_PWD_FILE: $pwd_file}} {{
            if (which sh | is-not-empty) {{
                ^sh -c ($fixed + ' && pwd > "$OOPSH_PWD_FILE"')
            }} else {{
                ^$nu.current-exe -c ($fixed + '; $env.PWD | save -f $env.OOPSH_PWD_FILE')
            }}
        }}
    }}
    let directory = (open --raw $pwd_file | str trim)
    rm -f $pwd_file
    if ($directory | is-not-empty) and ($directory != $env.PWD) {{
        cd $directory
    }}
}}
'''.format(name=alias_name, executable=EXECUTABLE,
           placeholder=ARGUMENT_PLACEHOLDER) \
            + self._executable_alias(alias_name)

    def _executable_alias(self, alias_name):
        """`oopsh` as a second name for the alias. Arguments meant for the
        executable (like `--alias` in the config) go to it instead."""
        if alias_name == EXECUTABLE:
            return ''
        pattern = '^(' + '|'.join(EXECUTABLE_ARGUMENTS) \
            + '|--alias=.*|--shell-logger=.*)$'
        return '''def --env --wrapped {executable} [...args] {{
    if ($args | is-not-empty) and (($args | first) =~ '{pattern}') {{
        ^{executable} ...$args
    }} else {{
        {name} ...$args
    }}
}}
'''.format(name=alias_name, executable=EXECUTABLE, pattern=pattern)

    def get_aliases(self):
        aliases = {}
        for line in os.environ.get('TF_SHELL_ALIASES', '').split('\n'):
            name, tab, value = line.partition('\t')
            if tab and name and value:
                aliases[name] = value
        return aliases

    def _get_history_file_name(self):
        path = os.environ.get('OOPSH_NU_HISTORY', '')
        return path if path.endswith(('.txt', '.sqlite3')) else ''

    def _get_history_lines(self):
        """Yield history entries, reading nushell's SQLite history when that
        is the configured format (the default since nushell 0.80)."""
        path = self._get_history_file_name()
        if path.endswith('.sqlite3'):
            for line in self._get_sqlite_history_lines(path):
                yield line
        else:
            for line in super(Nushell, self)._get_history_lines():
                yield line

    def _get_sqlite_history_lines(self, path):
        if not os.path.isfile(path):
            return

        query = 'SELECT command_line FROM history ORDER BY id'
        if settings.history_limit:
            # Keep the most recent entries, then restore chronological order.
            query = ('SELECT command_line FROM (SELECT id, command_line FROM'
                     ' history ORDER BY id DESC LIMIT {}) ORDER BY id'.format(
                         int(settings.history_limit)))

        try:
            # Read-only so a corrupt or non-database file can't be altered and
            # a missing file isn't created.
            connection = sqlite3.connect(
                '{}?mode=ro'.format(Path(path).as_uri()), uri=True)
        except sqlite3.Error as exc:
            warn(u'Can not open nushell history {}: {}'.format(path, exc))
            return

        try:
            for (command_line,) in connection.execute(query):
                prepared = (command_line or '').strip()
                if prepared:
                    yield prepared
        except sqlite3.Error as exc:
            warn(u'Can not read nushell history {}: {}'.format(path, exc))
        finally:
            connection.close()

    def how_to_configure(self):
        # Code is parsed before it runs, so `oopsh --alias | source` can't
        # work: the alias goes to a file that nushell autoloads after
        # config.nu
        autoload = '($nu.data-dir | path join vendor autoload)'
        content = (u'mkdir {0}; oopsh --alias | save -f ({0} | path join'
                   u' oopsh.nu)').format(autoload)
        path = self._get_config_path()
        return ShellConfiguration(
            content=content,
            path=path or '$nu.config-path',
            reload='exec nu',
            can_configure_automatically=bool(path) and os.path.isfile(path))

    def _get_config_path(self):
        try:
            proc = Popen(['nu', '-c', 'print $nu.config-path'],
                         stdout=PIPE, stderr=DEVNULL)
            return proc.stdout.read().decode('utf-8').strip()
        except OSError:
            return ''

    def _get_version(self):
        """Returns the version of the current shell"""
        proc = Popen(['nu', '--version'], stdout=PIPE, stderr=DEVNULL)
        return proc.stdout.read().decode('utf-8').strip()

    def get_builtin_commands(self):
        return super(Nushell, self).get_builtin_commands() + [
            'def', 'do', 'each', 'get', 'let', 'mkdir', 'mut', 'open',
            'print', 'save', 'where', 'with-env']
