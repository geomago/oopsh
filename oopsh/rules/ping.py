# -*- encoding: utf-8 -*-
from urllib.parse import urlparse
from oopsh.utils import for_app, memoize

# macOS / Linux (iputils) / BusyBox
RESOLVE_ERRORS = ('cannot resolve', 'Name or service not known', 'unknown host',
                  'bad address')


@memoize
def get_hostname_from_url(maybeUrl):
    try:
        results = urlparse(maybeUrl)
        return results.hostname
    except Exception:
        return None


@memoize
def get_index_of_url(parts):
    for i, part in enumerate(parts):
        if get_hostname_from_url(part):
            return i
    return None


@for_app('ping')
def match(command):
    if not any(error in command.output for error in RESOLVE_ERRORS):
        return False

    # It only fix if the command has a valid url
    index_of_url = get_index_of_url(command.script_parts)
    return index_of_url is not None


def get_new_command(command):
    index_of_url = get_index_of_url(command.script_parts)
    url = command.script_parts[index_of_url]
    hostname = get_hostname_from_url(url)
    return ' '.join(command.script_parts[:index_of_url] + [hostname] + command.script_parts[index_of_url + 1:])
