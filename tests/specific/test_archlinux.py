import subprocess
import pytest
from oopsh.specific.archlinux import get_pkgfile


@pytest.fixture(autouse=True)
def check_output(mocker):
    return mocker.patch('oopsh.specific.archlinux.subprocess.check_output')


@pytest.mark.usefixtures('no_memoize')
def test_get_pkgfile(check_output):
    check_output.return_value = 'extra/vim 9.0-1\t/usr/bin/vim\nextra/gvim 9.0-1\t/usr/bin/vim\n'
    assert get_pkgfile('sudo vim foo') == ['extra/vim', 'extra/gvim']
    assert check_output.call_args[0][0] == ['pkgfile', '-b', '-v', 'vim']


@pytest.mark.usefixtures('no_memoize')
@pytest.mark.parametrize('error', [
    FileNotFoundError('pkgfile'),
    subprocess.CalledProcessError(1, 'pkgfile', output=''),
    subprocess.CalledProcessError(2, 'pkgfile', output='')])
def test_get_pkgfile_errors(check_output, error):
    """nvbn/thefuck#1129: missing pkgfile or pkgfile database."""
    check_output.side_effect = error
    assert get_pkgfile('vim') == []
