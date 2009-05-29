"""
pycryptopp - Python wrappers for Crypto++
"""

__version__ = "unknown"
try:
    from _version import __version__
except ImportError:
    # We're running in a tree that hasn't run "./setup.py darcsver", and didn't
    # come with a _version.py, so we don't know what our version is. This should
    # not happen very often.
    pass

# we import the actual .so here with RTLD_GLOBAL. Other modules will import
# it again, but they'll hit sys.modules.
try:
    from ctypes import RTLD_GLOBAL
except ImportError:
    # ctypes was added in Python 2.5 -- we still support Python 2.4, which
    # had dl instead
    from dl import RTLD_GLOBAL

import sys
flags = sys.getdlopenflags()
try:
    sys.setdlopenflags(flags|RTLD_GLOBAL)
    import _pycryptopp
finally:
    sys.setdlopenflags(flags)

import publickey, hash, cipher

quiet_pyflakes=[__version__, publickey, hash, cipher, _pycryptopp]
