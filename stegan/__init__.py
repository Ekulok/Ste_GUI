import importlib

from .stegan import *

# wildcard import above does not import "private" variables like __version__
# this makes them available
globals().update(importlib.import_module('stegan.stegan').__dict__)