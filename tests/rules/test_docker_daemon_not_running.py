from oopsh.rules.docker_daemon_not_running import match, get_new_command
from oopsh.types import Command

output = ('Cannot connect to the Docker daemon at unix:///var/run/docker.sock. '
          'Is the docker daemon running?')


def test_match():
    assert match(Command('docker ps', output))
    assert match(Command('sudo docker ps', output))


def test_not_match():
    assert not match(Command('docker ps', ''))
    assert not match(Command('podman ps', output))


def test_get_new_command():
    assert (get_new_command(Command('docker ps', output))
            == 'systemctl start docker && docker ps')
    assert (get_new_command(Command('sudo docker ps', output))
            == 'sudo systemctl start docker && sudo docker ps')
