import pytest
from oopsh.types import Command
from oopsh.rules.chmod_x import match, get_new_command


@pytest.fixture
def file_exists(mocker):
    return mocker.patch('os.path.exists', return_value=True)


@pytest.fixture
def file_access(mocker):
    return mocker.patch('os.access', return_value=False)


@pytest.mark.usefixtures('file_exists', 'file_access')
@pytest.mark.parametrize('script, output', [
    ('./gradlew build', 'gradlew: Permission denied'),
    ('./install.sh --help', 'install.sh: permission denied'),
    ('/opt/tool/run.sh', 'zsh: permission denied: /opt/tool/run.sh'),
    ('~/bin/deploy', 'zsh: permission denied: /home/me/bin/deploy'),
    ('scripts/build.sh', 'bash: scripts/build.sh: Permission denied')])
def test_match(script, output):
    assert match(Command(script, output))


@pytest.mark.parametrize('script, output, exists, callable', [
    ('./gradlew build', 'gradlew: Permission denied', True, True),
    ('./gradlew build', 'gradlew: Permission denied', False, False),
    ('./gradlew build', 'gradlew: error', True, False),
    ('gradlew build', 'gradlew: Permission denied', True, False)])
def test_not_match(file_exists, file_access, script, output, exists, callable):
    file_exists.return_value = exists
    file_access.return_value = callable
    assert not match(Command(script, output))


@pytest.mark.parametrize('script, result', [
    ('./gradlew build', 'chmod +x gradlew && ./gradlew build'),
    ('./install.sh --help', 'chmod +x install.sh && ./install.sh --help'),
    ('/opt/tool/run.sh', 'chmod +x /opt/tool/run.sh && /opt/tool/run.sh'),
    ('scripts/build.sh', 'chmod +x scripts/build.sh && scripts/build.sh'),
    ('~/bin/deploy', 'chmod +x ~/bin/deploy && ~/bin/deploy'),
    ('"./my script.sh"', "chmod +x 'my script.sh' && \"./my script.sh\"")])
def test_get_new_command(script, result):
    assert get_new_command(Command(script, '')) == result
