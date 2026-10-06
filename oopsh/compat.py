"""Compatibility with thefuck, so that existing setups keep working."""
import importlib
import importlib.util
import sys


class ThefuckImportAlias(object):
    """Makes `import thefuck.x` return the `oopsh.x` module.

    Both a meta path finder and a loader; it doesn't subclass the
    `importlib.abc` classes, slow to import, as oopsh starts with every shell.

    Custom rules and `thefuck_contrib_*` packages written for thefuck import
    helpers like `from thefuck.utils import for_app`. They get the very same
    module objects as oopsh, so shared state like `settings` is shared too.

    """

    def __init__(self):
        self._original_specs = {}

    def find_spec(self, fullname, path, target=None):
        if fullname == 'thefuck' or fullname.startswith('thefuck.'):
            return importlib.util.spec_from_loader(fullname, self)
        return None

    def create_module(self, spec):
        module = importlib.import_module('oopsh' + spec.name[len('thefuck'):])
        self._original_specs[module.__name__] = module.__spec__
        return module

    def exec_module(self, module):
        """The `oopsh` module is already executed, only restore its spec,
        that the import system replaced with the `thefuck` one."""
        module.__spec__ = self._original_specs.pop(module.__name__)


def install_thefuck_import_alias():
    """Installs the alias before any other finder, so it also wins over a
    real thefuck installed in the same environment."""
    if not any(isinstance(finder, ThefuckImportAlias)
               for finder in sys.meta_path):
        sys.meta_path.insert(0, ThefuckImportAlias())
