import pytest
from oopsh.entrypoints import main as main_module


def test_broken_pipe_exits_cleanly(mocker):
    mocker.patch.object(main_module, '_main', side_effect=BrokenPipeError)
    mocker.patch('os.open', return_value=99)
    mocker.patch.object(main_module.sys, 'stdout', mocker.Mock(fileno=lambda: 1))
    dup2 = mocker.patch('os.dup2')
    with pytest.raises(SystemExit) as exit_info:
        main_module.main()
    assert exit_info.value.code == 0
    assert dup2.call_args[0][0] == 99
