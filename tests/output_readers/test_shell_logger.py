from oopsh.output_readers import shell_logger


def test_get_output_looks_at_every_command(mocker):
    mocker.patch.object(shell_logger, '_get_last_n', return_value=[
        {'command': 'ls', 'output': 'a b'},
        {'command': 'git psuh', 'output': "git: 'psuh' is not a git command."}])
    mocker.patch.object(shell_logger, '_get_output_lines',
                        side_effect=lambda output: [output])
    assert (shell_logger.get_output('git psuh')
            == "git: 'psuh' is not a git command.")


def test_get_output_not_found(mocker):
    mocker.patch.object(shell_logger, '_get_last_n', return_value=[
        {'command': 'ls', 'output': 'a b'}])
    assert shell_logger.get_output('git psuh') is None
