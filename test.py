#!/usr/bin/env python

from PIL import Image

im = Image.open("lena.ppm")

im.point(list(range(256))*3)
im.point(lambda x: x)

im = im.convert("I")
im.point(lambda x: x*1)
im.point(lambda x: x+1)
im.point(lambda x: x*1+1)

im.point(list(range(256))*256, 'L')
