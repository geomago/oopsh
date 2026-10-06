import pytest

from oopsh.rules.gcloud_cli import match, get_new_command
from oopsh.types import Command

no_suggestions = '''\
ERROR: (gcloud) Command name argument expected.
'''

misspelled_command = '''\
ERROR: (gcloud) Invalid choice: 'comute'.
Usage: gcloud [optional flags] <group | command>
  group may be           access-context-manager | ai-platform | alpha | app |
                         asset | auth | beta | bigtable | builds | components |
                         composer | compute | config | container | dataflow |
                         dataproc | datastore | debug | deployment-manager |
                         dns | domains | endpoints | filestore | firebase |
                         functions | iam | iot | kms | logging | ml |
                         ml-engine | organizations | projects | pubsub | redis |
                         resource-manager | scheduler | services | source |
                         spanner | sql | tasks | topic
  command may be         docker | feedback | help | info | init | version

For detailed information on this command and its flags, run:
  gcloud --help
'''

misspelled_subcommand = '''\
ERROR: (gcloud.compute) Invalid choice: 'instance'.
Maybe you meant:
  gcloud compute instance-groups
  gcloud compute instance-templates
  gcloud compute instances
  gcloud compute target-instances

To search the help text of gcloud commands, run:
  gcloud help -- SEARCH_TERMS
'''


def test_match():
    assert match(Command('gcloud compute instance list', misspelled_subcommand))


@pytest.mark.parametrize('command', [
    Command('gcloud', no_suggestions),
    Command('gcloud comute instances list', misspelled_command),
    Command('aws dynamodb invalid', misspelled_subcommand)])
def test_not_match(command):
    assert not match(command)


def test_get_new_command():
    new_commands = get_new_command(
        Command('gcloud compute instance list', misspelled_subcommand))
    assert new_commands[0] == 'gcloud compute instances list'
    assert set(new_commands) <= {
        'gcloud compute instances list',
        'gcloud compute instance-groups list',
        'gcloud compute instance-templates list',
        'gcloud compute target-instances list'}
