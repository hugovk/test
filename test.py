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
