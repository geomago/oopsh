# Changelog

All notable changes to oopsh are listed here. oopsh is a maintained fork of
[thefuck](https://github.com/nvbn/thefuck); this file starts from thefuck 3.32,
its last release.

## 1.0.0 (2026-10-07)

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

### From thefuck's open pull requests

oopsh reviewed all 151 pull requests left open on thefuck and merged 40 of
them, keeping their authors (see [docs/upstream-prs.md](docs/upstream-prs.md)).

New rules: `apt_unable_to_locate`, `cd_quotes`, `composer_not_package`,
`docker_daemon_not_running`, `edit_filename`, `gcloud_cli`,
`kedro_no_such_command`, `makefile`, `ninja`, `nix_shell`, `ping`,
`rbenv_install`, `restic_typo`, `su`, `terraform_init_upgrade`,
`upper_to_lower_case`, `xcode_license`.

Improved rules:

- `git_not_command`: common typos git doesn't catch, like `git lock` -> `git log`.
- `git_branch_delete`: also `--delete`; `git_branch_delete_checked_out` switches
  to the repository's default branch instead of always `master`.
- `chmod_x`: absolute and other non-relative paths.
- `composer_not_command`: only unknown commands, every suggestion.
- `npm_missing_script`: messages of npm 7 and later.
- `pacman` / `pacman_not_found`: `paru` support.
- `brew_unknown_command`: up-to-date list of Homebrew commands.
- `cd_mkdir`: PowerShell and cmd.exe errors.

Other fixes:

- fish: find the history where fish 2.3+ keeps it (`~/.local/share/fish`).
- bash/zsh: work with `set -u` (nounset); no crash on an empty bash alias.
- No traceback when the output pipe is closed, or when a process can't be killed.
- When stdin isn't a terminal, show the fix and explain `--yes` instead of crashing.
- Debug output no longer dumps the whole environment, which can hold secrets.
- Windows: commands are also known without their extension (`git.exe` as `git`).

### Security

Fixes for reports filed on thefuck and never addressed there:

- Rules could copy a URL from a command's output into the fix unquoted, letting
  it run arbitrary commands when the alias evaluated the fix (thefuck#1531).
- The instant mode session log was readable by other users (thefuck#1621), and
  oopsh now refuses a log other users can write (thefuck#1622).
- Third-party rule packages are only loaded from directories other users can't
  write (thefuck#1623).
- Rules quote the text they copy from a command's output into the fix when the
  shell would interpret it, so that output can't smuggle in shell code
  (thefuck#1622).

### Fixed

- `fix_file` no longer suggests `vim /bin/sh +1 && ...` for unknown commands
  (thefuck#1153).
- `oops` returns the exit status of the fixed command (thefuck#1342).
- Rules that replace or drop the command name keep the quotes of the rest of the
  command (thefuck#1543).
- Closing the terminal during the confirmation no longer leaves oopsh spinning
  at full CPU (thefuck#806).
- `git_pull` finds the set-upstream hint anywhere in git's output (thefuck#1406).
- Arch Linux rules don't fail when `pkgfile` or its database is missing
  (thefuck#1129).
- New `git_safe_directory` rule for git's "dubious ownership" error (thefuck#1376).
- `oopsh --alias`, run at every shell start, is faster.
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
