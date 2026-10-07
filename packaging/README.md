# Packaging

Recipes for package managers, kept in sync with each release.

| Directory | Where it goes |
|---|---|
| `homebrew/oopsh.rb` | `Formula/oopsh.rb` in the [geomago/homebrew-tap](https://github.com/geomago/homebrew-tap) repository |
| `aur/PKGBUILD` | the `oopsh` package on the [AUR](https://aur.archlinux.org/) (with its `.SRCINFO`) |
| `nix/package.nix` | `pkgs/by-name/oo/oopsh/package.nix` in [nixpkgs](https://github.com/NixOS/nixpkgs) |

For a new release, update the version and the hashes: the sdist's sha256 is on
its PyPI page, and the GitHub archive's with
`curl -sL https://github.com/geomago/oopsh/archive/refs/tags/vX.Y.Z.tar.gz | shasum -a 256`.
