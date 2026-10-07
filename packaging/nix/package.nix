# nixpkgs: pkgs/by-name/oo/oopsh/package.nix
{
  lib,
  python3Packages,
  fetchPypi,
}:

python3Packages.buildPythonApplication rec {
  pname = "oopsh";
  version = "1.1.0";
  pyproject = true;

  src = fetchPypi {
    inherit pname version;
    hash = "sha256-sz60ufsA8Lqw7oEd0DUx9q9MuYkoPc8xobW8pf1uwzU=";
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

  disabledTestPaths = [ "tests/functional" ];

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
