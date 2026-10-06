# Open pull requests of thefuck

oopsh reviewed every pull request that was open on [nvbn/thefuck](https://github.com/nvbn/thefuck/pulls) in October 2026 (151 in total). Merged ones keep their original author; the commit message links the pull request. Thanks to everyone who contributed them.

| Decision | Count |
|---|---|
| merged | 10 |
| merged, adapted | 27 |
| partly merged | 1 |
| superseded | 2 |
| already in oopsh | 56 |
| docs obsolete | 9 |
| deferred | 9 |
| not merged | 37 |

| PR | Title | Author | Decision | Notes |
|---|---|---|---|---|
| [#873](https://github.com/nvbn/thefuck/pull/873) | Use `yield from` | @abdulniyaspm | merged |  |
| [#948](https://github.com/nvbn/thefuck/pull/948) | Suppport rbenv install | @abramzog | merged |  |
| [#995](https://github.com/nvbn/thefuck/pull/995) | Only including necessary envs in THEFUCK_DEBUG=true. | @haneybarg | merged |  |
| [#1093](https://github.com/nvbn/thefuck/pull/1093) | Added quoting to ZSH `eval` parameters | @github-usr-name | merged |  |
| [#1281](https://github.com/nvbn/thefuck/pull/1281) | Small fixes to pacman_not_found rule | @scorphus | merged |  |
| [#1343](https://github.com/nvbn/thefuck/pull/1343) | #N/A: Add new `kedro_no_such_command` rule | @deepyaman | merged |  |
| [#1358](https://github.com/nvbn/thefuck/pull/1358) | minor improvement to test_brew_unknown_command | @andrehora | merged |  |
| [#1426](https://github.com/nvbn/thefuck/pull/1426) | Update list of 'Brew' commands | @pixel365 | merged |  |
| [#1600](https://github.com/nvbn/thefuck/pull/1600) | Handle denied process exe lookup in rerun | @puneetdixit200 | merged |  |
| [#1624](https://github.com/nvbn/thefuck/pull/1624) | Add xcode_license rule | @LeonFedotov | merged |  |
| [#777](https://github.com/nvbn/thefuck/pull/777) | fix $PATH problem when using cmder(git-bash) on windows. | @BurdenBear | merged, adapted | uses PATHEXT |
| [#992](https://github.com/nvbn/thefuck/pull/992) | Add edit filename rule | @riley-martine | merged, adapted | only real editors match (not vimdiff etc.), no crash on missing directories |
| [#1006](https://github.com/nvbn/thefuck/pull/1006) | Fallback to su if sudo doesn't exist | @moore3071 | merged, adapted | also matches the bash/sh message, only for commands starting with sudo |
| [#1007](https://github.com/nvbn/thefuck/pull/1007) | Fix Issue #959: breaks after composer require with single package, revamp composer rules | @caspycat | merged, adapted | kept the later `composer install` -> `require` case (#1135) |
| [#1060](https://github.com/nvbn/thefuck/pull/1060) | #962: Add the new apt_unable_to_locate rule | @cjoshmartin | merged, adapted | enabled only where apt exists |
| [#1082](https://github.com/nvbn/thefuck/pull/1082) | added gcloud cli | @ronandoolan2 | merged, adapted | keeps the rest of the command, offers every suggestion |
| [#1102](https://github.com/nvbn/thefuck/pull/1102) | add support for docker daemon not running | @soraxas | merged, adapted | handles sudo, enabled only with systemctl, tests added |
| [#1243](https://github.com/nvbn/thefuck/pull/1243) | Add `ping` rule | @mutoo | merged, adapted | also matches Linux/BusyBox messages |
| [#1244](https://github.com/nvbn/thefuck/pull/1244) | Add rule for restic | @saiwing-yeung | merged, adapted | parses the suggestions block |
| [#1258](https://github.com/nvbn/thefuck/pull/1258) | fix: fish history file location | @mainrs | merged, adapted | reimplemented on current code, legacy path as fallback |
| [#1289](https://github.com/nvbn/thefuck/pull/1289) | Makefile Error Rule | @andrewhuston | merged, adapted | parses only explicit targets, keeps options, tests in a temp dir |
| [#1297](https://github.com/nvbn/thefuck/pull/1297) | Upper to lower case | @nkakonas | merged, adapted | doesn't rely on `which` (case-insensitive filesystems) |
| [#1347](https://github.com/nvbn/thefuck/pull/1347) | Add rule for the ninja build tool | @alanzhao1 | merged, adapted | keeps other arguments, matches only ninja |
| [#1351](https://github.com/nvbn/thefuck/pull/1351) | Add terraform_init_upgrade | @iFreilicht | merged, adapted | tests added |
| [#1353](https://github.com/nvbn/thefuck/pull/1353) | Support long flag --delete | @asportnoy | merged, adapted | tests added |
| [#1355](https://github.com/nvbn/thefuck/pull/1355) | be compatible with nounset shells | @ds-cbo | merged, adapted | extended to the `oopsh` shell function |
| [#1362](https://github.com/nvbn/thefuck/pull/1362) | checkout to default branch instead of master | @KerH | merged, adapted | reimplemented without a shell pipeline |
| [#1367](https://github.com/nvbn/thefuck/pull/1367) | update npm missing script matchers | @songz | merged, adapted | npm 6, 7+ and 10 messages |
| [#1373](https://github.com/nvbn/thefuck/pull/1373) | Add `cd_quotes` rule | @FireFragment | merged, adapted | only when the quoted directory exists, never across `&&` etc. |
| [#1393](https://github.com/nvbn/thefuck/pull/1393) | feat: new rule for `nix-shell` | @thenbe | merged, adapted | shell quoting, missing command-not-found |
| [#1429](https://github.com/nvbn/thefuck/pull/1429) | Added Uncommon Typos | @preetham1239 | merged, adapted | fixed mutation of the typos table; table fixes always offered |
| [#1470](https://github.com/nvbn/thefuck/pull/1470) | Update chmod_x to work with non-relative paths | @non-bin | merged, adapted | kept absolute paths intact (the PR cut the first two characters) |
| [#1514](https://github.com/nvbn/thefuck/pull/1514) | Add support for 'paru' in pacman_not_found rule and tests | @xela-zone | merged, adapted | merged on top of #1281 |
| [#1517](https://github.com/nvbn/thefuck/pull/1517) | Add callout for WSL suggested config to improve performance | @stuartleeks | merged, adapted | reworded |
| [#1539](https://github.com/nvbn/thefuck/pull/1539) | Fix BrokenPipeError when terminal pipe is closed | @shaunpatterson | merged, adapted | applied by hand, test added |
| [#1551](https://github.com/nvbn/thefuck/pull/1551) | Fix IndexError when parsing empty alias value in bash shell | @Ektawadurkar | merged, adapted | test added |
| [#1562](https://github.com/nvbn/thefuck/pull/1562) | fix: gracefully handle non-TTY environments | @nazt | merged, adapted | doesn't run unconfirmed fixes: explains `--yes` instead |
| [#1186](https://github.com/nvbn/thefuck/pull/1186) | Cd rules | @ICalhoun | partly merged | only the PowerShell/cmd messages for cd_mkdir |
| [#883](https://github.com/nvbn/thefuck/pull/883) | Added git lock rule | @tobibechtold | superseded | covered by #1429 |
| [#1255](https://github.com/nvbn/thefuck/pull/1255) | Add support for paru to the pacman_not_found rule | @dylanmtaylor | superseded | paru support merged via #1514 |
| [#1180](https://github.com/nvbn/thefuck/pull/1180) | Explicitly require setuptools, thefuck/utils.py imports pkg_resources | @hroncok | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1247](https://github.com/nvbn/thefuck/pull/1247) | Remove distutils dependency | @nootr | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1344](https://github.com/nvbn/thefuck/pull/1344) | Use unittest's buildin mock | @jelly | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1359](https://github.com/nvbn/thefuck/pull/1359) | Python 3 language feature updates | @marksmayo | already in oopsh | Python 2 removal and modernisation done separately |
| [#1404](https://github.com/nvbn/thefuck/pull/1404) | replace distutils for python 3.12 | @branchv | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1412](https://github.com/nvbn/thefuck/pull/1412) | Fix path strip issue in which function(util.py) | @paintedblue | already in oopsh | the fallback it changes is dead code: shutil.which is always available |
| [#1437](https://github.com/nvbn/thefuck/pull/1437) | Update tests: mock is now part of unittest | @aylen384 | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1454](https://github.com/nvbn/thefuck/pull/1454) | Create python-publish.yml | @Shepherd36 | already in oopsh | oopsh has its own release workflow |
| [#1459](https://github.com/nvbn/thefuck/pull/1459) | Reduce Startup Execution Time | @cyuria | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1465](https://github.com/nvbn/thefuck/pull/1465) | Replace deprecated imp module with importlib for Python compatibility | @teja-pola | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1468](https://github.com/nvbn/thefuck/pull/1468) | Update conf.py | @teja-pola | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1474](https://github.com/nvbn/thefuck/pull/1474) | Make tests compatible with pytest v8.x | @carlsmedstad | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1475](https://github.com/nvbn/thefuck/pull/1475) | Fix compatibility with Python > 3.10 | @DJStompZone | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1479](https://github.com/nvbn/thefuck/pull/1479) | remove Python2 support | @a-detiste | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1483](https://github.com/nvbn/thefuck/pull/1483) | fixed import imp crash | @DL909 | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1487](https://github.com/nvbn/thefuck/pull/1487) | ♻️ refactor(unix): replace deprecated distutils.spawn with shutil.which | @lujin3 | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1497](https://github.com/nvbn/thefuck/pull/1497) | Fix Python 3.12 'imp' error | @robert-werner | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1499](https://github.com/nvbn/thefuck/pull/1499) | Fix crash on newer pythons | @andrew-vant | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1516](https://github.com/nvbn/thefuck/pull/1516) | Changes to induce compatablity with python 12+ | @RushilCodes | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1523](https://github.com/nvbn/thefuck/pull/1523) | fix #1515: add no_memoize to TestGetValidHistoryWithoutCurrent | @nktkhndlwl | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1525](https://github.com/nvbn/thefuck/pull/1525) | updated a module for python3 user compatibility | @AbhisekLimbu | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1534](https://github.com/nvbn/thefuck/pull/1534) | Fix `No module named 'distutils'` for Python3.12+ | @waketzheng | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1537](https://github.com/nvbn/thefuck/pull/1537) | fix: suppress Windows PowerShell encoding mismatch warning | @egger-meow | already in oopsh | win_unicode_console, the source of the warning, was removed |
| [#1550](https://github.com/nvbn/thefuck/pull/1550) | tests: make tests compatible with Pytest 9 | @stanislavlevin | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1555](https://github.com/nvbn/thefuck/pull/1555) | Replace deprecated pkg_resources with importlib.metadata | @ianhandy | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1557](https://github.com/nvbn/thefuck/pull/1557) | tests: remove fixture mark deprecated in pytest 9 | @ReinerBRO | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1569](https://github.com/nvbn/thefuck/pull/1569) | support:support for Python 3.12+ | @guguzea | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1573](https://github.com/nvbn/thefuck/pull/1573) | chore(deps): 2 outdated constraints identified. setuptools lower bound is 10+ years o | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1574](https://github.com/nvbn/thefuck/pull/1574) | chore(deps): 3 outdated constraints found. setuptools lower-bound is ancient (>=17.1 | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1575](https://github.com/nvbn/thefuck/pull/1575) | chore(deps): 3 concerns found: setuptools floor is 10 years old (>=17.1→>=70); mock i | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1577](https://github.com/nvbn/thefuck/pull/1577) | chore(deps): 6 potential improvements: psutil 5.0.0→>=5.9 (major bump, test after), s | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1578](https://github.com/nvbn/thefuck/pull/1578) | chore(deps): 3 outdated/obsolete constraints found. setuptools floor (17.1 from 2013) | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1579](https://github.com/nvbn/thefuck/pull/1579) | chore(deps): 2 outdated constraints found. setuptools>=17.1 is severely outdated (201 | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1581](https://github.com/nvbn/thefuck/pull/1581) | chore(deps): 1 clearly outdated dep found. setuptools pinned to >=17.1 (2014) is very | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1582](https://github.com/nvbn/thefuck/pull/1582) | chore(deps): 2 actionable changes identified. pyte<0.8.1 → pyte<0.9.0 widens safe upp | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1583](https://github.com/nvbn/thefuck/pull/1583) | chore(deps): 3 outdated deps found. pexpect 4.2.1→4.9.0 (minor, safe), decorator <5 → | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1584](https://github.com/nvbn/thefuck/pull/1584) | chore(deps): 3 outdated constraints found. setuptools constraint is severely outdated | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1585](https://github.com/nvbn/thefuck/pull/1585) | chore(deps): 2 actionable changes: (1) setuptools lower bound bumped to modern minimu | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1586](https://github.com/nvbn/thefuck/pull/1586) | chore(deps): 2 outdated dependencies identified. 'mock' should be removed (stdlib uni | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1587](https://github.com/nvbn/thefuck/pull/1587) | chore(deps): Found 5 areas of concern. Most critical: setuptools lower bound is 17.1 | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1588](https://github.com/nvbn/thefuck/pull/1588) | chore(deps): 4 outdated dependencies identified. decorator/pyte have hard caps in set | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1589](https://github.com/nvbn/thefuck/pull/1589) | chore(deps): 2 issues found. setuptools has a 2013-era minimum constraint (>=17.1 → > | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1590](https://github.com/nvbn/thefuck/pull/1590) | chore(deps): 3 outdated constraints found. setuptools min (>=17.1→>=75.0) is severely | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1591](https://github.com/nvbn/thefuck/pull/1591) | chore(deps): 5 outdated entries found. setuptools floor bumped to modern 75.x (high c | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1592](https://github.com/nvbn/thefuck/pull/1592) | chore(deps): 2 concerns found. mock should be removed (deprecated, replaced by stdlib | @isagoakira | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1593](https://github.com/nvbn/thefuck/pull/1593) | chore(deps): Major concern: setuptools lower bound (>=17.1 from 2014) is severely out | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1594](https://github.com/nvbn/thefuck/pull/1594) | chore(deps): 3 potential updates: setuptools is critically outdated (17.1→70.x, safe) | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1595](https://github.com/nvbn/thefuck/pull/1595) | chore(deps): Most deps in requirements.txt lack version pins, making stale detection | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1596](https://github.com/nvbn/thefuck/pull/1596) | chore(deps): 2 outdated version constraints in setup.py extras_require. The decorator | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1597](https://github.com/nvbn/thefuck/pull/1597) | chore(deps): 1 clearly outdated dep: setuptools>=17.1 (2014 vintage) should be modern | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1598](https://github.com/nvbn/thefuck/pull/1598) | chore(deps): 3 deps flagged for upgrade. setuptools constraint is critically outdated | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1599](https://github.com/nvbn/thefuck/pull/1599) | chore(deps): Most deps in requirements.txt lack pinned versions so current versions w | @isagoakira | already in oopsh | automated dependency PR; setup.py and requirements.txt were replaced by pyproject.toml |
| [#1601](https://github.com/nvbn/thefuck/pull/1601) | chore(deps): 3 dependencies need attention. mock (deprecated, use stdlib unittest.moc | @isagoakira | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1603](https://github.com/nvbn/thefuck/pull/1603) | chore(deps): 5 potential updates identified. mock is deprecated (unittest.mock in std | @isagoakira | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1619](https://github.com/nvbn/thefuck/pull/1619) | fix: Python 3.12+ compatibility (test speed +74%, zero regressions) | @chengganping-ship-it | already in oopsh | Python 3.12+ / pytest 8 / packaging work |
| [#1627](https://github.com/nvbn/thefuck/pull/1627) | Fix typo 'bellow' -> 'below' in SETTINGS_HEADER (thefuck/const.py) | @haimingZZ | already in oopsh |  |
| [#1010](https://github.com/nvbn/thefuck/pull/1010) | Updated README intro to be more precise | @haider-ilahi | docs obsolete | about thefuck's README/installation, rewritten for oopsh |
| [#1064](https://github.com/nvbn/thefuck/pull/1064) | Updated `CONTRIBUTING.md` to reflect what I learned at HackIllinois | @cjoshmartin | docs obsolete | about thefuck's README/installation, rewritten for oopsh |
| [#1260](https://github.com/nvbn/thefuck/pull/1260) | README: add Fedora to list of supported distros | @rocketraman | docs obsolete | about thefuck's README/installation, rewritten for oopsh |
| [#1284](https://github.com/nvbn/thefuck/pull/1284) | Repositioning the Table of Contents | @shad0wcrawl3r | docs obsolete | about thefuck's README/installation, rewritten for oopsh |
| [#1294](https://github.com/nvbn/thefuck/pull/1294) | Add some info in README.md | @nkakonas | docs obsolete | about thefuck's README/installation, rewritten for oopsh |
| [#1304](https://github.com/nvbn/thefuck/pull/1304) | Update CONTRIBUTING.md | @somT-oss | docs obsolete | about thefuck's README/installation, rewritten for oopsh |
| [#1375](https://github.com/nvbn/thefuck/pull/1375) | add Fedora install instructions and bash syntax highlight to arch | @unclamped | docs obsolete | about thefuck's README/installation, rewritten for oopsh |
| [#1493](https://github.com/nvbn/thefuck/pull/1493) | Add an alternative installation command for Windows | @tolunaydundar | docs obsolete | about thefuck's README/installation, rewritten for oopsh |
| [#1513](https://github.com/nvbn/thefuck/pull/1513) | Chinese README.md | @zhanglunpu | docs obsolete | about thefuck's README/installation, rewritten for oopsh |
| [#1038](https://github.com/nvbn/thefuck/pull/1038) | Statistics Feature | @Svaught598 | deferred | feature, not reviewed yet |
| [#1063](https://github.com/nvbn/thefuck/pull/1063) | [WIP]: Add a feature to edit commands | @cjoshmartin | deferred | work in progress |
| [#1101](https://github.com/nvbn/thefuck/pull/1101) | Allow commands to be wrapped as commands for correction | @soraxas | deferred | incomplete |
| [#1114](https://github.com/nvbn/thefuck/pull/1114) | * Pamac: Correct invalid operation | @earboxer | deferred | no tests |
| [#1363](https://github.com/nvbn/thefuck/pull/1363) | Add ChatGPT as a rule, disabled by default. | @XieGuochao | deferred | sends commands to an external API; maybe as an opt-in plugin |
| [#1365](https://github.com/nvbn/thefuck/pull/1365) | GPT-3.5 | @pannous | deferred | same as #1363 |
| [#1442](https://github.com/nvbn/thefuck/pull/1442) | Add nushell support | @afresquet | deferred | runs the fix in a subprocess, so `cd` has no effect; nushell support is planned |
| [#1506](https://github.com/nvbn/thefuck/pull/1506) | Add Escape key as an alternative way to abort selection | @Nau-stack-110 | deferred | would break arrow keys on Unix; needs a proper Esc implementation |
| [#1538](https://github.com/nvbn/thefuck/pull/1538) | #1536: Added --shell argument to force specific shell usage. | @gojodennis | deferred | `TF_SHELL=fish` already does it |
| [#734](https://github.com/nvbn/thefuck/pull/734) | Add special error message for 'shit' alias | @natesholland | not merged | joke |
| [#736](https://github.com/nvbn/thefuck/pull/736) | Added fuck off, per #420 | @Epse | not merged | joke |
| [#790](https://github.com/nvbn/thefuck/pull/790) | [WIP] Add smart_rule and integrate with shell_logger | @sameetandpotatoes | not merged | work in progress |
| [#804](https://github.com/nvbn/thefuck/pull/804) | Fix git commit | @afwilkin | not merged | hack in no_command |
| [#887](https://github.com/nvbn/thefuck/pull/887) | #N/A: Add Stack Overflow rule to lookup error messages in terminal | @payton | not merged | draft |
| [#964](https://github.com/nvbn/thefuck/pull/964) | Change The file | @spidermanir | not merged | syntax error |
| [#987](https://github.com/nvbn/thefuck/pull/987) | Move brew specific functions to specific/brew.py | @aaditkamat | not merged | refactor that no longer applies |
| [#988](https://github.com/nvbn/thefuck/pull/988) | Set rm / to be a safe call | @yoavtzelnick | not merged | suggests `rm -rf /` |
| [#1013](https://github.com/nvbn/thefuck/pull/1013) | fix missing_space_before_subcommand.py rule | @brahamdelam | not merged | unclear benefit, changes existing behaviour |
| [#1020](https://github.com/nvbn/thefuck/pull/1020) | Feature/self protect thefuck | @brahamdelam | not merged | includes #1013 plus a joke rule |
| [#1103](https://github.com/nvbn/thefuck/pull/1103) | [Add] uninstall to rm | @sdasasqkim | not merged | syntax error |
| [#1104](https://github.com/nvbn/thefuck/pull/1104) | Allow editing auto-correction provided by fuck with tab | @soraxas | not merged | TIOCSTI is disabled on recent Linux kernels |
| [#1115](https://github.com/nvbn/thefuck/pull/1115) | Npx: Create npx_add_npx_to_command.py | @KartikSoneji | not merged | relies on `npm bin`, removed in npm 9 |
| [#1121](https://github.com/nvbn/thefuck/pull/1121) | Import CommandNotFound system package on Debian | @SuperSandro2000 | not merged | modifies the global sys.path |
| [#1122](https://github.com/nvbn/thefuck/pull/1122) | New Rule : Version Commands | @roopeshvs | not merged | matches any `-v`, e.g. `grep -v` |
| [#1130](https://github.com/nvbn/thefuck/pull/1130) | Fix pacman tests | @theslimshaney | not merged | removes test data without reason |
| [#1155](https://github.com/nvbn/thefuck/pull/1155) | Added brew cask reinstall to the posibilities | @Armaxxx | not merged | wrong logic; brew cask is gone |
| [#1295](https://github.com/nvbn/thefuck/pull/1295) | #1259 tar missed argument | @nkakonas | not merged | matches any command containing "tar" |
| [#1306](https://github.com/nvbn/thefuck/pull/1306) | added support for Remote Cloud Development with Gitpod | @Siddhant-K-code | not merged | Gitpod config |
| [#1311](https://github.com/nvbn/thefuck/pull/1311) | Direct commit | @nkakonas | not merged | runs `git add --all`; covered by git_commit_add |
| [#1323](https://github.com/nvbn/thefuck/pull/1323) | proof of concept | @nopeless | not merged | proof of concept without tests |
| [#1331](https://github.com/nvbn/thefuck/pull/1331) | Reduce cyclomatic complexity | @miska924 | not merged | refactor without behaviour change |
| [#1378](https://github.com/nvbn/thefuck/pull/1378) | Add support for mdt | @Jiarong-Zhang | not merged | approximate matching |
| [#1387](https://github.com/nvbn/thefuck/pull/1387) | feat : Replace 'checkout master' with 'git checkout master',which is a common mistake beginners makes | @ryudonghyun123 | not merged | malformed rule file names, no tests |
| [#1388](https://github.com/nvbn/thefuck/pull/1388) | feat : Replace 'commit' with 'git commit' which is a common mistake beginners makes | @ryudonghyun123 | not merged | malformed rule file names, no tests |
| [#1417](https://github.com/nvbn/thefuck/pull/1417) | new_rule_created | @Silambarasa | not merged | only adds -y |
| [#1451](https://github.com/nvbn/thefuck/pull/1451) | Improved test coverage of script_parts and get_installation_version | @luca-denobili | not merged | deletes the README, adds screenshots |
| [#1494](https://github.com/nvbn/thefuck/pull/1494) | Create the experimental instant mode | @realeesh17 | not merged | stray file |
| [#1498](https://github.com/nvbn/thefuck/pull/1498) | [Edited] Add docstring to improve documentation | @MayureshMore | not merged | automated comment |
| [#1553](https://github.com/nvbn/thefuck/pull/1553) | Add rule for debian systems getting an externally managed enviroment error | @aahspaghetticode | not merged | suggests --break-system-packages |
| [#1576](https://github.com/nvbn/thefuck/pull/1576) | perf: parallel rule loading/matching, cache PATH executables on disk | @henewastaken | not merged | thread-unsafe parallel rules, heuristic rule skipping, stale executables cache |
| [#1580](https://github.com/nvbn/thefuck/pull/1580) | Fix: python 3.13 windows compat | @Low-Zi-Hong | not merged | stray files (uv.lock, home dir) |
| [#1607](https://github.com/nvbn/thefuck/pull/1607) | fix: remove shell-specific && assumption in sudo rule | @decembercomposer697-hue | not merged | `if True` breaks the sudo rule |
| [#1610](https://github.com/nvbn/thefuck/pull/1610) | Python 3.12 compatibility fixes for shell history parsing and history filtering | @olucasfracaro | not merged | duplicates done work; breaks fish/tcsh history reading |
| [#1614](https://github.com/nvbn/thefuck/pull/1614) | fix(sudo): replace hardcoded "&&" with shell-agnostic "and" operator for fish shell support | @rahul-COD3 | not merged | fish supports && since 3.0 |
| [#1615](https://github.com/nvbn/thefuck/pull/1615) | Fix for the gitr to suggesting gitk | @SahilPandit590 | not merged | commits a virtualenv with binaries |
| [#1626](https://github.com/nvbn/thefuck/pull/1626) | Feature: Add smart command suggestion rule | @Acostahack123 | not merged | far too permissive duplicate of no_command |
