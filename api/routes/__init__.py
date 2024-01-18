import pathlib
import pkgutil
import importlib

def register(api):
    base_path = pathlib.Path(__file__).parent
    package   = __package__

    for finder, name, isPkg in pkgutil.walk_packages([ str(base_path) ], prefix=package + '.'):
        module = importlib.import_module(name)

        if hasattr(module, 'register'):
            module.register(api)