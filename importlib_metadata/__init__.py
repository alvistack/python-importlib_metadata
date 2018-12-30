from .api import distribution, Distribution, PackageNotFoundError  # noqa: F401
from .api import metadata, entry_points, version, read_text, files, requires

# Import for installation side-effects.
from . import _hooks  # noqa: F401


__all__ = [
    'entry_points',
    'files',
    'metadata',
    'read_text',
    'requires',
    'version',
    ]


__version__ = version(__name__)
