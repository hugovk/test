#!/usr/bin/env python

from PIL import Image, PILLOW_VERSION
import sys

print("Python version:", sys.version)
print("PILLOW_VERSION:", PILLOW_VERSION)

files = [
    "grimmnight_bk.tga",
    "grimmnight_ft.tga",
    "grimmnight_rt.tga",
    "grimmnight_dn.tga",
    "grimmnight_lf.tga",
    "grimmnight_up.tga"]

for f in files:
    print(f)
    im = Image.open(f)
    im.load()
    print(im)


