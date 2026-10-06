# oopsh roadmap

**oopsh** is a maintained fork of [thefuck](https://github.com/nvbn/thefuck) by
Vladimir Iakovlev. thefuck's last release (3.32) came out in 2022 and its last
commit in January 2024, and on Python 3.12+ it no longer starts. oopsh keeps the
original git history and the MIT license, and it aims to stay compatible with
existing thefuck configurations and custom rules.

Once installed, you type `oops` (or `oopsh`) to fix the previous command.

## Milestone 0: Bootstrap ✅

- [x] Import the full thefuck history (`upstream` remote = nvbn/thefuck)
- [x] Fix startup and installation on Python 3.12+ (`distutils` → `shutil.which`,
      remove `pkg_resources` from `setup.py`)
- [x] Unit test suite green on Python 3.13 (1887 passed, 16 skipped)

## Milestone 1: Modern toolchain

- [x] Make the tests work with pytest 8+ (tested up to pytest 9.1)
- [x] Fix the ~270 DeprecationWarnings (e.g. positional `count` in `re.sub`)
- [x] Drop Python 2.7 and other EOL versions. Minimum: Python 3.10
- [x] Remove `six`, the `py2` branches and the `imp`, `pkg_resources`, `pathlib2`,
      `backports.*` and `win_unicode_console` fallbacks
- [x] Move to `pyproject.toml` (PEP 621) with PEP 735 dependency groups; drop `setup.py`,
      `fastentrypoints.py`, `release.py`, `requirements.txt`
- [x] New CI on GitHub Actions: Python 3.10–3.14 × Linux/macOS/Windows, lint, functional tests in Docker
- [ ] Bring the functional tests (`tests/functional`) back to green

## Milestone 2: Rebrand to oopsh

The command layout:

| Piece                 | thefuck                          | oopsh                              |
|-----------------------|----------------------------------|------------------------------------|
| PyPI package          | `thefuck`                        | `oopsh`                            |
| Python package        | `thefuck`                        | `oopsh` (+ `thefuck` compat shim)  |
| Executable            | `thefuck`                        | `oopsh`                            |
| Shell function        | `fuck`                           | `oops`, plus `oopsh`               |
| Shell setup           | `eval "$(thefuck --alias)"`      | `eval "$(oopsh --alias)"`          |
| Config dir            | `~/.config/thefuck/`             | `~/.config/oopsh/`                 |
| Env vars              | `THEFUCK_*`                      | `OOPSH_*`                          |

- [ ] Rename the Python package to `oopsh` and the entry points to `oopsh` / `oopsh_firstuse`
- [ ] `--alias` generates both the `oops` and the `oopsh` shell functions. The `oopsh` function
      shadows the executable, so the generated code must call the binary via `command oopsh`
      (bash/zsh) or the equivalent in fish, PowerShell, tcsh
- [ ] Update the first-run setup (`not_configured`) for the new names, on every supported shell
- [ ] Windows: the published wheels never installed `scripts/fuck.bat` / `fuck.ps1` (they were only
      added by `setup.py` when built on Windows). Decide whether to ship `oops.bat` / `oops.ps1`
      for cmd users or drop them
- [ ] Rename the user-facing env vars `THEFUCK_*` → `OOPSH_*`
- [ ] Rewrite the README: new name, "Based on thefuck by Vladimir Iakovlev", no original logo or gifs
- [ ] Add our copyright line to `LICENSE.md`, keeping the original one

## Milestone 3: Painless migration from thefuck

- [ ] If `~/.config/oopsh/` doesn't exist, read `settings.py` and `rules/` from `~/.config/thefuck/`
- [ ] Keep a `thefuck` compatibility package so custom rules that do
      `from thefuck.utils import ...` / `from thefuck.specific.git import ...` keep working
- [ ] Still honour `THEFUCK_*` env vars when the `OOPSH_*` equivalent isn't set
- [ ] `oopsh --migrate`: copy the config to `~/.config/oopsh/` and suggest how to update the shell rc file
- [ ] Optional `fuck` alias for people who want to keep it (off by default)
- [ ] Migration guide in the docs
- [ ] Tests covering all of the above

## Milestone 4: First release (oopsh 1.0)

- [ ] Choose the version scheme (proposal: 1.0.0, independent of thefuck 3.x)
- [ ] `CHANGELOG.md` listing the changes since thefuck 3.32
- [ ] Publish to PyPI with Trusted Publishing from GitHub Actions
- [ ] Recommended install methods: `pipx install oopsh` / `uv tool install oopsh`
- [ ] Open a PR upstream (nvbn/thefuck) with the Python 3.12 fix

## Milestone 5: Upstream backlog

- [ ] Triage the ~148 open upstream PRs: merge the useful ones by cherry-picking them
      with their original authors (many are new rules)
- [ ] Triage the ~309 open upstream issues: label them, reproduce the real bugs on oopsh
- [ ] `CONTRIBUTING.md`, issue/PR templates, labels, code of conduct

## Milestone 6: Distribution

- [ ] Homebrew: own tap (`geomago/tap`) first, homebrew-core later
- [ ] AUR, nixpkgs, Debian/Ubuntu
- [ ] Windows: Scoop / winget
- [ ] Decide what to do with the `snapcraft.yaml` and `install.sh` inherited from upstream

## Later

- [ ] Startup time (lazy rule loading) and making instant mode stable
- [ ] Better support for newer shells (e.g. nushell)
- [ ] Rule docs generated automatically from the code
