import re
from oopsh.utils import for_app, quote_if_unsafe


@for_app('heroku')
def match(command):
    return 'https://devcenter.heroku.com/articles/multiple-environments' in command.output


def get_new_command(command):
    apps = re.findall('([^ ]*) \\([^)]*\\)', command.output)
    return [command.script + ' --app ' + quote_if_unsafe(app) for app in apps]
