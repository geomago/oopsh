import pytest

# `sh` sets things up, then starts nushell. `TERM=dumb` stops reedline from
# asking the terminal for the cursor position (`ESC[6n`): the pexpect harness
# is not a real terminal and never answers, which otherwise hangs the prompt.
containers = ((u'oopsh/python3', u'', u'sh', [u'-e', u'TERM=dumb']),)

# Nushell has no `eval`, so the alias can't be sourced: it goes to a file that
# nushell autoloads. Generate it with `TF_SHELL=nu` since `oopsh` is run from
# `sh` here, not from within nushell.
init = u'''export TERM=dumb
AUTOLOAD="$(nu --no-config-file -c 'print ($nu.data-dir | path join vendor autoload)')"
mkdir -p "$AUTOLOAD"
TF_SHELL=nu oopsh --alias oops > "$AUTOLOAD/oopsh.nu"'''


@pytest.fixture(params=containers)
def proc(request, spawnu, TIMEOUT):
    proc = spawnu(*request.param)
    proc.sendline(init)
    proc.sendline(u'nu')
    return proc


def _set_confirmation(proc, require):
    # Written through `sh` because nushell has no `>` redirection and its
    # `mkdir` has no `-p` flag.
    proc.sendline(
        u'^sh -c \'mkdir -p ~/.config/oopsh && '
        u'printf "require_confirmation = {}\\n" > ~/.config/oopsh/settings.py\''
        .format(require))


@pytest.mark.functional
def test_with_confirmation(proc, TIMEOUT):
    _set_confirmation(proc, True)
    proc.sendline(u'ehco test')
    proc.sendline(u'oops')
    assert proc.expect([TIMEOUT, u'echo test'])
    assert proc.expect([TIMEOUT, u'enter'])
    assert proc.expect_exact([TIMEOUT, u'ctrl+c'])
    proc.send('\n')
    assert proc.expect([TIMEOUT, u'test'])


@pytest.mark.functional
def test_refuse_with_confirmation(proc, TIMEOUT):
    _set_confirmation(proc, True)
    proc.sendline(u'ehco test')
    proc.sendline(u'oops')
    assert proc.expect([TIMEOUT, u'echo test'])
    assert proc.expect([TIMEOUT, u'enter'])
    assert proc.expect_exact([TIMEOUT, u'ctrl+c'])
    proc.send('\003')
    assert proc.expect([TIMEOUT, u'Aborted'])


@pytest.mark.functional
def test_without_confirmation(proc, TIMEOUT):
    _set_confirmation(proc, False)
    proc.sendline(u'ehco test')
    proc.sendline(u'oops')
    assert proc.expect([TIMEOUT, u'echo test'])
    assert proc.expect([TIMEOUT, u'test'])


@pytest.mark.functional
def test_without_confirmation_oopsh(proc, TIMEOUT):
    _set_confirmation(proc, False)
    proc.sendline(u'ehco test')
    proc.sendline(u'oopsh')
    assert proc.expect([TIMEOUT, u'echo test'])
    assert proc.expect([TIMEOUT, u'test'])
