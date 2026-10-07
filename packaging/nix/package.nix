# nixpkgs: pkgs/by-name/oo/oopsh/package.nix
{
  lib,
  python3Packages,
  fetchPypi,
}:

python3Packages.buildPythonApplication rec {
  pname = "oopsh";
  version = "1.0.0";
  pyproject = true;

  src = fetchPypi {
    inherit pname version;
    hash = "sha256-d5Qkgz4L46d+kAT5ywbXhgCh3e20FGJVjjUpxinK1dw=";
  };

  build-system = with python3Packages; [ setuptools ];

  dependencies = with python3Packages; [
    colorama
    decorator
    psutil
    pyte
  ];

  nativeCheckInputs = with python3Packages; [
    pytestCheckHook
    pytest-mock
  ];

  # The 1.0.0 sdist lacks conftest.py and the tests/ subdirectories; later
  # releases ship them, and this line can go
  doCheck = false;

  pythonImportsCheck = [ "oopsh" ];

  meta = {
    description = "Corrects your previous console command (maintained fork of thefuck)";
    homepage = "https://github.com/geomago/oopsh";
    changelog = "https://github.com/geomago/oopsh/blob/v${version}/CHANGELOG.md";
    license = lib.licenses.mit;
    maintainers = with lib.maintainers; [ ];
    mainProgram = "oopsh";
  };
}
