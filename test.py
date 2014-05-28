#!/usr/bin/env python

from PIL import Image

im = Image.open("lena.ppm").convert("I")

im.point(lambda x: x*1)
