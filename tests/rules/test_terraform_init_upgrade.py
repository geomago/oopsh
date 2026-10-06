import pytest
from oopsh.rules.terraform_init_upgrade import match, get_new_command
from oopsh.types import Command

output = '''Error: Inconsistent dependency lock file

The following dependency selections recorded in the lock file are
inconsistent with the current configuration:
  - provider registry.terraform.io/hashicorp/aws: locked version selection 4.0.0 doesn't match the updated version constraints "~> 5.0"

To update the locked dependency selections to match a changed configuration,
run:
  terraform init -upgrade
'''


@pytest.mark.parametrize('script', ['terraform plan', 'terraform apply'])
def test_match(script):
    assert match(Command(script, output))


@pytest.mark.parametrize('script, output', [
    ('terraform plan', ''),
    ('terraform plan', 'Error: Initialization required.'),
    ('ls', output)])
def test_not_match(script, output):
    assert not match(Command(script, output))


def test_get_new_command():
    assert (get_new_command(Command('terraform plan', output))
            == 'terraform init -upgrade && terraform plan')
