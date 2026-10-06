# Security policy

## Reporting a vulnerability

Please don't open a public issue. Report it privately through GitHub:
go to the [Security tab](https://github.com/geomago/oopsh/security) of the
repository and click **Report a vulnerability**.

Include what you found, how to reproduce it and which version of oopsh you use
(`oopsh --version`). You'll get an answer within a week; once a fix is released,
the advisory is published with credit to you, unless you prefer otherwise.

## Supported versions

Only the latest release of oopsh gets security fixes.

## How oopsh runs commands

oopsh prints a corrected command and the shell alias evaluates it, so a rule
that copies text from a command's output into the fix must quote it. Issues
that let output, history or files other users can write steer the fix are in
scope.
