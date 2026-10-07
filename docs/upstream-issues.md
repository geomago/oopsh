# Open issues of thefuck

Every issue that was open on [nvbn/thefuck](https://github.com/nvbn/thefuck/issues) in October 2026 (310), and where it stands in oopsh. "fixed" means fixed in oopsh, with a test where possible; "to re-check" means it may well still apply and needs reproducing with oopsh. Reports are welcome at https://github.com/geomago/oopsh/issues.

| Status | Count |
|---|---|
| fixed | 61 |
| works | 2 |
| to re-check | 178 |
| request | 25 |
| discussion | 44 |

| Issue | Title | Area | Status | Notes |
|---|---|---|---|---|
| [#685](https://github.com/nvbn/thefuck/issues/685) | Drop Python 2 support | python-compat | fixed | Python 2 dropped |
| [#806](https://github.com/nvbn/thefuck/issues/806) | Quitting Terminal without canceling out of thefuck options leaves python process running | shell:zsh | fixed | end of input aborts the confirmation loop |
| [#882](https://github.com/nvbn/thefuck/issues/882) | Excluded rules still imported | windows | fixed | excluded rules are not imported |
| [#884](https://github.com/nvbn/thefuck/issues/884) | setup.py runs successfully in python2 | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#888](https://github.com/nvbn/thefuck/issues/888) | rbenv install | install | fixed | rbenv_install rule |
| [#946](https://github.com/nvbn/thefuck/issues/946) | Only including necessary envs in THEFUCK_DEBUG=true | meta | fixed | debug output no longer dumps the environment |
| [#959](https://github.com/nvbn/thefuck/issues/959) | Breaks after composer require when there is only one suggested package | install | fixed | composer rules rewritten (nvbn/thefuck#1007) |
| [#962](https://github.com/nvbn/thefuck/issues/962) | Installing Redis instead of RabbitMQ after using fuck | install | fixed | apt_unable_to_locate rule |
| [#1027](https://github.com/nvbn/thefuck/issues/1027) | Fish shell does not appear to have its history rewritten | shell:fish | fixed | fish history in $XDG_DATA_HOME |
| [#1076](https://github.com/nvbn/thefuck/issues/1076) | PytestUnknownMarkWarning | other | fixed | test markers registered |
| [#1129](https://github.com/nvbn/thefuck/issues/1129) | archlinux get_pkgfile fails if pkgfile metadata does not exist | other | fixed | pkgfile errors no longer crash |
| [#1153](https://github.com/nvbn/thefuck/issues/1153) | first suggestions show `vim /bin/sh +1 &&` in front | meta | fixed | fix_file no longer offers to edit the shell |
| [#1209](https://github.com/nvbn/thefuck/issues/1209) | no_command rule doesn't work properly with executables that have an uppercase name | windows | fixed | Windows: executables known by lowercase name |
| [#1242](https://github.com/nvbn/thefuck/issues/1242) | Support for `Makefile` fucks | rule-request | fixed | makefile rule |
| [#1246](https://github.com/nvbn/thefuck/issues/1246) | needs python distutils package during installation | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1262](https://github.com/nvbn/thefuck/issues/1262) | Migrate mock to unittest.mock | install | fixed | unittest.mock |
| [#1313](https://github.com/nvbn/thefuck/issues/1313) | Default Git branch is assumed to be master | other | fixed | default branch instead of master |
| [#1320](https://github.com/nvbn/thefuck/issues/1320) | Feature: npm missing script, did you mean this | install | fixed | npm 7+ messages |
| [#1341](https://github.com/nvbn/thefuck/issues/1341) | `git_branch_delete_checked_out` won't work if there is no master branch | rule-request | fixed | default branch instead of master |
| [#1342](https://github.com/nvbn/thefuck/issues/1342) | `fuck -v` and `fuck -h` exiting with code 1 | other | fixed | oops returns the fixed command's exit status |
| [#1354](https://github.com/nvbn/thefuck/issues/1354) | `PYTHONIOENCODING: parameter not set` | windows | fixed | works with set -u |
| [#1376](https://github.com/nvbn/thefuck/issues/1376) | [Git] Fix dubious ownership | shell:zsh | fixed | new git_safe_directory rule |
| [#1381](https://github.com/nvbn/thefuck/issues/1381) | imp removed in python 3.12 | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1382](https://github.com/nvbn/thefuck/issues/1382) | potential bug in utils.py | windows | fixed | which() is shutil.which |
| [#1391](https://github.com/nvbn/thefuck/issues/1391) | Ubuntu installation instructions no longer work | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1406](https://github.com/nvbn/thefuck/issues/1406) | no fucks given for git no tracking information for the current branch | shell:zsh | fixed | git_pull finds the hint anywhere in the output |
| [#1418](https://github.com/nvbn/thefuck/issues/1418) | Not fully compatible with python 3.12.0 yet. | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1438](https://github.com/nvbn/thefuck/issues/1438) | Compatibility with pytest 8 | other | fixed | pytest 8+ |
| [#1444](https://github.com/nvbn/thefuck/issues/1444) | ModuleNotFoundError: No module named 'distutils' related to #1434 | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1448](https://github.com/nvbn/thefuck/issues/1448) | Thefuck 3.32 issue on Fedora 40 | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1449](https://github.com/nvbn/thefuck/issues/1449) | Having a hard time getting set up on Ubuntu 24.04 | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1453](https://github.com/nvbn/thefuck/issues/1453) | Python 3.11 and 3.12 complains about `imp` which cannot be installed in those environments. | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1457](https://github.com/nvbn/thefuck/issues/1457) | Cannot install on Ubuntu 24.04 LTS Noble Numbat | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1464](https://github.com/nvbn/thefuck/issues/1464) | Compatibility Issue with Python 3.12: thefuck Package Uses Deprecated imp Module | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1467](https://github.com/nvbn/thefuck/issues/1467) | use python 3.12.5 on macOS Sonoma and cannot use the*ck as a result because the*ck depends on packages which have been removed in 3.12.5 | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1469](https://github.com/nvbn/thefuck/issues/1469) | Always suggests to edit bash with nano on NixOS (wtf) | shell:fish | fixed | same cause as #1153 |
| [#1477](https://github.com/nvbn/thefuck/issues/1477) | Installation as instructed for Mint fails | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1482](https://github.com/nvbn/thefuck/issues/1482) | It is using deleted library imp and distutils | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1489](https://github.com/nvbn/thefuck/issues/1489) | Python 3.13.1: No module named 'imp' | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1491](https://github.com/nvbn/thefuck/issues/1491) | Python 3.12.4: No module named 'imp' | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1501](https://github.com/nvbn/thefuck/issues/1501) | How to Fix:"No module named 'imp' " | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1508](https://github.com/nvbn/thefuck/issues/1508) | newest version of python | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1515](https://github.com/nvbn/thefuck/issues/1515) | Test Failing: test_get_valid_history_without_current on macOS + Python 3.11 | install | fixed | memoization no longer leaks between tests |
| [#1524](https://github.com/nvbn/thefuck/issues/1524) | Python 3: anydbm import is outdated (should use dbm) | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1527](https://github.com/nvbn/thefuck/issues/1527) | The 'imp' import in Python 3.13 is obsolete.\| imp库已经没了 | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1530](https://github.com/nvbn/thefuck/issues/1530) | Broken Pipe | other | fixed | no traceback on a closed pipe |
| [#1531](https://github.com/nvbn/thefuck/issues/1531) | [Bug]: open_command string-concatenates user-controlled output, enabling command injection | windows | fixed | open_command quotes the URL |
| [#1533](https://github.com/nvbn/thefuck/issues/1533) | cannot install on Ubuntu 24..04 | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1541](https://github.com/nvbn/thefuck/issues/1541) | IndexError: string index out of range | windows | fixed | empty/multi-line bash aliases |
| [#1543](https://github.com/nvbn/thefuck/issues/1543) | bug: git commit -m command fix error | other | fixed | rules keep quotes when they replace the command name |
| [#1544](https://github.com/nvbn/thefuck/issues/1544) | It seems that python3.12 is not supported | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1546](https://github.com/nvbn/thefuck/issues/1546) | No module named 'distutils' | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1549](https://github.com/nvbn/thefuck/issues/1549) | [self-tests] fail against pytest 9 | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1552](https://github.com/nvbn/thefuck/issues/1552) | Use of deprecated / removed pkg_resources | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1567](https://github.com/nvbn/thefuck/issues/1567) | Please support Python 3.14 | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1608](https://github.com/nvbn/thefuck/issues/1608) | fix: Stop fucking around with deprecated imports — Python 3.12/3.13/3.14 compatibility omnibus | python-compat | fixed | runs on Python 3.10-3.14 (no imp/distutils/pkg_resources) |
| [#1621](https://github.com/nvbn/thefuck/issues/1621) | Session transcript log created world-readable (mode 755 under default umask 022) | instant-mode | fixed | session log created 0600 |
| [#1622](https://github.com/nvbn/thefuck/issues/1622) | Poisoned THEFUCK_OUTPUT_LOG steers the corrected command; unquoted output token executes on alias eval | instant-mode | fixed | only a log owned by the user and not writable by others is read |
| [#1623](https://github.com/nvbn/thefuck/issues/1623) | thefuck_contrib_* packages are exec'd before enable-gating on every run | install | fixed | third-party rules only from directories others can't write |
| [#855](https://github.com/nvbn/thefuck/issues/855) | Layout switching for Ukrainian is not supported, the Russian one is used instead | windows | works | Ukrainian layout picked when needed (test added) |
| [#862](https://github.com/nvbn/thefuck/issues/862) | Greek keyboard mapping incorrect | windows | works | Greek layout (test added) |
| [#94](https://github.com/nvbn/thefuck/issues/94) | Statistics | other | to re-check |  |
| [#104](https://github.com/nvbn/thefuck/issues/104) | Integrate it with zsh and it can learn rules? | shell:zsh | to re-check |  |
| [#108](https://github.com/nvbn/thefuck/issues/108) | Doesn't handle pipes | other | to re-check |  |
| [#172](https://github.com/nvbn/thefuck/issues/172) | What if thefuck not installing? | install | to re-check |  |
| [#178](https://github.com/nvbn/thefuck/issues/178) | Display issue on Git for Windows CLI | windows | to re-check |  |
| [#302](https://github.com/nvbn/thefuck/issues/302) | How to install it on Windows? | install | to re-check |  |
| [#353](https://github.com/nvbn/thefuck/issues/353) | Command is slow | other | to re-check |  |
| [#360](https://github.com/nvbn/thefuck/issues/360) | Sometime cause my terminal text dislocation | install | to re-check |  |
| [#368](https://github.com/nvbn/thefuck/issues/368) | changing package name when I use "sudo apt-get install" | install | to re-check |  |
| [#371](https://github.com/nvbn/thefuck/issues/371) | Up to 1s lag when invoking "fuck" | install | to re-check |  |
| [#393](https://github.com/nvbn/thefuck/issues/393) | bash: syntax error near unexpected token `<' | other | to re-check |  |
| [#395](https://github.com/nvbn/thefuck/issues/395) | "git brnch" never completes. Freezes output. | windows | to re-check |  |
| [#399](https://github.com/nvbn/thefuck/issues/399) | line 168: `eval "$(thefuck --alias)"' | performance | to re-check |  |
| [#402](https://github.com/nvbn/thefuck/issues/402) | Memory leak and bash block on Ubuntu | install | to re-check |  |
| [#405](https://github.com/nvbn/thefuck/issues/405) | alias doesn't work when using oh-my-zsh `per-directory-history` | other | to re-check |  |
| [#410](https://github.com/nvbn/thefuck/issues/410) | put arguments into quotation marks | shell:zsh | to re-check |  |
| [#420](https://github.com/nvbn/thefuck/issues/420) | please support command line options 'off', 'me', 'you' | other | to re-check |  |
| [#453](https://github.com/nvbn/thefuck/issues/453) | disappointed that it didn't correct my typo'd "fuck" | other | to re-check |  |
| [#457](https://github.com/nvbn/thefuck/issues/457) | Проблема при исправлении команды с русскими символами | other | to re-check |  |
| [#459](https://github.com/nvbn/thefuck/issues/459) | amke becomes rake, not make | other | to re-check |  |
| [#469](https://github.com/nvbn/thefuck/issues/469) | Change way of interaction with shells | performance | to re-check |  |
| [#470](https://github.com/nvbn/thefuck/issues/470) | psutil: platform cygwin is not supported (thefuck won't install on Cygwin) | install | to re-check |  |
| [#475](https://github.com/nvbn/thefuck/issues/475) | got commit corrects itself to go commit instead of git commit | other | to re-check |  |
| [#490](https://github.com/nvbn/thefuck/issues/490) | white-space safe 'thefuck' with the history line passed as a single arg? | windows | to re-check |  |
| [#502](https://github.com/nvbn/thefuck/issues/502) | -bash: usage:: command not found | other | to re-check |  |
| [#519](https://github.com/nvbn/thefuck/issues/519) | When you fuck up using fuck fuck doesn't unfuck your fuck-up | other | to re-check |  |
| [#520](https://github.com/nvbn/thefuck/issues/520) | Command not found | shell:zsh | to re-check |  |
| [#541](https://github.com/nvbn/thefuck/issues/541) | fuck has issues with ssh identifier files | other | to re-check |  |
| [#544](https://github.com/nvbn/thefuck/issues/544) | Xonsh | shell:other | to re-check |  |
| [#575](https://github.com/nvbn/thefuck/issues/575) | Always outputs "No fucks given" on iTerm2 and zsh | shell:zsh | to re-check |  |
| [#583](https://github.com/nvbn/thefuck/issues/583) | fuck should not yield anything for `ls` | other | to re-check |  |
| [#593](https://github.com/nvbn/thefuck/issues/593) | alias doesn't want to fuck (doesn't recognise  the fuck command) | install | to re-check |  |
| [#594](https://github.com/nvbn/thefuck/issues/594) | Strange behaviour in Windows (Git Bash) | install | to re-check |  |
| [#626](https://github.com/nvbn/thefuck/issues/626) | Can I add this to Windows Command Prompt? | windows | to re-check |  |
| [#631](https://github.com/nvbn/thefuck/issues/631) | Use type annotations and mypy | other | to re-check |  |
| [#636](https://github.com/nvbn/thefuck/issues/636) | evaluation buffer and fuck | other | to re-check |  |
| [#642](https://github.com/nvbn/thefuck/issues/642) | thefuck: fork failed | install | to re-check |  |
| [#646](https://github.com/nvbn/thefuck/issues/646) | No module named 'thefuck' | install | to re-check |  |
| [#648](https://github.com/nvbn/thefuck/issues/648) | Suggest yarn add x for yarn install x | install | to re-check |  |
| [#649](https://github.com/nvbn/thefuck/issues/649) | error: Unable to find  vcvarsall.bat | other | to re-check |  |
| [#653](https://github.com/nvbn/thefuck/issues/653) | Use py-backwards | other | to re-check |  |
| [#654](https://github.com/nvbn/thefuck/issues/654) | Installing through brew / pip in Mac | install | to re-check |  |
| [#659](https://github.com/nvbn/thefuck/issues/659) | Not working in windows7 mingw64 | install | to re-check |  |
| [#672](https://github.com/nvbn/thefuck/issues/672) | Hitting enter does not execute the previous command in Windows Git Bash | other | to re-check |  |
| [#682](https://github.com/nvbn/thefuck/issues/682) | Instant fuck mode | performance | to re-check |  |
| [#686](https://github.com/nvbn/thefuck/issues/686) | [feature request] Support openSUSE Scout (command-not-found) | install | to re-check |  |
| [#687](https://github.com/nvbn/thefuck/issues/687) | Scripting with thefuck | other | to re-check |  |
| [#690](https://github.com/nvbn/thefuck/issues/690) | Using vim command success and type fuck cause display error | other | to re-check |  |
| [#712](https://github.com/nvbn/thefuck/issues/712) | Handle params like `-rlv` in `utils.replace_argument` | other | to re-check |  |
| [#716](https://github.com/nvbn/thefuck/issues/716) | ImportError: No module named 'thefuck.entrypoints' | install | to re-check |  |
| [#738](https://github.com/nvbn/thefuck/issues/738) | Don't rely on $SHELL for detecting shell | shell:zsh | to re-check |  |
| [#739](https://github.com/nvbn/thefuck/issues/739) | Please consider shipping tests within PyPI releases | install | to re-check |  |
| [#743](https://github.com/nvbn/thefuck/issues/743) | how to fix this  problem? thanks | install | to re-check |  |
| [#769](https://github.com/nvbn/thefuck/issues/769) | fuck configured, but not working with zsh | windows | to re-check |  |
| [#774](https://github.com/nvbn/thefuck/issues/774) | Error in code Recommended by 'fuck' while removing any package especially with -- operations | install | to re-check |  |
| [#775](https://github.com/nvbn/thefuck/issues/775) | Error in Recommendations when the correct command is typed. | shell:zsh | to re-check |  |
| [#781](https://github.com/nvbn/thefuck/issues/781) | binding fuck to \e\e behaves wired | shell:zsh | to re-check |  |
| [#792](https://github.com/nvbn/thefuck/issues/792) | Arrow symbols are missing for xos4 Terminus font | install | to re-check |  |
| [#795](https://github.com/nvbn/thefuck/issues/795) | gir commiy does not fix itself to git commit | shell:zsh | to re-check |  |
| [#798](https://github.com/nvbn/thefuck/issues/798) | Zsh argument list too long: head | install | to re-check |  |
| [#800](https://github.com/nvbn/thefuck/issues/800) | eval $(thefuck --alias --enable-experimental-instant-mode) not working in ~/.bash_profile | windows | to re-check |  |
| [#811](https://github.com/nvbn/thefuck/issues/811) | Enabling experimental instant mode causes The Fuck to stop working entirely | shell:zsh | to re-check |  |
| [#859](https://github.com/nvbn/thefuck/issues/859) | Shell startup time | performance | to re-check |  |
| [#875](https://github.com/nvbn/thefuck/issues/875) | Running fuck from command_not_found_handle Not Working Right | install | to re-check |  |
| [#879](https://github.com/nvbn/thefuck/issues/879) | How does thefuck work with history command? | other | to re-check |  |
| [#881](https://github.com/nvbn/thefuck/issues/881) | Doesn't repair apt-get command | install | to re-check |  |
| [#885](https://github.com/nvbn/thefuck/issues/885) | Leading `\` in TEMPLATE in fastentrypoints.py | other | to re-check |  |
| [#889](https://github.com/nvbn/thefuck/issues/889) | how can you get the history for current terminal session | other | to re-check |  |
| [#890](https://github.com/nvbn/thefuck/issues/890) | Does it not try splitting up the command? | install | to re-check |  |
| [#891](https://github.com/nvbn/thefuck/issues/891) | I have installed but it doesn't work? | install | to re-check |  |
| [#903](https://github.com/nvbn/thefuck/issues/903) | Issue after second run | other | to re-check |  |
| [#906](https://github.com/nvbn/thefuck/issues/906) | Flutter is not accurate,Can you support it? | other | to re-check |  |
| [#909](https://github.com/nvbn/thefuck/issues/909) | Problem using "fuck" with git push alias gp | other | to re-check |  |
| [#911](https://github.com/nvbn/thefuck/issues/911) | Sudo Retry Fails on Fish | install | to re-check |  |
| [#914](https://github.com/nvbn/thefuck/issues/914) | Why it doesn't work after I pressed enter while it print [enter/↑/↓/ctrl+c] ? | windows | to re-check |  |
| [#927](https://github.com/nvbn/thefuck/issues/927) | .bash_history permission denied despite running on latest version | other | to re-check |  |
| [#929](https://github.com/nvbn/thefuck/issues/929) | how to use it in windows | install | to re-check |  |
| [#935](https://github.com/nvbn/thefuck/issues/935) | Rule `rules.git_checkout` does not work with file checkout. | shell:zsh | to re-check |  |
| [#936](https://github.com/nvbn/thefuck/issues/936) | Thefuck crashes when applying `brew_cask_dependency` rule | install | to re-check |  |
| [#941](https://github.com/nvbn/thefuck/issues/941) | Add support for brew command not found | install | to re-check |  |
| [#943](https://github.com/nvbn/thefuck/issues/943) | Detect derivates of the rm  / | other | to re-check |  |
| [#945](https://github.com/nvbn/thefuck/issues/945) | snap remove correction suggest installing snap instead of using sudo | install | to re-check |  |
| [#951](https://github.com/nvbn/thefuck/issues/951) | gbk encoding problem | install | to re-check |  |
| [#956](https://github.com/nvbn/thefuck/issues/956) | Suggest correct filename for editing | windows | to re-check |  |
| [#970](https://github.com/nvbn/thefuck/issues/970) | Bash cursor position bugged with instant mode | install | to re-check |  |
| [#972](https://github.com/nvbn/thefuck/issues/972) | Support `source ~/.bashrc` when installing | install | to re-check |  |
| [#973](https://github.com/nvbn/thefuck/issues/973) | issue with python module requests whcile import in jython | other | to re-check |  |
| [#980](https://github.com/nvbn/thefuck/issues/980) | Give advice on Python version | other | to re-check |  |
| [#990](https://github.com/nvbn/thefuck/issues/990) | self-protect thefuck | install | to re-check |  |
| [#1008](https://github.com/nvbn/thefuck/issues/1008) | thefuck won't run at all | other | to re-check |  |
| [#1011](https://github.com/nvbn/thefuck/issues/1011) | Command expecting a tty fail to be rerun correctly | shell:zsh | to re-check |  |
| [#1026](https://github.com/nvbn/thefuck/issues/1026) | AccessDenied after quitting "sudo su" | windows | to re-check |  |
| [#1034](https://github.com/nvbn/thefuck/issues/1034) | No results for a npm global install missing sudo | install | to re-check |  |
| [#1035](https://github.com/nvbn/thefuck/issues/1035) | Windows cmd support | windows | to re-check |  |
| [#1040](https://github.com/nvbn/thefuck/issues/1040) | ProcessNotFound on zsh in Virtual archlinux | shell:zsh | to re-check |  |
| [#1073](https://github.com/nvbn/thefuck/issues/1073) | Order suggestions based on suggesttions selected earlier | windows | to re-check |  |
| [#1080](https://github.com/nvbn/thefuck/issues/1080) | Experimental instant mode breaks bash wrapping / overflow | install | to re-check |  |
| [#1081](https://github.com/nvbn/thefuck/issues/1081) | Color goes wrong on windows powershell | windows | to re-check |  |
| [#1107](https://github.com/nvbn/thefuck/issues/1107) | Compatibility with jthistle's SUDO program? | install | to re-check |  |
| [#1112](https://github.com/nvbn/thefuck/issues/1112) | [Bug] Key error when running thefuck on termux | other | to re-check | psutil on Android/Termux |
| [#1126](https://github.com/nvbn/thefuck/issues/1126) | thefuck doesn't ask for confirmation when fixing `reboot` | shell:zsh | to re-check |  |
| [#1136](https://github.com/nvbn/thefuck/issues/1136) | error on termux | other | to re-check | psutil on Android/Termux |
| [#1144](https://github.com/nvbn/thefuck/issues/1144) | correct 'cask reinstall' to 'brew cask reinstall' instead of 'brew cask install' | install | to re-check |  |
| [#1169](https://github.com/nvbn/thefuck/issues/1169) | Working fine, but will automatically open ".zshrc" file every time | performance | to re-check |  |
| [#1172](https://github.com/nvbn/thefuck/issues/1172) | Commands with variable definition are not matched by most rules | install | to re-check |  |
| [#1177](https://github.com/nvbn/thefuck/issues/1177) | Feature Request: rvm | install | to re-check |  |
| [#1189](https://github.com/nvbn/thefuck/issues/1189) | EOL (end of line) issue on windows | windows | to re-check |  |
| [#1195](https://github.com/nvbn/thefuck/issues/1195) | The Fuck Does not Respect Aliases in Shell | shell:zsh | to re-check |  |
| [#1229](https://github.com/nvbn/thefuck/issues/1229) | sudo.py assumes && for shell 'and' | shell:fish | to re-check | fish 3.0+ supports && |
| [#1230](https://github.com/nvbn/thefuck/issues/1230) | Command Format | shell:zsh | to re-check |  |
| [#1237](https://github.com/nvbn/thefuck/issues/1237) | what to delete to reset/clear/remove "profile" | windows | to re-check |  |
| [#1257](https://github.com/nvbn/thefuck/issues/1257) | Different rule found when using fish vs bash/zsh | windows | to re-check |  |
| [#1265](https://github.com/nvbn/thefuck/issues/1265) | Causes shell crash on first loads | other | to re-check |  |
| [#1268](https://github.com/nvbn/thefuck/issues/1268) | Getting `nologin git push` when pushing to a git branch without upstream | shell:zsh | to re-check |  |
| [#1269](https://github.com/nvbn/thefuck/issues/1269) | Gnome gets stuck on a login loop with pip version of thefuck | install | to re-check |  |
| [#1273](https://github.com/nvbn/thefuck/issues/1273) | [SUGGESTION] Bash "command_not_found_handle" function replacement | install | to re-check |  |
| [#1278](https://github.com/nvbn/thefuck/issues/1278) | git push not getting the upstream branch with aliased git | shell:zsh | to re-check |  |
| [#1296](https://github.com/nvbn/thefuck/issues/1296) | pnpm does not work | windows | to re-check |  |
| [#1322](https://github.com/nvbn/thefuck/issues/1322) | [suggestion] correcting commands from the wrong platform | install | to re-check |  |
| [#1330](https://github.com/nvbn/thefuck/issues/1330) | Quote URLs if zsh is used | shell:zsh | to re-check |  |
| [#1332](https://github.com/nvbn/thefuck/issues/1332) | Feature Suggestion: Provide single line installation script | install | to re-check |  |
| [#1333](https://github.com/nvbn/thefuck/issues/1333) | Output is always "No fucks given" on Windows PowerShell | install | to re-check |  |
| [#1338](https://github.com/nvbn/thefuck/issues/1338) | newest version fixes date command incorrectly | windows | to re-check |  |
| [#1339](https://github.com/nvbn/thefuck/issues/1339) | Change the utility name | install | to re-check | oopsh has a new name |
| [#1345](https://github.com/nvbn/thefuck/issues/1345) | Code style is inconsistent | performance | to re-check |  |
| [#1349](https://github.com/nvbn/thefuck/issues/1349) | make appimage or binary file | install | to re-check |  |
| [#1350](https://github.com/nvbn/thefuck/issues/1350) | Multiple problems | performance | to re-check |  |
| [#1356](https://github.com/nvbn/thefuck/issues/1356) | OSS License compatibility question | other | to re-check |  |
| [#1360](https://github.com/nvbn/thefuck/issues/1360) | time-out exception seems triggered by a correct command | performance | to re-check |  |
| [#1364](https://github.com/nvbn/thefuck/issues/1364) | install.sh | install | to re-check |  |
| [#1372](https://github.com/nvbn/thefuck/issues/1372) | App just hangs when invoking | windows | to re-check |  |
| [#1379](https://github.com/nvbn/thefuck/issues/1379) | Using fuck outputs the right correction, but freezes the terminal and doesn't execute or let me input anything else. | other | to re-check |  |
| [#1385](https://github.com/nvbn/thefuck/issues/1385) | QuickFuck - automatic, no confirmation, multi-typo-fix, togglable | other | to re-check |  |
| [#1395](https://github.com/nvbn/thefuck/issues/1395) | The command does not work after brew install | install | to re-check |  |
| [#1396](https://github.com/nvbn/thefuck/issues/1396) | Passing arguments to thefuck | windows | to re-check |  |
| [#1400](https://github.com/nvbn/thefuck/issues/1400) | Conflicting documentation for correct syntax of alias | other | to re-check |  |
| [#1401](https://github.com/nvbn/thefuck/issues/1401) | Instant mode crashes KDE Plasma on login | instant-mode | to re-check |  |
| [#1403](https://github.com/nvbn/thefuck/issues/1403) | Command takes 6 seconds, then doesn't find the correction | shell:zsh | to re-check |  |
| [#1411](https://github.com/nvbn/thefuck/issues/1411) | subprocess.run does not work inside side_effect | other | to re-check |  |
| [#1420](https://github.com/nvbn/thefuck/issues/1420) | [Suggestion] Correct pip remove, delete to uninstall | install | to re-check |  |
| [#1421](https://github.com/nvbn/thefuck/issues/1421) | How about adding a typo correction rule related to 'nvm'? | windows | to re-check |  |
| [#1422](https://github.com/nvbn/thefuck/issues/1422) | Request for adding Pull Request Template | performance | to re-check |  |
| [#1423](https://github.com/nvbn/thefuck/issues/1423) | I can't run thefuck on powershell | install | to re-check |  |
| [#1424](https://github.com/nvbn/thefuck/issues/1424) | Unhandled `apt` "Packages were downgraded and -y was used without --allow-downgrades" error | install | to re-check |  |
| [#1428](https://github.com/nvbn/thefuck/issues/1428) | Shell slow to start with `eval "$(thefuck --alias)"`, workaround is a lazy loading trick | other | to re-check |  |
| [#1431](https://github.com/nvbn/thefuck/issues/1431) | When using Windows Terminal to ssh to a remote server with Zsh/OMZ/powerlevel10k, and instant mode in ~/.zshrc, sometimes crash on start up. | windows | to re-check |  |
| [#1433](https://github.com/nvbn/thefuck/issues/1433) | Help for installing on windows | install | to re-check |  |
| [#1435](https://github.com/nvbn/thefuck/issues/1435) | Error in building development container | windows | to re-check |  |
| [#1436](https://github.com/nvbn/thefuck/issues/1436) | Feature Request: Instant-Interactive Mode + Zoxide with FZF | performance | to re-check |  |
| [#1439](https://github.com/nvbn/thefuck/issues/1439) | apt command completion error | install | to re-check |  |
| [#1440](https://github.com/nvbn/thefuck/issues/1440) | Alternative Exit sequence? | other | to re-check |  |
| [#1441](https://github.com/nvbn/thefuck/issues/1441) | Doesn't work in nushell (sees it as generic shell) | shell:other | fixed | Nushell support |
| [#1460](https://github.com/nvbn/thefuck/issues/1460) | I get a error when i run fuck command in windows, installed fuck with pip | install | to re-check |  |
| [#1461](https://github.com/nvbn/thefuck/issues/1461) | Tests failures on aarch64 | windows | to re-check |  |
| [#1462](https://github.com/nvbn/thefuck/issues/1462) | Is there any proper documentation on how to install The Fuck on Windows CMD? | install | to re-check |  |
| [#1463](https://github.com/nvbn/thefuck/issues/1463) | `fuck` is inordinately slow, even with instant mode enabled | performance | to re-check |  |
| [#1472](https://github.com/nvbn/thefuck/issues/1472) | liamosaur has set his or her tweets to private, so we're unable to view the referenced post. | other | to re-check |  |
| [#1481](https://github.com/nvbn/thefuck/issues/1481) | Not important, but the easter egg doesn't work with sudo | other | to re-check |  |
| [#1484](https://github.com/nvbn/thefuck/issues/1484) | No matter what command is given, it says No fucks given | other | to re-check | Windows: likely fixed by finding python.exe as python |
| [#1485](https://github.com/nvbn/thefuck/issues/1485) | Fuck is all you need | other | to re-check |  |
| [#1488](https://github.com/nvbn/thefuck/issues/1488) | What if I spelled "fcuk" wrong? | other | to re-check |  |
| [#1490](https://github.com/nvbn/thefuck/issues/1490) | the fuck can't work correctly | other | to re-check |  |
| [#1492](https://github.com/nvbn/thefuck/issues/1492) | `No fuck given` when i run `fuck` with a typo on the last prompt | other | to re-check |  |
| [#1495](https://github.com/nvbn/thefuck/issues/1495) | Instand mode doesn't work with omp (oh-my-posh) | performance | to re-check |  |
| [#1496](https://github.com/nvbn/thefuck/issues/1496) | error from thefuck when resizing terminal window | other | to re-check |  |
| [#1500](https://github.com/nvbn/thefuck/issues/1500) | No fucks given for homebrew update command | other | to re-check | the rule matches; rerunning `brew update` exceeds the 3 s timeout, and recent Homebrew runs the upgrade itself |
| [#1502](https://github.com/nvbn/thefuck/issues/1502) | fish issue on termux with psutil | other | to re-check |  |
| [#1504](https://github.com/nvbn/thefuck/issues/1504) | ~100ms Impact on Zsh Startup | install | to re-check |  |
| [#1509](https://github.com/nvbn/thefuck/issues/1509) | `psutil.AccessDenied` and `PermissionError` after exiting `sudo su` | other | to re-check |  |
| [#1511](https://github.com/nvbn/thefuck/issues/1511) | Request to add a Chinese README document | performance | to re-check |  |
| [#1512](https://github.com/nvbn/thefuck/issues/1512) | More Windows commands | windows | to re-check |  |
| [#1529](https://github.com/nvbn/thefuck/issues/1529) | Have to source bashrc every time I open a shell | other | to re-check |  |
| [#1532](https://github.com/nvbn/thefuck/issues/1532) | Small issue when using “fuck” command with oh-my-zsh | other | to re-check |  |
| [#1536](https://github.com/nvbn/thefuck/issues/1536) | Force specific shell with `thefuck --alias` | install | to re-check | setting TF_SHELL does it |
| [#1554](https://github.com/nvbn/thefuck/issues/1554) | Gives "no fucks given" error | other | to re-check |  |
| [#1556](https://github.com/nvbn/thefuck/issues/1556) | Mentioned "Ubuntu/Mint" in README | other | to re-check |  |
| [#1560](https://github.com/nvbn/thefuck/issues/1560) | libexpat now an explicit install requirement on macOS | install | to re-check |  |
| [#1561](https://github.com/nvbn/thefuck/issues/1561) | Is a different command correction tool -- Typo | install | to re-check |  |
| [#1570](https://github.com/nvbn/thefuck/issues/1570) | thefuck-fixed | other | to re-check |  |
| [#39](https://github.com/nvbn/thefuck/issues/39) | Add a way to trigger this for certain commands when the shell gets a failure value | rule-request | request |  |
| [#90](https://github.com/nvbn/thefuck/issues/90) | Is it possible for tab completion to replace "fuck" with the command it is going to execute? | rule-request | request |  |
| [#297](https://github.com/nvbn/thefuck/issues/297) | Add ability to edit suggested command | rule-request | request |  |
| [#380](https://github.com/nvbn/thefuck/issues/380) | Strange suggestions for `cd ,,` | rule-request | request |  |
| [#624](https://github.com/nvbn/thefuck/issues/624) | Dynamic priorities of fixed commands | rule-request | request |  |
| [#638](https://github.com/nvbn/thefuck/issues/638) | When pushing to or pulling from a git repository that needs merging, open mergetool. | rule-request | request |  |
| [#675](https://github.com/nvbn/thefuck/issues/675) | Can we make thefuck learn alias + function in bash? | rule-request | request |  |
| [#713](https://github.com/nvbn/thefuck/issues/713) | Corrections are not suggested from the history of an ongoing bash session | rule-request | request |  |
| [#742](https://github.com/nvbn/thefuck/issues/742) | Messing up with tmux vertical panes | rule-request | request |  |
| [#871](https://github.com/nvbn/thefuck/issues/871) | I have a problem on my centos. | rule-request | request |  |
| [#955](https://github.com/nvbn/thefuck/issues/955) | Feature Request: Invoke the fuck automatically with exit status | rule-request | request |  |
| [#957](https://github.com/nvbn/thefuck/issues/957) | `&&` or `\|` support | rule-request | request |  |
| [#1065](https://github.com/nvbn/thefuck/issues/1065) | Feature request - "fuck" for "fuck" that's misspelled | rule-request | request |  |
| [#1068](https://github.com/nvbn/thefuck/issues/1068) | Recognize K8s commands? | rule-request | request |  |
| [#1158](https://github.com/nvbn/thefuck/issues/1158) | running `fuck` after successful `apt update` errors after several seconds | rule-request | request |  |
| [#1312](https://github.com/nvbn/thefuck/issues/1312) | Support for doas | rule-request | request |  |
| [#1315](https://github.com/nvbn/thefuck/issues/1315) | Is it possible to add correction for environment variables? | rule-request | request |  |
| [#1334](https://github.com/nvbn/thefuck/issues/1334) | [Enhancement] add rule for git commit message | rule-request | request |  |
| [#1402](https://github.com/nvbn/thefuck/issues/1402) | Command intercepted but not presented a fuck, have to run fuck manually for the suggestion | rule-request | request |  |
| [#1443](https://github.com/nvbn/thefuck/issues/1443) | [Suggestion] | rule-request | request |  |
| [#1455](https://github.com/nvbn/thefuck/issues/1455) | [Suggestion] | rule-request | request |  |
| [#1486](https://github.com/nvbn/thefuck/issues/1486) | [Feature Request] Enhanced IDE Integration Support | rule-request | request |  |
| [#1606](https://github.com/nvbn/thefuck/issues/1606) | Security issue | rule-request | request | details were sent privately to the original maintainer; see SECURITY.md to report to oopsh |
| [#1617](https://github.com/nvbn/thefuck/issues/1617) | Support cowsay if present | rule-request | request |  |
| [#1625](https://github.com/nvbn/thefuck/issues/1625) | Feature: Add Smart Command Suggestions | rule-request | request |  |
| [#97](https://github.com/nvbn/thefuck/issues/97) | Voice command? :) | meta | discussion |  |
| [#320](https://github.com/nvbn/thefuck/issues/320) | Handling of simple compilation errors | meta | discussion |  |
| [#334](https://github.com/nvbn/thefuck/issues/334) | "history" rule runs very slow when bash history is huge | meta | discussion |  |
| [#440](https://github.com/nvbn/thefuck/issues/440) | Does not reduce feelings of inadequacy | meta | discussion |  |
| [#480](https://github.com/nvbn/thefuck/issues/480) | pacman is not sudoed after typo | meta | discussion |  |
| [#497](https://github.com/nvbn/thefuck/issues/497) | Cannot associate to 'fuck' self | meta | discussion |  |
| [#498](https://github.com/nvbn/thefuck/issues/498) | Archlinux fuck after command not working with zsh | meta | discussion |  |
| [#528](https://github.com/nvbn/thefuck/issues/528) | Terminal input fucked after running fuck | meta | discussion |  |
| [#542](https://github.com/nvbn/thefuck/issues/542) | zsh command not found with git push | meta | discussion |  |
| [#576](https://github.com/nvbn/thefuck/issues/576) | "thefuck" typically loads slower that I manually type the command | meta | discussion |  |
| [#589](https://github.com/nvbn/thefuck/issues/589) | bash: bad parsing of command substitutions | meta | discussion |  |
| [#628](https://github.com/nvbn/thefuck/issues/628) | No such file or Directory rule missing | meta | discussion |  |
| [#634](https://github.com/nvbn/thefuck/issues/634) | A seeming error, after 'apt update && apt upgrade' | meta | discussion |  |
| [#666](https://github.com/nvbn/thefuck/issues/666) | Sometimes offers bad fucks from history | meta | discussion |  |
| [#677](https://github.com/nvbn/thefuck/issues/677) | Try hitting 'tab' on previous command | meta | discussion |  |
| [#694](https://github.com/nvbn/thefuck/issues/694) | Strange proposals for docker ps | meta | discussion |  |
| [#720](https://github.com/nvbn/thefuck/issues/720) | Doesn't handle quotes and arguments with spaces well | meta | discussion |  |
| [#726](https://github.com/nvbn/thefuck/issues/726) | Add fuck when git fix the wrong command | meta | discussion |  |
| [#782](https://github.com/nvbn/thefuck/issues/782) | [bug] Support the hashtag symbol in branch names | meta | discussion |  |
| [#799](https://github.com/nvbn/thefuck/issues/799) | cannot import name '_psutil_linux' | meta | discussion |  |
| [#802](https://github.com/nvbn/thefuck/issues/802) | correct uppercase fuckups | meta | discussion |  |
| [#866](https://github.com/nvbn/thefuck/issues/866) | You are a genius. | meta | discussion |  |
| [#878](https://github.com/nvbn/thefuck/issues/878) | Instant Mode in Fish Shell | meta | discussion |  |
| [#893](https://github.com/nvbn/thefuck/issues/893) | there is no such file named 'settings.py' in ~thefuck dir | meta | discussion |  |
| [#910](https://github.com/nvbn/thefuck/issues/910) | This is awesome | meta | discussion |  |
| [#969](https://github.com/nvbn/thefuck/issues/969) | The command runs again and again with no exit. MacOs, Zsh | meta | discussion |  |
| [#1018](https://github.com/nvbn/thefuck/issues/1018) | `eval $(thefuck --alias)` is slow | meta | discussion |  |
| [#1057](https://github.com/nvbn/thefuck/issues/1057) | TypeError: 'DeprecationWrapper' object is not callable | meta | discussion |  |
| [#1146](https://github.com/nvbn/thefuck/issues/1146) | [SUGGESTION] Write to stdin instead of using the confirmation prompt | meta | discussion |  |
| [#1159](https://github.com/nvbn/thefuck/issues/1159) | Feature Request: Correct me when I type `figlet moo \| cowsay` | meta | discussion |  |
| [#1254](https://github.com/nvbn/thefuck/issues/1254) | Alias for nushell | meta | fixed | Nushell support |
| [#1337](https://github.com/nvbn/thefuck/issues/1337) | Proposition: rules with no alternative command and only side effects | meta | discussion |  |
| [#1346](https://github.com/nvbn/thefuck/issues/1346) | [fish] Some command output is missing | meta | discussion |  |
| [#1377](https://github.com/nvbn/thefuck/issues/1377) | Adding Support For Mendel Development Kit (MDT) | meta | discussion |  |
| [#1398](https://github.com/nvbn/thefuck/issues/1398) | [Suggestion] Detect "did you mean ...?" | meta | discussion |  |
| [#1408](https://github.com/nvbn/thefuck/issues/1408) | [WARN] Output log isn't specified when "instant mode" turned on | meta | discussion |  |
| [#1458](https://github.com/nvbn/thefuck/issues/1458) | Feature request: LLM / GPT integration | meta | discussion |  |
| [#1466](https://github.com/nvbn/thefuck/issues/1466) | The repo is dead | meta | discussion | oopsh is the maintained fork |
| [#1518](https://github.com/nvbn/thefuck/issues/1518) | Rewrite it in C | meta | discussion |  |
| [#1520](https://github.com/nvbn/thefuck/issues/1520) | Have you considered integrating AI tools to improve command analysis and error correction capabilities? | meta | discussion |  |
| [#1521](https://github.com/nvbn/thefuck/issues/1521) | Rewrite it in Rust | meta | discussion |  |
| [#1528](https://github.com/nvbn/thefuck/issues/1528) | Use AI instead of pattern recognition | meta | discussion |  |
| [#1566](https://github.com/nvbn/thefuck/issues/1566) | Is this project not be maintained so long? | meta | discussion | oopsh is the maintained fork |
| [#1616](https://github.com/nvbn/thefuck/issues/1616) | The ScriptPorn panel judged utils.py: 72/100 Filthy | meta | discussion |  |
| [#1618](https://github.com/nvbn/thefuck/issues/1618) | The Bleep - A fast, maintained successor to The Fuck | meta | discussion | another fork |
