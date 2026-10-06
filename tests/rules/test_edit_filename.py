import os

import pytest

from oopsh.rules.edit_filename import EDITORS, get_new_command, match
from oopsh.types import Command

parametrize_editor = pytest.mark.parametrize("editor", EDITORS)


@pytest.fixture(autouse=True)
def cwd(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)


def _edit_command(editor, path):
    """Uses paths relative to the current dir, as typed in practice (and
    without Windows backslashes, that shell-like splitting would eat)."""
    return Command(editor + " " + os.path.relpath(path).replace(os.sep, "/"), "")


@parametrize_editor
def test_correct_file_no_match(tmp_path, editor):
    f = tmp_path / "module.py"
    f.touch()
    assert not match(_edit_command(editor, f))


@parametrize_editor
def test_similar_correct_file(tmp_path, editor):
    f = tmp_path / "module.py"
    f2 = tmp_path / "module.html"
    f.touch()
    f2.touch()
    assert not match(_edit_command(editor, f))


@parametrize_editor
def test_match_for_nonexisting(tmp_path, editor):
    f = tmp_path / "module.py"
    edited = tmp_path / "module"
    f.touch()
    assert match(_edit_command(editor, edited))


@parametrize_editor
def test_match_for_nonexisting_editor_flag(tmp_path, editor):
    f = tmp_path / "module.py"
    edited = tmp_path / "module"
    f.touch()
    assert match(_edit_command(editor + " --servername server", edited))


@pytest.mark.parametrize("program", ["vimdiff", "nethack", "mcedit-foo"])
def test_match_only_editors(tmp_path, program):
    (tmp_path / "module.py").touch()
    assert not match(_edit_command(program, tmp_path / "module"))


def test_no_match_in_missing_dir(tmp_path):
    assert not match(_edit_command("vim", tmp_path / "missing" / "module"))


def test_match_for_nonexisting_bad_editor(tmp_path):
    f = tmp_path / "module.py"
    edited = tmp_path / "module"
    f.touch()
    assert not match(_edit_command("cat", edited))


@parametrize_editor
def test_get_new_command(tmp_path, editor):
    f = tmp_path / "module.py"
    edited = tmp_path / "module"
    f.touch()
    assert get_new_command(_edit_command(editor, edited)) == [
        _edit_command(editor, f).script
    ]


@parametrize_editor
def test_get_new_command_multiple(tmp_path, editor):
    f = tmp_path / "module.py"
    f2 = tmp_path / "module.html"
    edited = tmp_path / "module"
    f.touch()
    f2.touch()
    assert sorted(get_new_command(_edit_command(editor, edited))) == sorted(
        [_edit_command(editor, f).script, _edit_command(editor, f2).script]
    )


@parametrize_editor
def test_get_new_command_for_nonexisting_editor_flag(tmp_path, editor):
    f = tmp_path / "module.py"
    edited = tmp_path / "module"
    f.touch()
    assert get_new_command(_edit_command(editor + " --servername server", edited)) == [
        _edit_command(editor + " --servername server", f).script
    ]
