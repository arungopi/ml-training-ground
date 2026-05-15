# src/__init__.py
"""
Package initializer.

Exports:
- __version__: semantic version string (env override via PROJECT_VERSION)
- lazy access to subpackages: utils, sklearn_project, pytorch_project, tf_project, hf_project
"""

from importlib import import_module
import types

__all__ = [
    "__version__",
    "utils",
    "sklearn_project",
    "pytorch_project",
    "tf_project",
    "hf_project",
]

# Import version helper from separate module
from .version import get_version

# Replace "PROJECT_NAME" with your package name when packaging
__version__ = get_version("PROJECT_NAME", default="0.0.0-dev")

# Lazy importer helper
def _lazy_import(name: str):
    return import_module(f"src.{name}")

# Public submodules as lightweight placeholders
utils = types.SimpleNamespace(__doc__="Utilities package (import functions directly)")
sklearn_project = types.SimpleNamespace(__doc__="sklearn project module (import functions directly)")
pytorch_project = types.SimpleNamespace(__doc__="pytorch project module (import functions directly)")
tf_project = types.SimpleNamespace(__doc__="tf project module (import functions directly)")
hf_project = types.SimpleNamespace(__doc__="huggingface project module (import functions directly)")

# Lazy-load subpackages on first attribute access
def __getattr__(name: str):
    if name in ("utils", "sklearn_project", "pytorch_project", "tf_project", "hf_project"):
        module = _lazy_import(name)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

