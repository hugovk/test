#!/usr/bin/env python
from PIL import Image
from PIL import ImageDraw
from PIL import ImageChops
print(Image.PILLOW_VERSION)

try:
    # give Tk a chance to set up the environment, in case we're
    # using an _imaging module linked against libtcl/libtk (use
    # __import__ to hide this from naive packagers; we don't really
    # depend on Tk unless ImageTk is used, and that module already
    # imports Tkinter)
    __import__("FixTk")
except ImportError:
    pass


try:
    # If the _imaging C module is not present, you can still use
    # the "open" function to identify files, but you cannot load
    # them.  Note that other modules should not refer to _imaging
    # directly; import Image and use the Image.core variable instead.
    from PIL import _imaging as core

except ImportError as v:

    # Fail here anyway. Don't let people run with a mostly broken Pillow.
    raise


try:
    import builtins
except ImportError:
    import __builtin__
    builtins = __builtin__


from PIL import ImageMode
from PIL._binary import i8, o8
from PIL._util import isPath, isStringType #, deferred_error

import os, sys

# type stuff
import collections
import numbers
