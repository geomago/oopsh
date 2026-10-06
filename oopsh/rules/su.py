def match(command):
    output = command.output.lower()
    return (command.script_parts[:1] == ['sudo']
            and ('command not found: sudo' in output
                 or 'sudo: command not found' in output
                 or 'sudo: not found' in output))


def get_new_command(command):
    script = command.script[len('sudo '):]
    return u'su -c "{}"'.format(script.replace('"', '\\"'))


priority = 1200
