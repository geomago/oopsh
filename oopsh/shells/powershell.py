from subprocess import Popen, PIPE
from ..const import EXECUTABLE, EXECUTABLE_ARGUMENTS
from ..utils import DEVNULL
from .generic import Generic, ShellConfiguration


class Powershell(Generic):
    friendly_name = 'PowerShell'

    def app_alias(self, alias_name):
        # The `oopsh` function shadows the executable, so call it by type
        executable = '(Get-Command -CommandType Application {} | ' \
                     'Select-Object -First 1)'.format(EXECUTABLE)
        return 'function ' + alias_name + ' {\n' \
               '    $history = (Get-History -Count 1).CommandLine;\n' \
               '    if (-not [string]::IsNullOrWhiteSpace($history)) {\n' \
               '        $fixed = $(& ' + executable + ' $args $history);\n' \
               '        if (-not [string]::IsNullOrWhiteSpace($fixed)) {\n' \
               '            if ($fixed.StartsWith("echo")) { $fixed = $fixed.Substring(5); }\n' \
               '            else { iex "$fixed"; }\n' \
               '        }\n' \
               '    }\n' \
               '    [Console]::ResetColor() \n' \
               '}\n' + self._executable_alias(alias_name, executable)

    def _executable_alias(self, alias_name, executable):
        """`oopsh` as a second name for the alias. Arguments meant for the
        executable (like `--alias` in the profile) go to it instead."""
        if alias_name == EXECUTABLE:
            return ''
        pattern = '^(' + '|'.join(EXECUTABLE_ARGUMENTS) \
            + '|--alias=.*|--shell-logger=.*)$'
        return 'function ' + EXECUTABLE + ' {\n' \
               "    if ($args.Count -gt 0 -and $args[0] -cmatch '" + pattern + "') {\n" \
               '        & ' + executable + ' @args\n' \
               '    } else {\n' \
               '        ' + alias_name + ' @args\n' \
               '    }\n' \
               '}\n'

    def and_(self, *commands):
        return u' -and '.join('({0})'.format(c) for c in commands)

    def how_to_configure(self):
        return ShellConfiguration(
            content=u'iex "$(oopsh --alias)"',
            path='$profile',
            reload='. $profile',
            can_configure_automatically=False)

    def _get_version(self):
        """Returns the version of the current shell"""
        try:
            proc = Popen(
                ['powershell.exe', '$PSVersionTable.PSVersion'],
                stdout=PIPE,
                stderr=DEVNULL)
            version = proc.stdout.read().decode('utf-8').rstrip().split('\n')
            return '.'.join(version[-1].split())
        except IOError:
            proc = Popen(['pwsh', '--version'], stdout=PIPE, stderr=DEVNULL)
            return proc.stdout.read().decode('utf-8').split()[-1]
