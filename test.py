#!/usr/bin/env python

from PIL import Image

im = Image.open("lena.ppm")

im.point(list(range(256))*3)
