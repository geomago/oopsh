import subprocess
from oopsh.shells import shell
from oopsh.specific.git import git_support
from oopsh.utils import DEVNULL, replace_argument


@git_support
def match(command):
    return (
        ("branch -d" in command.script or "branch -D" in command.script)
        and "error: Cannot delete branch '" in command.output
        and "' checked out at '" in command.output
    )


def _git(*args):
    try:
        return subprocess.check_output(('git',) + args, stderr=DEVNULL) \
            .decode('utf-8').strip()
    except (OSError, subprocess.CalledProcessError):
        return ''


def _get_default_branch():
    """The branch `origin/HEAD` points to, else `main` if it exists, else
    `master`."""
    remote_head = _git('symbolic-ref', '--short', 'refs/remotes/origin/HEAD')
    if '/' in remote_head:
        return remote_head.split('/', 1)[1]
    if _git('rev-parse', '--verify', '--quiet', 'refs/heads/main'):
        return 'main'
    return 'master'


@git_support
def get_new_command(command):
    return shell.and_("git checkout {}".format(_get_default_branch()), "{}").format(
        replace_argument(command.script, "-d", "-D")
    )
