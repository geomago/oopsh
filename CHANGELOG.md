# Changelog

All notable changes to oopsh are listed here. oopsh is a maintained fork of
[thefuck](https://github.com/nvbn/thefuck); this file starts from thefuck 3.32,
its last release.

## 1.0.0 (unreleased)

First release of oopsh, based on thefuck 3.32 and the unreleased thefuck commits
up to January 2024.

### New name

- The project, the PyPI package and the Python package are now called `oopsh`.
- You type `oops` (or `oopsh`) instead of `fuck`. Set it up with
  `eval "$(oopsh --alias)"`; `oopsh --alias fuck` keeps the old word.
- Settings env vars are now `OOPSH_*`, the config dir is `~/.config/oopsh/`,
  the cache dir is `~/.cache/oopsh/`.

### Migrating from thefuck

- Without an oopsh config dir, oopsh uses thefuck's (`~/.config/thefuck/` or
  `~/.thefuck/`) as it is.
- Custom rules and `thefuck_contrib_*` packages that import from `thefuck` keep
  working unchanged.
- `THEFUCK_*` env vars still work when the `OOPSH_*` one isn't set.
- New `oopsh --migrate` copies thefuck's config to `~/.config/oopsh/` without
  overwriting anything, and explains what else to change.
- Third-party rule packages can be named `oopsh_contrib_*`.

### Fixed

- Starts and installs on Python 3.12 and later: thefuck used `distutils`, which
  Python 3.12 removed, and `pkg_resources` in `setup.py`.
- No more deprecation warnings on recent Python versions (e.g. `re.sub` with a
  positional `count` in the `git_remote_delete` rule).

### Removed

- Support for Python 2.7 and Python 3.5–3.9. oopsh requires Python 3.10 or later.
- The `six`, `pathlib2`, `backports.shutil_get_terminal_size` and
  `win_unicode_console` dependencies.
- The Windows `fuck.bat` / `fuck.ps1` scripts, which the published packages never
  installed. On PowerShell, use `iex "$(oopsh --alias)"`.

### Development

- Packaging moved to `pyproject.toml`; dev dependencies are dependency groups
  (`pip install -e . --group dev`).
- The test suite runs on pytest 8+ and in CI on Python 3.10–3.14 on Linux, macOS
  and Windows, plus functional tests with bash, zsh, fish and tcsh in Docker.
