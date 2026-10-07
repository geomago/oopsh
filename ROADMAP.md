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
- [x] Bring the functional tests (`tests/functional`) back to green

## Milestone 2: Rebrand to oopsh

The command layout:

| Piece                 | thefuck                          | oopsh                              |
|-----------------------|----------------------------------|------------------------------------|
| PyPI package          | `thefuck`                        | `oopsh`                            |
| Python package        | `thefuck`                        | `oopsh` (`thefuck.*` imports still work) |
| Executable            | `thefuck`                        | `oopsh`                            |
| Shell function        | `fuck`                           | `oops`, plus `oopsh`               |
| Shell setup           | `eval "$(thefuck --alias)"`      | `eval "$(oopsh --alias)"`          |
| Config dir            | `~/.config/thefuck/`             | `~/.config/oopsh/`                 |
| Env vars              | `THEFUCK_*`                      | `OOPSH_*`                          |

- [x] Rename the Python package to `oopsh` and the entry points to `oopsh` (main) / `oops` (first run)
- [x] `--alias` generates both the `oops` and the `oopsh` shell functions (bash, zsh, fish, PowerShell).
      `oopsh` passes executable arguments (`--alias`, `--version`, `--help`, …) to the binary,
      everything else to `oops`. tcsh and generic POSIX shells get `oops` only
- [x] Update the first-run setup (`not_configured`) for the new names
- [x] Windows: drop `scripts/fuck.bat` / `fuck.ps1`. The published wheels never installed them
      (`setup.py` only added them when built on Windows); PowerShell uses `iex "$(oopsh --alias)"`
- [x] Rename the user-facing env vars `THEFUCK_*` → `OOPSH_*`
- [x] Rewrite the README: new name, "Based on thefuck by Vladimir Iakovlev", no original logo or gifs
- [x] Add our copyright line to `LICENSE.md`, keeping the original one

## Milestone 3: Painless migration from thefuck

- [x] If `~/.config/oopsh/` doesn't exist, read `settings.py` and `rules/` from `~/.config/thefuck/`
      (or the legacy `~/.thefuck/`)
- [x] Custom rules that do `from thefuck.utils import ...` / `from thefuck.specific.git import ...`
      keep working: inside oopsh, `thefuck.*` imports resolve to the `oopsh.*` modules. No `thefuck`
      package is installed, so oopsh can sit next to a real thefuck
- [x] Third-party rule packages: look for `oopsh_contrib_*` as well as `thefuck_contrib_*`
- [x] Still honour `THEFUCK_*` env vars when the `OOPSH_*` equivalent isn't set
- [x] `oopsh --migrate`: copy the config to `~/.config/oopsh/` (never overwriting) and suggest how
      to update the shell rc file and env vars
- [x] Optional `fuck` alias for people who want to keep it: `eval "$(oopsh --alias fuck)"`
- [x] Migration guide in the docs (README, "Coming from thefuck")
- [x] Tests covering all of the above

## Milestone 4: Release preparation ✅

- [x] Choose the version scheme: semantic versioning from 1.0.0, independent of thefuck 3.x
- [x] `CHANGELOG.md` listing the changes since thefuck 3.32
- [x] Release workflow: pushing a `vX.Y.Z` tag builds, publishes to PyPI with Trusted Publishing
      and creates the GitHub release
- [x] PyPI and GitHub metadata people actually search for: description and topics with
      "thefuck alternative", "maintained fork", "Python 3.12"

## Milestone 5: Upstream backlog ✅

- [x] Triage the 151 open upstream PRs: 40 merged with their original authors, the rest
      documented in [docs/upstream-prs.md](docs/upstream-prs.md)
- [x] Triage the 310 open upstream issues ([docs/upstream-issues.md](docs/upstream-issues.md)):
      fix the real bugs found, including five security reports
- [x] The ~180 issues marked "to re-check" stay documented: they're handled when someone reports
      them on oopsh
- [x] `CONTRIBUTING.md`, `SECURITY.md`, issue forms, PR template, code of conduct
- [x] Create the `bug` and `rule request` labels
- [ ] Enable private vulnerability reporting on GitHub

## Milestone 6: First release (oopsh 1.0)

- [ ] Configure the trusted publisher on PyPI, tag `v1.0.0`
- [x] Recommended install methods in the README: `pipx install oopsh` / `uv tool install oopsh`
- [ ] Write to the thefuck maintainer, offering to help maintain thefuck itself. No new upstream PR:
      at least 8 open PRs already carry the same `distutils` fix (#1247, #1404, #1534, #1619, …)

## Milestone 7: Distribution

- [ ] Homebrew: own tap (`geomago/tap`) first, homebrew-core later
- [ ] AUR, nixpkgs, Debian/Ubuntu
- [ ] Where the thefuck package is broken on Python 3.12+ (Homebrew, AUR, nixpkgs, Debian/Ubuntu),
      report it with a link to the fix; once oopsh has some traction, propose it as a new package
- [ ] Windows: Scoop / winget
- [x] Remove the `snapcraft.yaml` and `install.sh` inherited from upstream

## Milestone 8: Launch

Once 1.0 is out, be findable where thefuck users look for a replacement. Every step once, no spam.

- [ ] One helpful comment in each of the main upstream issues (Python 3.12, `distutils`,
      Ubuntu 24.04, #1566 "is it still maintained?") with the fix and how to install oopsh
- [ ] Curated lists: awesome-shell, awesome-cli-apps; list oopsh on AlternativeTo as a
      thefuck alternative
- [ ] Announce: Show HN, r/commandline, r/Python
- [ ] Keep the README's first screen about the one-line switch from thefuck

## Later

- [ ] Startup time: `oopsh --alias` went from ~70 to ~60 ms; lazy rule loading for the fix itself;
      make instant mode stable
- [ ] Nushell support done properly (nvbn/thefuck#1254, #1441; the PR #1442 ran fixes in a subprocess)
- [ ] Esc to cancel the selection without breaking the arrow keys (nvbn/thefuck#1506)
- [ ] `--shell` option, or document `TF_SHELL` (nvbn/thefuck#1536, #1538)
- [ ] Commands wrapped by others, like `hub` for `git` (nvbn/thefuck#1101)
- [ ] An opt-in plugin for LLM suggestions (nvbn/thefuck#1363, #1365, #1458): never on by default,
      commands are sent to an external service
- [ ] Keep auditing rules that build fixes from output, now that most go through `replace_argument`
- [ ] Rule docs generated automatically from the code
